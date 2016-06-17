Name:           metapkg-desktop-plasma
Version:        1.1
Release:        1%{?dist}
Summary:        Plasma 5 desktop metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# metapackages
Requires:       metapkg-desktop-xorg

# plasma
Requires:       plasma-breeze
Requires:       plasma-desktop
Requires:       plasma-nm
Requires:       plasma-nm-openvpn
Requires:       plasma-nm-vpnc
Requires:       plasma-pa
Requires:       plasma-systemsettings
Requires:       plasma-workspace
Requires:       plasma-workspace-drkonqi
Suggests:       plasma-workspace-wallpapers

# settings
Requires:       kcm-gtk
Requires:       kcm_systemd
Requires:       kde-settings-pulseaudio

# bluetooth support
Requires:       bluedevil

# breeze style for KDE 4
Requires:       kde-style-breeze

# display manager
Requires:       sddm
Requires:       sddm-breeze
Requires:       sddm-kcm

# weak deps
Recommends:     libreoffice-kde4


%description
Install Plasma 5 desktop.


%posttrans
systemctl set-default graphical
systemctl enable sddm.service


%files


%changelog
* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add bluedevil.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
