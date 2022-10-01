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
- Matrix Multiplication (Intel MKL Library's DGEMM routine on Stampede2, single/multi-threaded execution): parameters [m,n,k] define matrix dimensions as follows: $C_{m\times n}\gets A_{m\times k}B_{k\times n}$
- MPI Allreduce (Intel MPI Library on Stampede2): parameters [nbytes,nnodes,ppn] define message size, number of nodes, and number of processes-per-node, respectively.
- MPI Bcast (Intel MPI Library on Stampede2): parameters [nbytes,nnodes,ppn] define message size, number of nodes, and number of processes-per-node, respectively.
- Parallel QR Factorization (SLATE Library's PDGEQRF routine on Stampede2, multi-node/multi-processes-per-node execution): parameters [m,n,nnodes] define matrix dimensions as follows: $Q_{m\times n}R_{n\times n}\gets A_{m\times n}$, number of nodes, and number of processes-per-node, respectively.
- Kripke Library on Stampede2, multi-node/multi-processes-per-node/multi-threaded execution): parameters [node_count,ppn_count,thread_count,layout,dset,gset,zset,groups,quad,zones,legendre,solver] define number of nodes, number of processes-per-node, number of threads-per-process, and the remaining are defined within Kripke's Github page.

### List of tensor datasets
We provide the kernel name, followed by execution descriptions (e.g., single-threaded execution), followed by a list of configuration parameters with corresponding ranges and spacing. We then provide the list of execution data.

- GEMM::z-thread execution::equidistant spacing on a log-scale for the following parameter ranges:
$$32\sqrt{z}\le m,n,k \le 4096\sqrt{z}, \forall z\in\{1,4,16,64}$$
*mean*: execution-time sample mean of $\le 50$ iterations.  
*std*: execution-time sample standard deviation of $\le 50$ iterations.   

- MPI_Allreduce::multi-node/multi-processes-per-node execution::equidistant spacing on a log-scale for the range of parameter *nbytes*, while parameters *nnodes,ppn* are given by the following sets:
$$64\le nbytes \le 16777216$$  
$$nnodes\in\{1,2,4,8,16,32\}$$  
$$ppn\in\{1,2,4,8,16,32,64\}$$  
*mean*: execution-time sample mean of $\le 50$ iterations.  
*std*: execution-time sample standard deviation of $\le 50$ iterations.  

- MPI_Bcast::multi-node/multi-processes-per-node execution::equidistant spacing on a log-scale for the range of parameter *nbytes*, while parameters *nnodes,ppn* are given by the following sets:
$$64\le nbytes \le 16777216$$  
$$nnodes\in\{1,2,4,8,16,32\}$$  
$$ppn\in\{1,2,4,8,16,32,64\}$$  
*mean*: execution-time sample mean of $\le 50$ iterations.  
*std*: execution-time sample standard deviation of $\le 50$ iterations.

- PDGEQRF::z-processes-per-node execution::equidistant spacing on a log-scale for the ranges of parameters *m,n*, while parameters *nnodes* are given by the following sets:
$$1024\le nbytes \le 65536, \forall z\in\{1,4,16,64}$$  
$$16\le nbytes \le 1024, \forall z\in\{1,4,16,64}$$  
$$nnodes\in\{1,4,16,64\}$$  
*mean*: execution-time sample mean of $\le 50$ iterations.  
*std*: execution-time sample standard deviation of $\le 50$ iterations.

- KRIPKE::multi-node, multi-processes-per-node, multi-threaded execution::the ranges of all parameters are given by the following sets:
$$groups\in\{8,16,24,32,64\}$$  
$$legendre\in\{0,1,2,3,4\}$$  
$$quad\{8,16,32\}$$  
$$zones\{8,16,32\}$$  
$$thread_count\in\{1,2,4\}$$  
$$ppn_count\in\{32,64\}$$  
$$node_count\in\{1,2,4,8,16,32\}$$  
$$layout\in\{"DGZ","DZG","GDZ","DGZ","ZDG","ZGD"\}$$  
$$solver\in\{"sweep","bj"\}$$  
$$dset\in\{8,16,24,32\}$$  
$$gset\in\{1,2,4,8\}$$  
$$zset\in\{1,2,4,8\}$$  
$$layout_dict\in\{"DGZ","DZG","GDZ","GZD","ZDG","ZGD"\}$$  
$$solver\in\{"sweep","bj"\}$$  
*k1,k2,k3,k4,k5,k7,k9*: execution-time sample mean of $\le 50$ iterations.  
*k6*: execution-time of solver  
*k8*: execution-time of sweep-solver  
