%define debug_package %{nil}

%define commit a649f2a

Summary:	Nagios plugin - check_ram
Name:		nagios-plugins-ram
Version:	2.0
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		https://github.com/thesharp/nagios-plugins
Source0:	thesharp-nagios-plugins-%{commit}.tar.gz
Requires:	nagios-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A plugin for nagios that will check RAM.

%prep
%setup -q -n thesharp-nagios-plugins-%{commit}
# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" check_ram

%build

%install
rm -rf %{buildroot}
install -D -p -m 0755 check_ram %{buildroot}%{_libdir}/nagios/plugins/check_ram

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/nagios/plugins/check_ram

%changelog
* Wed Jul 11 2012  Ilya A. Otyutskiy <sharp@thesharp.ru> - 2.0-1.vortex
- New upstream release.

* Thu Sep 22 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.0-1.vortex
- Initial packaging for Enterprise Linux.

