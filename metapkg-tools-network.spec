Name:           metapkg-tools-network
Version:        1.1
Release:        1%{?dist}
Summary:        Network tools metapackage

Group:          Metapackages
License:        MIT


Requires:       bind-utils
Requires:       curl
Requires:       iproute
Requires:       iputils
Requires:       links
Requires:       minicom
Requires:       mtr
Requires:       net-tools
Requires:       nftables
Requires:       nmap
Requires:       rsync
Requires:       tcpdump
Requires:       telnet
Requires:       tftp
Requires:       traceroute
Requires:       wget
Requires:       whois
Requires:       wireless-tools
Requires:       wpa_supplicant


%description
Install network tools packages.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require iproute, iputils, nftables, rsync, wpa_supplicant
- Drop ebtables, iptables

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
