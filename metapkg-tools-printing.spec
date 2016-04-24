Name:           metapkg-tools-printing
Version:        1.0
Release:        1%{?dist}
Summary:        Printing tools metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# cups
Requires:       cups
Requires:       cups-filters


%description
Install printing tools.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
