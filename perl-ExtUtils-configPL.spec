%define upstream_name	 ExtUtils-configPL
%define upstream_version 1.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension to automagiclly configure perl scripts 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEASE/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is used to add configuration information to a perl script, and is
meant to be used with the ExtUtils::MakeMaker module.

ExtUtils::configPL is not a "normal" Perl extension. It does add or encapsulate
functionality to your script, but it filters the script, replacing tags with
items from the Config module, writing the resulting script to a new file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
# parallel build is broken!
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/ExtUtils
%{_mandir}/*/*
