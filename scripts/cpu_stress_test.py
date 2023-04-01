import psutil
import time

def test_cpu_stress(duration):
    print("Running CPU stress test for {} seconds...".format(duration))
    start_time = time.time()
    while True:
        if time.time() - start_time >= duration:
            break
        psutil.cpu_percent()
