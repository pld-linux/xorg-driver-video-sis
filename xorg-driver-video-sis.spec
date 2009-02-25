Summary:	X.org video driver for SiS and XGI video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych SiS i XGI
Name:		xorg-driver-video-sis
Version:	0.10.0
Release:	5
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
# Source0-md5:	331d432dccccca91ec7da39ff6bf1218
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-libdri >= 1.0.99.901
Requires:	xorg-xserver-libglx >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-sis < 1:7.0.0
Obsoletes:	XFree86-SiS
Obsoletes:	XFree86-driver-sis < 1:7.0.0
Obsoletes:	XFree86-driver-xgi < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for SiS and XGI video chips. It supports PCI, AGP
and PCIe video cards based on the following chipsets: SiS5597/5598,
SiS530/620, SiS6326/AGP/DVD (called old series), SiS300/305, SiS540,
SiS630/730 (called 300 series), SiS315/E/H/PRO, SiS550/551/552,
SiS650/651/661/741, SiS330 (Xabre), SiS760/761, XGI Volari V3/V5/V8,
XGI Volari Z7 (called 315/330/340 series).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych SiS i XGI. Obsługuje
karty PCI, AGP i PCIe oparte na następujących układach: SiS5597/5598,
SiS530/620, SiS6326/AGP/DVD (zwanych starą serią), SiS300/305, SiS540,
SiS630/730 (zwanych serią 300), SiS315/E/H/PRO, SiS550/551/552,
SiS650/651/661/741, SiS330 (Xabre), SiS760/761, XGI Volari V3/V5/V8,
XGI Volari Z7 (zwanych serią 315/330/340).

%prep
%setup -q -n xf86-video-sis-%{version}

# https://bugs.freedesktop.org/show_bug.cgi?id=18304
sed -i -e 's|#define.*SIS_USE_BIOS_SCRATCH.*|#undef SIS_USE_BIOS_SCRATCH|g' src/sis.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sis_drv.so
%{_mandir}/man4/sis.4*
