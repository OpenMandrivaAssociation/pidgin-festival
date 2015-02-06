Summary: Pidgin extension, to use speech synthetisis
Name:		pidgin-festival
Version: 	2.4
Release: 	2
Group: 		Networking/Instant messaging
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		pidgin-festival-2.4-str-fmt.patch
License: 	GPL
URL: 		http://pidgin-festival.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel
Requires:	pidgin
Requires:	festival
Obsoletes:	gaim-festival


%description
Pidgin allows you to talk to anyone using a variety of messaging  
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.  

This package is a Pidgin plugin, to allow you using the Festival
speech system to read your message aloud.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .strfmt

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove files not bundled
rm -f %{buildroot}%{_libdir}/purple-2/*.la \
      %{buildroot}%{_libdir}/purple-2/*.a

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/purple-2/*.so

%clean
rm -rf %{buildroot}



%changelog
* Fri Jun 12 2009 Frederik Himpe <fhimpe@mandriva.org> 2.4-1mdv2010.0
+ Revision: 385599
- Update to new version 2.4
- Add patch to build with -Werror=format-security

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 2.3-1mdv2009.0
+ Revision: 227744
- New version 2.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 19 2007 Götz Waschk <waschk@mandriva.org> 2.2-1mdv2008.1
+ Revision: 100230
- new version for pidgin
- import

