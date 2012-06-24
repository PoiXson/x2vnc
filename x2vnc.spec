Summary:	A dual-screen hack for one keyboard and mouse on two machines
Summary(pl):	Program umo�liwiaj�cy prac� jedn� klawaitur� i myszk� na dw�ch komptuerach
Name:		x2vnc
Version:	1.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.gz
# Source0-md5:	e4bb4dec31bc1b3b56d777bc365c9534
URL:		http://fredrik.hubbe.net/x2vnc.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will let you use two screens on two different computers
as if they were connected to the same computer. Even if one of the
computers runs Windows 95/98/NT and the other one runs X-window. If
they are both running Windows, you probably want to use Win2VNC
instead.

%description -l pl
Program umozliwia korzystanie z dw�ch ekran�w na dw�ch r�nych
maszynach tak jakby by�y pod��czone do tego samego komputera. Nawet
je�eli jeden z komputer�w korzysta z windows 95/98/NT a drugi z
X-window. Je�eli oba korzystaj� z windows, prawdopodobnie lepiej
by�oby skorzysta� z Win2VNC.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x2vnc
%{_mandir}/man*/*
