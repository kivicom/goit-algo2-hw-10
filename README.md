# Algorithmic Complexity, Approximation, and Randomized Algorithms Homework

This repository contains solutions for homework tasks on algorithmic complexity, approximation, and randomized algorithms.

## Tasks
- **Task 1**: Compare the performance of Randomized and Deterministic QuickSort algorithms.
- **Task 2**: Implement a greedy algorithm for university class scheduling to minimize the number of teachers.

## Files
- `quicksort_comparison.py`: Solution for Task 1.
- `greedy_schedule.py`: Solution for Task 2.
- `requirements.txt`: Dependency list for the project.

## Requirements
- Python 3.x
- Libraries:
  - `matplotlib>=3.5.0`
  - `numpy<2.0`
  - `tabulate>=0.9.0`
- Install dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```

## Usage
Run each script to test:
```bash
python3 quicksort_comparison.py
python3 greedy_schedule.py
```

## Notes
- Task 1 outputs a table and graph comparing QuickSort performance.
- Task 2 creates a schedule ensuring all subjects are covered with minimal teachers.
- Tested on Python 3.11.