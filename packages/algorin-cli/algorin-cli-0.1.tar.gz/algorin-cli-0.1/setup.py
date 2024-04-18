from setuptools import setup, find_packages

setup(
    name='algorin-cli',
    version='0.1',
    author='JP',
    author_email='jorge.polanco@itesm.mx',
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt", "r")],
    description='Acceso a GPT-3 y procesamiento de documentos desde la línea de comandos.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    url='https://github.com/Jorge-Polanco-Roque/bot_cli',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
