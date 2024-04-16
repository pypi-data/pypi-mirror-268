from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='udio_wrapper',
    version='0.0.3',
    author='Flowese',
    author_email='flowese@gmail.com',
    description='Generates songs using the Udio API using textual prompts.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/flowese/UdioWrapper',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    keywords='audio, music, generation, API, AI, Udio',
)
