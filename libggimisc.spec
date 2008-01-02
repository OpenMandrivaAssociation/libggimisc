%define major 2
%define libname %mklibname ggimisc %{major}

Summary:	Extension to libggi for misc graphics target features
Name:		libggimisc
Version:	2.2.2
Release:	%mkrel 2
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

%package -n %{libname}-devel
Summary:	Header files for libggimisc library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel

%description -n %{libname}-devel
Header files for libggimisc library.

%package -n %{libname}-static-devel
Summary:	Static files for libggimisc library
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}

%description -n %{libname}-static-devel
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
%defattr(644,root,root,755)
%doc COPYING README ChangeLog TODO
%config(noreplace) %{_sysconfdir}/ggi/libggimisc.conf
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/*.so
%attr(755,root,root) %{_libdir}/ggi/ggimisc/display/*.la
%{_mandir}/man3/*

%files -n %{libname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{libname}-devel
%defattr(644,root,root,755)
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_mandir}/man7/*

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/ggi/ggimisc/display/*.a


