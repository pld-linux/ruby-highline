#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	doc			# don't build ri/rdoc

%define	pkgname	highline
Summary:	HighLine is a high-level command-line IO library
Summary(pl.UTF-8):	Wysokopoziomowa biblioteka I/O z kontrolą poprawności, konwersją typów itp. do aplikacji CLI
Name:		ruby-%{pkgname}
Version:	3.1.2
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	bc9b1b4769980f802db4c42600ad7536
URL:		https://github.com/JEG2/highline
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces. HighLine also includes a complete
menu system that can crank out anything from simple list selection to
complete shells with just minutes of work.

%description -l pl.UTF-8
Wysokopoziomowa biblioteka wejścia-wyjścia obsługująca kontrolę
poprawności, konwersję typów i inne, przeznaczona dla interfejsów
linii poleceń.

%package rdoc
Summary:	Documentation files for highline library
Summary(pl.UTF-8):	Pliki dokumentacji do biblioteki highline
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for highline library.

%description rdoc -l pl.UTF-8
Pliki dokumentacji do biblioteki highline.

%prep
%setup -q -n %{pkgname}-%{version}

find lib -name '*.rb' | xargs chmod a-x

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
%{__ruby} -S testrb -Ilib test/*
%endif

%if %{with doc}
rdoc --op rdoc --main README.md README.md lib
rdoc --ri --op ri lib

rm -r ri/Kernel
rm -r ri/Object
rm -r ri/IO
rm -r ri/String
rm -r ri/StringIO
rm ri/cache.ri
rm ri/created.rid
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%if %{with doc}
install -d $RPM_BUILD_ROOT{%{ruby_rdocdir}/%{name}-%{version},%{ruby_ridir}}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md TODO AUTHORS LICENSE COPYING
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/File
%{ruby_ridir}/HighLine
%{ruby_ridir}/IOConsoleCompatible
%{ruby_ridir}/Tempfile
%endif
