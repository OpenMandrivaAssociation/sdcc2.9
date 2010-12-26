#FIXME: Too lazy to patch source :\ (wally 12/2010)
%define Werror_cflags %nil

%define name	sdcc2.9
%define oname	sdcc
%define version	2.9.0
%define rel	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	SDCC - Small Device C Compiler
Group:		Development/Other
License:	GPLv2
URL:		http://sdcc.sourceforge.net/
Source:		http://sdcc.sourceforge.net/snapshots/sdcc.src/%{oname}-src-%{version}.tar.bz2
Patch0:		sdcc-2.9.0-configure.patch
Patch1:		sdcc-2.9.0-patch-out-getline.patch
Patch2:		sdcc-2.9.0-r5476-fix-doublefree.patch
Patch3:		sdcc-2.9.0-r5508-fix-bug2805333.patch
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel
BuildRequires:	gputils
BuildRequires:	latex2html
BuildRequires:	libgc-devel
BuildRequires:	libncurses-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lyx
BuildRequires:	make
BuildRequires:	python
BuildRequires:	readline-devel
Requires:	gputils
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts:	%{oname}

%description
SDCC is a retargettable, optimizing ANSI-C compiler that targets the
Intel 8051, Maxim 80DS390, Zilog Z80 and the Motorola 68HC08 based
MCUs. Work is in progress on supporting the Microchip PIC16 and
PIC18 series.

This package provides older, stable, version 2.9 of sdcc.

%prep
%setup -q -n %{oname}
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p1

%build
%configure2_5x \
	--enable-libgc \
	--enable-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mv -f %{buildroot}/%{_datadir}/doc installed-docs

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README ChangeLog installed-docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{oname}
