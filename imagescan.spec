#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imagescan
Version  : 3.61.0
Release  : 4
URL      : http://support.epson.net/linux/src/scanner/imagescanv3/common/imagescan_3.61.0.orig.tar.gz
Source0  : http://support.epson.net/linux/src/scanner/imagescanv3/common/imagescan_3.61.0.orig.tar.gz
Summary  : Build tool
Group    : Development/Tools
License  : BSL-1.0 GPL-3.0 LGPL-2.1
Requires: imagescan-bin = %{version}-%{release}
Requires: imagescan-config = %{version}-%{release}
Requires: imagescan-data = %{version}-%{release}
Requires: imagescan-lib = %{version}-%{release}
Requires: imagescan-libexec = %{version}-%{release}
Requires: imagescan-license = %{version}-%{release}
Requires: imagescan-locales = %{version}-%{release}
BuildRequires : ImageMagick
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : boost-dev
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : gettext-bin
BuildRequires : graphviz
BuildRequires : libjpeg-turbo-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gtkmm-2.4)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(sane-backends)
BuildRequires : tiff-dev
Patch1: 0001-Always-create-SANE-dll.d-entry.patch
Patch2: 0002-Do-not-give-bad-perms-to-scanner-device.patch

%description
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible
with Perforce Jam.

Authors:
    Perforce Jam : Cristopher Seiwald
    FT Jam : David Turner
    Boost Jam : David Abrahams

Copyright:
    /+\
    +\  Copyright 1993-2002 Christopher Seiwald and Perforce Software, Inc.
    \+/
    License is hereby granted to use this software and distribute it
    freely, as long as this copyright notice is retained and modifications
    are clearly marked.
    ALL WARRANTIES ARE HEREBY DISCLAIMED.

Also:
    Copyright 2001-2006 David Abrahams.
    Copyright 2002-2006 Rene Rivera.
    Copyright 2003-2006 Vladimir Prus.

    Distributed under the Boost Software License, Version 1.0.
    (See accompanying file LICENSE_1_0.txt or http://www.boost.org/LICENSE_1_0.txt)

%package bin
Summary: bin components for the imagescan package.
Group: Binaries
Requires: imagescan-data = %{version}-%{release}
Requires: imagescan-libexec = %{version}-%{release}
Requires: imagescan-config = %{version}-%{release}
Requires: imagescan-license = %{version}-%{release}

%description bin
bin components for the imagescan package.


%package config
Summary: config components for the imagescan package.
Group: Default

%description config
config components for the imagescan package.


%package data
Summary: data components for the imagescan package.
Group: Data

%description data
data components for the imagescan package.


%package dev
Summary: dev components for the imagescan package.
Group: Development
Requires: imagescan-lib = %{version}-%{release}
Requires: imagescan-bin = %{version}-%{release}
Requires: imagescan-data = %{version}-%{release}
Provides: imagescan-devel = %{version}-%{release}
Requires: imagescan = %{version}-%{release}

%description dev
dev components for the imagescan package.


%package lib
Summary: lib components for the imagescan package.
Group: Libraries
Requires: imagescan-data = %{version}-%{release}
Requires: imagescan-libexec = %{version}-%{release}
Requires: imagescan-license = %{version}-%{release}

%description lib
lib components for the imagescan package.


%package libexec
Summary: libexec components for the imagescan package.
Group: Default
Requires: imagescan-config = %{version}-%{release}
Requires: imagescan-license = %{version}-%{release}

%description libexec
libexec components for the imagescan package.


%package license
Summary: license components for the imagescan package.
Group: Default

%description license
license components for the imagescan package.


%package locales
Summary: locales components for the imagescan package.
Group: Default

%description locales
locales components for the imagescan package.


%prep
%setup -q -n utsushi-0.61.0
cd %{_builddir}/utsushi-0.61.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573689102
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static --with-udev-confdir=/usr/lib/udev \
--with-sane-confdir=/usr/share/defaults/sane
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1573689102
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imagescan
cp %{_builddir}/utsushi-0.61.0/COPYING %{buildroot}/usr/share/package-licenses/imagescan/5d5b272eee7052483f8893c6da9de0c258b1036c
cp %{_builddir}/utsushi-0.61.0/upstream/boost/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/imagescan/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/utsushi-0.61.0/upstream/boost/tools/bcp/licence_info.cpp %{buildroot}/usr/share/package-licenses/imagescan/bf3f8ac9bd569a03cfabf79b75d5fa70440407c8
cp %{_builddir}/utsushi-0.61.0/upstream/boost/tools/bcp/licence_info.hpp %{buildroot}/usr/share/package-licenses/imagescan/d7d282609a551cd74bba985bf9f93c2bbffea35b
cp %{_builddir}/utsushi-0.61.0/upstream/boost/tools/build/v2/engine/debian/copyright %{buildroot}/usr/share/package-licenses/imagescan/91367cdb429a2ecf03f07f332c27a3588aa8915e
cp %{_builddir}/utsushi-0.61.0/upstream/ltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/imagescan/3ac522f07da0f346b37b29cd73a60f79e992ffba
%make_install
%find_lang utsushi
## install_append content
mv %{buildroot}/usr/lib/udev/rules.d/utsushi-esci.rules %{buildroot}/usr/lib/udev/rules.d/59-utsushi-esci.rules
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/utsushi

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/59-utsushi-esci.rules

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sane/dll.d/utsushi
/usr/share/utsushi/drivers/esci/DS-1610.dat
/usr/share/utsushi/drivers/esci/DS-1630.dat
/usr/share/utsushi/drivers/esci/DS-1660W.dat
/usr/share/utsushi/drivers/esci/DS-310.dat
/usr/share/utsushi/drivers/esci/DS-320.dat
/usr/share/utsushi/drivers/esci/DS-360W.dat
/usr/share/utsushi/drivers/esci/DS-40.dat
/usr/share/utsushi/drivers/esci/DS-50000.dat
/usr/share/utsushi/drivers/esci/DS-510.dat
/usr/share/utsushi/drivers/esci/DS-520.dat
/usr/share/utsushi/drivers/esci/DS-530.dat
/usr/share/utsushi/drivers/esci/DS-535.dat
/usr/share/utsushi/drivers/esci/DS-535H.dat
/usr/share/utsushi/drivers/esci/DS-5500.dat
/usr/share/utsushi/drivers/esci/DS-560.dat
/usr/share/utsushi/drivers/esci/DS-570W.dat
/usr/share/utsushi/drivers/esci/DS-575W.dat
/usr/share/utsushi/drivers/esci/DS-60000.dat
/usr/share/utsushi/drivers/esci/DS-6500.dat
/usr/share/utsushi/drivers/esci/DS-70000.dat
/usr/share/utsushi/drivers/esci/DS-7500.dat
/usr/share/utsushi/drivers/esci/DS-760.dat
/usr/share/utsushi/drivers/esci/DS-770.dat
/usr/share/utsushi/drivers/esci/DS-775.dat
/usr/share/utsushi/drivers/esci/DS-860.dat
/usr/share/utsushi/drivers/esci/ES-200.dat
/usr/share/utsushi/drivers/esci/ES-300W.dat
/usr/share/utsushi/drivers/esci/ES-400.dat
/usr/share/utsushi/drivers/esci/ES-500W.dat
/usr/share/utsushi/drivers/esci/PX-M7050.dat
/usr/share/utsushi/drivers/esci/PX-M7050FX.dat
/usr/share/utsushi/drivers/esci/PX-M860F.dat
/usr/share/utsushi/drivers/esci/WF-6590.dat
/usr/share/utsushi/gtkmm/about.xml
/usr/share/utsushi/gtkmm/dialog.glade
/usr/share/utsushi/gtkmm/dialog.rc

%files dev
%defattr(-,root,root,-)
/usr/include/utsushi/array.hpp
/usr/include/utsushi/buffer.hpp
/usr/include/utsushi/condition-variable.hpp
/usr/include/utsushi/connexion.hpp
/usr/include/utsushi/constraint.hpp
/usr/include/utsushi/context.hpp
/usr/include/utsushi/cstdint.hpp
/usr/include/utsushi/descriptor.hpp
/usr/include/utsushi/device-info.hpp
/usr/include/utsushi/device.hpp
/usr/include/utsushi/exception.hpp
/usr/include/utsushi/filter.hpp
/usr/include/utsushi/format.hpp
/usr/include/utsushi/functional.hpp
/usr/include/utsushi/i18n.hpp
/usr/include/utsushi/iobase.hpp
/usr/include/utsushi/key.hpp
/usr/include/utsushi/log.hpp
/usr/include/utsushi/media.hpp
/usr/include/utsushi/memory.hpp
/usr/include/utsushi/monitor.hpp
/usr/include/utsushi/mutex.hpp
/usr/include/utsushi/octet.hpp
/usr/include/utsushi/option.hpp
/usr/include/utsushi/pattern/decorator.hpp
/usr/include/utsushi/preset.hpp
/usr/include/utsushi/pump.hpp
/usr/include/utsushi/quantity.hpp
/usr/include/utsushi/range.hpp
/usr/include/utsushi/regex.hpp
/usr/include/utsushi/run-time.hpp
/usr/include/utsushi/scanner.hpp
/usr/include/utsushi/signal.hpp
/usr/include/utsushi/store.hpp
/usr/include/utsushi/stream.hpp
/usr/include/utsushi/string.hpp
/usr/include/utsushi/tag.hpp
/usr/include/utsushi/thread.hpp
/usr/include/utsushi/toggle.hpp
/usr/include/utsushi/type-traits.hpp
/usr/include/utsushi/value.hpp

%files lib
%defattr(-,root,root,-)
/usr/lib64/sane/libsane-utsushi.so
/usr/lib64/sane/libsane-utsushi.so.1
/usr/lib64/sane/libsane-utsushi.so.1.0.28
/usr/lib64/utsushi/libcnx-hexdump.so
/usr/lib64/utsushi/libcnx-hexdump.so.0
/usr/lib64/utsushi/libcnx-hexdump.so.0.0.0
/usr/lib64/utsushi/libcnx-usb.so
/usr/lib64/utsushi/libcnx-usb.so.0
/usr/lib64/utsushi/libcnx-usb.so.0.0.0
/usr/lib64/utsushi/libdrv-combo.so
/usr/lib64/utsushi/libdrv-combo.so.0
/usr/lib64/utsushi/libdrv-combo.so.0.0.0
/usr/lib64/utsushi/libdrv-esci.so
/usr/lib64/utsushi/libdrv-esci.so.0
/usr/lib64/utsushi/libdrv-esci.so.0.0.0
/usr/lib64/utsushi/libflt-all.so
/usr/lib64/utsushi/libflt-all.so.0
/usr/lib64/utsushi/libflt-all.so.0.0.0
/usr/lib64/utsushi/libutsushi-gtkmm.so
/usr/lib64/utsushi/libutsushi-gtkmm.so.0
/usr/lib64/utsushi/libutsushi-gtkmm.so.0.0.0
/usr/lib64/utsushi/libutsushi.so
/usr/lib64/utsushi/libutsushi.so.0
/usr/lib64/utsushi/libutsushi.so.0.0.0
/usr/lib64/utsushi/sane/libsane-utsushi.so
/usr/lib64/utsushi/sane/libsane-utsushi.so.1
/usr/lib64/utsushi/sane/libsane-utsushi.so.1.0.28

%files libexec
%defattr(-,root,root,-)
/usr/libexec/utsushi/esci-interpreter
/usr/libexec/utsushi/get-text-orientation
/usr/libexec/utsushi/utsushi-help
/usr/libexec/utsushi/utsushi-list
/usr/libexec/utsushi/utsushi-main
/usr/libexec/utsushi/utsushi-scan
/usr/libexec/utsushi/utsushi-scan-cli
/usr/libexec/utsushi/utsushi-scan-gtkmm
/usr/libexec/utsushi/utsushi-version

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imagescan/3ac522f07da0f346b37b29cd73a60f79e992ffba
/usr/share/package-licenses/imagescan/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/imagescan/5d5b272eee7052483f8893c6da9de0c258b1036c
/usr/share/package-licenses/imagescan/91367cdb429a2ecf03f07f332c27a3588aa8915e
/usr/share/package-licenses/imagescan/bf3f8ac9bd569a03cfabf79b75d5fa70440407c8
/usr/share/package-licenses/imagescan/d7d282609a551cd74bba985bf9f93c2bbffea35b

%files locales -f utsushi.lang
%defattr(-,root,root,-)

