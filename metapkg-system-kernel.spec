Name:           metapkg-system-kernel
Version:        1.0
Release:        1%{?dist}
Summary:        System kernel metapackage

Group:          Metapackages
License:        MIT


# kernel
Requires:       kernel
Requires:       kernel-core
Requires:       kernel-modules
Requires:       linux-firmware

# firmware
Requires:       iwl3945-firmware
Requires:       iwl7260-firmware


%description
Install system kernel and firmware.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
