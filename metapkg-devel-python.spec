Name:           metapkg-devel-python
Version:        1.1
Release:        1%{?dist}
Summary:        Python development metapackage

Group:          Metapackages
License:        MIT


Requires:       python-tools

Requires:       python-virtualenv
Requires:       python3-virtualenv

Requires:       python-pip
Requires:       python3-pip

Requires:       python2-setuptools
Requires:       python3-setuptools

%if 0%{?fedora} == 23
Requires:       python-flake8
%else
Requires:       python2-flake8
%endif
Requires:       python3-flake8

Requires:       pylint
Requires:       python3-pylint


%description
Install packages for developing Python applications.


%files


%changelog
* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require python-flake8 instead python2-flake8 on Fedora 23.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
