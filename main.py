import subprocess
import time

while True:
    process = subprocess.Popen(["bot1.py"], shell=True) 
    time.sleep(240)
    process.kill() 
