A Simulated annealing framework for inverse

copyright:
    ZIYI XI(xiziyi2015@gmail.com)

license:
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.en.html)

How to use it?
1. Wrap your forward model into form as < command name > parameter1 parameter2 ...
and its output should be the value of objective function
2. Use config.ini to config your settings, commonly you just need set, CpuNumber, 
ParameterNumber, RangeHigh, RangeLow, CommandName, and stopMoveStep. If you want to
disable a parameter, just set its sensity accordingly 0.
3. I want to wrap the code into some form nicer, but as the dynamic support for mpi4py
is really poor, I could just use this not pretty good-looking coding structure. But at
least, it could run, isn't it?
4. I believe you could use your code interactiving with bash, to call the command: 
mpiexec -n < core you want to use which is also CPUNUMBER in config> python main.py, 
and it returns a list of number in the form such as 0 1 2 3, here 0 is the final objective 
function, 1 2 3 are parameters in the optimation form. I think it's easy for you to analysis.
5. I strongly suggest you to use anaconda and install mpi4py using "conda install mpi4py", 
thus this code could run!