Name:           erlang
Version:        R11B
Release:        2.5%{?dist}
Summary:        General-purpose programming language and runtime environment

Group:          Development/Languages
License:        Erlang Public License
URL:            http://www.erlang.org
Source:         http://www.erlang.org/download/otp_src_R11B-2.tar.gz
Source1:	http://www.erlang.org/download/otp_doc_html_R11B-2.tar.gz
Source2:	http://www.erlang.org/download/otp_doc_man_R11B-2.tar.gz
Patch1:		otp-R11B-2-0001-Do-not-create-links-instead-of-real-files.patch
Patch2:		otp-R11B-2-0002-Fix-symlinking-of-epmd.patch
Patch3:		otp-R11B-2-0003-Do-not-format-man-pages.patch
Patch4:		otp-R11B-2-0004-Remove-rpath.patch
Patch5:		otp-R11B-2-0005-Fix-shared-libraries-installation.patch
Patch6:		otp-R11B-2-0006-Fix-missing-ssl-libraries-in-EPEL.patch
Patch7:		otp-R11B-2-0007-Fix-for-Glibc-2.5.patch
Patch8:		otp-R11B-2-0008-Fix-for-run_erl-utility.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  unixODBC-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	java-1.4.2-gcj-compat-devel
BuildRequires:  flex
BuildRequires:	m4
Provides: erlang-appmon = %{version}-%{release}
Provides: erlang-asn1 = %{version}-%{release}
Provides: erlang-compiler = %{version}-%{release}
Provides: erlang-cosEvent = %{version}-%{release}
Provides: erlang-cosEventDomain = %{version}-%{release}
Provides: erlang-cosFileTransfer = %{version}-%{release}
Provides: erlang-cosNotification = %{version}-%{release}
Provides: erlang-cosProperty = %{version}-%{release}
Provides: erlang-cosTime = %{version}-%{release}
Provides: erlang-cosTransactions = %{version}-%{release}
Provides: erlang-crypto = %{version}-%{release}
Provides: erlang-debugger = %{version}-%{release}
Provides: erlang-dialyzer = %{version}-%{release}
Provides: erlang-edoc = %{version}-%{release}
Provides: erlang-et = %{version}-%{release}
Provides: erlang-gs = %{version}-%{release}
Provides: erlang-hipe = %{version}-%{release}
Provides: erlang-ic = %{version}-%{release}
Provides: erlang-inets = %{version}-%{release}
Provides: erlang-inviso = %{version}-%{release}
Provides: erlang-kernel = %{version}-%{release}
Provides: erlang-megaco = %{version}-%{release}
Provides: erlang-mnemosyne = %{version}-%{release}
Provides: erlang-mnesia = %{version}-%{release}
Provides: erlang-mnesia_session = %{version}-%{release}
Provides: erlang-observer = %{version}-%{release}
Provides: erlang-odbc = %{version}-%{release}
Provides: erlang-orber = %{version}-%{release}
Provides: erlang-os_mon = %{version}-%{release}
Provides: erlang-otp_mibs = %{version}-%{release}
Provides: erlang-parsetools = %{version}-%{release}
Provides: erlang-pman = %{version}-%{release}
Provides: erlang-runtime_tools = %{version}-%{release}
Provides: erlang-sasl = %{version}-%{release}
Provides: erlang-snmp = %{version}-%{release}
Provides: erlang-ssh = %{version}-%{release}
Provides: erlang-ssl = %{version}-%{release}
Provides: erlang-stdlib = %{version}-%{release}
Provides: erlang-syntax_tools = %{version}-%{release}
Provides: erlang-toolbar = %{version}-%{release}
Provides: erlang-tools = %{version}-%{release}
Provides: erlang-tv = %{version}-%{release}
Provides: erlang-webtool = %{version}-%{release}
Provides: erlang-xmerl = %{version}-%{release}
Requires:	tk

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.


%package doc
Summary:	Erlang documentation
Group:		Development/Languages

%description doc
Documentation for Erlang.


%prep
%setup -q -n otp_src_R11B-2
%patch1 -p1 -b .links
%patch2 -p1 -b .epmd
%patch3 -p1 -b .manpages
%patch4 -p1 -b .rpath
%patch5 -p1 -b .shared_libs
%patch6 -p1 -b .missing_ssl_libs
%patch7 -p1 -b .glibc25
%patch8 -p1 -b .run_erl


%build
# cannot be built with %%configure macros
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --libdir=%{_libdir}
chmod -R u+w .
make


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_PREFIX=$RPM_BUILD_ROOT install

# clean up
find $RPM_BUILD_ROOT%{_libdir}/erlang -perm 0775 | xargs chmod 755
find $RPM_BUILD_ROOT%{_libdir}/erlang -name Makefile | xargs chmod 644
find $RPM_BUILD_ROOT%{_libdir}/erlang -name \*.bat | xargs rm -f
find $RPM_BUILD_ROOT%{_libdir}/erlang -name index.txt.old | xargs rm -f

# doc
mkdir -p erlang_doc
tar -C erlang_doc -zxf %{SOURCE1}
tar -C $RPM_BUILD_ROOT/%{_libdir}/erlang -zxf %{SOURCE2}

# make links to binaries
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cd $RPM_BUILD_ROOT/%{_bindir}
for file in erl erlc
do
  ln -sf ../%{_lib}/erlang/bin/$file .
done

# remove buildroot from installed files
cd $RPM_BUILD_ROOT/%{_libdir}/erlang
sed -i "s|$RPM_BUILD_ROOT||" erts*/bin/{erl,start} releases/RELEASES bin/{erl,start}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS EPLICENCE README
%{_bindir}/*
%{_libdir}/erlang


%files doc
%defattr(-,root,root)
%doc erlang_doc/*


%post
%{_libdir}/erlang/Install -minimal %{_libdir}/erlang >/dev/null 2>/dev/null


%changelog
* Mon Jun  7 2010 Peter Lemenkov <lemenkov@gmail.com> - R11B-2.5
- Added virtual provides for erlang modules

* Mon Apr 19 2010 Peter Lemenkov <lemenkov@gmail.com> - R11B-2.4
- Patches rebased
- Added patches 6,7 from trunk

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
