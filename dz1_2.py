#!/usr/bin/python
import subprocess

subprocess.run('cp ./copydz/dz1.py ./copydz/dz1_run.py', shell=True)
subprocess.run('chown root:root ./copydz/dz1_run.py')
subprocess.run('chmod u+r-x ./copydz/dz1_run.py')
subprocess.run('./copydz/dz1_run.py')