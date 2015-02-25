Name            : x2vnc
Summary         : A dual-screen hack for one keyboard and mouse on two machines
Summary(pl.UTF-8): Program umożliwiający pracę jedną klawiaturą i myszką na dwóch komputerach
Version         : 1.7.2
Release         : 14_%{BUILD_NUMBER}
BuildRequires   : libX11-devel, autoconf, automake
# BuildRequires : XFree86-devel, autoconf, automake
Prefix          : /usr/local/bin
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

License         : GPL
Group           : X11/Applications/Networking
Packager        : PoiXson <support@poixson.com>
Source0         : http://fredrik.hubbe.net/x2vnc/%{name}-%{version}.tar.gz
# Source0-md5   : f23f86bcfa12a80eaeb886ab9b3ee447
URL             : http://fredrik.hubbe.net/x2vnc.html

%description
This program will let you use two screens on two different computers
as if they were connected to the same computer. Even if one of the
computers runs Windows 95/98/NT and the other one runs X-Window. If
they are both running Windows, you probably want to use Win2VNC
instead.

%description -l pl.UTF-8
Program umożliwia korzystanie z dwóch ekranów na dwóch różnych
maszynach, tak jakby były podłączone do tego samego komputera. Nawet
jeżeli jeden z komputerów korzysta z Windows 95/98/NT a drugi z
X-Window. Jeżeli oba korzystają z Windows, prawdopodobnie lepiej
będzie użyć Win2VNC.



%prep
%setup -q



%build
%{__aclocal}
chmod +x "%{_topdir}/BUILD/%{name}-%{version}/configure"
%{__autoconf}



%configure --without-xf86dga
%{__make} %{?_smp_mflags}



%install
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*".${RPM_ARCH}.rpm"
%{__rm} -fv "%{_rpmdir}/%{name}-"*".src.rpm"
# build installables
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__install} -d ${RPM_BUILD_ROOT}%{_mandir}
%{__make} install DESTDIR=${RPM_BUILD_ROOT}



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root!"
fi



%files
%defattr(644,root,root,755)
%doc README ChangeLog COPYING
%attr(755,root,root) %{_bindir}/x2vnc
%{_mandir}/man*/*



%changelog
* Mon Oct 06 2014 LorenzoP <lorenzo@poixson.com> - 1.7.2-14
- Rebuilt for http://yum.poixson.com/

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.7.2-9
- Fix %%patch without corresponding "Patch:" tag error which broke the build.

* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.7.2-8
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.7.2-7
- Autorebuild for GCC 4.3

* Sun Mar 04 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-6
- Fixed a bug in spec

* Sun Mar 04 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-5
- Cleaned up spec file

* Sat Mar 03 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-4
- Removed ls and pwd from spec (was used for debugging).

* Sat Feb 24 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-3
- Fixing a few more items presented in Bug #228434.

* Tue Feb 20 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-2
- Fixing Items presented in Bug #228434.

* Mon Feb 12 2007 Michael Stahnke <mastahnke@gmail.com> - 1.7.2-1
- Initial packaging.

