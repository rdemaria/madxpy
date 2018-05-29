import os
import ast
import setuptools

def get_version_from_init():
    init_file = os.path.join(
        os.path.dirname(__file__), 'madxpy', '__init__.py'
    )
    with open(init_file, 'r') as fd:
        for line in fd:
            if line.startswith('__version__'):
                return ast.literal_eval(line.split('=', 1)[1].strip())

setuptools.setup(
        name='madxpy',
        version=get_version_from_init(),
        description='A MadX library wrapper',
        author='Riccardo De Maria',
        author_email='riccardo.de.maria@cern.ch',
        url='https://github.com/rdemaria/pjlsa',
        packages=['madxpy'],
        package_dir={'madxpy': 'madxpy'},
        python_requires='>=3.6',
        )

