## Install xgboost as a Python 2.7 package on OS X Sierra

Run the cmds below in the virtualenv dir where xgboost is required

From: https://github.com/dmlc/xgboost/blob/master/doc/build.md#building-on-osx

* `git clone --recursive https://github.com/dmlc/xgboost` (recursive needed since packages are in sub-modules)
* `cd xgboost`

For **single-threaded** xgboost (clang on OS X doesn't have OpenMP by default)
* `cp make/minimum.mk ./config.mk`
* `make -j4`

For **multi-threaded** xgboost (need to install OpenMP-enabled compiler first)
* *To install Home Brew, see https://github.com/Homebrew/install*
* `brew install gcc --without-multilib` (takes ~ 45 mins)
* `cp make/config.mk ./config.mk`
* `make -j4`

From: https://github.com/dmlc/xgboost/blob/master/python-package/README.rst

To install python package for xgboost
* `./build.sh` (in root dir of xgboost repository)
* `cd python-package`
* `python setup.py install`

This will install the file `xgboost-0.6-py2.7.egg in `lib/python2.7/site-packages` dir

## Testing installation
In Python intepreter in cmd line:
* `import xgboost`
* `print xgboost.__version__` will print current version of xgboost Python package
