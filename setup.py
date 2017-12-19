from setuptools import setup, find_packages



setup(name='ParallelSA',

      version='1.0',

      url='https://github.com/ziyixi/Parallel-simulated-annealing',

      license='gpl-3.0',

      author='Ziyi Xi',

      author_email='xiziyi2015@gmail.com',

      description='A Parallel SA module',

      packages=find_packages(exclude=['tests_import','Procedural programming']),

      long_description=open('README.md').read(),

      zip_safe=False,

      setup_requires=['mpi4py','numpy'],)