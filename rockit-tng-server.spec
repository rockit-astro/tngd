Name:      rockit-tng-server
Version:   %{_version}
Release:   1
Url:       https://github.com/rockit-astro/tngd
Summary:   TNG weather feed client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-requests python3-rockit-common

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/tngd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/tngd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/tngd
%defattr(-,root,root,-)
%{_unitdir}/tngd.service

%changelog
