%global pypi_name snowballstemmer

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms

License:        BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.


%package -n     python2-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildArch:      noarch
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.

%if 0%{?with_python3}
%package -n     python3-%{pypi_name}
Summary:        Provides 16 stemmer algorithms generated from Snowball algorithms
BuildArch:      noarch
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
It includes following language algorithms:

* Danish
* Dutch
* English (Standard, Porter)
* Finnish
* French
* German
* Hungarian
* Italian
* Norwegian
* Portuguese
* Romanian
* Russian
* Spanish
* Swedish
* Turkis

This is a pure Python stemming library. If PyStemmer is available, this module
uses it to accelerate.
%endif

%prep
%setup -qn %{pypi_name}-%{version}
# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check
# No tests


%files -n python2-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/%{pypi_name}/

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}/
%endif


%changelog
* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-2
- Rebuilt for python 3.5

* Mon Aug 24 2015 Julien Enselme <jujens@jujens.eu> - 1.2.0-1
- Initial package
