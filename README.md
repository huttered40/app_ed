# app_ed
Welcome!
This repository hosts benchmark performance data of multi-dimensional applications/kernels.

Datasets are classified as 1) datasets, 2) tensor datasets, 3) test datasets, or 4) curated datasets.

## Datasets
Recent datasets live in the datasets/stampede2/ directory.
The first line in each file defines the configuration parameters and corresponding
execution times and related statistical information (e.g., sample variance).
The first column in subsequent lines is an index unrelated to the specification
of configuration parameters.
Raw datasets consist of a list of executed configurations.

### List of machines
Current datasets have been collected on the following machines:
- Stampede2

Current datasets consist of the following kernels/applications.
See paper [https://arxiv.org/abs/2210.10184] for benchmark parameter descriptions.
- QR Factorization (Intel MKL Library's DGEQRF routine on Stampede2, single/multi-threaded execution)
  - Training set: datasets/stampede2/geqrf/geqrf_kt0_st1_1threads.csv
  - Test set: test_sets/stampede2/geqrf/1threads.csv
  - Benchmark parameter column indices (zero-indexed): 1,2
  - Benchmark runtime column index (zero-indexed): 3
- Matrix Multiplication (Intel MKL Library's DGEMM routine on Stampede2, single/multi-threaded execution)
  - Training set: datasets/stampede2/gemm/1-thread.csv
  - Test set: test_sets/stampede2/gemm/1-thread.csv
  - Benchmark parameter column indices (zero-indexed): 1,2,3
  - Benchmark runtime column index (zero-indexed): 4
- MPI Bcast (Intel MPI Library on Stampede2)
  - Training set: datasets/stampede2/bcast/kt1_st1.csv
  - Test set: datasets/stampede2/bcast/kt1_st1_test.csv
  - Benchmark parameter column indices (zero-indexed): 1,2,3
  - Benchmark runtime column index (zero-indexed): 4
- ExaFMM Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  - Training set: datasets/stampede2/exafmm/kt1_nnodes1.csv
  - Test set: datasets/stampede2/exafmm/kt1_nnodes1_test.csv
  - Benchmark parameter column indices (zero-indexed): 2,3,4,6,7,8
  - Benchmark runtime column index (zero-indexed): 15
- AMG Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  - Training set: datasets/stampede2/amg/kt0_nnodes1.csv
  - Test set: datasets/stampede2/amg/kt0_nnodes1_test.csv
  - Benchmark parameter column indices (zero-indexed): 1,2,3,4,5,6,10,11
  - Benchmark runtime column index (zero-indexed): 14
- Kripke Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  - Training set: datasets/stampede2/kripke/kt0_nnodes1.csv
  - Test set: datasets/stampede2/kripke/kt0_nnodes1_test.csv
  - Benchmark parameter column indices (zero-indexed): 2,3,4,5,6,10,11,15,16
  - Benchmark runtime column index (zero-indexed): 25
