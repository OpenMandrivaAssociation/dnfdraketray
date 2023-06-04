%global gb3_ver %(gbc3 -V || echo 3.18.2)

Summary:	Icon tray for dnfdrake
Name:		dnfdraketray
Version:	2.0.8
Release:	3
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		https://mib.pianetalinux.org
#URL:		https://github.com/astrgl/dnfdraketray
Source0:	https://github.com/astrgl/dnfdraketray/archive/%{version}/%{name}-%{version}.tar.gz
#Patch0:		dnfdraketray-2.0.8-fix_icon_name.patch
#Patch1:		dnfdraketray-2.0.8-fix_desktop_file.patch
#Patch2:		dnfdraketray-2.0.8-fix_icon_path.patch

BuildRequires:	gambas3-devel
BuildRequires:	gambas3-gb-dbus
BuildRequires:	gambas3-gb-form
BuildRequires:	gambas3-gb-form-stock
BuildRequires:	gambas3-gb-gtk3
BuildRequires:	gambas3-gb-gui
BuildRequires:	gambas3-gb-image
BuildRequires:	gambas3-gb-qt5
BuildRequires:	imagemagick

Requires:	sudo
Requires:	createrepo_c
Requires:	dnf-utils
Requires:	gambas3-runtime = %{gb3_ver}
Requires:	gambas3-devel
Requires:	gambas3-gb-dbus
Requires:	gambas3-gb-form
Requires:	gambas3-gb-form-stock
Requires:	gambas3-gb-gtk3
Requires:	gambas3-gb-gui
Requires:	gambas3-gb-image
Requires:	gambas3-gb-qt5
Requires:	lsb-release
Requires:	python-dnf-plugin-versionlock
Requires:	xrandr

BuildArch: noarch

%files
%license FILE-EXTRA/license
%{_bindir}/%{name}.gambas
%{_datadir}/dnfdrake/%{name}.desktop

#---------------------------------------------------------------------------

%description
Icon tray for dnfdrake.

%prep
%autosetup -p1

%build
gbc3 -e -a -g -t -f public-module -f public-control -j%{?_smp_mflags}
gba3

# unversion binary
mv %{name}-%{version}.gambas %{name}.gambas

%install
# binary
install -Dm 0755 %{name}.gambas -t %{buildroot}/%{_bindir}/

#.desktop used by dnfdrake
install -Dm 0755 FILE-EXTRA/%{name}.desktop -t %{buildroot}/%{_datadir}/dnfdrake/

