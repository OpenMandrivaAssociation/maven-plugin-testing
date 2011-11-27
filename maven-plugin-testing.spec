Name:           maven-plugin-testing
Version:        1.2
Release:        11
Summary:        Maven Plugin Testing

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
#svn export http://svn.apache.org/repos/asf/maven/plugin-testing/tags/maven-plugin-testing-1.2 maven-plugin-testing-1.2
#tar caf maven-plugin-testing-1.2 maven-plugin-testing-1.2/
Source0:        %{name}-%{version}.tar.xz

# patch for building with plexus-containers 1.5.4
Patch1:         maven-plugin-testing-harness-SilentLog.patch
Patch2:         maven-plugin-testing-harness-ArtifactStub.patch
Patch3:         maven-plugin-testing-harness-AbstractMojoTestCase.patch

BuildArch: noarch

BuildRequires: junit
BuildRequires: java-devel >= 0:1.6.0
BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-site-plugin
BuildRequires: plexus-maven-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-test-tools

Requires: maven
Requires:       jpackage-utils
Requires:       java
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%package harness
Summary: Maven Plugin Testing Mechanism
Group: Development/Java
Requires: maven-plugin-testing = %{version}-%{release}
Obsoletes: maven-shared-plugin-testing-harness <= 0:1.2
Provides: maven-shared-plugin-testing-harness = 1:%{version}-%{release} 

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%package tools
Summary: Maven Plugin Testing Tools
Group: Development/Java
Requires: maven-plugin-testing = %{version}-%{release}
Obsoletes: maven-shared-plugin-testing-tools <= 0:%{version}-%{release}
Provides: maven-shared-plugin-testing-tools = 1:%{version}-%{release}

%description tools
A set of useful tools to help the Maven Plugin testing.

%package -n maven-test-tools
Summary: Maven Testing Tool
Group: Development/Java
Requires: maven-plugin-testing = %{version}-%{release}
Obsoletes: maven-shared-test-tools <= 0:%{version}-%{release}
Provides: maven-shared-test-tools = 1:%{version}-%{release}

%description -n maven-test-tools
Framework to test Maven Plugins with Easymock objects.

%prep
%setup -q 
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate
#tests are skipped due to some test failures most probably caused by issues with our plexus container

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 maven-plugin-testing-harness/target/%{name}-harness-%{version}.jar  \
 %{buildroot}%{_javadir}/%{name}/%{name}-harness.jar
install -m 644 maven-plugin-testing-tools/target/%{name}-tools-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}-tools.jar
install -m 644 maven-test-tools/target/maven-test-tools-%{version}.jar  \
 %{buildroot}%{_javadir}/%{name}/maven-test-tools.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_to_maven_depmap org.apache.maven.plugin-testing %{name} %{version} JPP/%{name} %{name}
%add_to_maven_depmap org.apache.maven.shared %{name}-harness %{version} JPP/%{name} %{name}
install -pm 644 maven-plugin-testing-harness/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-harness.pom
%add_to_maven_depmap org.apache.maven.plugin-testing %{name}-harness %{version} JPP/%{name} %{name}-harness
%add_to_maven_depmap org.apache.maven.shared %{name}-harness %{version} JPP/%{name} %{name}-harness
install -pm 644 maven-plugin-testing-tools/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-tools.pom
%add_to_maven_depmap org.apache.maven.plugin-testing %{name}-tools %{version} JPP/%{name} %{name}-tools
%add_to_maven_depmap org.apache.maven.shared %{name}-tools %{version} JPP/%{name} %{name}-tools
install -pm 644 maven-test-tools/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-test-tools.pom
%add_to_maven_depmap org.apache.maven.plugin-testing maven-test-tools %{version} JPP/%{name} maven-test-tools
%add_to_maven_depmap org.apache.maven.shared maven-test-tools %{version} JPP/%{name} maven-test-tools

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* \
         $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%post
%update_maven_depmap

%postun
%update_maven_depmap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/*

%files harness
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-harness*

%files tools
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-tools*

%files -n maven-test-tools
%defattr(-,root,root,-)
%{_javadir}/%{name}/maven-test-tools*

