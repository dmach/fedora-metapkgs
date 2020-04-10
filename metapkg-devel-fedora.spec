Name:           metapkg-devel-fedora
Version:        1.1
Release:        1%{?dist}
Summary:        Fedora development metapackage

Group:          Metapackages
License:        MIT


# metapackage
Requires:       metapkg-devel-rpm

Requires:       bodhi-client
Requires:       copr-cli
Requires:       fedpkg
Requires:       koji
Requires:       mock


%description
Install packages for developing Fedora packages.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require copr-cli
- Drop fedora-cert, packagedb-cli

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
