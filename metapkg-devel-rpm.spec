Name:           metapkg-devel-rpm
Version:        1.0
Release:        1%{?dist}
Summary:        RPM development metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:       redhat-rpm-config
Requires:       rpm-build
Requires:       rpmdevtools
Requires:       rpmlint


%description
Install packages for developing RPM packages.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
