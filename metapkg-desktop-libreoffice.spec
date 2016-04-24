Name:           metapkg-desktop-libreoffice
Version:        1.0
Release:        1%{?dist}
Summary:        LibreOffice metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:       libreoffice-calc
Requires:       libreoffice-impress
Requires:       libreoffice-opensymbol-fonts
Requires:       libreoffice-writer


%description
Install Libreoffice packages.



%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
