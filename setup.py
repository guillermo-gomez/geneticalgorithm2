
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geneticalgorithm2", 
    version="6.8.2",
    author="Demetry Pascal",
    author_email="qtckpuhdsa@gmail.com",
    maintainer='Demetry Pascal',
    description="Supported highly optimized and flexible genetic algorithm package for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PasaOpasen/geneticalgorithm2",
    license='MIT',
    keywords=['solve', 'optimization', 'problem', 'genetic', 'algorithm', 'GA', 'easy', 'fast', 'genetic-algorithm', 'combinatorial', 'mixed', 'evolutionary'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'func-timeout',
        'numpy',
        'matplotlib',
        'joblib',
        'OppOpPopInit>=2.0.0'
        ]
    
    )





