Summary:	ncurses-based MP3 player for Linux
Summary(pl):	Bazowany na ncurses odtwarzacz MP3 dla Linuksa
Name:		playmp3list
Version:	0.94
Release:	1
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	http://rucus.ru.ac.za/~urban/archive/%{name}-%{version}.tar.gz
URL:		http://rucus.ru.ac.za/~urban/playmp3list/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
Requires:	mpg123 >= 0.59r
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
playmp3list is an ncurses-based MP3 player for Linux, that uses mpg123
as it's backend.

%description -l pl
playmp3list jest bazowanym na ncurses odtwarzaczem MP3 dla Linuksa,
który u¿ywa mpg123 jako narzêdzia do odgrywania plików.

%prep
%setup -q

%build
aclocal
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc playmp3listrc

%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
