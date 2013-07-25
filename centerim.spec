%define __noautoreq '.*/bin/awk|.*/bin/gawk'

Name:		centerim
Summary:	Console ncurses based multi-protocol instant messenger
Version:	4.22.10
Release:	2
License:	GPLv2+ and LGPLv2+
Group:		Networking/Instant messaging
Source:		http://www.centerim.org/download/releases/%{name}-%{version}.tar.gz
Patch0:         centerim-4.22.6-url-escape-fedora.patch
Patch1:         centerim-gcc46.patch
URL:		http://www.centerim.org
BuildRequires:	liblzo-devel 
BuildRequires:	autoconf
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	jpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)

Obsoletes:	centericq
Provides:	centericq

%description
CenterIM is a text mode menu- and window-driven instant messenger. ICQ,
Yahoo!, AIM TOC, IRC, MSN, Gadu-Gadu and Jabber protocols are currently
supported.  There is also an internal RSS reader and a LiveJournal client.

CenterIM is a fork of the CenterICQ project.

%prep 
%setup -q
#security fix from fedora
%patch0 -p1 -b .url-escape-fedora
%patch1 -p1 -b .gcc46

%build
autoconf
%configure \
        --with-ssl \
        --disable-rpath \
        --enable-locales-fix

%make

%install
%makeinstall_std

%find_lang %name

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog FAQ NEWS README THANKS TODO
%{_bindir}/CenterIMLog2HTML.py
%{_bindir}/centerim
%{_bindir}/cimconv
%{_mandir}/man1/centerim.1*
%{_mandir}/man1/cimconv.1*
%{_datadir}/%{name}
%{_bindir}/cimformathistory
%{_bindir}/cimextracthistory.pl


%changelog
* Sun Dec 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.22.10-1mdv2011.0
+ Revision: 610624
- update to 4.22.10

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 4.22.9-2mdv2010.1
+ Revision: 537517
- rebuild

* Thu Jan 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.22.9-1mdv2010.1
+ Revision: 494439
- update sources to 4.22.9
- update to new version 4.22.9

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.22.8-2mdv2010.0
+ Revision: 455772
- rebuild for new curl SSL backend

* Sat Aug 15 2009 Frederik Himpe <fhimpe@mandriva.org> 4.22.8-1mdv2010.0
+ Revision: 416606
- update to new version 4.22.8

* Wed Mar 18 2009 Funda Wang <fwang@mandriva.org> 4.22.7-1mdv2009.1
+ Revision: 357124
- New version 4.22.7

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.22.5-2mdv2009.0
+ Revision: 266506
- rebuild early 2009.0 package (before pixel changes)

* Sat May 03 2008 Frederik Himpe <fhimpe@mandriva.org> 4.22.5-1mdv2009.0
+ Revision: 200800
- Initial centerim import, based on the centericq spec which it obsoletes
- create centerim

