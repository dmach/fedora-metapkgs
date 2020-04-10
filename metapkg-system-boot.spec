Name:           metapkg-system-boot
Version:        1.1
Release:        1%{?dist}
Summary:        System boot metapackage

Group:          Metapackages
License:        MIT

Requires:       efibootmgr
Requires:       grub2
Requires:       grubby
Requires:       grub2-efi-x64
Requires:       shim-x64


%description
Install packages required for system boot.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require efibootmgr, grub2-efi-x64, shim-x64
- Drop grub2, grubby

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
