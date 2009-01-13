Summary:	A high-level IO library that provides validation, type conversion, and more for command-line interfaces
Name:		highline
Version:	1.5.0
Release:	0.1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/46329/%{name}-%{version}.tgz
# Source0-md5:	b60d5199a9e19a9ac6d20a141cef98e5
URL:		http://highline.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level IO library that provides validation, type conversion, and
more for command-line interfaces.

%prep
%setup -q

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc -S --main README README lib

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO rdoc/*
%{ruby_rubylibdir}
