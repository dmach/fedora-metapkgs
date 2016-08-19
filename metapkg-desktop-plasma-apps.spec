Name:           metapkg-desktop-plasma-apps
Version:        1.1
Release:        1%{?dist}
Summary:        Applications for Plasma 5 desktop metapackage

Group:          Metapackages
License:        MIT


# metapackages
Requires:       metapkg-desktop-xorg

# kde apps
Requires:       dolphin
Requires:       gwenview
Requires:       kate
Requires:       kcalc
Requires:       kde-baseapps
Requires:       kdepasswd
Requires:       konsole5
Requires:       konversation
Requires:       kscreen
Requires:       ksnapshot
Requires:       ksysguardd
Requires:       kwalletmanager5
Requires:       kwrite
Requires:       okular
Requires:       psi


%description
Install applications for Plasma 5 desktop.


%posttrans
systemctl set-default graphical
systemctl enable sddm.service


%files


%changelog
* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add gwenview.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
