%define upstream_name    Text-Context-EitherSide
%define upstream_version 1.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Get n words either side of search keywords
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Suppose you have a large piece of text - typically, say, a web page or a
mail message. And now suppose you've done some kind of full-text search on
that text for a bunch of keywords, and you want to display the context in
which you found the keywords inside the body of the text.

A simple-minded way to do that would be just to get the two words either
side of each keyword. But hey, don't be too simple minded, because you've
got to make sure that the list doesn't overlap. If you have

    the quick brown fox jumped over the lazy dog

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
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.400.0-2mdv2011.0
+ Revision: 654321
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 471149
- import perl-Text-Context-EitherSide


* Sun Nov 29 2009 cpan2dist 1.4-1mdv
- initial mdv release, generated with cpan2dist
