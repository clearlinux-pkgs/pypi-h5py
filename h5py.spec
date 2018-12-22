#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBCD928050D713D75 (tcaswell@gmail.com)
#
Name     : h5py
Version  : 2.9.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/43/27/a6e7dcb8ae20a4dbf3725321058923fec262b6f7835179d78ccc8d98deec/h5py-2.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/27/a6e7dcb8ae20a4dbf3725321058923fec262b6f7835179d78ccc8d98deec/h5py-2.9.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/43/27/a6e7dcb8ae20a4dbf3725321058923fec262b6f7835179d78ccc8d98deec/h5py-2.9.0.tar.gz.asc
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: h5py-license = %{version}-%{release}
Requires: h5py-python = %{version}-%{release}
Requires: h5py-python3 = %{version}-%{release}
Requires: numpy
Requires: six
BuildRequires : Cython-python
BuildRequires : buildreq-distutils3
BuildRequires : hdf5-dev
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-pkgconfig
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

%package license
Summary: license components for the h5py package.
Group: Default

%description license
license components for the h5py package.


%package python
Summary: python components for the h5py package.
Group: Default
Requires: h5py-python3 = %{version}-%{release}

%description python
python components for the h5py package.


%package python3
Summary: python3 components for the h5py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the h5py package.


%prep
%setup -q -n h5py-2.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545507720
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/h5py
cp docs/licenses.rst %{buildroot}/usr/share/package-licenses/h5py/docs_licenses.rst
cp licenses/license.txt %{buildroot}/usr/share/package-licenses/h5py/licenses_license.txt
cp lzf/LICENSE.txt %{buildroot}/usr/share/package-licenses/h5py/lzf_LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/h5py/docs_licenses.rst
/usr/share/package-licenses/h5py/licenses_license.txt
/usr/share/package-licenses/h5py/lzf_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
