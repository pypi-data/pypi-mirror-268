from setuptools import setup
setup(
    name='ligo-softioc',
    version='0.1.3',
    description='Library to support EPICS soft iocs in Python.',
    author='Erik von Reis',
    author_email='evonreis@caltech.edu',
    url='https://git.ligo.org/cds/admin/softioc',
    packages=['ligo_softioc'],
    package_dir={'': 'src'}
)
