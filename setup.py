from setuptools import setup

setup(name='gwalker-simple-model',
      version='0.0.1',
      description='Graph Walker Simple Model',
      author='pycb6a',
      author_email='pycb6a@gmail.com',
      py_modules=['gwalker-simple-model'],
      install_requires=['click', 'requests', ],
      entry_points="""
            [console_scripts]
            gwalker-simple-model=gwalker:cli
      """
      )
