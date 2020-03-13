from setuptools import setup

setup(name='lng_rec',
      version='0.1.0',
      entry_points='''
            [gui_scripts]
            lng_Rec = src.__main__:main
      ''',
      )
