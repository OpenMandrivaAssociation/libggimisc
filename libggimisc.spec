%define major 2
%define libname %mklibname ggimisc %{major}
%define develname %mklibname ggimisc -d
%define staticname %mklibname ggimisc -d -s

Summary:	Extension to libggi for misc graphics target features
Name:		libggimisc
Version:	2.2.2
Release:	9
License:	Public Domain
Group:		System/Libraries
Url:		http://www.ggi-project.org/
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
BuildRequires:	libggi-devel	>= 2.2.2
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}

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
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%mklibname ggimisc 2 -d

%description -n %{develname}
Header files for libggimisc library.

%package -n %{staticname}
Summary:	Static files for libggimisc library
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Obsoletes:	%mklibname ggimisc 2 -d -s

%description -n %{staticname}
Static files for libggimisc library.

%prep
%setup -q

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

%files
%doc README ChangeLog TODO
%config(noreplace) %{_sysconfdir}/ggi/libggimisc.conf
%{_libdir}/ggi/ggimisc/display/*.so
%{_mandir}/man3/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc doc/*.txt
%{_includedir}/ggi/*.h
%{_includedir}/ggi/internal/*.h
%{_libdir}/*.so
%{_mandir}/man7/*

%files -n %{staticname}
%{_libdir}/*.a


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-8mdv2011.0
+ Revision: 620124
- the mass rebuild of 2010.0 packages

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 2.2.2-7mdv2010.0
+ Revision: 438603
- rebuild

* Thu Mar 26 2009 Frederic Crozat <fcrozat@mandriva.com> 2.2.2-6mdv2009.1
+ Revision: 361342
- Fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Funda Wang <fwang@mandriva.org>
    - fix requires

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.2-3mdv2008.1
+ Revision: 174780
- new devel library policy
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.2-2mdv2007.0
+ Revision: 125160
- fix dependencies

* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2.2-1mdv2007.1
+ Revision: 125108
- add missing buildrequires
- make it work
- remove rpath
- Import libggimisc

