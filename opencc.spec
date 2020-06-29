Name:           opencc
Version:        1.0.5
Release:        5
Summary:        Simplified Chinese Traditional Conversion Library
License:        ASL 2.0
URL:            https://github.com/BYVoid/OpenCC
Source0:        https://github.com/BYVoid/OpenCC/archive/ver.%{version}.tar.gz#/OpenCC-ver.%{version}.tar.gz
Patch0001:      opencc-fixes-cmake.patch
Patch0002:      opencc-check-bounds.patch
Patch0003:      opencc-stop-copy.patch

Provides:       %{name}-tools = %{version}-%{release}
Obsoletes:      %{name}-tools < %{version}-%{release}
BuildRequires:  gcc-c++ gettext cmake doxygen python3

%description
Opencc is for between Traditional Chinese and Simplified Chinese characters and phrases conversion library.

%package     devel
Summary:     Development files for OpenCC
Requires:    %{name} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications that use opencc.

%package     help
Summary:     Documentation for opencc
Requires:    %{name} = %{version}-%{release}
Provides:    %{name}-doc = %{version}-%{release}
Obsoletes:   %{name}-doc < %{version}-%{release}

%description help
This package provides documentation for opencc.

%prep
%autosetup -n OpenCC-ver.%{version} -p1

%build
%cmake . -DENABLE_GETTEXT:BOOL=ON -DBUILD_DOCUMENTATION:BOOL=ON
%make_build VERBOSE=1

%install
%make_install

%check
ctest

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS LICENSE README.md
%{_libdir}/lib*.so.*
%{_datadir}/opencc/
%{_bindir}/*
%exclude %{_datadir}/opencc/doc
%exclude %{_libdir}/*.a

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files help
%{_datadir}/opencc/doc

%changelog
* Mon Jun 29 2020 huanghaitao <huanghaitao8@huawei.com> - 1.0.5-5
- Fix build error

* Thu Dec 12 2019 fengbing <fengbing7@huawei.com> - 1.0.5-4
- Package init
