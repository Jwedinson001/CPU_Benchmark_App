# Benchmarking Project

This project is designed to evaluate concurrency performance using threads, measuring CPU speed in terms of Floating Point Operations Per Second (FLOPS) and Input/Output Operations Per Second (IOPS). The benchmarks are automated to run three times, and the results are reported with average and standard deviation values.

## Project Structure

```
benchmarking-project
├── src
│   ├── benchmark.py      # Main entry point for running benchmarks
│   ├── flops.py          # Implementation of FLOPS benchmark
│   ├── iops.py           # Implementation of IOPS benchmark
│   └── utils.py          # Utility functions for timing and statistics
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

To set up the environment, ensure you have Python installed. Then, create a virtual environment and install the required packages:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Benchmarks

To run the benchmarks, execute the following command:

```bash
python src/benchmark.py
```

This will initiate the benchmarking process for both FLOPS and IOPS, running each benchmark three times and calculating the average and standard deviation of the results.

## Interpreting Results

After the benchmarks complete, the results will be displayed in the console. You will see the average FLOPS and IOPS values along with their standard deviations. Higher values indicate better performance.

## Contributing

Contributions to improve the benchmarking methods or add new features are welcome. Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.