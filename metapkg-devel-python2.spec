Name:           metapkg-devel-python2
Version:        1.3
Release:        1%{?dist}
Summary:        Python2 development metapackage

Group:          Metapackages
License:        MIT


Requires:       python2-pip
Requires:       python2-pylint
Requires:       python2-setuptools
Requires:       python2-tools
Requires:       python2-virtualenv

Provides:       metapkg-devel-python
Obsoletes:      metapkg-devel-python <= 1.1


%description
Install packages for developing Python2 applications.


%files


%changelog
* Fri Jul 19 2019 Daniel Mach <daniel.mach@gmail.com> - 1.3-1
- Update package names to match the latest Fedora.
- Drop python2-flake8 as it's no longer available.

* Sun Mar 19 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Split into -python2 and python3 standalone metapackages.

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require python-flake8 instead python2-flake8 on Fedora 23.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
