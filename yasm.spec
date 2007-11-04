Summary:	The YASM Modular Assembler
Summary(pl.UTF-8):	Modularny assembler YASM
Name:		yasm
Version:	0.6.2
Release:	1
License:	distributable (BSD, GPL, LGPL, Artistic; see COPYING)
Group:		Development/Tools
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a9d5508702991de2bdd0903b8ba680ba
URL:		http://www.tortall.net/projects/yasm/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmlto
Obsoletes:	libyasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasm is a complete rewrite of the NASM assembler under the "new"
BSD License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%description -l pl.UTF-8
Yasm to całkowite przepisanie asemblera NASM na "nowej" licencji BSD
(niektóre fragmenty są na innych licencjach, szczegóły w pliku
COPYING). Jest zaprojektowany od podstaw, aby umożliwić obsługę
wielu składni asemblera (np. NASM, TASM, GAS itd.), a ponadto wiele
formatów obiektów wyjściowych, a nawet wiele zestawów instrukcji.
Kolejny główny moduł ogólnego projektu to moduł optymalizatora.

%package -n libyasm-devel
Summary:	Header files and static libyasm library
Summary(pl.UTF-8):	Pliki nagłówkowe i statyczna biblioteka libyasm
Group:		Development/Libraries
License:	BSD+Artistic or LGPL or GPL (see COPYING)
Obsoletes:	libyasm
Obsoletes:	libyasm-static

%description -n libyasm-devel
Header files and static libyasm library.

%description -n libyasm-devel -l pl.UTF-8
Pliki nagłówkowe i statyczna biblioteka libyasm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug}

%{__make} -j1 all check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD.txt COPYING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[17]/*

%files -n libyasm-devel
%defattr(644,root,root,755)
%doc AUTHORS BSD.txt COPYING
%{_libdir}/libyasm.a
%{_includedir}/libyasm*.h
%{_includedir}/libyasm
