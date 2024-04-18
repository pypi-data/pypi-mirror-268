from setuptools import setup, find_packages

setup(
          name='simbapy',
          version='0.2.2',
          description='SIMBa: System Identification Methods leveraging Backpropagation',
          long_description= "SIMBa (System Identification Methods leveraging Backpropagation) is an open-source toolbox leveraging the Pytorch Automatic Differentiation framework for stable state-space linear SysID. It allows the user to incorporate prior knowledge (like sparsity patterns of the state-space matrices) during the identification procedure.  More details on https://github.com/Cemempamoi/simba.",
          author='',
          author_email='loris.dinatale@alumni.epfl.ch',
          url='',
          license='GNU LESSER GENERAL PUBLIC LICENSE Version 3',
          py_modules=['simba'],
          python_requires='>=3.8,<3.11', #python version required
          install_requires = [
          'numpy',
          'scipy',
          'torch'
          ],
          packages=find_packages(),
        )