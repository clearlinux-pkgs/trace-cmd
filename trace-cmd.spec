#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : trace-cmd
Version  : 2.9.3
Release  : 9
URL      : https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v2.9.3.tar.gz
Source0  : https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v2.9.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: trace-cmd-bin = %{version}-%{release}
Requires: trace-cmd-lib = %{version}-%{release}
Requires: trace-cmd-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : freeglut-dev
BuildRequires : glu-dev
BuildRequires : json-c-dev
BuildRequires : mesa-dev
BuildRequires : qtbase-dev

%description
For more information on contributing please see: https://www.trace-cmd.org
Note: The official repositiory for trace-cmd and KernelShark is here:

%package bin
Summary: bin components for the trace-cmd package.
Group: Binaries
Requires: trace-cmd-license = %{version}-%{release}

%description bin
bin components for the trace-cmd package.


%package dev
Summary: dev components for the trace-cmd package.
Group: Development
Requires: trace-cmd-lib = %{version}-%{release}
Requires: trace-cmd-bin = %{version}-%{release}
Provides: trace-cmd-devel = %{version}-%{release}
Requires: trace-cmd = %{version}-%{release}

%description dev
dev components for the trace-cmd package.


%package lib
Summary: lib components for the trace-cmd package.
Group: Libraries
Requires: trace-cmd-license = %{version}-%{release}

%description lib
lib components for the trace-cmd package.


%package license
Summary: license components for the trace-cmd package.
Group: Default

%description license
license components for the trace-cmd package.


%prep
%setup -q -n trace-cmd-v2.9.3
cd %{_builddir}/trace-cmd-v2.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621363634
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1621363634
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/trace-cmd
cp %{_builddir}/trace-cmd-v2.9.3/COPYING %{buildroot}/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a
cp %{_builddir}/trace-cmd-v2.9.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721
%make_install prefix=/usr libdir=/usr/lib64 install_libs
## Remove excluded files
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_blk.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_cfg80211.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_function.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_futex.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_hrtimer.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_jbd2.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_kmem.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_kvm.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_mac80211.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_sched_switch.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_scsi.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_tlb.so
rm -f %{buildroot}/usr/lib64/traceevent/plugins/plugin_xen.so
## install_append content
mkdir -p %{buildroot}/usr/share/bash_completion.d
#mv %{buildroot}/usr/etc/bash_completion.d/trace-cmd.bash  %{buildroot}/usr/share/bash_completion.d
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/trace-cmd

%files dev
%defattr(-,root,root,-)
/usr/include/trace-cmd/trace-cmd.h
/usr/lib64/libtracecmd.so
/usr/lib64/pkgconfig/libtracecmd.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtracecmd.so.0
/usr/lib64/libtracecmd.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721
/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a
