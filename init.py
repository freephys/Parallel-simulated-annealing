#!/usr/bin/env python
from mpi4py import MPI
comm = MPI.COMM_SELF.Spawn('python',
                           args=['main.py'],
                           maxprocs=8)
comm.Disconnect()
