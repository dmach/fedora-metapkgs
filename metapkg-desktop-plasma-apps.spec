Name:           metapkg-desktop-plasma-apps
Version:        1.4
Release:        1%{?dist}
Summary:        Applications for Plasma 5 desktop metapackage

Group:          Metapackages
License:        MIT


# metapackages
Requires:       metapkg-desktop-xorg

# kde apps
Requires:       ark
Requires:       dolphin
Requires:       dragon
Requires:       gwenview
Requires:       kate
Requires:       kate-plugins
Requires:       kcalc
Requires:       kde-baseapps
Requires:       konsole5
Requires:       konversation
Requires:       kscreen
Requires:       ksysguardd
Requires:       kwalletmanager5
Requires:       kwrite
Requires:       okular
Requires:       psi
Requires:       spectacle


%description
Install applications for Plasma 5 desktop.


%posttrans
systemctl set-default graphical
systemctl enable sddm.service


%files


%changelog
* Fri Apr  2 2021 Daniel Mach <daniel.mach@gmail.com> - 1.4-1
- Require arg, dragon

* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.3-1
- Require kate-plugins, spectacle
- Drop kdepasswd, ksnapshot

* Sun Mar 19 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Remove kdepasswd on Fedora >= 26
- Replace ksnapshot with spectacle on Fedora >= 26

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add gwenview.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
