Name:           metapkg-desktop-plasma-apps
Version:        1.2
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
%if 0%{fedora} && 0%{?fedora} <= 25
Requires:       kdepasswd
%endif
Requires:       konsole5
Requires:       konversation
Requires:       kscreen
%if 0%{fedora} && 0%{?fedora} <= 25
Requires:       ksnapshot
%else
Requires:       spectacle
%endif
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
* Sun Mar 19 2017 Daniel Mach <daniel.mach@gmail.com> - 1.2-1
- Remove kdepasswd on Fedora >= 26
- Replace ksnapshot with spectacle on Fedora >= 26

* Fri Jun 17 2016 Daniel Mach <daniel.mach@gmail.com> - 1.1-1
- Add gwenview.

* Sun Apr 24 2016 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
