Name:           metapkg-system-core
Version:        1.1
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
%if 0%{?fedora} >= 24
Requires:       glibc-langpack-en
%endif
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
* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require glibc-langpack-en only on Fedora >= 24

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
