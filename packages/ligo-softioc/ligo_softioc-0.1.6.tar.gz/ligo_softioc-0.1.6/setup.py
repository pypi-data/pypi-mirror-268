from setuptools import setup
setup(
    name='ligo-softioc',
    version='0.1.6',
    description='Library to support EPICS soft IOCs in Python.',
    author='Erik von Reis',
    author_email='evonreis@caltech.edu',
    url='https://git.ligo.org/cds/admin/softioc',
    packages=['ligo_softioc'],
    package_data={'ligo_softioc': ['py.typed']},
    package_dir={'': 'src'},
    scripts={'src/print_ini'},
)
