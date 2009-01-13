Summary:	A high-level IO library that provides validation, type conversion, and more for command-line interfaces
Name:		ruby-highline
Version:	1.5.0
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/46329/highline-%{version}.tgz
# Source0-md5:	b60d5199a9e19a9ac6d20a141cef98e5
URL:		http://highline.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces.

%package rdoc
Summary:	Documentation files for highline library
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for highline library.

%prep
%setup -q -n highline-%{version}

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README lib
rdoc --ri --op ri lib

rm -rf ri/Kernel
rm -rf ri/Object
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%{ruby_rubylibdir}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/HighLine
