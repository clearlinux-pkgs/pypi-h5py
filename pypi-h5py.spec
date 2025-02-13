#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: e180208
#
Name     : pypi-h5py
Version  : 3.12.1
Release  : 96
URL      : https://files.pythonhosted.org/packages/cc/0c/5c2b0a88158682aeafb10c1c2b735df5bc31f165bfe192f2ee9f2a23b5f1/h5py-3.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cc/0c/5c2b0a88158682aeafb10c1c2b735df5bc31f165bfe192f2ee9f2a23b5f1/h5py-3.12.1.tar.gz
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
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
Requires: python3-core
Provides: pypi(h5py)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-h5py package.


%prep
%setup -q -n h5py-3.12.1
cd %{_builddir}/h5py-3.12.1
pushd ..
cp -a h5py-3.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730137701
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-h5py
cp %{_builddir}/h5py-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-h5py/75e30d84df76091f6aaa16a714073a72127a8158 || :
cp %{_builddir}/h5py-%{version}/licenses/license.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1 || :
cp %{_builddir}/h5py-%{version}/licenses/license.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1 || :
cp %{_builddir}/h5py-%{version}/licenses/pytables.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/169c3c74b1c28363d5b4dcacd8e91ed830a879f8 || :
cp %{_builddir}/h5py-%{version}/lzf/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-h5py/aa5045989d4313b21faf709c6fa3e83ba81c2ed5 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1
/usr/share/package-licenses/pypi-h5py/169c3c74b1c28363d5b4dcacd8e91ed830a879f8
/usr/share/package-licenses/pypi-h5py/75e30d84df76091f6aaa16a714073a72127a8158
/usr/share/package-licenses/pypi-h5py/aa5045989d4313b21faf709c6fa3e83ba81c2ed5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
