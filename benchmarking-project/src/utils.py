import time
import statistics
import numpy as np

def measure_time(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return result, end_time - start_time

def calculate_average(results):
    return np.mean(results)

def calculate_standard_deviation(data):
    return statistics.stdev(data)

def format_time(seconds):
    return f"{seconds:.6f} seconds"

def collect_results(results):
    average = calculate_average(results)
    stddev = calculate_standard_deviation(results)
    return average, stddev

def print_results(average, stddev):
    print(f"Average Time: {format_time(average)}")
    print(f"Standard Deviation: {format_time(stddev)}")

def calculate_std_dev(results):
    return np.std(results)

def timed_execution(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time