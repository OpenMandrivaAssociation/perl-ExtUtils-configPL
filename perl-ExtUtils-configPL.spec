%define upstream_name	 ExtUtils-configPL
%define upstream_version 1.1
Name:		perl-%{upstream_name}
Version:	1.1
Release:	2

Summary:	Perl extension to automagiclly configure perl scripts 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/ExtUtils-configPL
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEASE/ExtUtils-configPL-1.1.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module is used to add configuration information to a perl script, and is
meant to be used with the ExtUtils::MakeMaker module.

ExtUtils::configPL is not a "normal" Perl extension. It does add or encapsulate
functionality to your script, but it filters the script, replacing tags with
items from the Config module, writing the resulting script to a new file.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/ExtUtils
%{_mandir}/*/*


