#!/usr/bin/env python
from mpi4py import MPI
import multiprocessing as mp
import numpy as np
import sys
CPUNUMBER=8
ParameterNumber=4
comm = MPI.COMM_SELF.Spawn('python',args=['main.py'],maxprocs=CPUNUMBER)

def f(parameters):
    x1=parameters[0]
    x2=parameters[1]
    x3=parameters[2]
    x4=parameters[3]
    res=-20*np.exp(-0.2*np.sqrt(0.25*(x1*x1+x2*x2+x3*x3+x4*x4)))-np.exp(0.25*(np.cos(4*x1)+np.cos(4*x2)+np.cos(4*x3)+np.cos(4*x4)))+20+np.exp(1)
    return res

pool=mp.Pool(processes=CPUNUMBER)


positionContainer=np.zeros((CPUNUMBER,ParameterNumber))
valueContainer=np.zeros(CPUNUMBER)
RContainer=np.zeros(CPUNUMBER)

comm.Gather(None,positionContainer,root=MPI.ROOT)
# print(positionContainer)
comm.Scatter(np.array(pool.map(f,positionContainer)),None,root=MPI.ROOT)

# print('dd')
# sys.stdout.flush()
R=int(comm.recv(source=0,tag=0))
# print(R,'dd')
# sys.stdout.flush()
mycount=0
for i in range(R):
    mycount+=1
    comm.Gather(None,positionContainer,root=MPI.ROOT)
    comm.Scatter(np.array(pool.map(f,positionContainer)),None,root=MPI.ROOT)
    # comm.Barrier()
    # print(mycount)
    # sys.stdout.flush()
# print('ffllag')
# sys.stdout.flush()
while(R!=0):
    R=int(comm.recv(source=0,tag=0))
    if(R == 0):
        break
    mycount=0
    for i in range(R):
        # mycount+=1
        comm.Gather(None,positionContainer,root=MPI.ROOT)
        comm.Scatter(np.array(pool.map(f,positionContainer)),None,root=MPI.ROOT)
        # print(mycount)
        # sys.stdout.flush()
    # print('ffllag')
    # sys.stdout.flush()
        
comm.Disconnect()
# print(f([1,0,0,0]))
