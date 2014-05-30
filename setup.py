from distutils.core import setup

setup(
    name='statecode',
    version='0.1',
    author='Vincent Arel-Bundock',
    author_email='varel@umich.edu',
    packages=['statecode'],
    #scripts=[],
    url='http://umich.edu/~varel',
    license='LICENSE.txt',
    description='Convert country names and country codes',
    long_description=open('README.txt').read(),
    package_data={'statecode': ['data/statecode_data.csv']}
)
