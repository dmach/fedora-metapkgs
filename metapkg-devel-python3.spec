Name:           metapkg-devel-python3
Version:        1.2
Release:        1%{?dist}
Summary:        Python3 development metapackage

Group:          Metapackages
License:        MIT


Requires:       python3-tools
Requires:       python3-virtualenv
Requires:       python3-pip
Requires:       python3-setuptools
Requires:       python3-flake8
Requires:       python3-pylint


%description
Install packages for developing Python3 applications.


%files


%changelog
* Sun Mar 19 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Split into -python2 and python3 standalone metapackages.

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require python-flake8 instead python2-flake8 on Fedora 23.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
