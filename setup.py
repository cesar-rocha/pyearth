from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyearth',
      version='0.1dev1',
      description='A set of constants commonly used in earth sciences\
              analysis',
      url='http://github.com/crocha700/pyearth',
      author='Cesar B Rocha',
      author_email='crocha@ucsd.edu',
      license='MIT',
      packages=['pyearth'],
      install_requires=[
          'numpy',
      ],
      test_suite = 'nose.collector',
      zip_safe=False)
