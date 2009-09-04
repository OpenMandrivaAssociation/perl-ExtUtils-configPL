%define module	ExtUtils-configPL
%define name	perl-%{module}
%define version	1.1
%define release	%mkrel 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension to automagiclly configure perl scripts 
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/P/PE/PEASE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This module is used to add configuration information to a perl script, and is
meant to be used with the ExtUtils::MakeMaker module.

ExtUtils::configPL is not a "normal" Perl extension. It does add or encapsulate
functionality to your script, but it filters the script, replacing tags with
items from the Config module, writing the resulting script to a new file.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
# parallel build is broken!
make

%check
%{__make} test

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

