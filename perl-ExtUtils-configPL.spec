%define upstream_name	 ExtUtils-configPL
%define upstream_version 1.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension to automagiclly configure perl scripts 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEASE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module is used to add configuration information to a perl script, and is
meant to be used with the ExtUtils::MakeMaker module.

ExtUtils::configPL is not a "normal" Perl extension. It does add or encapsulate
functionality to your script, but it filters the script, replacing tags with
items from the Config module, writing the resulting script to a new file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 504817
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-9mdv2010.0
+ Revision: 430432
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2009.0
+ Revision: 256818
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.1-6mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-6mdv2008.0
+ Revision: 86358
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-5mdv2007.0
- Rebuild

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-4mdk
- spec cleanup
- %%mkrel

* Wed Dec 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.1-3mdk 
- fix buildrequires in a backward compatible way

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.1-2mdk 
- fix buildrequires

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.1-1mdk 
- first mdk release

