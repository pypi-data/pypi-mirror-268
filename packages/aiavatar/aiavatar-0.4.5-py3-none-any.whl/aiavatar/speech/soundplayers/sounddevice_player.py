import asyncio
import io
import os
import select
import sys
import wave
import numpy
import sounddevice


if __name__ == "__main__":
    device_index = int(sys.argv[1]) if len(sys.argv) > 2 else 0
    timeout = float(sys.argv[2]) if len(sys.argv) > 3 else 5.0

    try:
        ready, _, _ = select.select([sys.stdin], [], [], timeout)

        if not ready:
            raise Exception(f"Sound timeout ({timeout}sec)")

        data = sys.stdin.buffer.read()

        if not data:
            raise Exception("No sound data")

        with wave.open(io.BytesIO(data), "rb") as f:
            data = numpy.frombuffer(
                f.readframes(f.getnframes()),
                dtype=numpy.int16
            )
            framerate = f.getframerate()
            sounddevice.play(data, framerate, device=device_index)
            sounddevice.wait()
    
    except Exception as ex:
        sys.stderr.write(f"{ex}\n")
        sys.exit(1)

else:
    from . import SoundPlayerBase

    class SoundDevicePlayer(SoundPlayerBase):
        def __init__(self, device_index: int=-1, playback_margin: float=0.1, subprocess_timeout: float=5.0):
            self.device_index = device_index
            self.playback_margin = playback_margin
            self.subprocess_timeout = subprocess_timeout

        async def play_wave(self, data):
            with wave.open(io.BytesIO(data), "rb") as f:
                data = numpy.frombuffer(
                    f.readframes(f.getnframes()),
                    dtype=numpy.int16
                )
                framerate = f.getframerate()
                sounddevice.play(data, framerate, device=self.device_index, blocking=False)
                await asyncio.sleep(len(data) / framerate + self.playback_margin)

        async def play_wave_on_subprocess(self, data):
            process = await asyncio.create_subprocess_exec(
                "python", os.path.abspath(__file__), str(self.device_index), str(self.subprocess_timeout),
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await process.communicate(input=data)

            if process.returncode != 0:
                raise Exception(stderr.decode())

            return stdout
