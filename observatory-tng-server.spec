Name:      observatory-tng-server
Version:   2.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

tngd is a Pyro frontend for querying the TNG weather feed via http.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/tngd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/tngd.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre tngd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post tngd.service
%endif
%if 0%{?centos_ver}
%systemd_post tngd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal tngd.service
%service_del_preun tngd.service
%endif
%if 0%{?centos_ver}
%systemd_preun tngd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update tngd.service
%service_del_postun tngd.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart tngd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/tngd
%defattr(-,root,root,-)
%{_unitdir}/tngd.service

%changelog
