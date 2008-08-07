%define name centerim
%define version 4.22.5
%define release %mkrel 2

Version:	%{version}
Summary:	Console ncurses based multi-protocol instant messenger
Name:		%{name}
Release:	%{release}
License:	GPLv2+ and LGPLv2+
Group:		Networking/Instant messaging
Source:		http://www.centerim.org/download/releases/%{name}-%{version}.tar.gz
URL:		http://www.centerim.org
Buildrequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	curl-devel
BuildRequires:	jpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
Obsoletes:	centericq
Provides:	centericq
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CenterIM is a text mode menu- and window-driven instant messenger. ICQ,
Yahoo!, AIM TOC, IRC, MSN, Gadu-Gadu and Jabber protocols are currently
supported.  There is also an internal RSS reader and a LiveJournal client.

CenterIM is a fork of the CenterICQ project.

%prep 
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr (-,root,root)
%doc README TODO AUTHORS
%{_bindir}/centerim
%{_bindir}/cimconv
%{_mandir}/man1/centerim.1*
%{_mandir}/man1/cimconv.1*
%{_datadir}/%{name}/
%{_datadir}/%{name}/*.wav
