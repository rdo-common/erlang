Name:           erlang
Version:        R10B
Release:        9.1%{?dist}
Summary:        General-purpose programming language and runtime environment

Group:          Development/Languages
License:        Erlang Public License
URL:            http://www.erlang.org
Source:         http://www.erlang.org/download/otp_src_R10B-9.tar.gz
Source1:	http://www.erlang.org/download/otp_doc_html_R10B-9.tar.gz
Source2:	http://www.erlang.org/download/otp_doc_man_R10B-9.tar.gz
Patch:		otp-links.patch
Patch1:		otp-install.patch
Patch2:		otp-rpath.patch
Patch3:         otp-sslrpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  unixODBC-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	java-1.4.2-gcj-compat-devel
BuildRequires:  flex

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
%setup -q -n otp_src_R10B-9
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
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
