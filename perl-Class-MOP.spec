#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	MOP
Summary:	Class::MOP - A Meta Object Protocol for Perl 5
Summary(pl.UTF-8):	Class::MOP - protokół metaobiektów (Meta Object Protocol) dla Perla 5
Name:		perl-Class-MOP
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	19fa19752df27396cfb9d826002ccdce
URL:		http://search.cpan.org/dist/Class-MOP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-GlobalDestruction
BuildRequires:	perl-MRO-Compat >= 0.05
BuildRequires:	perl-Scalar-List-Utils >= 1.18
BuildRequires:	perl-Sub-Identify >= 0.03
BuildRequires:	perl-Sub-Name >= 0.02
BuildRequires:	perl-Test-Exception >= 0.21
BuildRequires:	perl-Test-Simple >= 0.62
%endif
Requires:	perl-Scalar-List-Utils >= 1.18
Requires:	perl-Sub-Identify >= 0.03
Requires:	perl-Sub-Name >= 0.02
Conflicts:	perl-Moose < 0:0.72
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::MOP is a fully functioning meta object protocol for the
Perl 5 object system. It makes no attempt to change the behavior or
characteristics of the Perl 5 object system, only to create a protocol
for its manipulation and introspection.

That said, it does attempt to create the tools for building a rich
set of extensions to the Perl 5 object system. Every attempt has been
made for these tools to keep to the spirit of the Perl 5 object system
that we all know and love.

%description -l pl.UTF-8
Class::MOP to w pełni funkcjonalny protokół metaobiektów dla systemu
obiektowego Perla 5. Nie próbuje zmieniać zachowania czy
charakterystyki systemu obiektowego Perla 5, a jedynie tworzy protokół
do własnych operacji i obserwacji.

Oznacza to, że klasa ta nie tworzy narzędzi do budowania bogatego
zbioru rozszerzeń do systemu obiektowego Perla 5 - dołożono wszelkich
starań, aby utrzymać te narzędzia w duchu znanego i lubianego systemu
obiektowego Perla 5.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/metaclass.pm
%{perl_vendorarch}/Class/MOP.pm
%{perl_vendorarch}/Class/MOP
%dir %{perl_vendorarch}/auto/Class/MOP
%{perl_vendorarch}/auto/Class/MOP/MOP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Class/MOP/MOP.so
%{_mandir}/man3/Class::MOP*.3pm*
%{_mandir}/man3/metaclass.3pm*
%{_examplesdir}/%{name}-%{version}
