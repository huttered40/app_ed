# app_ed
Welcome!
This repository hosts execution data of multi-dimensional applications/kernels.

Datasets are classified as 1) tensor datasets or 2) raw datasets.

Each dataset is in CSV format.
The first line in each file defines the configuration parameters and corresponding
execution times and related statistical information (e.g., sample variance).
The first column in subsequent lines is an index unrelated to the specification
of configuration parameters.

## Tensor datasets
Tensor datasets consist of a list of executed configurations in which each configuration corresponds to a distinct element of a multi-dimensional array (i.e., tensor).
Such datasets typically follow from the mapping of a discrete multi-dimensional configuration space onto a regular grid, each grid-point of which corresponds to a distinct configuration (and tensor element).
They are not necessarily in any order, nor are all grid-points/tensor elements necessarily executed.

Tensor datasets have a file name corresponding to the size of the underlying tensor. Thus, a file titled 8x8x8.csv consists of 512 distinct configurations and corresponding (sample mean) execution times.

## Raw datasets
Raw datasets consist of a list of executed configurations without those configurations being constrained to a grid-point of some underlying regular grid.

### List of machines
Current datasets have been collected on the following machines:
- Stampede2

Current datasets consist of the following kernels/applications.
Each defines a distinct sub-directory.
- DGEMM (Intel MKL Library on Stampede2, single/multi-threaded execution): parameters [m,n,k] define matrix dimensions as follows: $\mathbf{C}_{m\times n}\gets\mathbf{A}_{m\times k}\mathbf{B}_{k\times n}$
- MPI Allreduce (Intel MPI Library on Stampede2): parameters [nbytes,nnodes,ppn] define message size, number of nodes, and number of processes-per-node, respectively.
- MPI Bcast (Intel MPI Library on Stampede2): parameters [nbytes,nnodes,ppn] define message size, number of nodes, and number of processes-per-node, respectively.
- Parallel QR Factorization (SLATE Library's PDGEQRF routine on Stampede2, multi-node/multi-processes-per-node execution): parameters [m,n,nnodes] define matrix dimensions as follows: $\mathbf{Q}_{m\times n}\mathbf{R}_{n\times n}\gets \mathbf{A}$$, number of nodes, and number of processes-per-node, respectively.

### List of tensor datasets
We provide the kernel name, followed by execution descriptions (e.g., single-threaded execution), followed by a list of configuration parameters with corresponding ranges and spacing. We then provide the list of execution data.
- GEMM::1-thread execution::{[m,(32,4096),log],[n,(32,4096),log],[k,(32,4096),log]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- GEMM::4-thread execution::{[m,(64,8192),log],[n,(64,8192),log],[k,(64,8192),log]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- GEMM::16-thread execution::{[m,(128,16384),log],[n,(128,16384),log],[k,(128,16384),log]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- GEMM::64-thread execution::{[m,(256,32768),log],[n,(256,32768),log],[k,(256,32768),log]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- Allreduce::multi-node/multi-processes-per-node execution::{[nbytes,(64,16777216),log],[nnodes,(1,2,4,8,16,32)],[ppn,(1,2,4,8,16,32,64)]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- Bcast::multi-node/multi-processes-per-node execution::{[nbytes,(64,16777216),log],[nnodes,(1,2,4,8,16,32)],[ppn,(1,2,4,8,16,32,64)]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
- SlateQR::8-processes-per-node execution::{[m,($1024*\sqrt{nnodes}$,$65536*\sqrt{nnodes}$),log],[m,($16*\sqrt{nnodes}$,$1024*\sqrt{nnodes}$),log],[nnodes,(1,4,16,64)]}::[sample mean of $\le 50$ iterations,sample variance of $\le 50$ iterations].
