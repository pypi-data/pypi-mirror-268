from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='IsNumberOdd',
    version='1.0.0',    
    description='Return true if the given number is odd.',
    author='Gabriel R Amaral',
    author_email='professor.gabriel.amaral@gmail.com',
    url='https://github.com/GabouKing/IsOdd',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['IsNumberEven'],  # Dependência do pacote IsNumberOdd
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)