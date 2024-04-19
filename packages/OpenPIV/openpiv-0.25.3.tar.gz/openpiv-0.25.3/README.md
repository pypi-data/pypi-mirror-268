# OpenPIV
![Build and upload to PyPI](https://github.com/OpenPIV/openpiv-python/workflows/Build%20and%20upload%20to%20PyPI/badge.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4409178.svg)](https://doi.org/10.5281/zenodo.4409178)
![PyPI](https://img.shields.io/pypi/v/openpiv)
![Anaconda](https://anaconda.org/openpiv/openpiv/badges/version.svg)


OpenPIV consists in a Python and Cython modules for scripting and executing the analysis of 
a set of PIV image pairs. In addition, a Qt and Tk graphical user interfaces are in 
development, to ease the use for those users who don't have python skills.

## Warning

The OpenPIV python version is still in its *beta* state. This means that
it still might have some bugs and the API may change. However, testing and contributing
is very welcome, especially if you can contribute with new algorithms and features.


## Test it without installation
Click the link - thanks to BinderHub, Jupyter and Conda you can now get it in your browser with zero installation:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/openpiv/openpiv-python/master?filepath=openpiv%2Fexamples%2Fnotebooks%2Ftutorial1.ipynb)




## Installing

Use PyPI: <https://pypi.python.org/pypi/OpenPIV>:

    pip install openpiv


## Or `conda` 

    conda install -c alexlib openpiv

## Or [Poetry](https://python-poetry.org/)

    poetry add openpiv
    
    
### To build from source

<!-- TODO: Change this build method to use poetry -->

Download the package from the Github: https://github.com/OpenPIV/openpiv-python/archive/master.zip
or clone using git

    git clone https://github.com/OpenPIV/openpiv-python.git

Using distutils create a local (in the same directory) compilation of the Cython files:

    python setup.py build_ext --inplace

Or for the global installation, use:

    python setup.py install 


## Documentation

The OpenPIV documentation is available on the project web page at <http://openpiv.readthedocs.org>

## Demo notebooks 

1. [Tutorial Notebook 1](https://nbviewer.jupyter.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/tutorial1.ipynb)
2. [Tutorial notebook 2](https://nbviewer.jupyter.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/tutorial2.ipynb)
3. [Dynamic masking tutorial](https://nbviewer.jupyter.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/masking_tutorial.ipynb)
4. [Multipass with Windows Deformation](https://nbviewer.jupyter.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/window_deformation_comparison.ipynb)
5. [Multiple sets in one notebook](https://nbviewer.jupyter.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/all_test_cases_sample.ipynb)
6. [3D PIV](https://nbviewer.org/github/OpenPIV/openpiv-python-examples/blob/main/notebooks/PIV_3D_example.ipynb)


These and many additional examples are in another repository: [OpenPIV-Python-Examples](https://github.com/OpenPIV/openpiv-python-examples)


## Contributors

1. [Alex Liberzon](http://github.com/alexlib)
2. [Roi Gurka](http://github.com/roigurka)
3. [Zachary J. Taylor](http://github.com/zjtaylor)
4. [David Lasagna](http://github.com/gasagna)
5. [Mathias Aubert](http://github.com/MathiasAubert)
6. [Pete Bachant](http://github.com/petebachant)
7. [Cameron Dallas](http://github.com/CameronDallas5000)
8. [Cecyl Curry](http://github.com/leycec)
9. [Theo Käufer](http://github.com/TKaeufer)
10. [Andreas Bauer](https://github.com/AndreasBauerGit)
11. [David Bohringer](https://github.com/davidbhr)
12. [Erich Zimmer](https://github.com/ErichZimmer)
13. [Peter Vennemann](https://github.com/eguvep)
14. [Lento Manickathan](https://github.com/lento234)
15. [Yuri Ishizawa](https://github.com/yuriishizawa)


Copyright statement: `smoothn.py` is a Python version of `smoothn.m` originally created by D. Garcia [https://de.mathworks.com/matlabcentral/fileexchange/25634-smoothn], written by Prof. Lewis and available on Github [https://github.com/profLewis/geogg122/blob/master/Chapter5_Interpolation/python/smoothn.py]. We include a version of it in the `openpiv` folder for convenience and preservation. We are thankful to the original authors for releasing their work as an open source. OpenPIV license does not relate to this code. Please communicate with the authors regarding their license. 

## How to cite this work
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4409178.svg)](https://doi.org/10.5281/zenodo.4409178)




