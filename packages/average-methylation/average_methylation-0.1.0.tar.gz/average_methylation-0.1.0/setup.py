from setuptools import setup, find_packages

setup(
    name='average_methylation',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to calculate average methylation scores.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrimis/average-methylation-calculation.git',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=1.0.1',
        'numpy>=1.18.1'
    ],
    extras_require={
        "dev": [
            "pytest>=5.4.1"
        ]
    },
    include_package_data=True,
)
