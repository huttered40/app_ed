# pmodel_data
Multi-Dimensional Application/Kernel Execution Time Datasets

Datasets are classified as 1) tensor datasets or 2) raw datasets.

Each dataset is in CSV format.
The first line in each file defines the configuration parameters and corresponding
execution times and related statistical information (e.g., sample variance).
The first column in subsequent lines is an index unrelated to the specification
of configuration parameters.

## Tensor datasets
Tensor datasets consist of a list of executed configurations in which each configuration corresponds to a distinct element of a multi-dimensional array (i.e., tensor). Such datasets typically follow from the mapping of a discrete multi-dimensional configuration space onto a regular grid, each grid-point of which corresponds to a distinct configuration (and tensor element).

Tensor datasets have a file name corresponding to the size of the underlying tensor. Thus, a file titled 8x8x8.csv consists of 512 distinct configurations and corresponding execution times.

## Raw datasets
Raw datasets consist of a list of executed configurations without those configurations being constrained to a grid-point of some underlying regular grid.

### List of machines
Current datasets have been collected on the following machines:
- Stampede2

Current datasets consist of the following kernels/applications.
Each defines a distinct sub-directory.

### List of tensor datasets
We provide the kernel name, followed by execution descriptions (e.g., single-threaded execution), followed by a list of configuration parameters with corresponding ranges and spacing
- GEMM::Matrix Multiplication[m,n,k]::1-thread execution::{[m,(32,4096),log],[n,(32,4096),log],[k,(32,4096),log]}::[sample mean,sample variance].
