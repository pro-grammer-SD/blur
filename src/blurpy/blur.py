import os
import subprocess
import time
import inspect

CONFIG = 'blur-bins/config/blur-config.cfg'
EXE = 'blur-bins/bin/blur.exe'

def blur(input_: str, output: str = "output.mp4", config_loc: str = CONFIG):
    caller_dir = os.path.dirname(os.path.abspath(inspect.stack()[1].filename))
    exe_path = os.path.join(caller_dir, EXE)
    config_path = os.path.join(caller_dir, config_loc)
    output_path = os.path.join(caller_dir, output)

    start = time.perf_counter()
    result = subprocess.run([exe_path, "-i", input_, "-o", output_path, "-c", config_path, "-v"], capture_output=True, text=True)
    end = time.perf_counter()

    if os.path.exists(output_path):
        mins, secs = divmod(end - start, 60)
        print(f"✅ Done: {output_path}")
        print(f"⏱️  Time taken: {int(mins)}m {secs:.2f}s")
        os.startfile(output_path)
    else:
        print("❌ Output not created.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        