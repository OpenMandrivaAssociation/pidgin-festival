%define version 1.1
%define release %mkrel 1

%define gaim_epoch 1
%define pkgname festival-gaim

Summary:	Gaim extension, to use speech synthetisis
Name:		gaim-festival
Version: 	%{version}
Release: 	%{release}
Epoch:		%{gaim_epoch}
Group: 		Networking/Instant messaging
Source0:	http://prdownloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.bz2
License: 	GPL
URL: 		http://gaim.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gaim-devel >= %{gaim_epoch}:1.0.0
BuildRequires:	automake >= 1.6
Requires:	gaim >= %{gaim_epoch}:1.0.0
Requires:	festival
Obsoletes:	%{pkgname}
Provides:	%{pkgname} = %{gaim_epoch}:%{version}


%description
Gaim allows you to talk to anyone using a variety of messaging  
protocols, including AIM (Oscar and TOC), ICQ, IRC, Yahoo!,
MSN Messenger, Jabber, Gadu-Gadu, Napster, and Zephyr.  These
protocols are implemented using a modular, easy to use design.  

This package is a Gaim plugin, to allow you using the Festival
speech system to read your message aloud.


%prep
%setup -q -n %{pkgname}-%{version}
autoreconf --force --install

# it uses glib-gettextize which strictly requires mkinstalldirs to exist
cat << _EOF_ > ./mkinstalldirs
#!/bin/sh
mkdir -p "\$@"
_EOF_

chmod 755 ./mkinstalldirs

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{pkgname}

# remove files not bundled
rm -f %{buildroot}%{_libdir}/gaim/*.la \
      %{buildroot}%{_libdir}/gaim/*.a

%files -f %{pkgname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gaim/*.so

%clean
rm -rf %{buildroot}

