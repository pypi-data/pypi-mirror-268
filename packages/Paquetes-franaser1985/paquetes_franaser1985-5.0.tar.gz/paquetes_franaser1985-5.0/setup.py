# Destribución de paquetes (Distribuible)

from setuptools import setup, find_packages

setup(
      #nombre_del_paquete
      name='Paquetes-franaser1985',
      #versión_del_paquete
      version='5.0',
      #breve descripción
      description='Un paquete para hola y adios',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='Franchesco Naranjo Serrano',
      author_email='franchesco.naranjoserrano@gmail.com',
      url='https://www.hektor.dev',
      license_files=['LICENSE'],
      #Lista de modulos
      packages=find_packages(), 
      # Lista de archivos ejecutables
      scripts=[],
      # Para poner la carpeta donde estan los test
      test_suite='tests',
      # Instalar las librerias requeridas con == nos intala la versión que digo
      # con >= la misma o una superior
      install_requires=[paquete.strip()
                        for paquete in open("requirements.txt").readlines()],
      classifiers=[
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
],

)

