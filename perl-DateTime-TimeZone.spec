#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: c1050fe
#
Name     : perl-DateTime-TimeZone
Version  : 2.60
Release  : 99
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-2.60.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-TimeZone-2.60.tar.gz
Summary  : 'Time zone object base class and factory'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DateTime-TimeZone-license = %{version}-%{release}
Requires: perl-DateTime-TimeZone-perl = %{version}-%{release}
Requires: perl(B::Hooks::EndOfScope)
Requires: perl(Class::Singleton)
Requires: perl(DateTime::Duration)
Requires: perl(Module::Runtime)
Requires: perl(Params::ValidationCompiler)
Requires: perl(Specio)
Requires: perl(Try::Tiny)
Requires: perl(namespace::autoclean)
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::More)
BuildRequires : perl(Test::Output)
BuildRequires : perl(Test::Taint)
BuildRequires : perl-DateTime
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
DateTime::TimeZone - Time zone object base class and factory
# VERSION
version 2.60

%package dev
Summary: dev components for the perl-DateTime-TimeZone package.
Group: Development
Provides: perl-DateTime-TimeZone-devel = %{version}-%{release}
Requires: perl-DateTime-TimeZone = %{version}-%{release}

%description dev
dev components for the perl-DateTime-TimeZone package.


%package license
Summary: license components for the perl-DateTime-TimeZone package.
Group: Default

%description license
license components for the perl-DateTime-TimeZone package.


%package perl
Summary: perl components for the perl-DateTime-TimeZone package.
Group: Default
Requires: perl-DateTime-TimeZone = %{version}-%{release}

%description perl
perl components for the perl-DateTime-TimeZone package.


%prep
%setup -q -n DateTime-TimeZone-2.60
cd %{_builddir}/DateTime-TimeZone-2.60

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-TimeZone
cp %{_builddir}/DateTime-TimeZone-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-TimeZone/36886d89a91598e418fbfc5f0bf288f9583ccdb3 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::TimeZone.3
/usr/share/man/man3/DateTime::TimeZone::Catalog.3
/usr/share/man/man3/DateTime::TimeZone::Floating.3
/usr/share/man/man3/DateTime::TimeZone::Local.3
/usr/share/man/man3/DateTime::TimeZone::Local::Unix.3
/usr/share/man/man3/DateTime::TimeZone::Local::VMS.3
/usr/share/man/man3/DateTime::TimeZone::OffsetOnly.3
/usr/share/man/man3/DateTime::TimeZone::OlsonDB.3
/usr/share/man/man3/DateTime::TimeZone::UTC.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-TimeZone/36886d89a91598e418fbfc5f0bf288f9583ccdb3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
