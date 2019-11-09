%define iname	odfpy

Name:		python-odf
Version:	1.4.0
Release:	1
Summary:	Python library for manipulating OpenDocument files
Group:		Development/Python
License:	GPLv2+
URL:		https://github.com/eea/odfpy/wiki
Source0:	https://pypi.python.org/packages/source/o/%{iname}/%{iname}-%{version}.tar.gz
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

%package -n python-odf-doc
Summary:	documentation and examples for python-odf and python3-odf
Group:		Development/Python

%description -n python-odf-doc
Odfpy is a library to read and write OpenDocument v. 1.1 files.

%package -n python-odf-tools
Summary:	Python API and tools to manipulate OpenDocument files
Group:		Development/Python
Requires:	python3-odf = %{version}-%{release}

%description -n python-odf-tools
Odfpy is a library to read and write OpenDocument v. 1.1 files.

%package -n python2-odf	 
Summary:        Python3 library for manipulating OpenDocument files	 
Group:          Development/Python	 
BuildRequires:  python2dist(setuptools)	 
BuildRequires:  pkgconfig(python2)	 
Recommends:     python-odf-tools	 
Recommends:     python-odf-doc	 
Provides:       python2-odf = %{version}-%{release}	 
Obsoletes:      python2-odfpy < 1.3.6-2	 
%{?python_provide:%python_provide python2-%{srcname}}	 
	 
%description -n python2-odf	 
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
%py2_build
%py3_build

%install
%py2_install
%py3_install

sed -i '/#!\/usr\/bin\/python/d' %{buildroot}%{python_sitelib}/odf/*.py
sed -i '/#!\/usr\/bin\/python/d' %{buildroot}%{python2_sitelib}/odf/*.py

%files
%docdir examples
%docdir contrib
%{_bindir}/*
%{_mandir}/man1/*
%{py_puresitedir}/*egg-info
%{py_puresitedir}/odf

%files -n python-odf-doc
%doc examples contrib

%files -n python-odf-tools
%{_mandir}/man1/*
%{_bindir}/*

%files -n python2-odf	 
%{python2_sitelib}/*egg-info	 
%{python2_sitelib}/odf


%changelog
* Tue Apr 20 2010 Tomas Kindl <supp@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 537126
- python-odf a.k.a. odfpy initial import
- create python-odf


