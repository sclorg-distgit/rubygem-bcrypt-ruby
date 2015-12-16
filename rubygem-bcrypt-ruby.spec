%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

# Generated from bcrypt-ruby-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bcrypt-ruby

Summary: Wrapper around bcrypt() password hashing algorithm
Name: %{?scl:%scl_prefix}rubygem-%{gem_name}
Version: 3.1.2
Release: 4%{?dist}
Group: Development/Languages
# ext/* - Public Domain
# spec/TestBCrypt.java - ISC
License: MIT and Public Domain and ISC
URL: http://bcrypt-ruby.rubyforge.org
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby-devel
BuildRequires: %{?scl_prefix}rubygem(rspec)
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. bcrypt-ruby provides a simple, humane wrapper for
safely handling
passwords.


%prep
%setup -q -c -T

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mv %{buildroot}%{gem_libdir}/bcrypt_ext.so %{buildroot}%{gem_extdir_mri}/lib

%check
pushd .%{gem_instdir}
%{?scl:scl enable %{scl} - << \EOF}
rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/bcrypt-ruby.gemspec
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/COPYING
%exclude %{gem_instdir}/ext
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%{gem_libdir}
%{gem_extdir_mri}
%{gem_instdir}/spec
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 3.1.2-4
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Thu Jan 23 2014 Josef Stribny <jstribny@redhat.com> - 3.1.2-3
- Fix: use scl_prefix_ruby macro in requires

* Thu Jan 23 2014 Vít Ondruch <vondruch@redhat.com> - 3.1.2-2
- Fix rubygems-devel BR.

* Wed Nov 20 2013 Josef Stribny <jstribny@redhat.com> - 3.1.2-1
- Update to brypt-ruby 3.1.2

* Wed Jun 12 2013 Josef Stribny <jstribny@redhat.com> - 3.0.1-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Wed Feb 27 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.1-7
- Rebuild to fix documentation vulnerability due to CVE-2013-0256.

* Wed Jul 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.1-6
- Specfile cleanup.

* Mon Apr 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.1-5
- Rebuilt for scl.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-4
- Fixed wrong provide.

* Mon Jan 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.1-1
- Update to bcrypt-ruby 3.0.1.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 2.1.2-4
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-2
- Updates / fixes based on review feedback
- Fixed bcrypt_ext.so install location

* Tue Aug 10 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-1
- Initial package
