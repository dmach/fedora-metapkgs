Name:           metapkg-tools-filesystem
Version:        1.1
Release:        1%{?dist}
Summary:        Filesystem tools metapackage

Group:          Metapackages
License:        MIT


Requires:       btrfs-progs
Requires:       cryptsetup
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       f2fs-tools
Requires:       fuse-sshfs
Requires:       gpart
Requires:       hddtemp
Requires:       hdparm
Requires:       kpartx
Requires:       lvm2
Requires:       mdadm
Requires:       nfs-utils
Requires:       ntfsprogs
Requires:       nvme-cli
Requires:       smartmontools
Requires:       xfsprogs


%description
Install tools to mount, format or repair file systems.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add btrfs-progs, cryptsetup, dosfstools, e2fsprogs, f2fs-tools, fuse-sshfs, hddtemp, mdadm, nvme-cli, xfsprogs

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
