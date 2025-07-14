import os
import subprocess
import time

SCRIPT_DIR = os.path.dirname(__file__)
INPUT = os.path.join(SCRIPT_DIR, 'samples', 'video.mp4')
CONFIG = 'config/blur-config.cfg'
EXE = 'bin/blur.exe'

def blur(input: str = INPUT, output: str = "output.mp4", config_loc: str = CONFIG):
    start = time.perf_counter()
    subprocess.run([EXE, "-i", input, "-o", output, "-c", config_loc, "-v"])
    end = time.perf_counter()
    
    output_path = os.path.abspath(output)
    if os.path.exists(output_path):
        elapsed = end - start
        mins, secs = divmod(elapsed, 60)
        print(f"✅ Done: {output_path}")
        print(f"⏱️  Time taken: {int(mins)}m {secs:.2f}s")
        os.startfile(output_path)
        