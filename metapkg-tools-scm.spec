Name:           metapkg-tools-scm
Version:        1.0
Release:        1%{?dist}
Summary:        SCM tools metapackage

Group:          Metapackages
License:        MIT


# shell
Requires:       git
Requires:       subversion
Suggests:       cvs
Suggests:       mercurial


%description
Install Source Control Management tools.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
