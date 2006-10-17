Summary:	X.org video driver for SiS and XGI video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych SiS i XGI
Name:		xorg-driver-video-sis
Version:	0.9.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sis-%{version}.tar.bz2
# Source0-md5:	66d9a4a3d168249f0e41f7f1fe8639e2
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
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for SiS and XGI video chips. It supports PCI, AGP
and PCIe video cards based on the following chipsets: SiS5597/5598,
SiS530/620, SiS6326/AGP/DVD (called old series), SiS300/305, SiS540,
SiS630/730 (called 300 series), SiS315/E/H/PRO, SiS550/551/552,
SiS650/651/661/741, SiS330 (Xabre), SiS760/761, XGI Volari V3/V5/V8,
XGI Volari Z7 (called 315/330/340 series).

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych SiS i XGI. Obs³uguje
karty PCI, AGP i PCIe oparte na nastêpuj±cych uk³adach: SiS5597/5598,
SiS530/620, SiS6326/AGP/DVD (zwanych star± seri±), SiS300/305, SiS540,
SiS630/730 (zwanych seri± 300), SiS315/E/H/PRO, SiS550/551/552,
SiS650/651/661/741, SiS330 (Xabre), SiS760/761, XGI Volari V3/V5/V8,
XGI Volari Z7 (zwanych seri± 315/330/340).

%prep
%setup -q -n xf86-video-sis-%{version}

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
