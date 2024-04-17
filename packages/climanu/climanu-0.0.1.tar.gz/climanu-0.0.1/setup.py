from setuptools import setup,find_packages

with open("README.md",'r') as f:
    long_description=f.read()

setup(
        name='climanu',
        version='0.0.1',
        author='Hui Hola',
        description='A cli project to make many type of chosser menu',
        github='https://github.com/HuiHola/climanu',
        keywords=['cli app','create you own simple manu','python3'],
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        python_requires='>=3.11.8',
        py_modules=['climanu'],
        install_requires=[],
)
