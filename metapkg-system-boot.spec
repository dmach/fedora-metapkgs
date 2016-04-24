Name:           metapkg-system-boot
Version:        1.0
Release:        1%{?dist}
Summary:        System boot metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# kernel
Requires:       grub2
Requires:       grubby


%description
Install packages required for system boot.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
