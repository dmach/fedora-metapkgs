Name:           metapkg-desktop-gnomeshell
Version:        1.0
Release:        1%{?dist}
Summary:        Gnome Shell 3 desktop metapackage

Group:          Metapackages
License:        MIT


# metapackages
Requires:       metapkg-desktop-xorg

# gnome shell
Requires:       gnome-desktop3
Requires:       gnome-keyring
Requires:       gnome-menus
Requires:       gnome-screensaver
Requires:       gnome-session-xsession
Requires:       gnome-shell

# NetworkManager support
Requires:       NetworkManager-openvpn-gnome
Requires:       NetworkManager-vpnc-gnome

# extensions
Requires:       gnome-shell-extension-alternate-tab
Requires:       gnome-shell-extension-apps-menu
Requires:       gnome-shell-extension-window-list
Requires:       gnome-tweak-tool

# display manager
Requires:       gdm

# weak deps
Recommends:     libreoffice-gtk3


%description
Install Gnome Shell 3 desktop packages.


%posttrans
systemctl set-default graphical
systemctl enable gdm.service


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
