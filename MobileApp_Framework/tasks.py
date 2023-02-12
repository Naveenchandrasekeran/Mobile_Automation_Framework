
from invoke import task
S
import os

@task
def test(c, env='staging', lang='en', app='android', device='emulator'):
    c.run(f'python3 -m pytest src/spec/{app}/*.py --app={app} --device={device}')

