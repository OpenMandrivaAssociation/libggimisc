%define major 2
%define libname %mklibname ggimisc %{major}
%define develname %mklibname ggimisc -d
%define staticname %mklibname ggimisc -d -s

Summary:	Extension to libggi for misc graphics target features
Name:		libggimisc
Version:	2.2.2
Release:	%mkrel 3
License:	Public Domain
Group:		System/Libraries
Url:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libggi-devel	>= 2.2.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
LibGGIMisc is a place to put support for graphics target 
features which are not deserving their own special extensions. 
Right now this means basically some VGA adaptor features -
- getting and waiting for the raster position, using 
a hardware horizontal splitline feature, and loading/unloading font 
data from hardware text modes.

%package -n %{libname}
Summary:	Main library for libggimisc
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Main library for libggimisc.

%package -n %{develname}
Summary:	Header files for libggimisc library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname ggimisc 2 -d

%description -n %{develname}
Header files for libggimisc library.

%package -n %{staticname}
Summary:	Static files for libggimisc library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}
Obsoletes:	%mklibname ggimisc 2 -d -s

%description -n %{staticname}
Static files for libggimisc library.

%prep
%setup -q
./autogen.sh

%build
export echo=echo

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
export echo=echo

%makeinstall_std

%ifarch x86_64
chrpath -d %{buildroot}%{_libdir}/ggi/ggimisc/display/fbdev_ggimisc.so
chrpath -d %{buildroot}%{_libdir}/ggi/ggimisc/display/pseudo_stubs_ggimisc.so
%endif

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog TODO
%config(noreplace) %{_sysconfdir}/ggi/libggimisc.conf
%{_libdir}/ggi/ggimisc/display/*.so
%{_libdir}/ggi/ggimisc/display/*.la
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man7/*

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/ggi/ggimisc/display/*.a
