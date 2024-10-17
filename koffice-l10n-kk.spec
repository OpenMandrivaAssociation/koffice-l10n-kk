Name: koffice-l10n-kk
Version: 2.3.2
Release: %mkrel 2
Summary: Language files for KOffice Kazakh
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-kk
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Kazakh translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2011.0
+ Revision: 639862
- rebuild

* Fri Feb 18 2011 Funda Wang <fwang@mandriva.org> 2.3.2-1
+ Revision: 638330
- New version 2.3.2

* Thu Jan 20 2011 Funda Wang <fwang@mandriva.org> 2.3.1-1
+ Revision: 631766
- New version 2.3.1

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2011.0
+ Revision: 626267
- New version 2.3.0

* Thu Dec 09 2010 Funda Wang <fwang@mandriva.org> 2.2.91-1mdv2011.0
+ Revision: 617999
- New version 2.2.91

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2.2.84-1mdv2011.0
+ Revision: 598546
- New version 2.2.84

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 2.2.83-1mdv2011.0
+ Revision: 589874
- New version 2.2.83

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 2.2.82-1mdv2011.0
+ Revision: 583750
- new version 2.2.82

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 2.2.81-1mdv2011.0
+ Revision: 578547
- new version 2.2.81

* Sat Aug 28 2010 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 573632
- new version 2.2.2

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 2.2.1-1mdv2011.0
+ Revision: 550696
- new version 2.2.1

* Thu May 27 2010 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2010.1
+ Revision: 546377
- new version 2.2.0

* Wed Apr 28 2010 Funda Wang <fwang@mandriva.org> 2.1.91-1mdv2010.1
+ Revision: 540384
- new version 2.1.91

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 2.1.82-1mdv2010.1
+ Revision: 535942
- new version 2.1.82

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491265
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469531
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465553
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443742
- new version 2.0.82

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415841
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389654
- new version 2.0.1

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 380446
- New version 2.0.0
- new version 1.9.99.0

* Sun Feb 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.98.6-1mdv2009.1
+ Revision: 335953
- Update to beta6

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330493
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312730
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305050
- add source and spec
- Created package structure for koffice-l10n-kk.

