Summary:	An Easy-to-use Virtual Keyboard Toolkit
Summary(pl.UTF-8):	Łatwy w użyciu toolkit wirtualnej klawiatury
Name:		eekboard
Version:	1.0.8
Release:	7
License:	LGPL v2+ (libraries), GPL v3+ (programs)
Group:		Applications/System
#Source0Download: https://github.com/ueno/eekboard/downloads
Source0:	http://github.com/downloads/ueno/eekboard/%{name}-%{version}.tar.gz
# Source0-md5:	83584689cd3353d2f471d01f4f5f2efd
URL:		http://fedorahosted.org/eekboard/
BuildRequires:	at-spi2-core-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libcroco-devel >= 0.6
BuildRequires:	libxklavier-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eekboard is a virtual keyboard software package, including a set of
tools to implement desktop virtual keyboards.

%description -l pl.UTF-8
eekboard to pakiet oprogramowania wirtualnej klawiatury, zawierający
zestaw narzędzi do implementowania graficznych wirtualnych klawiatur.

%package libs
Summary:	Runtime libraries for eekboard
Summary(pl.UTF-8):	Biblioteki współdzielone eekboard
License:	LGPL v2+
Group:		Libraries
Requires:	glib2 >= 1:2.26.0
Obsoletes:	python-eekboard

%description libs
This package contains the libraries for eekboard.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki eekboard.

%package devel
Summary:	Development files for eekboard
Summary(pl.UTF-8):	Pliki programistyczne bibliotek eekboard
License:	LGPL v2+ (libraries), FDL v1.3+ (documentation)
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+3-devel >= 3.0
Requires:	libxklavier-devel

%description devel
This package contains the development files for eekboard.

%description devel -l pl.UTF-8
Pliki programistyczne bibliotek eekboard.

%package -n vala-eekboard
Summary:	Vala API for eekboard libraries
Summary(pl.UTF-8):	API języka Vala do bibliotek eekboard
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.10.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-eekboard
Vala API for eekboard libraries.

%description -n vala-eekboard -l pl.UTF-8
API języka Vala do bibliotek eekboard.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-atspi \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%attr(755,root,root) %{_bindir}/eekboard
%attr(755,root,root) %{_bindir}/eekboard-server
%attr(755,root,root) %{_libexecdir}/eekboard-setup
%{_datadir}/eekboard
%{_datadir}/dbus-1/services/eekboard-server.service
%{_datadir}/glib-2.0/schemas/org.fedorahosted.eekboard.gschema.xml
%{_iconsdir}/hicolor/*/apps/eekboard.png
%{_iconsdir}/hicolor/scalable/apps/eekboard.svg
%{_desktopdir}/%{name}.desktop

%files libs
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libeek.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeek.so.0
%attr(755,root,root) %{_libdir}/libeek-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeek-gtk.so.0
%attr(755,root,root) %{_libdir}/libeek-xkl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeek-xkl.so.0
%attr(755,root,root) %{_libdir}/libeekboard.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeekboard.so.0
%{_libdir}/girepository-1.0/Eek-0.90.typelib
%{_libdir}/girepository-1.0/EekGtk-0.90.typelib
%{_libdir}/girepository-1.0/EekXkl-0.90.typelib
%{_libdir}/girepository-1.0/Eekboard-0.90.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeek.so
%attr(755,root,root) %{_libdir}/libeek-gtk.so
%attr(755,root,root) %{_libdir}/libeek-xkl.so
%attr(755,root,root) %{_libdir}/libeekboard.so
%{_includedir}/eek-0.90
%{_includedir}/eekboard-0.90
%{_datadir}/gir-1.0/Eek-0.90.gir
%{_datadir}/gir-1.0/EekGtk-0.90.gir
%{_datadir}/gir-1.0/EekXkl-0.90.gir
%{_datadir}/gir-1.0/Eekboard-0.90.gir
%{_pkgconfigdir}/eek-0.90.pc
%{_pkgconfigdir}/eek-gtk-0.90.pc
%{_pkgconfigdir}/eek-xkl-0.90.pc
%{_pkgconfigdir}/eekboard-0.90.pc
%{_gtkdocdir}/eek
%{_gtkdocdir}/eekboard

%files -n vala-eekboard
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/eek-0.90.deps
%{_datadir}/vala/vapi/eek-0.90.vapi
%{_datadir}/vala/vapi/eek-gtk-0.90.deps
%{_datadir}/vala/vapi/eek-gtk-0.90.vapi
%{_datadir}/vala/vapi/eek-xkl-0.90.deps
%{_datadir}/vala/vapi/eek-xkl-0.90.vapi
