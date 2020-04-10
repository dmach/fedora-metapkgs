Name:           metapkg-system-core
Version:        1.2
Release:        1%{?dist}
Summary:        System core metapackage

Group:          Metapackages
License:        MIT


# file system hierarchy
Requires:       basesystem
Requires:       filesystem
Requires:       setup
Requires:       rootfiles

# core packages
Requires:       audit
Requires:       bash
Requires:       coreutils
Requires:       glibc
Requires:       glibc-langpack-en
Requires:       glibc-minimal-langpack
Requires:       NetworkManager
Requires:       openssh-server
Requires:       pam
Requires:       passwd
Requires:       plymouth-theme-spinner
Requires:       selinux-policy-targeted
Requires:       systemd
Requires:       util-linux


%description
Install system core packages.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Require audit, glibc-minimal-langpack, passwd, plymouth-theme-spinner
- Drop cryptsetup, lvm2 (moved to metapkg-tools-filesystem)

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require glibc-langpack-en only on Fedora >= 24

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
