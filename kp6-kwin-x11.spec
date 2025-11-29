# TODO:
# - libhybris
#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	6.5.3
%define		kf_ver		6.5.0
%define		kp_ver		6.3.2
%define		qt_ver		6.7.0
%define		kpname		kwin-x11
#
Summary:	KDE Window manager
Summary(pl.UTF-8):	Zarządca okien KDE
Name:		kp6-%{kpname}
Version:	6.5.3
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	e4e24dc26913fe21c4e476051bdf5a9a
URL:		https://kde.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel >= 21.3
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Multimedia-devel >= %{qt_ver}
BuildRequires:	Qt6Qml-devel >= %{qt_ver}
BuildRequires:	Qt6Qt5Compat-devel >= %{qt_ver}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	Qt6Sensors-devel >= %{qt_ver}
BuildRequires:	Qt6Svg-devel >= %{qt_ver}
%if %{with tests}
BuildRequires:	Qt6Test-devel >= %{qt_ver}
%endif
BuildRequires:	Qt6UiTools-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	hwdata
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-kauth-devel >= %{kf_ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kcolorscheme-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kcrash-devel >= %{kf_ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kdeclarative-devel >= %{kf_ver}
BuildRequires:	kf6-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kidletime-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-kirigami-devel >= %{kf_ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf6-knotifications-devel >= %{kf_ver}
BuildRequires:	kf6-kpackage-devel >= %{kf_ver}
BuildRequires:	kf6-krunner-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-ksvg-devel >= %{kf_ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kp6-breeze-devel >= 5.23.0
BuildRequires:	kp6-kdecoration-devel >= %{kp_ver}
BuildRequires:	kp6-kglobalacceld-devel
%if %{with tests}
BuildRequires:	kp6-kpipewire-devel
%endif
BuildRequires:	kp6-kscreenlocker-devel
BuildRequires:	kp6-libplasma-devel >= %{kp_ver}
BuildRequires:	kp6-plasma-activities-devel >= %{kp_ver}
BuildRequires:	lcms2-devel
BuildRequires:	libcap
BuildRequires:	libcap-devel
BuildRequires:	libdisplay-info-devel >= 0.2.0
BuildRequires:	libdrm-devel >= 2.4.116
BuildRequires:	libeis-devel
BuildRequires:	libepoxy-devel >= 1.3
BuildRequires:	libinput-devel >= 1.19
BuildRequires:	libstdc++-devel
BuildRequires:	libxcb-devel >= 1.10
BuildRequires:	ninja
BuildRequires:	pipewire-devel >= 0.3.65
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	systemd-devel
BuildRequires:	udev-devel
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel >= 0.4
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libxcvt-devel >= 0.1.1
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.7.0
BuildRequires:	xorg-lib-libxkbcommon-x11-devel >= 0.7.0
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt6Concurrent >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Qml >= %{qt_ver}
Requires:	Qt6Qt5Compat >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	Qt6Sensors >= %{qt_ver}
Requires:	Qt6Svg >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kcompletion >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kconfigwidgets >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kcrash >= %{kf_ver}
Requires:	kf6-kdeclarative >= %{kf_ver}
Requires:	kf6-kglobalaccel >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kidletime >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-knewstuff >= %{kf_ver}
Requires:	kf6-knotifications >= %{kf_ver}
Requires:	kf6-kpackage >= %{kf_ver}
Requires:	kf6-kservice >= %{kf_ver}
Requires:	kf6-ktextwidgets >= %{kf_ver}
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kwindowsystem >= %{kf_ver}
Requires:	kf6-kxmlgui >= %{kf_ver}
Requires:	kp6-kdecoration >= %{kp_ver}
Requires:	kp6-kscreenlocker
Requires:	kp6-plasma-activities >= %{kp_ver}
Requires:	libdrm >= 2.4.116
Requires:	libepoxy >= 1.3
Requires:	libinput >= 1.19
Requires:	libxcb >= 1.10
Requires:	pipewire-libs >= 0.3.65
Requires:	xcb-util-wm >= 0.4
Requires:	xorg-lib-libxcvt >= 0.1.1
Requires:	xorg-lib-libxkbcommon >= 0.7.0
%requires_eq_to Qt6Core Qt6Core-devel
Suggests:	hwdata
Obsoletes:	kp5-kwin < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Window manager X11.

%description -l pl.UTF-8
Zarządca okien KDE X11.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
Requires(post,postun):	desktop-file-utils
Obsoletes:	kp5-%{kpname}-data < 6
BuildArch:	noarch

%description data
Data files for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Gui-devel >= %{qt_ver}
Requires:	kf6-kconfig-devel >= %{kf_ver}
Requires:	kf6-kcoreaddons-devel >= %{kf_ver}
Requires:	kf6-kwindowsystem-devel >= %{kf_ver}
Requires:	libepoxy-devel
Requires:	libstdc++-devel
Requires:	libxcb-devel
Obsoletes:	kp5-kwin-devel < 6

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%{__rm} -r po/id

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

find $RPM_BUILD_ROOT%{_datadir}/kconf_update -type f -name "*.py" \
	-exec sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' '{}' +

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post data
%update_desktop_database_post

%postun data
%update_desktop_database_postun


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin_x11
%{systemduserunitdir}/plasma-kwin_x11.service
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts-x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default-x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen-x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts-x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin5_update_default_rules_x11
%ghost %{_libdir}/libkcmkwincommon-x11.so.6
%{_libdir}/libkcmkwincommon-x11.so.*.*
%ghost %{_libdir}/libkwin-x11.so.6
%{_libdir}/libkwin-x11.so.*.*
%{_libdir}/qt6/plugins/kf6/packagestructure/kwin_aurorae_x11.so
%{_libdir}/qt6/plugins/kf6/packagestructure/kwin_decoration_x11.so
%{_libdir}/qt6/plugins/kf6/packagestructure/kwin_effect_x11.so
%{_libdir}/qt6/plugins/kf6/packagestructure/kwin_scripts_x11.so
%{_libdir}/qt6/plugins/kf6/packagestructure/kwin_windowswitcher_x11.so
%dir %{_libdir}/qt6/plugins/kwin-x11
%dir %{_libdir}/qt6/plugins/kwin-x11/effects
%dir %{_libdir}/qt6/plugins/kwin-x11/effects/configs
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kcm_kwin4_genericscripted.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_blur_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_diminactive_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_glide_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_magiclamp_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_mouseclick_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_mousemark_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_overview_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_slide_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_thumbnailaside_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_tileseditor_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_trackmouse_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_windowview_config.so
%{_libdir}/qt6/plugins/kwin-x11/effects/configs/kwin_wobblywindows_config.so
%dir %{_libdir}/qt6/plugins/kwin-x11/plugins
%{_libdir}/qt6/plugins/kwin-x11/plugins/krunnerintegration.so
%{_libdir}/qt6/plugins/kwin-x11/plugins/nightlight.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_animations_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_effects_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_scripts_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwin_virtualdesktops_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwindecoration_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_kwinrules_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinoptions_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwinscreenedges_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintabbox_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kwintouchscreen_x11.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%dir %{_libdir}/qt6/qml/org/kde/kwin_x11
%dir %{_libdir}/qt6/qml/org/kde/kwin_x11/private
%dir %{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/WindowHeap.qml
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/WindowHeapDelegate.qml
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/effectsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/libeffectsplugin.so
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/effects/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kwin_x11/private/kdecoration
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/kdecoration/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/kdecoration/kdecorationprivatedeclarative.qmltypes
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/kdecoration/libkdecorationprivatedeclarative.so
%{_libdir}/qt6/qml/org/kde/kwin_x11/private/kdecoration/qmldir
%attr(755,root,root) %{_prefix}/libexec/kwin-applywindowdecoration-x11
%attr(755,root,root) %{_prefix}/libexec/kwin_killer_helper_x11
%attr(755,root,root) %{_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes-x11

%files data -f %{kpname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/kcm_animations_x11.desktop
%{_desktopdir}/kcm_kwin_effects_x11.desktop
%{_desktopdir}/kcm_kwin_scripts_x11.desktop
%{_desktopdir}/kcm_kwin_virtualdesktops_x11.desktop
%{_desktopdir}/kcm_kwindecoration_x11.desktop
%{_desktopdir}/kcm_kwinoptions_x11.desktop
%{_desktopdir}/kcm_kwinrules_x11.desktop
%{_desktopdir}/kcm_kwintabbox_x11.desktop
%{_desktopdir}/kwincompositing.desktop
%{_desktopdir}/org.kde.kwin_x11.killer.desktop
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.NightLight.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.Plugins.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.TabletModeManager.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.VirtualDesktopManager.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.KWin.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.kwin.Effects.xml
%{_datadir}/dbus-1/interfaces/kwin_x11_org.kde.kwin.VirtualKeyboard.xml
%{_iconsdir}/hicolor/*x*/apps/kwin-x11.png
%{_iconsdir}/hicolor/scalable/apps/kwin-x11.svg*
%{_datadir}/kconf_update/kwin-x11.upd
%{_datadir}/knotifications6/kwin-x11.notifyrc
%{_datadir}/knsrcfiles/kwineffect-x11.knsrc
%{_datadir}/knsrcfiles/kwinscripts-x11.knsrc
%{_datadir}/knsrcfiles/kwinswitcher-x11.knsrc
%{_datadir}/knsrcfiles/window-decorations-x11.knsrc
%{_datadir}/krunner/dbusplugins/kwin-runner-windows-x11.desktop
%{_datadir}/kwin-x11
%{_datadir}/qlogging-categories6/org_kde_kwin_x11.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/kwin-x11
%{_libdir}/cmake/KWinX11
%{_libdir}/cmake/KWinX11DBusInterface
%{_libdir}/libkwin-x11.so
