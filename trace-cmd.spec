#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : trace-cmd
Version  : 3.3.1
Release  : 25
URL      : https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v3.3.1.tar.gz
Source0  : https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v3.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: trace-cmd-bin = %{version}-%{release}
Requires: trace-cmd-data = %{version}-%{release}
Requires: trace-cmd-license = %{version}-%{release}
Requires: trace-cmd-python = %{version}-%{release}
Requires: trace-cmd-python3 = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(cunit)
BuildRequires : pkgconfig(libtraceevent)
BuildRequires : pkgconfig(libtracefs)
BuildRequires : pkgconfig(libzstd)
BuildRequires : python3-dev
BuildRequires : swig
BuildRequires : xmlto
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
For more information on contributing please see: https://www.trace-cmd.org
Note: The official repositiory for trace-cmd and KernelShark is here:

%package bin
Summary: bin components for the trace-cmd package.
Group: Binaries
Requires: trace-cmd-data = %{version}-%{release}
Requires: trace-cmd-license = %{version}-%{release}

%description bin
bin components for the trace-cmd package.


%package data
Summary: data components for the trace-cmd package.
Group: Data

%description data
data components for the trace-cmd package.


%package license
Summary: license components for the trace-cmd package.
Group: Default

%description license
license components for the trace-cmd package.


%package python
Summary: python components for the trace-cmd package.
Group: Default
Requires: trace-cmd-python3 = %{version}-%{release}

%description python
python components for the trace-cmd package.


%package python3
Summary: python3 components for the trace-cmd package.
Group: Default
Requires: python3-core

%description python3
python3 components for the trace-cmd package.


%prep
%setup -q -n trace-cmd-v3.3.1
cd %{_builddir}/trace-cmd-v3.3.1
pushd ..
cp -a trace-cmd-v3.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728920011
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
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

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
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/trace-cmd
cp %{_builddir}/trace-cmd-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a || :
cp %{_builddir}/trace-cmd-v%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/traceevent/plugins/*.so
## install_append content
mkdir -p %{buildroot}/usr/share/bash_completion.d
#mv %{buildroot}/usr/etc/bash_completion.d/trace-cmd.bash  %{buildroot}/usr/share/bash_completion.d
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/trace-cmd
/usr/bin/trace-cmd

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/trace-cmd.bash

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721
/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
