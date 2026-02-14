%define module	odfpy

Name:		python-odf
Version:	1.4.2
Release:	1
Summary:	Python library for manipulating OpenDocument files
Group:		Development/Python
License:	GPLv2+
URL:		https://github.com/eea/odfpy
# Specific URI to grab this repos tagged release tarballs
Source0:	%{URL}/archive/refs/tags/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# This package used to provide a python-odf-tools package with identical files
# which also existed in the main package causing a conflict/circ-dep,
# lets us not do that & also provide a replacement for packages that require it.
%rename %{name}-tools

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
Summary:	Documentation and examples for python-odf and python3-odf
Group:		Development/Python

%description -n python-odf-doc
%{module} is a library to read and write OpenDocument v. 1.2 files.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info
# fix non-unix line endings
dos2unix examples/ods-currency.py
# fix interpreter, order of ops is important here else we end up mashing interps
find . -type f -exec sed -i 's@#!/usr/bin/python@#!/usr/bin/python3@g' {} +
find . -type f -exec sed -i 's@#!/usr/bin/env python@#!/usr/bin/python3@g' {} +
# remove python dependency from doc files and disable the executive bit
sed -i '/#!\/usr\/bin\/python3/d' contrib/{gutenberg/gbtext2odt.py,odf2gbzip/odf2gbzip,odf2war/odf2war,odfsign/odfsign,odscell/odscell}
chmod -x contrib/{gutenberg/gbtext2odt.py,odf2gbzip/odf2gbzip,odf2war/odf2war,odfsign/odfsign,odscell/odscell}

%install -a
# fix non-executable-script linting errors
for file in %{buildroot}/%{python_sitelib}/odf/{element,elementtypes,load,manifest,odf2xhtml,odfmanifest,thumbnail,userfield}.py; do
   chmod a+x $file
done

%files
%{_bindir}/*
%{_mandir}/man1/*
%{py_puresitedir}/%{module}-%{version}*.egg-info
%{py_puresitedir}/odf

%files -n python-odf-doc
%doc examples contrib
