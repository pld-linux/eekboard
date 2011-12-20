Summary:	An Easy-to-use Virtual Keyboard Toolkit
Name:		eekboard
Version:	0.90.7
Release:	2
License:	GPL v3+
Group:		Applications/System
Source0:	http://github.com/downloads/ueno/eekboard/%{name}-%{version}.tar.gz
# Source0-md5:	204aa3914a1e0e12c0d7c1029bf74685
URL:		http://fedorahosted.org/eekboard/
BuildRequires:	at-spi2-core-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libcroco-devel
BuildRequires:	libfakekey-devel
BuildRequires:	libxklavier-devel
BuildRequires:	python-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-eekboard
Requires:	python-virtkey
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eekboard is a virtual keyboard software package, including a set of
tools to implement desktop virtual keyboards.

%package libs
Summary:	Runtime libraries for eekboard
License:	LGPL v2+
Group:		Libraries

%description libs
This package contains the libraries for eekboard

%package devel
Summary:	Development tools for eekboard
License:	LGPLv2+ and GFDL
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	vala

%description devel
This package contains the development tools for eekboard.

%package -n python-eekboard
Summary:	Python binding of eekboard client library
Group:		Libraries

%description -n python-eekboard
This package contains the Python language binding of eekboard client
library.

%prep
%setup -q

%build
%configure \
	--with-gtk=3.0 \
	--enable-atspi \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%attr(755,root,root) %{_bindir}/eekboard
%attr(755,root,root) %{_bindir}/eekboard-inscript
%attr(755,root,root) %{_bindir}/eekboard-server
%attr(755,root,root) %{_bindir}/eekboard-xml
%{_datadir}/eekboard
%{_datadir}/eekboard-inscript
%{_iconsdir}/hicolor/*/apps/eekboard.png
%{_iconsdir}/hicolor/scalable/apps/eekboard.svg
%{_desktopdir}/%{name}.desktop
%{_datadir}/dbus-1/services/eekboard-server.service

%files libs
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libeek*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeek*.so.[0-9]
%{_libdir}/girepository-1.0/Eek*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeek*.so
%{_includedir}/eek-0.90
%{_includedir}/eekboard-0.90
%{_datadir}/gir-1.0/Eek*.gir
%{_datadir}/vala/vapi/eek*.vapi
%{_pkgconfigdir}/eek*.pc
%{_gtkdocdir}/eek*

%files -n python-eekboard
%defattr(644,root,root,755)
%{py_sitescriptdir}/eekboard
