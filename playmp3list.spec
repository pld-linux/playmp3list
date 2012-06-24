Summary:	ncurses-based MP3 player for Linux
Summary(pl):	Bazowany na ncurses odtwarzacz MP3 dla Linuksa
Name:		playmp3list
Version:	0.95a
Release:	1
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
License:	GPL
Source0:	http://rucus.ru.ac.za/~urban/projects/playmp3list/download/%{name}-%{version}.tar.gz
URL:		http://rucus.ru.ac.za/~urban/projects/playmp3list/
BuildRequires:	ncurses-devel
Requires:	mpg123 >= 0.59r
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
playmp3list is a console-based MP3 player frontend for mpg123   
that browses directories and playlists even while playing songs. It
allows complete customization of key-mappings, startup settings, and
color schemes (themes) through a playmp3listrc file. It allows
additional parameters to be passed to mpg123 if necessary. It features
real-time toggling of shuffle and repeat modes, ID3v1 tag extraction,
and more.

%description -l pl
playmp3list jest ca�kiem sympatyczn� nak�adk� dla mpg123 pod konsol�
za pomoc� kt�rej mo�emy przemieszcza� si� po katalogach nawet podczas
odtwarzania utworu. Umo�liwia przypisywanie klawiszom r�nych zdarze�,
ustawie� startowych oraz zmian kolorystycznych (temat�w) poprzez 
plik playmp3listrc. Pozwala uruchamia� mpg123 wraz z dodatkowymi opcjami.
Obs�uguje prze��czanie powtarzania lub losowego odgrywania plik�w w 
czasie rzeczywistym, ID3v1 tagi, zwi�kszanie/zmniejszanie g�o�no�ci,
przewijanie za pomoc� strza�ek, ustawianie utwor�w wg. alfabetu itp.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf README AUTHORS TODO ChangeLog COPYING INSTALL playmp3listrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz playmp3listrc
%{_mandir}/man1/*
