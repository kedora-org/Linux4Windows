Name: kedora-kde-theme
Version: 1.0
Release: 1%{?dist}
Summary: kedora KDE global theme
License: GPL
URL: http://example.com/my-kde-theme/
Source0: %{name}-%{version}.tar.gz


%description
This is kedora KDE global theme.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
rm -rf %{buildroot}
#install -d %{buildroot}/%{_datadir}/usr/share/
mkdir -p %{buildroot}/
cp -rp * %{buildroot}/

%preun
#rm -Rf %{_datadir}/icons/breeze_cursors

%files
%{_sysconfdir}/*
%{_datadir}/*

%changelog
* Tue Mar 29 2023 Your Name <you@example.com> - 1.0-1
- Initial package
