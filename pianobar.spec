Name: pianobar
Version: 2013.05.19
Release: 1%{?dist}
Summary: "pianobar is a free/open-source, console-based replacement for pandora's flash player."

Group: Applications/Multimedia
License: AS-IS
URL: http://6xq.net/html/00/17.html
Source: http://6xq.net/projects/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: make, libao-devel, libxml2-devel, faad2-devel, libmad-devel, json-c-devel
Requires: libao, faad2-libs, libxml2, json-c

%description
 "pianobar" supports all important features pandora has:
 * Create, delete, rename stations and add more music
 * Rate and temporary ban tracks as well as move them to another station
 * "Shared stations"
 * last.fm scrobbling
 * Proxy support for non-americans

%prep
%setup -q
%build
gmake
gmake VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
gmake install PREFIX=usr DESTDIR=$RPM_BUILD_ROOT

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING INSTALL README
%{_bindir}/*
%{_mandir}/man1/*

%changelog
