from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='COVIDcover',
      version='1.0.0',
      description='Educational game about COVID infection',
      executables=executables)