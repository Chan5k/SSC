import time
import psutil

def test_cpu_stress(duration):
    """
    Test CPU stress for a specified duration.

    :param duration: The duration of the CPU stress test (in seconds).
    """
    print("Running CPU stress test...")
    end_time = time.time() + duration
    while time.time() < end_time:
        psutil.cpu_percent(interval=1)

def get_cpu_score():
    """
    Calculate the CPU score based on the average CPU usage.

    :return: The CPU score.
    """
    cpu_usage_percent = psutil.cpu_percent(interval=1, percpu=True)
    num_cores = psutil.cpu_count(logical=False)
    score = sum(cpu_usage_percent) / (num_cores * 100)
    return round(score, 2)
