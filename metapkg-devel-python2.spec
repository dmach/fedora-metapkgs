Name:           metapkg-devel-python2
Version:        1.2
Release:        1%{?dist}
Summary:        Python2 development metapackage

Group:          Metapackages
License:        MIT


Requires:       python-tools
Requires:       python-virtualenv
Requires:       python-pip
Requires:       python2-setuptools
%if 0%{?fedora} == 23
Requires:       python-flake8
%else
Requires:       python2-flake8
%endif

Requires:       pylint

Provides:       metapkg-devel-python
Obsoletes:      metapkg-devel-python <= 1.1


%description
Install packages for developing Python2 applications.


%files


%changelog
* Sun Mar 19 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Split into -python2 and python3 standalone metapackages.

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require python-flake8 instead python2-flake8 on Fedora 23.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
