Name:      observatory-tng-client
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/tngd
Summary:   TNG weather feed client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common

%description

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
