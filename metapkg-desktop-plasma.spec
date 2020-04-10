Name:           metapkg-desktop-plasma
Version:        1.3
Release:        1%{?dist}
Summary:        Plasma 5 desktop metapackage

Group:          Metapackages
License:        MIT


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
Requires:       kde-gtk-config
Requires:       kde-settings-pulseaudio

# display
Requires:       colord-kde

# sound
Requires:       phonon-qt5
Requires:       phonon-qt5-backend-gstreamer

# bluetooth support
Requires:       bluedevil

# display manager
Requires:       sddm
Requires:       sddm-breeze
Requires:       sddm-kcm

# libreoffice - plasma gui
Requires:       (libreoffice-kf5 if libreoffice-core)


%description
Install Plasma 5 desktop.


%posttrans
systemctl set-default graphical
systemctl enable sddm.service


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.3-1
- Require colord-kde, phonon-qt5, phonon-qt5-backend-gstreamer, libreoffice-kf5
- Drop kcm-gtk, kcm_systemd, kde-style-breeze

* Sun Dec 25 2016 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Fix kde-gtk-config dependency on f25.

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add bluedevil.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
