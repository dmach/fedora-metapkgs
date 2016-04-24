Name:           metapkg-devel-python
Version:        1.0
Release:        1%{?dist}
Summary:        Python development metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:       python-tools

Requires:       python-virtualenv
Requires:       python3-virtualenv

Requires:       python-pip
Requires:       python3-pip

Requires:       python2-setuptools
Requires:       python3-setuptools

Requires:       python2-flake8
Requires:       python3-flake8

Requires:       pylint
Requires:       python3-pylint


%description
Install packages for developing Python applications.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
