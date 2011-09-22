%define debug_package %{nil}

Summary:	Nagios plugin - check_ram
Name:		nagios-plugins-ram
Version:	1.0
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Applications/System
URL:		http://thesharp.ru/nagios-plugins/
Source0:	http://thesharp.ru/nagios-plugins/crond/nagios-plugins-ram-%{version}.tar.gz
Requires:	nagios-plugins
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A plugin for nagios that will check RAM.

%prep
%setup -q -n nagios-plugins-ram-%{version}
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
%doc LICENSE ChangeLog
%{_libdir}/nagios/plugins/check_ram

%changelog
* Thu Sep 22 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.0-1.vortex
- Initial packaging for Enterprise Linux.

