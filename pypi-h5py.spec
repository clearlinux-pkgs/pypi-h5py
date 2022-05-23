#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-h5py
Version  : 3.6.0
Release  : 72
URL      : https://files.pythonhosted.org/packages/0a/39/62ec4c1cc96408f6cf27c1d10a26409b98eb6aa2dda7d9c48d204c09b970/h5py-3.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0a/39/62ec4c1cc96408f6cf27c1d10a26409b98eb6aa2dda7d9c48d204c09b970/h5py-3.6.0.tar.gz
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
%setup -q -n h5py-3.6.0
cd %{_builddir}/h5py-3.6.0
pushd ..
cp -a h5py-3.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653335264
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
cp %{_builddir}/h5py-3.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-h5py/75e30d84df76091f6aaa16a714073a72127a8158
cp %{_builddir}/h5py-3.6.0/licenses/license.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1
cp %{_builddir}/h5py-3.6.0/lzf/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/aa5045989d4313b21faf709c6fa3e83ba81c2ed5
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
