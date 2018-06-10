from setuptools import setup

setup(name='vrep_python_remote_api',
      version='0.2',
      description='Package that contains the neccessary files to use the V-REP Remote API from python code (Tested on windows)',
      url='-',
      author='Dániel Rácz',
      author_email='racz.daniel.93@gmail.com',
      license='MIT',
      packages=['vrep_remote_api'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
