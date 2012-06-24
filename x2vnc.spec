Summary:	A dual-screen hack for one keyboard and mouse on two machines
Summary(pl):	Program umo�liwiaj�cy prac� jedn� klawiatur� i myszk� na dw�ch komputerach
Name:		x2vnc
Version:	1.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.gz
# Source0-md5:	b0804c9078ab3537943f29a02deccfd9
URL:		http://fredrik.hubbe.net/x2vnc.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will let you use two screens on two different computers
as if they were connected to the same computer. Even if one of the
computers runs Windows 95/98/NT and the other one runs X-Window. If
they are both running Windows, you probably want to use Win2VNC
instead.

%description -l pl
Program umo�liwia korzystanie z dw�ch ekran�w na dw�ch r�nych
maszynach, tak jakby by�y pod��czone do tego samego komputera. Nawet
je�eli jeden z komputer�w korzysta z Windows 95/98/NT a drugi z
X-Window. Je�eli oba korzystaj� z Windows, prawdopodobnie lepiej
b�dzie u�y� Win2VNC.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x2vnc
%{_mandir}/man*/*
