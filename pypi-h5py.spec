#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-h5py
Version  : 3.7.0
Release  : 83
URL      : https://files.pythonhosted.org/packages/c5/40/7cf58e6230f0e76699f011c6d293dd47755997709a303a4e644823f3a753/h5py-3.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/40/7cf58e6230f0e76699f011c6d293dd47755997709a303a4e644823f3a753/h5py-3.7.0.tar.gz
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-h5py-filemap = %{version}-%{release}
Requires: pypi-h5py-lib = %{version}-%{release}
Requires: pypi-h5py-license = %{version}-%{release}
Requires: pypi-h5py-python = %{version}-%{release}
Requires: pypi-h5py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : hdf5-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pkgconfig)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://travis-ci.org/h5py/h5py.png
:target: https://travis-ci.org/h5py/h5py
.. image:: https://ci.appveyor.com/api/projects/status/h3iajp4d1myotprc/branch/master?svg=true
:target: https://ci.appveyor.com/project/h5py/h5py/branch/master
.. image:: https://dev.azure.com/h5pyappveyor/h5py/_apis/build/status/h5py.h5py?branchName=master
:target: https://dev.azure.com/h5pyappveyor/h5py/_build/latest?definitionId=1&branchName=master

%package filemap
Summary: filemap components for the pypi-h5py package.
Group: Default

%description filemap
filemap components for the pypi-h5py package.


%package lib
Summary: lib components for the pypi-h5py package.
Group: Libraries
Requires: pypi-h5py-license = %{version}-%{release}
Requires: pypi-h5py-filemap = %{version}-%{release}

%description lib
lib components for the pypi-h5py package.


%package license
Summary: license components for the pypi-h5py package.
Group: Default

%description license
license components for the pypi-h5py package.


%package python
Summary: python components for the pypi-h5py package.
Group: Default
Requires: pypi-h5py-python3 = %{version}-%{release}

%description python
python components for the pypi-h5py package.


%package python3
Summary: python3 components for the pypi-h5py package.
Group: Default
Requires: pypi-h5py-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(h5py)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-h5py package.


%prep
%setup -q -n h5py-3.7.0
cd %{_builddir}/h5py-3.7.0
pushd ..
cp -a h5py-3.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672278917
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-h5py
cp %{_builddir}/h5py-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-h5py/75e30d84df76091f6aaa16a714073a72127a8158 || :
cp %{_builddir}/h5py-%{version}/licenses/license.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1 || :
cp %{_builddir}/h5py-%{version}/lzf/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/aa5045989d4313b21faf709c6fa3e83ba81c2ed5 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-h5py

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1
/usr/share/package-licenses/pypi-h5py/75e30d84df76091f6aaa16a714073a72127a8158
/usr/share/package-licenses/pypi-h5py/aa5045989d4313b21faf709c6fa3e83ba81c2ed5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
