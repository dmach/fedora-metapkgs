Name:           confpkg-powersave
Version:        1.0
Release:        1%{?dist}
Summary:        Power saving configuration

Group:          Metapackages
License:        MIT

BuildRequires:  systemd


%description
Power saving configuration


%build
# Disable NMI watchdog; interrupts can increase power consumption
cat > kernel_nmi_watchdog.conf << EOF
kernel.nmi_watchdog = 0
EOF


# Increase writeback time to aggregate disk writes
cat > vm_dirty_writeback_centisecs.conf << EOF
vm.dirty_writeback_centisecs = 6000
EOF


# Decrease swappiness to avoid disk writes
cat > vm_swappiness.conf << EOF
vm.swappiness = 20
EOF


# Set link_power_management_policy to med_power_with_dipm
# saves ~ 1.5W
cat > hd_power_save.rules << EOF
ACTION=="add", SUBSYSTEM=="scsi_host", KERNEL=="host*", ATTR{link_power_management_policy}="med_power_with_dipm"
EOF


# Turn pcie_aspm policy to powersave
# saves ~ 0.5W
cat > pcie_aspm_powersave.service << EOF
[Unit]
Description=Set pcie_aspm policy to powersave

[Service]
User=root
Type=oneshot
RemainAfterExit=yes
ExecStart=sh -c 'echo powersave > /sys/module/pcie_aspm/parameters/policy'
ExecStop=sh -c 'echo default > /sys/module/pcie_aspm/parameters/policy'

[Install]
WantedBy=multi-user.target
EOF


%install
install -Dpm 644 kernel_nmi_watchdog.conf %{buildroot}%{_sysconfdir}/sysctl.d/kernel_nmi_watchdog.conf
install -Dpm 644 vm_dirty_writeback_centisecs.conf %{buildroot}%{_sysconfdir}/sysctl.d/vm_dirty_writeback_centisecs.conf
install -Dpm 644 vm_swappiness.conf %{buildroot}%{_sysconfdir}/sysctl.d/vm_swappiness.conf
install -Dpm 644 hd_power_save.rules %{buildroot}%{_sysconfdir}/udev/rules.d/hd_power_save.rules
install -Dpm 644 pcie_aspm_powersave.service %{buildroot}%{_unitdir}/pcie_aspm_powersave.service


%post
%systemd_post pcie_aspm_powersave.service


%preun
%systemd_preun pcie_aspm_powersave.service


%files
%{_sysconfdir}/sysctl.d/*
%{_sysconfdir}/udev/rules.d/*
%{_unitdir}/*


%changelog
* Tue Apr 07 2020 Daniel Mach <daniel.mach@gmail.com> - 1.0-1
- Initial package
