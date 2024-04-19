from setuptools import setup, find_packages

setup(
    name='pypacgen',
    version='1.0.0',
    author='Kayleigh Conti',
    author_email='kc8528@pm.me',
    description='A module to generate Proxy Auto Config files on the fly.',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
