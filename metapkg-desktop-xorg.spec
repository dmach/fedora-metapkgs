Name:           metapkg-desktop-xorg
Version:        1.0
Release:        1%{?dist}
Summary:        Xorg metapackage

Group:          Metapackages
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# server
Requires:       xorg-x11-server-utils
Requires:       xorg-x11-server-Xorg

# Touchpad/Mouse support
Requires:       xorg-x11-drv-libinput
Requires:       xorg-x11-drv-evdev
# Graphic drivers
Requires:       mesa-dri-drivers
Requires:       xorg-x11-drv-ati
Requires:       xorg-x11-drv-intel
Requires:       xorg-x11-drv-nouveau
Requires:       xorg-x11-drv-vesa

# pulseaudio
Requires:       pulseaudio-module-x11

# NetworkManager support
Requires:       NetworkManager
Requires:       NetworkManager-wifi

# fonts
Requires:       abattis-cantarell-fonts
Requires:       dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts
Requires:       dejavu-serif-fonts
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       liberation-mono-fonts
Requires:       liberation-sans-fonts
Requires:       liberation-serif-fonts


%description
Install Xorg, drivers and fonts.


%files


%changelog
* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
