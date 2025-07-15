import os
import subprocess
import time
import sys

CONFIG = 'blur-bins/config/blur-config.cfg'
EXE = 'blur-bins/bin/blur.exe'

def blur(input_: str, output: str = "output.mp4", config_loc: str = CONFIG):
    caller_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(caller_dir)

    exe_path = os.path.join(caller_dir, EXE)
    config_path = os.path.join(caller_dir, config_loc)
    output_path = os.path.join(caller_dir, output)

    start = time.perf_counter()
    subprocess.run([exe_path, "-i", input_, "-o", output_path, "-c", config_path, "-v"], shell=True, check=True)
    end = time.perf_counter()
    mins, secs = divmod(end - start, 60)
    print(f"✅ Done: {output_path}")
    print(f"⏱️  Time taken: {int(mins)}m {secs:.2f}s")
    os.startfile(output_path)
    