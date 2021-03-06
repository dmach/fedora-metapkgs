Name:           metapkg-desktop-xorg
Version:        1.2
Release:        1%{?dist}
Summary:        Xorg metapackage

Group:          Metapackages
License:        MIT


# server
Requires:       xorg-x11-server-Xorg
Requires:       xorg-x11-xinit

# utils
%if 0%{?fedora} && 0%{?fedora} <= 34
Requires:       xorg-x11-server-utils
%else
Requires:       xrandr
%endif

# Touchpad/Mouse support
Requires:       xorg-x11-drv-libinput
Requires:       xorg-x11-drv-evdev
# Graphic drivers
Requires:       libva-vdpau-driver
Requires:       mesa-dri-drivers
Requires:       mesa-vdpau-drivers
Requires:       xorg-x11-drv-amdgpu
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
* Fri Apr  2 2021 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Require xrandr instead of xorg-x11-server-utils on fedora >= 35

* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Require libva-vdpau-driver, mesa-vdpau-drivers, xorg-x11-drv-amdgpu, xorg-x11-xinit

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
