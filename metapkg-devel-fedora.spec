Name:           metapkg-devel-fedora
Version:        1.0
Release:        1%{?dist}
Summary:        Fedora development metapackage

Group:          Metapackages
License:        MIT


# metapackage
Requires:       metapkg-devel-rpm

Requires:       bodhi-client
Requires:       fedora-cert
Requires:       fedpkg
Requires:       koji
Requires:       mock
Requires:       packagedb-cli


%description
Install packages for developing Fedora packages.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
