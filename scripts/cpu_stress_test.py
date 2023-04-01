import psutil
import time

def test_cpu_stress(duration):
    print("Running CPU stress test for {} seconds...".format(duration))
    start_time = time.time()
    cpu_usage_list = []
    while True:
        if time.time() - start_time >= duration:
            break
        cpu_usage = psutil.cpu_percent()
        cpu_usage_list.append(cpu_usage)
    cpu_score = 100 - sum(cpu_usage_list) / len(cpu_usage_list)
    print("CPU score: {:.2f}".format(cpu_score))
