#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD6E95F20305701A1 (trbs@trbs.net)
#
Name     : pid
Version  : 3.0.4
Release  : 12
URL      : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz.asc
Summary  : Pidfile featuring stale detection and file-locking, can also be used as context-manager or decorator
Group    : Development/Tools
License  : Apache-2.0
Requires: pid-license = %{version}-%{release}
Requires: pid-python = %{version}-%{release}
Requires: pid-python3 = %{version}-%{release}
Requires: psutil
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : psutil
BuildRequires : pytest

%description
===

%package license
Summary: license components for the pid package.
Group: Default

%description license
license components for the pid package.


%package python
Summary: python components for the pid package.
Group: Default
Requires: pid-python3 = %{version}-%{release}

%description python
python components for the pid package.


%package python3
Summary: python3 components for the pid package.
Group: Default
Requires: python3-core
Provides: pypi(pid)

%description python3
python3 components for the pid package.


%prep
%setup -q -n pid-3.0.4
cd %{_builddir}/pid-3.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629126160
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m pytest
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pid
cp %{_builddir}/pid-3.0.4/LICENSE %{buildroot}/usr/share/package-licenses/pid/790bd88a7078375e9e85a058079a7d663ccf9273
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pid/790bd88a7078375e9e85a058079a7d663ccf9273

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
