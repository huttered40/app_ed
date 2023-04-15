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
  -
  -
- Matrix Multiplication (Intel MKL Library's DGEMM routine on Stampede2, single/multi-threaded execution)
  -
  -
- MPI Bcast (Intel MPI Library on Stampede2)
  -
  -
- ExaFMM Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  -
  -
- AMG Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  -
  -
- Kripke Library on Stampede2 (single-node/multi-processes-per-node/multi-threaded execution)
  - Training set: datasets/stampede2/kripke/kt0_nnodes1.csv
  - Test set: datasets/stampede2/kripke/kt0_nnodes1_test.csv
