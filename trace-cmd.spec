#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : trace-cmd
Version  : 2.9
Release  : 4
URL      : https://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git/snapshot/trace-cmd-v2.9.tar.gz
Source0  : https://git.kernel.org/pub/scm/linux/kernel/git/rostedt/trace-cmd.git/snapshot/trace-cmd-v2.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: trace-cmd-bin = %{version}-%{release}
Requires: trace-cmd-data = %{version}-%{release}
Requires: trace-cmd-lib = %{version}-%{release}
Requires: trace-cmd-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
Note: The official repositiory for trace-cmd and KernelShark is here:
git://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git

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


%package lib
Summary: lib components for the trace-cmd package.
Group: Libraries
Requires: trace-cmd-data = %{version}-%{release}
Requires: trace-cmd-license = %{version}-%{release}

%description lib
lib components for the trace-cmd package.


%package license
Summary: license components for the trace-cmd package.
Group: Default

%description license
license components for the trace-cmd package.


%prep
%setup -q -n trace-cmd-v2.9
cd %{_builddir}/trace-cmd-v2.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595264343
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1595264343
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/trace-cmd
cp %{_builddir}/trace-cmd-v2.9/COPYING %{buildroot}/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a
cp %{_builddir}/trace-cmd-v2.9/COPYING.LIB %{buildroot}/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721
%make_install prefix=/usr libdir=/usr/lib64
## install_append content
mkdir -p %{buildroot}/usr/share/bash_completion.d
mv %{buildroot}/usr/etc/bash_completion.d/trace-cmd.bash  %{buildroot}/usr/share/bash_completion.d
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/trace-cmd

%files data
%defattr(-,root,root,-)
/usr/share/bash_completion.d/trace-cmd.bash

%files lib
%defattr(-,root,root,-)
/usr/lib64/traceevent/plugins/plugin_blk.so
/usr/lib64/traceevent/plugins/plugin_cfg80211.so
/usr/lib64/traceevent/plugins/plugin_function.so
/usr/lib64/traceevent/plugins/plugin_futex.so
/usr/lib64/traceevent/plugins/plugin_hrtimer.so
/usr/lib64/traceevent/plugins/plugin_jbd2.so
/usr/lib64/traceevent/plugins/plugin_kmem.so
/usr/lib64/traceevent/plugins/plugin_kvm.so
/usr/lib64/traceevent/plugins/plugin_mac80211.so
/usr/lib64/traceevent/plugins/plugin_sched_switch.so
/usr/lib64/traceevent/plugins/plugin_scsi.so
/usr/lib64/traceevent/plugins/plugin_tlb.so
/usr/lib64/traceevent/plugins/plugin_xen.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/trace-cmd/1927bd74419ad757a1d8e010f558c162bc7a4721
/usr/share/package-licenses/trace-cmd/29156b719d2cbb6630525c4f4d4a4657ef76649a
