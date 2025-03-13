import threading
import time
import numpy as np
from utils import timed_execution

class FLOPSBenchmark:
    def __init__(self, num_operations, num_threads):
        self.num_operations = num_operations
        self.num_threads = num_threads
        self.lock = threading.Lock()
        self.results = []

    def perform_operations(self):
        count = 0
        for _ in range(self.num_operations):
            # Simulate a floating point operation
            count += 1.0 / (1.0 + count)
        return count

    def thread_worker(self):
        start_time = time.time()
        self.perform_operations()
        elapsed_time = time.time() - start_time

        with self.lock:
            self.results.append(elapsed_time)

    def run_benchmark(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.thread_worker)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def calculate_fps(self):
        total_time = sum(self.results)
        total_operations = self.num_operations * self.num_threads
        return total_operations / total_time if total_time > 0 else 0

    def get_average_and_stddev(self):
        return np.mean(self.results), np.std(self.results)

def run_flops_benchmark(num_operations, num_threads, iterations=3):
    benchmark = FLOPSBenchmark(num_operations, num_threads)
    for _ in range(iterations):
        benchmark.run_benchmark()
    average_time, stddev_time = benchmark.get_average_and_stddev()
    flops = benchmark.calculate_fps()
    return flops, average_time, stddev_time

def flops_operation(iterations):
    result = 0.0
    for _ in range(iterations):
        result += np.sin(np.pi / 4) * np.cos(np.pi / 4)
    return result

def benchmark_flops():
    iterations = 10**7
    _, elapsed_time = timed_execution(flops_operation, iterations)
    return iterations / elapsed_time