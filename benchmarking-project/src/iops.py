import threading
import time
import random
import numpy as np
from utils import timed_execution

class IOPSTest:
    def __init__(self, num_operations, num_threads):
        self.num_operations = num_operations
        self.num_threads = num_threads
        self.lock = threading.Lock()
        self.results = []

    def perform_io_operation(self):
        # Simulate an I/O operation with a random sleep
        time.sleep(random.uniform(0.01, 0.1))  # Simulate I/O delay

    def thread_function(self):
        for _ in range(self.num_operations):
            with self.lock:
                self.perform_io_operation()
                self.results.append(1)  # Count the operation

    def run_benchmark(self):
        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.thread_function)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def calculate_iops(self):
        return len(self.results) / (self.num_operations * self.num_threads)

def benchmark_iops(num_operations, num_threads, iterations=3):
    iops_results = []
    for _ in range(iterations):
        test = IOPSTest(num_operations, num_threads)
        test.run_benchmark()
        iops_results.append(test.calculate_iops())

    average_iops = np.mean(iops_results)
    std_dev_iops = np.std(iops_results)
    return average_iops, std_dev_iops

def iops_operation(iterations):
    result = 0
    for _ in range(iterations):
        result += 1
    return result

def benchmark_iops():
    iterations = 10**7
    _, elapsed_time = timed_execution(iops_operation, iterations)
    return iterations / elapsed_time

if __name__ == "__main__":
    num_operations = 100  # Number of I/O operations per thread
    num_threads = 5       # Number of threads to use
    average, std_dev = benchmark_iops(num_operations, num_threads)
    print(f"Average IOPS: {average}, Standard Deviation: {std_dev}")