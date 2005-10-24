Summary:	The YASM Modular Assembler
Summary(pl):	Modularny assembler YASM
Name:		yasm
Version:	0.4.0
Release:	0.1
License:	distributable (BSD, GPL, LGPL, Artistic; see COPYING)
Group:		Development/Tools
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz
# Source0-md5:	2360e20c4e105ba95f4e9135a7901183
URL:		http://www.tortall.net/projects/yasm/
BuildRequires:	bison >= 1.25
# convenience is used in frontend
#BuildRequires:	libltdl-devel
BuildRequires:	xmlto
Requires:	libyasm = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasm is a complete rewrite of the NASM assembler under the "new"
BSD License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%description -l pl
Yasm to ca³kowite przepisanie asemblera NASM na "nowej" licencji BSD
(niektóre fragmenty s± na innych licencjach, szczegó³y w pliku
COPYING). Jest zaprojektowany od podstaw, aby umo¿liwiæ obs³ugê
wielu sk³adni asemblera (np. NASM, TASM, GAS itd.), a ponadto wiele
formatów obiektów wyj¶ciowych, a nawet wiele zestawów instrukcji.
Kolejny g³ówny modu³ ogólnego projektu to modu³ optymalizatora.

%package -n libyasm
Summary:	YASM - libyasm
Summary(pl):	YASM - biblioetka libyasm
Group:		Libraries

%description -n libyasm
YASM - libyasm.

%description -n libyasm -l pl
YASM - biblioteka libyasm.

%package -n libyasm-devel
Summary:	Header files for libyasm library
Summary(pl):	Pliki nag³ówkowe biblioteki libyasm
Group:		Development/Libraries
Requires:	libyasm = %{version}-%{release}

%description -n libyasm-devel
Header files for libyasm library.

%description -n libyasm-devel -l pl
Pliki nag³ówkowe biblioteki libyasm.

%package -n libyasm-static
Summary:	Static libyasm library
Summary(pl):	Statyczna biblioteka libyasm
Group:		Development/Libraries
Requires:	libyasm-devel = %{version}-%{release}

%description -n libyasm-static
Static libyasm library.

%description -n libyasm-static -l pl
Statyczna biblioteka libyasm.

%prep
%setup -q

%build
%configure \
	%{?debug:--enable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/yasm/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libyasm -p /sbin/ldconfig
%postun	-n libyasm -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD.txt COPYING
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/yasm
%attr(755,root,root) %{_libdir}/yasm/*.so
%{_mandir}/man[17]/*

%files -n libyasm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyasm.so.*.*.*

%files -n libyasm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyasm.so
%{_libdir}/libyasm.la
%{_includedir}/libyasm.h
%{_includedir}/libyasm

%files -n libyasm-static
%defattr(644,root,root,755)
%{_libdir}/libyasm.a
