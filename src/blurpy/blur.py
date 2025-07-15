import os
import subprocess
import time

CONFIG = 'blur-bins/config/blur-config.cfg'
EXE = 'blur-bins/bin/blur.exe'

def blur(input_: str, output: str = "output.mp4", config_loc: str = CONFIG):
    start = time.perf_counter()
    subprocess.run([EXE, "-i", input_, "-o", output, "-c", config_loc, "-v"])
    end = time.perf_counter()
    
    output_path = os.path.abspath(output)
    if os.path.exists(output_path):
        elapsed = end - start
        mins, secs = divmod(elapsed, 60)
        print(f"✅ Done: {output_path}")
        print(f"⏱️  Time taken: {int(mins)}m {secs:.2f}s")
        os.startfile(output_path)
        