# TODO: install and package init script?
%define	selinux_ver	3.8
Summary:	SELinux sandbox utilities
Summary(pl.UTF-8):	Narzędzia do obsługi piaskownic SELinuksa
Name:		selinux-sandbox
Version:	3.8
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	59452fc4a05e08e36450efac23e575b1
Patch0:		%{name}-init.patch
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	libcap-ng-devel
BuildRequires:	libselinux-devel >= %{selinux_ver}
BuildRequires:	rpm-pythonprov
Requires:	libselinux >= 3.7
# uses "policycoreutils" translations domain
Requires:	policycoreutils >= %{selinux_ver}
Requires:	python3-selinux >= %{selinux_ver}
Requires:	python3-sepolicy >= %{selinux_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains SELinux sandbox utilities.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera narzędzia do obsługi piaskownic SELinuksa.

%prep
%setup -q
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install -Dp sandbox.init $RPM_BUILD_ROOT/etc/rc.d/init.d/sandbox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sandbox
%attr(755,root,root) %{_sbindir}/seunshare
#%attr(754,root,root) /etc/rc.d/init.d/sandbox
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/sandbox
%dir %{_datadir}/sandbox
%attr(755,root,root) %{_datadir}/sandbox/*.sh
%attr(755,root,root) %{_datadir}/sandbox/start
%{_mandir}/man5/sandbox.5*
%{_mandir}/man8/sandbox.8*
%{_mandir}/man8/seunshare.8*
