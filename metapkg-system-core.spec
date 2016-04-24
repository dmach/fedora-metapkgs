Name:           metapkg-system-core
Version:        1.0
Release:        1%{?dist}
Summary:        System core metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# file system hierarchy
Requires:       basesystem
Requires:       filesystem
Requires:       setup
Requires:       rootfiles

# core packages
Requires:       bash
Requires:       coreutils
Requires:       glibc
Requires:       glibc-langpack-en
Requires:       NetworkManager
Requires:       openssh-server
Requires:       pam
Requires:       selinux-policy-targeted
Requires:       systemd
Requires:       util-linux



%description
Install system core packages.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
