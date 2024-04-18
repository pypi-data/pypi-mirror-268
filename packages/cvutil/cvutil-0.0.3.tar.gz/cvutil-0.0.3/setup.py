from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cvutil',
    description='Set of auxiliary scripts for computer vision tasks',
    url='https://github.com/osmr/cvutil',
    author='Oleg Sémery',
    author_email='osemery@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='datasets image audio processing',
    packages=find_packages(exclude=['others', '*.others', 'others.*', '*.others.*']),
    install_requires=['opencv-python', 'pyrender'],
    python_requires='>=3.7',
    include_package_data=True,
)
