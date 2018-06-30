#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x57FA4540DD4EFCF7 (tcaswell@gmail.com)
#
Name     : h5py
Version  : 2.7.1
Release  : 27
URL      : https://pypi.debian.net/h5py/h5py-2.7.1.tar.gz
Source0  : https://pypi.debian.net/h5py/h5py-2.7.1.tar.gz
Source99 : https://pypi.debian.net/h5py/h5py-2.7.1.tar.gz.asc
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: h5py-python3
Requires: h5py-python
Requires: numpy
Requires: six
BuildRequires : Cython-python
BuildRequires : hdf5-dev
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python-pkgconfig
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
The h5py package provides both a high- and low-level interface to the HDF5
        library from Python. The low-level interface is intended to be a complete
        wrapping of the HDF5 API, while the high-level component supports  access to
        HDF5 files, datasets and groups using established Python and NumPy concepts.
        
        A strong emphasis on automatic conversion between Python (Numpy) datatypes and
        data structures and their HDF5 equivalents vastly simplifies the process of
        reading and writing data from Python.
        
        Supports HDF5 versions 1.8.4 and higher.  On Windows, HDF5 is included with
        the installer.

%package python
Summary: python components for the h5py package.
Group: Default
Requires: h5py-python3

%description python
python components for the h5py package.


%package python3
Summary: python3 components for the h5py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the h5py package.


%prep
%setup -q -n h5py-2.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519136671
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
