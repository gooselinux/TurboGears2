%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           TurboGears2
Version:        2.0.3
Release:        4%{?dist}
Summary:        Next generation Front-to-back web development megaframework built on Pylons

Group:          Development/Languages
License:        MIT
URL:            http://www.turbogears.org
Source0:        http://www.turbogears.org/2.0/downloads/%{version}/%{name}-%{version}.tar.gz


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel
BuildRequires:  python-nose python-coverage python-paver python-pylons
BuildRequires:  python-turbokid python-zope-sqlalchemy python-jinja2 python-toscawidgets python-genshi
BuildRequires:  python-repoze-what python-repoze-who-testutil python-repoze-what-pylons
BuildRequires:  python-webflash python-tw-forms python-turbojson python-repoze-what-quickstart

%{?el5:BuildRequires: python-wsgiref}

Requires:       python-pylons >= 0.9.7
Requires:       python-webflash >= 0.1-0.a8
Requires:       python-weberror >= 0.10.1
Requires:       python-genshi >= 0.5.1
Requires:       python-zope-sqlalchemy
Requires:       python-toscawidgets >= 0.9.4
Requires:       python-turbojson >= 1.2.1
Requires:       python-repoze-tm2 >= 1.0-0.a4
Requires:       python-repoze-what-pylons >= 1.0-0.rc3


%description
TurboGears2, provides a comprehensive web development toolkit.  It is designed
to help you create the basic outline of a database-driven web application in
minutes.

TurboGears provides you with sane default for designer friendly templates,
tools to make  AJAX, and dynamic Javascript driven pages easy on both the
browser side and the server side.

TurboGears is a project that is built upon a foundation of reuse and building
up.  In retrospect, much of the code that was home grown in the TurboGears
project should have been released as independent projects that integrate with
TurboGears.


%prep
%setup -q


%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --skip-build --root %{buildroot}

%check
# Disabled until we package chameleon.genshi
#nosetests

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README.txt
%{python_sitelib}/%{name}-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/tg/


%changelog
* Tue Jan 26 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.3-4
- Fix the source URL

* Mon Sep 14 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-3
- Tweak our python-wsgiref conditional for EL5

* Tue Sep 01 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-2
- Remove the SQLAlchemy requirement, as python-zope-sqlalchemy
  is now set to include the appropriate version

* Wed Aug 12 2009 Luke Macken <lmacken@redhat.com> - 2.0.3-1
- 2.0.3

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> 2.0.1-1
- 2.0.1
- Bump our ToscaWigdets requirement to 0.9.4
- Remove TurboGears2-custom-content-type.patch, which is upstream

* Sat Jun 06 2009 Luke Macken <lmacken@redhat.com> 2.0-4
- Require the new python-sqlalchemy0.5 package

* Thu Jun 04 2009 Luke Macken <lmacken@redhat.com> 2.0-3
- Add a patch to fix custom content types.
  http://trac.turbogears.org/ticket/2280

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> 2.0-2
- Conditionally include wsgiref

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> 2.0-1
- Update to 2.0 final.
- Add python-repoze-what-pylons and python-webflash to the BuildRequires
- Disable the test suite until we package chameleon.genshi

* Tue Oct 28 2008 Luke Macken <lmacken@redhat.com> 1.9.7.0.3.b1dev.r5627
- Update to a svn snapshot to support tgext.authorization instead of
  tg.ext.repoze.who

* Mon Oct 27 2008 Luke Macken <lmacken@redhat.com> 1.9.7-0.2.b1
- Update to 1.9.7b1

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> 1.9.7-0.1.a5dev.r5564
- Initial packaging of TurboGears2 for Fedora.
