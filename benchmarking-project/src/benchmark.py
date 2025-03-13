import threading
import time
import numpy as np
from flops import benchmark_flops
from iops import benchmark_iops
from utils import calculate_average, calculate_std_dev

class Benchmark:
    def __init__(self, iterations=3):
        self.iterations = iterations
        self.flops_results = []
        self.iops_results = []
        self.lock = threading.Lock()

    def run_flops_benchmark(self):
        for _ in range(self.iterations):
            result = benchmark_flops()
            with self.lock:
                self.flops_results.append(result)

    def run_iops_benchmark(self):
        for _ in range(self.iterations):
            result = benchmark_iops()
            with self.lock:
                self.iops_results.append(result)

    def run_benchmarks(self):
        flops_thread = threading.Thread(target=self.run_flops_benchmark)
        iops_thread = threading.Thread(target=self.run_iops_benchmark)

        flops_thread.start()
        iops_thread.start()

        flops_thread.join()
        iops_thread.join()

        avg_flops = calculate_average(self.flops_results)
        std_flops = calculate_std_dev(self.flops_results)
        avg_iops = calculate_average(self.iops_results)
        std_iops = calculate_std_dev(self.iops_results)

        print(f"FLOPS: Average = {avg_flops}, Standard Deviation = {std_flops}")
        print(f"IOPS: Average = {avg_iops}, Standard Deviation = {std_iops}")

if __name__ == "__main__":
    benchmark = Benchmark()
    benchmark.run_benchmarks()