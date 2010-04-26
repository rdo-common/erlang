%{?__erlang_provides_requires: %{__erlang_provides_requires}}

%define ver R13B
%define rel 04

Name:           erlang
Version:        %{ver}
Release:        %{rel}.6%{?dist}
Summary:        General-purpose programming language and runtime environment

Group:          Development/Languages
License:        ERPL
URL:            http://www.erlang.org
Source:         http://www.erlang.org/download/otp_src_%{ver}%{rel}.tar.gz
Source1:        http://www.erlang.org/download/otp_doc_html_%{ver}%{rel}.tar.gz
Source2:        http://www.erlang.org/download/otp_doc_man_%{ver}%{rel}.tar.gz
Source3:	erlang-find-provides.escript
Source4:	erlang-find-provides.sh
Source5:	erlang-find-requires.escript
Source6:	erlang-find-requires.sh
Source7:	macros.erlang
# TODO this patch needs rebase against current tree
Patch0:         otp-links.patch
# Fedora-specific
Patch1:		otp-0001-Do-not-format-man-pages.patch
# Fedora-specific
Patch2:		otp-0002-Remove-rpath.patch
# Upstreamed
Patch6:		otp-0006-Fix-shared-libraries-installation.patch
# Fedora-specific
Patch7:		otp-0007-Fix-for-dlopening-libGL-and-libGLU.patch
# Upstreamed
Patch8:		otp-0008-Fix-check-for-compile-workspace-overflow.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:	zlib-devel
BuildRequires:  flex
BuildRequires:	m4
BuildRequires:	fop

Requires: erlang-appmon = %{version}-%{release}
Requires: erlang-asn1 = %{version}-%{release}
Requires: erlang-common_test = %{version}-%{release}
Requires: erlang-compiler = %{version}-%{release}
Requires: erlang-cosEvent = %{version}-%{release}
Requires: erlang-cosEventDomain = %{version}-%{release}
Requires: erlang-cosFileTransfer = %{version}-%{release}
Requires: erlang-cosNotification = %{version}-%{release}
Requires: erlang-cosProperty = %{version}-%{release}
Requires: erlang-cosTime = %{version}-%{release}
Requires: erlang-cosTransaction = %{version}-%{release}
Requires: erlang-crypto = %{version}-%{release}
Requires: erlang-debugger = %{version}-%{release}
Requires: erlang-dialyzer = %{version}-%{release}
Requires: erlang-docbuilder = %{version}-%{release}
Requires: erlang-edoc = %{version}-%{release}
Requires: erlang-erl_docgen = %{version}-%{release}
Requires: erlang-erl_interface = %{version}-%{release}
Requires: erlang-erts = %{version}-%{release}
Requires: erlang-et = %{version}-%{release}
Requires: erlang-eunit = %{version}-%{release}
Requires: erlang-examples = %{version}-%{release}
Requires: erlang-gs = %{version}-%{release}
Requires: erlang-hipe = %{version}-%{release}
Requires: erlang-ic = %{version}-%{release}
Requires: erlang-inets = %{version}-%{release}
Requires: erlang-inviso = %{version}-%{release}
Requires: erlang-jinterface = %{version}-%{release}
Requires: erlang-kernel = %{version}-%{release}
Requires: erlang-megaco = %{version}-%{release}
Requires: erlang-mnesia = %{version}-%{release}
Requires: erlang-observer = %{version}-%{release}
Requires: erlang-odbc = %{version}-%{release}
Requires: erlang-orber = %{version}-%{release}
Requires: erlang-os_mon = %{version}-%{release}
Requires: erlang-otp_mibs = %{version}-%{release}
Requires: erlang-parsetools = %{version}-%{release}
Requires: erlang-percept = %{version}-%{release}
Requires: erlang-pman = %{version}-%{release}
Requires: erlang-public_key = %{version}-%{release}
Requires: erlang-reltool = %{version}-%{release}
Requires: erlang-rpm-macros = %{version}-%{release}
Requires: erlang-runtime_tools = %{version}-%{release}
Requires: erlang-sasl = %{version}-%{release}
Requires: erlang-snmp = %{version}-%{release}
Requires: erlang-ssh = %{version}-%{release}
Requires: erlang-ssl = %{version}-%{release}
Requires: erlang-stdlib = %{version}-%{release}
Requires: erlang-syntax_tools = %{version}-%{release}
Requires: erlang-test_server = %{version}-%{release}
Requires: erlang-toolbar = %{version}-%{release}
Requires: erlang-tools = %{version}-%{release}
Requires: erlang-tv = %{version}-%{release}
Requires: erlang-typer = %{version}-%{release}
Requires: erlang-webtool = %{version}-%{release}
Requires: erlang-wx = %{version}-%{release}
Requires: erlang-xmerl = %{version}-%{release}

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package appmon
Summary:	A utility used to supervise Applications executing on several Erlang nodes
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description appmon
A utility used to supervise Applications executing on several Erlang nodes.

%package asn1
Summary:	Provides support for Abstract Syntax Notation One
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description asn1
Provides support for Abstract Syntax Notation One.

%package common_test
Summary:	A portable framework for automatic testing
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description common_test
A portable framework for automatic testing.

%package compiler
Summary:	A byte code compiler for Erlang which produces highly compact code
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description compiler
A byte code compiler for Erlang which produces highly compact code.

%package cosEvent
Summary:	Orber OMG Event Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosEvent
Orber OMG Event Service.

%package cosEventDomain
Summary:	Orber OMG Event Domain Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosEventDomain
Orber OMG Event Domain Service.

%package cosFileTransfer
Summary:	Orber OMG File Transfer Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosFileTransfer
Orber OMG File Transfer Service.

%package cosNotification
Summary:	Orber OMG Notification Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosNotification
Orber OMG Notification Service.

%package cosProperty
Summary:	Orber OMG Property Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosProperty
Orber OMG Property Service.

%package cosTime
Summary:	Orber OMG Timer and TimerEvent Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosTime
Orber OMG Timer and TimerEvent Service.

%package cosTransaction
Summary:	Orber OMG Transaction Service
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description cosTransaction
Orber OMG Transaction Service.

%package crypto
Summary:	Cryptographical support
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description crypto
Cryptographical support.

%package debugger
Summary:	A debugger for debugging and testing of Erlang programs
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:	A DIscrepany AnaLYZer for ERlang programs
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package doc
Summary:	Erlang documentation
Group:		Development/Languages
BuildArch:	noarch
Obsoletes:	%{name}-doc < R13B-04.4

%description doc
Documentation for Erlang.

%package docbuilder
Summary:	Tool for generating HTML documentation for applications
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description docbuilder
Tool for generating HTML documentation for applications.

%package edoc
Summary:	A utility used to generate documentation out of tags in source files
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description edoc
A utility used to generate documentation out of tags in source files.

%package erl_docgen
Summary:	A utility used to generate erlang HTML documentation
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description erl_docgen
A utility used to generate erlang HTML documentation.

%package erl_interface
Summary:	Low level interface to C
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description erl_interface
Low level interface to C.

%package erts
Summary:	Functionality necessary to run the Erlang System itself
Group:		Development/Languages
Obsoletes:	%{name} < R13B-04.5

%description erts
Functionality necessary to run the Erlang System itself.

%package et
Summary:	An event tracer for Erlang programs
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description et
An event tracer for Erlang programs.

%package eunit
Summary:	Support for unit testing
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description eunit
Support for unit testing.

%package examples
Summary:	Examples for some Erlang modules
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description examples
Examples for some Erlang modules.

%package gs
Summary:	A library for Tcl/Tk support in Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
Requires:       tk
Obsoletes:	%{name} < R13B-04.5

%description gs
A Graphics System used to write platform independent user interfaces.

%package hipe
Summary:	High Performance Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description hipe
High Performance Erlang.

%package ic
Summary:	IDL compiler
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ic
IDL compiler.

%package inets
Summary:	A set of services such as a Web server and a ftp client etc
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description inets
A set of services such as a Web server and a ftp client etc.

%package inviso
Summary:	A trace tool for both development and delivered systems
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description inviso
A trace tool for both development and delivered systems.

%package jinterface
Summary:	A library for accessing Java from Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
BuildRequires:	java-1.6.0-openjdk-devel

%description jinterface
Low level interface to Java.

%package kernel
Summary:	Main erlang library
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description kernel
Main erlang library.

%package megaco
Summary:	Megaco/H.248 support library
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description megaco
Megaco/H.248 is a protocol for control of elements in a physically
decomposed multimedia gateway, enabling separation of call control
from media conversion.

%package mnesia
Summary:	A heavy duty real-time distributed database
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description mnesia
A heavy duty real-time distributed database.

%package observer
Summary:	A set of tools for tracing and investigation of distributed systems
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description observer
A set of tools for tracing and investigation of distributed systems.

%package odbc
Summary:	A library for unixODBC support in Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5
BuildRequires:  unixODBC-devel

%description odbc
An interface to relational SQL-databases built on ODBC (Open Database
Connectivity).

%package orber
Summary:	A CORBA Object Request Broker
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description orber
A CORBA Object Request Broker.

%package os_mon
Summary:	A monitor which allows inspection of the underlying operating system
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description os_mon
A monitor which allows inspection of the underlying operating system.

%package otp_mibs
Summary:	SNMP management information base for Erlang/OTP nodes
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description otp_mibs
SNMP management information base for Erlang/OTP nodes.

%package parsetools
Summary:	A set of parsing and lexical analysis tools
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description parsetools
A set of parsing and lexical analysis tools.

%package percept
Summary:	A concurrency profiler tool
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description percept
A concurrency profiler tool.

%package pman
Summary:	A graphical process manager used to inspect Erlang processes
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description pman
A graphical process manager used to inspect Erlang processes.

%package public_key
Summary:	API to public key infrastructure
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description public_key
API to public key infrastructure.

%package reltool
Summary:	A release management tool
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.

%package rpm-macros
Summary:	Necessary macros for building Erlang
Group:		Development/Languages
Obsoletes:	%{name} < R13B-04.5

%description rpm-macros
Necessary macros for building Erlang.

%package runtime_tools
Summary:	A set of tools to include in a production system
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description runtime_tools
A set of tools to include in a production system.

%package sasl
Summary:	The System Architecture Support Libraries
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description sasl
The System Architecture Support Libraries is a set of tools for
release upgrades and alarm handling etc.

%package snmp
Summary:	Simple Network Management Protocol (SNMP) support
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description snmp
Simple Network Management Protocol (SNMP) support including a
MIB compiler and tools for creating SNMP agents.

%package ssh
Summary:	Secure Shell application with sftp and ssh support
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ssh
Secure Shell application with sftp and ssh support.

%package ssl
Summary:	Secure Socket Layer support
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description ssl
Secure Socket Layer support.

%package stdlib
Summary:	The Erlang standard libraries
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description stdlib
The Erlang standard libraries.

%package syntax_tools
Summary:	A set of tools for dealing with erlang sources
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description syntax_tools
A utility used to handle abstract Erlang syntax trees,
reading source files differently, pretty-printing syntax trees.

%package test_server
Summary:	The OTP Test Server
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description test_server
The OTP Test Server.

%package toolbar
Summary:	A tool bar simplifying access to the Erlang tools
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description toolbar
A tool bar simplifying access to the Erlang tools.

%package tools
Summary:	A set of programming tools including a coverage analyzer etc
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description tools
A set of programming tools including a coverage analyzer etc.

%package tv
Summary:	An ETS and MNESIA graphical table visualizer
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description tv
An ETS and MNESIA graphical table visualizer.

%package typer
Summary:	TYPe annotator for ERlang programs
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description typer
TYPe annotator for ERlang programs.

%package webtool
Summary:	A tool that simplifying the use of web based Erlang tools
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description webtool
A tool that simplifying the use of web based Erlang tools.

%package wx
Summary:	A library for wxWidgets support in Erlang
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Requires:	mesa-libGL
Requires:	mesa-libGLU
Obsoletes:	%{name} < R13B-04.5
BuildRequires:  wxGTK-devel

%description wx
A Graphics System used to write platform independent user interfaces.

%package xmerl
Summary:	Provides support for XML 1.0
Group:		Development/Languages
Requires:	%{name}-erts = %{version}-%{release}
Obsoletes:	%{name} < R13B-04.5

%description xmerl
Provides support for XML 1.0.

%prep
%setup -q -n otp_src_%{ver}%{rel}
%patch1 -p1 -b .do_not_format_manpages
%patch2 -p1 -b .rpath
%patch6 -p1 -b .fix_shared_lib_install
%patch7 -p1 -b .dlopen_opengl_libs
%patch8 -p1 -b .pcre_overflow
# remove shipped zlib sources
rm -f erts/emulator/zlib/*.[ch]


%build
%ifarch sparcv9 sparc64
CFLAGS="$RPM_OPT_FLAGS -mcpu=ultrasparc -fno-strict-aliasing" %configure --enable-shared-zlib
%else
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure --enable-shared-zlib
%endif
make


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_PREFIX=$RPM_BUILD_ROOT install

# fix 0775 permission on some directories
find $RPM_BUILD_ROOT%{_libdir}/erlang -type d -perm 0775 | xargs chmod 755

# Fix 664 file mode
chmod 644 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/kernel-*/examples/uds_dist/c_src/Makefile
chmod 644 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/kernel-*/examples/uds_dist/src/Makefile
chmod 644 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/certs/Makefile
chmod 644 $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/src/Makefile

# install additional doc files
mkdir -p erlang_doc
tar -C erlang_doc -zxf %{SOURCE1}

# install man-pages
tar -C $RPM_BUILD_ROOT%{_libdir}/erlang -zxf %{SOURCE2}
gzip $RPM_BUILD_ROOT%{_libdir}/erlang/man/man*/*

# make links to binaries
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cd $RPM_BUILD_ROOT%{_bindir}
for file in erl erlc escript dialyzer
do
  ln -sf ../%{_lib}/erlang/bin/$file .
done

# Remove batch files intended to use on one proprietary OS.
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/observer-*/priv/bin/etop.bat
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/observer-*/priv/bin/getop.bat
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/webtool-*/priv/bin/start_webtool.bat

# Remove old txt files
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/certs/etc/otpCA/index.txt.old
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/examples/certs/etc/erlangCA/index.txt.old

# remove unneeded Erlang sources, but keep *.hrl files
for d in $RPM_BUILD_ROOT%{_libdir}/erlang/lib/* ; do find $d/src -type f ! -name "*.hrl" -print -delete || true ; done
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/hipe-*/{cerl,flow,icode,main,misc,util}/*.erl
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/orber-*/COSS/CosNaming/*.erl
find $RPM_BUILD_ROOT%{_libdir}/erlang/lib/*/src -type d -empty -delete

# remove C and Java sources
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/asn1-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/erl_interface-*/src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ic-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ic-*/java_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/jinterface-*/java_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/odbc-*/c_src
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/tools-*/c_src

# remove empty directories
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/doc
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/man

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/cosEvent-*/info
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/lib/cosEventDomain-*/info
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/hipe-*/vsn.mk

# No longer needed utilities for formatting man-pages
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/misc

# Remove *.o files
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/crypto-*/priv/obj
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/odbc-*/priv/obj
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/ssl-*/priv/obj

# Install RPM related files
install -D -p -m 0755 %{SOURCE3} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-provides.escript
install -D -p -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-provides.sh
install -D -p -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-requires.escript
install -D -p -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_rpmconfigdir}/erlang-find-requires.sh
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.erlang


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)

%doc AUTHORS EPLICENCE README.md
%doc %{_libdir}/erlang/PR.template
%doc %{_libdir}/erlang/README
%doc %{_libdir}/erlang/COPYRIGHT

%files appmon
%defattr(-,root,root)
%{_libdir}/erlang/lib/appmon-*/

%files asn1
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/asn1-*/ebin
%{_libdir}/erlang/lib/asn1-*/priv
%{_libdir}/erlang/lib/asn1-*/src

%files common_test
%defattr(-,root,root)
%{_libdir}/erlang/lib/common_test-*/

%files compiler
%defattr(-,root,root)
%{_libdir}/erlang/lib/compiler-*/

%files cosEvent
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosEvent-*/

%files cosEventDomain
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosEventDomain-*/

%files cosFileTransfer
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosFileTransfer-*/

%files cosNotification
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosNotification-*/

%files cosProperty
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosProperty-*/

%files cosTime
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosTime-*/

%files cosTransaction
%defattr(-,root,root)
%{_libdir}/erlang/lib/cosTransactions-*/

%files crypto
%defattr(-,root,root)
%{_libdir}/erlang/lib/crypto-*/

%files debugger
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/

%files dialyzer
%defattr(-,root,root)
%{_libdir}/erlang/lib/dialyzer-*/

%files doc
%defattr(-,root,root)
%doc erlang_doc/*

%files docbuilder
%defattr(-,root,root)
%{_libdir}/erlang/lib/docbuilder-*/

%files edoc
%defattr(-,root,root)
%{_libdir}/erlang/lib/edoc-*/

%files erl_docgen
%defattr(-,root,root)
%{_libdir}/erlang/lib/erl_docgen-*/

%files erl_interface
%defattr(-,root,root)
%{_libdir}/erlang/lib/erl_interface-*/

%files erts
%defattr(-,root,root)
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/lib/
%{_bindir}/*
%{_libdir}/erlang/bin/
%{_libdir}/erlang/erts-*/
%{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/man/
%{_libdir}/erlang/releases/
%{_libdir}/erlang/usr/
%{_libdir}/erlang/Install

%files et
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/et-*/
%{_libdir}/erlang/lib/et-*/ebin
%{_libdir}/erlang/lib/et-*/include
%{_libdir}/erlang/lib/et-*/src

%files eunit
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/eunit-*/ebin
%{_libdir}/erlang/lib/eunit-*/include

%files examples
%defattr(-,root,root)
%{_libdir}/erlang/lib/asn1-*/examples
%{_libdir}/erlang/lib/et-*/examples
%{_libdir}/erlang/lib/eunit-*/examples
%{_libdir}/erlang/lib/gs-*/examples
%{_libdir}/erlang/lib/ic-*/examples
%{_libdir}/erlang/lib/inets-*/examples
%{_libdir}/erlang/lib/kernel-*/examples
%{_libdir}/erlang/lib/megaco-*/examples
%{_libdir}/erlang/lib/mnesia-*/examples
%{_libdir}/erlang/lib/orber-*/examples
%{_libdir}/erlang/lib/reltool-*/examples
%{_libdir}/erlang/lib/snmp-*/examples
%{_libdir}/erlang/lib/ssl-*/examples
%{_libdir}/erlang/lib/stdlib-*/examples
%{_libdir}/erlang/lib/syntax_tools-*/examples
%{_libdir}/erlang/lib/tools-*/examples
%{_libdir}/erlang/lib/wx-*/examples

%files gs
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/gs-*/
%{_libdir}/erlang/lib/gs-*/contribs
%{_libdir}/erlang/lib/gs-*/ebin
%{_libdir}/erlang/lib/gs-*/priv
%{_libdir}/erlang/lib/gs-*/src

%files hipe
%defattr(-,root,root)
%{_libdir}/erlang/lib/hipe-*/

%files ic
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/ic-*/
%{_libdir}/erlang/lib/ic-*/ebin
%{_libdir}/erlang/lib/ic-*/include
%{_libdir}/erlang/lib/ic-*/priv
%{_libdir}/erlang/lib/ic-*/src

%files inets
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inets-*/ebin
%{_libdir}/erlang/lib/inets-*/priv
%{_libdir}/erlang/lib/inets-*/src

%files inviso
%defattr(-,root,root)
%{_libdir}/erlang/lib/inviso-*/

%files jinterface
%defattr(-,root,root)
%{_libdir}/erlang/lib/jinterface-*/

%files kernel
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/kernel-*/ebin
%{_libdir}/erlang/lib/kernel-*/include
%{_libdir}/erlang/lib/kernel-*/src

%files megaco
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/megaco-*/ebin
%{_libdir}/erlang/lib/megaco-*/include
%{_libdir}/erlang/lib/megaco-*/priv
%{_libdir}/erlang/lib/megaco-*/src

%files mnesia
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/mnesia-*/ebin
%{_libdir}/erlang/lib/mnesia-*/include
%{_libdir}/erlang/lib/mnesia-*/src

%files observer
%defattr(-,root,root)
%{_libdir}/erlang/lib/observer-*/

%files odbc
%defattr(-,root,root)
%{_libdir}/erlang/lib/odbc-*/

%files orber
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/orber-*/
%{_libdir}/erlang/lib/orber-*/COSS
%{_libdir}/erlang/lib/orber-*/ebin
%{_libdir}/erlang/lib/orber-*/include
%{_libdir}/erlang/lib/orber-*/java_src
%{_libdir}/erlang/lib/orber-*/priv
%{_libdir}/erlang/lib/orber-*/src

%files os_mon
%defattr(-,root,root)
%{_libdir}/erlang/lib/os_mon-*/

%files otp_mibs
%defattr(-,root,root)
%{_libdir}/erlang/lib/otp_mibs-*/

%files parsetools
%defattr(-,root,root)
%{_libdir}/erlang/lib/parsetools-*/

%files percept
%defattr(-,root,root)
%{_libdir}/erlang/lib/percept-*/

%files pman
%defattr(-,root,root)
%{_libdir}/erlang/lib/pman-*/

%files public_key
%defattr(-,root,root)
%{_libdir}/erlang/lib/public_key-*/

%files reltool
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/reltool-*/
%{_libdir}/erlang/lib/reltool-*/ebin
%{_libdir}/erlang/lib/reltool-*/src

%files rpm-macros
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.erlang
%{_rpmconfigdir}/erlang-find-provides.escript
%{_rpmconfigdir}/erlang-find-provides.sh
%{_rpmconfigdir}/erlang-find-requires.escript
%{_rpmconfigdir}/erlang-find-requires.sh

%files runtime_tools
%defattr(-,root,root)
%{_libdir}/erlang/lib/runtime_tools-*/

%files sasl
%defattr(-,root,root)
%{_libdir}/erlang/lib/sasl-*/

%files snmp
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/snmp-*/ebin
%{_libdir}/erlang/lib/snmp-*/include
%{_libdir}/erlang/lib/snmp-*/mibs
%{_libdir}/erlang/lib/snmp-*/priv
%{_libdir}/erlang/lib/snmp-*/src

%files ssh
%defattr(-,root,root)
%{_libdir}/erlang/lib/ssh-*/

%files ssl
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/ssl-*/ebin
%{_libdir}/erlang/lib/ssl-*/include
%{_libdir}/erlang/lib/ssl-*/pkix
%{_libdir}/erlang/lib/ssl-*/priv
%{_libdir}/erlang/lib/ssl-*/src

%files stdlib
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/stdlib-*/ebin
%{_libdir}/erlang/lib/stdlib-*/include
%{_libdir}/erlang/lib/stdlib-*/src

%files syntax_tools
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/syntax_tools-*/ebin

%files test_server
%defattr(-,root,root)
%{_libdir}/erlang/lib/test_server-*/

%files toolbar
%defattr(-,root,root)
%{_libdir}/erlang/lib/toolbar-*/

%files tools
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/tools-*/bin
%{_libdir}/erlang/lib/tools-*/ebin
%{_libdir}/erlang/lib/tools-*/emacs
%{_libdir}/erlang/lib/tools-*/priv
%{_libdir}/erlang/lib/tools-*/src

%files tv
%defattr(-,root,root)
%{_libdir}/erlang/lib/tv-*/

%files typer
%defattr(-,root,root)
%{_libdir}/erlang/lib/typer-*/

%files webtool
%defattr(-,root,root)
%{_libdir}/erlang/lib/webtool-*/

%files wx
%defattr(-,root,root)
%dir %{_libdir}/erlang/lib/wx-*/
%{_libdir}/erlang/lib/wx-*/ebin
%{_libdir}/erlang/lib/wx-*/include
%{_libdir}/erlang/lib/wx-*/priv
%{_libdir}/erlang/lib/wx-*/src

%files xmerl
%defattr(-,root,root)
%{_libdir}/erlang/lib/xmerl-*/


%post
%{_libdir}/erlang/Install -minimal -cross %{_libdir}/erlang >/dev/null 2>/dev/null


%changelog
* Mon Apr 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.6
- Made erlang-rpm-macros as separate package
- Fix error while installing erlang-rpm-macros

* Wed Apr 17 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.5
- Use erlang rpm macros for adding provides/reqires
- All %%{_libdir}/erlang/lib/* items were splitted off from main package, which
  in turn becomes purely virtual now.
- Removing RPM_BUILD_ROOT from several installed files is no longer required

* Sat Apr 17 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.4
- Added missing Requires mesa-libGL{U} for wx module (rhbz #583287)
- Fix for buffer overflow in pcre module (rhbz #583288)
- Doc sub-package marked as noarch (partially resolves rhbz #491165)

* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.3
- Added rpm-related stuff for auto-generating erlang dependencies in the future builds
- Since now *.yrl files are removed too.
- Removed unnecessary C and Java sources

* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.2
- Do not remove all files from %%{_libdir}/erlang/lib/*/src - keep
  *.[yh]rl intact
- Fix permissions for megaco *.so objects
- Fix permissions for asn1 *.so objects

* Sat Feb 13 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.1
- New release R13B-04
- Since now we're using %%configure instead of ./configure
- Removed no longer needed fix for newer glibc version
- Dropped %%patch3 (applied upstream)
- Rebased patches
- Added BR fop for rebuilding of docs
- Use system-wide zlib instead of shipped one
- Dropped BR gd-devel
- Removed unneeded sources (should be fixed upstream)
- Fixed permission for wx driver (should be fixed upstream)

* Thu Oct 22 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - R13B-02-1
- Update to R13B-02 (patched for what's released as 02-1 by upstream)

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - R13B-01.2
- rebuilt with new openssl

* Mon Aug 10 2009 Gerard Milmeister <gemi@bluewin.ch> - R13B-01.1
- update to R13B01

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Debarshi Ray <rishi@fedoraproject.org> R12B-5.7
- Updated rpath patch.
- Fixed configure to respect $RPM_OPT_FLAGS.

* Sun Mar  1 2009 Gerard Milmeister <gemi@bluewin.ch> - R12B-5.6
- new release R12B-5
- link escript and dialyzer to %{_bindir}

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-5.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Dennis Gilmore <dennis@ausil.us> - R12B-4.5
- fix sparc arches to compile

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - R12B-4.4
- rebuild with new openssl

* Sat Oct 25 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-4.1
- new release R12B-4

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.3
- fixed sslrpath patch

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - R12B-3.2
- fix license tag

* Sun Jul  6 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.1
- new release R12B-3

* Thu Mar 27 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-1.1
- new release R12B-1

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.3
- disable strict aliasing optimization

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - R12B-0.2
- Autorebuild for GCC 4.3

* Sat Dec  8 2007 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.1
- new release R12B-0

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - R11B-6
 - Rebuild for deps

* Sun Aug 19 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.3
- fix some permissions

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.2
- enable dynamic linking for ssl

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.1
- new release R11B-5

* Sat Mar 24 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - R11B-2.4
- Require java-1.5.0-gcj-devel for build.

* Sun Dec 31 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.3
- remove buildroot from installed files

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.2
- added patch for compiling with glibc 2.5

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.1
- new version R11B-2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.3
- Rebuild for FE6

* Wed Jul  5 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.2
- add BR m4

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.1
- new version R11B-0

* Wed May  3 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.3
- added patch for run_erl by Knut-Håvard Aksnes

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.1
- new version R10B-10

* Thu Dec 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-9.1
- New Version R10B-9

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.2
- updated rpath patch

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.1
- New Version R10B-8

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.4
- Added tk-devel and tcl-devel to buildreq
- Added tk to req

* Tue Sep  6 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.3
- Remove perl BuildRequires

* Tue Aug 30 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.2
- change /usr/lib to %%{_libdir}
- redirect output in %%post to /dev/null
- add unixODBC-devel to BuildRequires
- split doc off to erlang-doc package

* Sat Jun 25 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.1
- New Version R10B-6

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-3.1
- New Version R10B-3

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-2-0.fdr.1
- New Version R10B-2

* Wed Oct  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-0.fdr.1
- New Version R10B

* Thu Oct 16 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:R9B-1.fdr.1
- First Fedora release
