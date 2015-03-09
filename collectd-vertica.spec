Name:		collectd-vertica
Version:	0.0
Release:	0%{?dist}
Group:		Applications/System
Summary:	Collectd vertica plugin
License:	TBD
URL:		TODO:
Source0:	collectd-vertica.tar
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
# TODO: Add requires
Requires:	python
#Requires:	net-snmp-utils nagios-plugins-http

%description
# TODO: Be more verbose
Collectd plugin for vertica

%prep
%setup -q -n kra

%build

%install
# TODO: Deliver default config as well
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib64/collectd
cp -a vertica.py $RPM_BUILD_ROOT/usr/lib64/collectd/

#install -D -p monitoringplugin.py $RPM_BUILD_ROOT%{python_sitelib}/monitoringplugin.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755, root, root, -)
/usr/lib64/collectd/vertica.py*
#%attr(0644, root, root) %{python_sitelib}/monitoringplugin.py*

%changelog

* Mon Mar 09 2015 Matej Hasul <matej.hasul@gooddata.com> 0.0.0
- Initial package
