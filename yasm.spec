#
# TODO:
# - proper split to subpackages
# - check BR
#
Summary:	The YASM Modular Assembler
Summary(pl):	Modularny assembler YASM
Name:		yasm
Version:	0.4.0
Release:	0.1
License:	distributable (BSD, GPL, LGPL, Artistic; see COPYING)
Group:		Development/Tools
Source0:	http://www.tortall.net/projects/yasm/releases/yasm-0.4.0.tar.gz
# Source0-md5:	2360e20c4e105ba95f4e9135a7901183
URL:		http://www.tortall.net/projects/yasm/
BuildRequires:	bison
BuildRequires:	libltdl
BuildRequires:	libtool
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libyasm -p /sbin/ldconfig
%postun	-n libyasm -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/yasm
%attr(755,root,root) %{_libdir}/yasm/*.so
%{_mandir}/man?/*

#%files devel
%{_includedir}/*

#%files static

%files -n libyasm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
