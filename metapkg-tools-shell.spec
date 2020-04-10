Name:           metapkg-tools-shell
Version:        1.2
Release:        1%{?dist}
Summary:        Shell tools metapackage

Group:          Metapackages
License:        MIT


# shell
Requires:       bash-completion
Requires:       openssh-clients
Requires:       screen
Requires:       sudo
Requires:       tmux

# tools
Requires:       alsa-utils
Requires:       chrony
Requires:       dmidecode
Requires:       dos2unix
Requires:       gpm
Requires:       hardlink
Requires:       htop
Requires:       kbd
Requires:       lsof
Requires:       mc
Requires:       pciutils
Requires:       pinentry
Requires:       psmisc
Requires:       time
Requires:       usbutils

# doc readers
Requires:       info
Requires:       man-db
Requires:       man-pages

# packaging
Requires:       fwupd
Requires:       rpm
Requires:       dnf
Requires:       dnf-plugins-core
Requires:       dnf-utils
Recommends:     rpmconf
Requires:       rpmreaper

# editor
Requires:       vim-minimal
Requires:       vim-enhanced

# compression
Requires:       bzip2
Requires:       gzip
Requires:       lz4
Requires:       tar
Requires:       xz
Requires:       zstd


%description
Install shell tools.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Require alsa-utils, dnf-utils, fwupd, man-db, pinentry, psmisc, tmux, vim-enhanced
- Require bzip2, gzip, lz4, tar, xz, zstd
- Drop wireless-tools

* Sun Dec 25 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Remove dnf-langpacks dependency on fedora >= 25.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
