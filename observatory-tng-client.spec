Name:      observatory-tng-client
Version:   2.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

tng is a commandline utility that queries the TNG weather feed daemon.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/tng %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/tng %{buildroot}/etc/bash_completion.d/tng

%files
%defattr(0755,root,root,-)
%{_bindir}/tng
/etc/bash_completion.d/tng

%changelog
