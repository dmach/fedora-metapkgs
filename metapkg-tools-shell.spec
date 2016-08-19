Name:           metapkg-tools-shell
Version:        1.0
Release:        1%{?dist}
Summary:        Shell tools metapackage

Group:          Metapackages
License:        MIT


# shell
Requires:       bash-completion
Requires:       openssh-clients
Requires:       screen
Requires:       sudo

# tools
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
Requires:       time
Requires:       usbutils

# networking
Requires:       wireless-tools

# doc readers
Requires:       info
Requires:       man-pages

# packaging
Requires:       rpm
Requires:       dnf
Requires:       dnf-langpacks
Requires:       dnf-plugins-core
Recommends:     rpmconf
Recommends:     rpmreaper

# editor
Requires:       vim-minimal
Recommends:     vim-enhanced


%description
Install shell tools.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
