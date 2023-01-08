import subprocess
from datetime import datetime
import random
import os

subprocess.run('whoami')
subprocess.run('pwd')
subprocess.run('mkdir dz1')

current_datetime = datetime.now().date()
subprocess.run(f'touch ./dz1/{current_datetime}')
subprocess.run('chown root:root ./dz1/')
subprocess.run('rm ./dz1/2022-11-09')
for i in range(5):
    i = os.listdir('dz1')
    file = random.choice(i)
    print(file)
    subprocess.call(f'rm ./dz1/{file}')

