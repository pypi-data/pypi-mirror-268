#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup, Extension, find_packages
import pip

from setuptools.command.build_ext import build_ext as build_ext_orig


version='0.52.4'
libName="mazalib"

file_dir_path = os.path.dirname(os.path.realpath(__file__))

def package_files(directory):
    return [os.path.join(p,f) for p,d,files in os.walk(directory) for f in files]

with open("README.md", "r") as fh:
	long_description = fh.read()
short_description = "Cross-platform 2d/3d image segmentation C++ library"

language="c++"
extra_compile_args=['-O3', '-w', '-std=c++11']
installRequiresList=['numpy']
entry_points_Command={'main_library': ['kriging = mazalib:kriging',
                                       'mrf = mazalib:mrf',
                                       'rgs = mazalib:rgs',
                                       'hessian = mazalib:hessian',
                                       'windowedHessian = mazalib:windowedHessian',
                                       'nlm = mazalib:nlm',
                                       'unsharp = mazalib:unsharp',
									   'cac = mazalib:cac']}
license='GPLv3'
author='Mathieu Gravey, Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina, Andrey A. Ananev'
author_email='andrey.ananev@phystech.edu'

classifiers=[
			'Development Status :: 3 - Alpha',
			'Intended Audience :: Science/Research',
			'Intended Audience :: Education',
			'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
			'Programming Language :: C++',
			'Programming Language :: Python :: 3 :: Only'
		]

packages=find_packages('src',include=['mazalib*']) + ['segmentation', 'eigen3']

eigen_path=os.path.join(file_dir_path,"src","eigen3","")
eigen_package_files=package_files(eigen_path)



os.environ["CXX"]='g++'
os.environ["CC"]='gcc'

pip.main(['install', 'numpy'])

class get_numpy_include(object):
    """Defer numpy.get_include() until after numpy is installed."""

    def __str__(self):
        import numpy
        return numpy.get_include()

mazalib_module = Extension(libName, 
						sources=['./src/mazalib/mazalib.cpp'] + package_files('./src/segmentation/src/'),
						language=language, 
						extra_compile_args=extra_compile_args,
						include_dirs=["./src/segmentation/include/", "./src/eigen3/", get_numpy_include()])
setup(
	name=libName,
	version=version,
	description=short_description,
	long_description=long_description,
    long_description_content_type="text/markdown",
	author=author,
	author_email=author_email,
	license=license,
	packages=packages,
	package_dir={'': 'src'},
	package_data={'segmentation': ['./src/*.cpp', './include/*.h'],
					'eigen3': eigen_package_files},
	classifiers=classifiers,
	ext_modules=[mazalib_module],
	setup_requires=installRequiresList,
	install_requires=installRequiresList,
	entry_points=entry_points_Command
)