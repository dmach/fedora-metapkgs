Name:           metapkg-tools-network
Version:        1.0
Release:        1%{?dist}
Summary:        Network tools metapackage

Group:          Metapackages
License:        MIT


Requires:       bind-utils
Requires:       curl
Requires:       ebtables
Requires:       iptables
Requires:       links
Requires:       minicom
Requires:       mtr
Requires:       net-tools
Requires:       nmap
Requires:       tcpdump
Requires:       telnet
Requires:       tftp
Requires:       traceroute
Requires:       wget
Requires:       whois
Requires:       wireless-tools


%description
Install network tools packages.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
