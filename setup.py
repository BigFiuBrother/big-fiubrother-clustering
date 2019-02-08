from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='big-fiubrother-clustering',
   version='0.0.1',
   description='Big Fiubrother Clustering application',
   license="GPLv3",
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Eduardo Neira, Gabriel Gayoso',
   author_email='aneira@fi.uba.ar',
   packages=['big_fiubrother_clustering'],
   url= 'https://github.com/BigFiuBrother/big-fiubrother-clustering'
)