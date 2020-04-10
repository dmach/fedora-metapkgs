Name:           metapkg-devel-c
Version:        1.0
Release:        1%{?dist}
Summary:        C and C++ development metapackage

Group:          Metapackages
License:        MIT


# compiler
Requires:       annobin
Requires:       ccache
# clang-format
Requires:       clang
# clang-tidy
Requires:       clang-tools-extra
Requires:       gcc
Requires:       gcc-c++
Requires:       gcc-gdb-plugin

# sanitizers
Requires:       libasan-static
Requires:       liblsan-static
Requires:       libubsan-static

# build tools
Requires:       cmake
Requires:       make

# debugging
Requires:       gdb
Requires:       strace


%description
Install packages for developing Python3 applications.


%files


%changelog
* Sun Mar  1 2020 Daniel Mach <daniel.mach@gmail.com> - 1.3-1
- Initial package
