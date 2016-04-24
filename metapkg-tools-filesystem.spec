Name:           metapkg-tools-filesystem
Version:        1.0
Release:        1%{?dist}
Summary:        Filesystem tools metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:       gpart
Requires:       hdparm
Requires:       kpartx
Requires:       lvm2
Requires:       nfs-utils
Requires:       ntfsprogs
Requires:       smartmontools


%description
Install tools to mount, format or repair file systems.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
