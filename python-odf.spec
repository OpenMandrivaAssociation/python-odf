%define iname	odfpy

Name:		python-odf
Version:	0.9.2
Release:	%mkrel 1
Summary:	Python library for manipulating OpenDocument files
Group:		Development/Python
License:	GPLv2+
URL:		http://forge.osor.eu/projects/odfpy/
Source0:	http://forge.osor.eu/frs/download.php/805/%{iname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildArch:	noarch
BuildRequires:	python-devel 
BuildRequires:	python-setuptools

%description
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.
 
These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.


%prep
%setup -q -n %{iname}-%{version}

%build
CFLAGS="%{optflags}" %{__python} -c 'import setuptools; execfile("setup.py")' build


%install
rm -rf %{buildroot}
%{__python} -c 'import setuptools; execfile("setup.py")' install --skip-build --root %{buildroot}
sed -i '/#!\/usr\/bin\/python/d' %{buildroot}%{python_sitelib}/odf/*.py

 
%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%docdir examples
%docdir contrib
%{_bindir}/*
%{_mandir}/man1/*
%{python_sitelib}/*egg-info
%{python_sitelib}/odf
