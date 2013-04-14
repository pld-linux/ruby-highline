Summary:	A high-level IO library with validation, type conversion etc. for command-line interfaces
Summary(pl.UTF-8):	Wysokopoziomowa biblioteka I/O z kontrolą poprawności, konwersją typów itp. do aplikacji CLI
Name:		ruby-highline
Version:	1.5.1
Release:	0.1
License:	GPL v2, Ruby License
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/56461/highline-%{version}.tgz
# Source0-md5:	23d9221b5ffd55e5af35f5aa90590c57
URL:		http://highline.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	rpm-rubyprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces.

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
%setup -q -n highline-%{version}

%build
ruby setup.rb config \
	--siterubyver=%{ruby_vendorlibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README lib
rdoc --ri --op ri lib

rm -r ri/Kernel
rm -r ri/Object
rm -r ri/IO
rm -r ri/String
rm -r ri/StringIO
rm ri/cache.ri
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%{ruby_vendorlibdir}/highline.rb
%{ruby_vendorlibdir}/highline

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/HighLine
