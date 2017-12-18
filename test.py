# from mpi4py import MPI
import multiprocessing as mp
import numpy as np
# pool = mp.Pool()

def job(x):
    print(x**2)
pool = mp.Pool()
res = pool.map(job, range(10))
# print(res)