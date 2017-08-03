Name:      onemetre-tng-server
Version:   1.4
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-feedparser, python3-warwickobservatory, onemetre-obslog-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

tngd is a Pyro frontend for querying the TNG weather feed via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/tngd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/tngd.service %{buildroot}%{_unitdir}

%pre
%service_add_pre tngd.service

%post
%service_add_post tngd.service

%preun
%stop_on_removal tngd.service
%service_del_preun tngd.service

%postun
%restart_on_update tngd.service
%service_del_postun tngd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/tngd
%defattr(-,root,root,-)
%{_unitdir}/tngd.service

%changelog
