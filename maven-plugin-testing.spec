
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		maven-plugin-testing
Version:	2.1
Release:	9.2
License:	GPLv3+
Source0:	maven-plugin-testing-2.1-9.0-omv2014.1.noarch.rpm
Source1:	maven-plugin-testing-harness-2.1-9.0-omv2014.1.noarch.rpm
Source2:	maven-plugin-testing-javadoc-2.1-9.0-omv2014.1.noarch.rpm
Source3:	maven-plugin-testing-tools-2.1-9.0-omv2014.1.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/maven-plugin-testing
BuildArch:	noarch
Summary:	maven-plugin-testing bootstrap version
#Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Requires:	mvn(junit:junit)
Requires:	mvn(org.apache.maven.plugins:maven-site-plugin)
Requires:	mvn(org.apache.maven:maven-parent)
Provides:	maven-plugin-testing = 2.1-9.0:2014.1
Provides:	mvn(org.apache.maven.plugin-testing:maven-plugin-testing) = 2.1
Provides:	mvn(org.apache.maven.plugin-testing:maven-plugin-testing:pom:) = 2.1
Provides:	mvn(org.apache.maven.shared:maven-plugin-testing) = 2.1
Provides:	mvn(org.apache.maven.shared:maven-plugin-testing:pom:) = 2.1

%description
maven-plugin-testing bootstrap version.

%files
/usr/share/doc/maven-plugin-testing
/usr/share/doc/maven-plugin-testing/LICENSE
/usr/share/doc/maven-plugin-testing/NOTICE
/usr/share/maven-fragments/maven-plugin-testing-maven-plugin-testing.xml
/usr/share/maven-poms/JPP.maven-plugin-testing-maven-plugin-testing.pom

#------------------------------------------------------------------------
%package	-n maven-plugin-testing-harness
Version:	2.1
Release:	9.2
Summary:	maven-plugin-testing-harness bootstrap version
#Requires:	javapackages-bootstrap
Requires:	java >= 1.5
Requires:	jpackage-utils
Requires:	mvn(org.codehaus.plexus:plexus-archiver)
Provides:	maven-plugin-testing-harness = 2.1-9.0:2014.1
Provides:	maven-shared-plugin-testing-harness = 1:2.1-9.0
Provides:	mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness) = 2.1
Provides:	mvn(org.apache.maven.shared:maven-plugin-testing-harness) = 2.1
Obsoletes:	maven-shared-plugin-testing-harness <= 0:1.2

%description	-n maven-plugin-testing-harness
maven-plugin-testing-harness bootstrap version.

%files		-n maven-plugin-testing-harness
/usr/share/java/maven-plugin-testing/maven-plugin-testing-harness.jar
/usr/share/maven-effective-poms/JPP.maven-plugin-testing-maven-plugin-testing-harness.pom
/usr/share/maven-fragments/maven-plugin-testing-maven-plugin-testing-harness.xml
/usr/share/maven-poms/JPP.maven-plugin-testing-maven-plugin-testing-harness.pom

#------------------------------------------------------------------------
%package	-n maven-plugin-testing-javadoc
Version:	2.1
Release:	9.2
Summary:	maven-plugin-testing-javadoc bootstrap version
#Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	maven-plugin-testing-javadoc = 2.1-9.0:2014.1

%description	-n maven-plugin-testing-javadoc
maven-plugin-testing-javadoc bootstrap version.

%files		-n maven-plugin-testing-javadoc
/usr/share/doc/maven-plugin-testing-javadoc
/usr/share/doc/maven-plugin-testing-javadoc/LICENSE
/usr/share/doc/maven-plugin-testing-javadoc/NOTICE
/usr/share/javadoc/maven-plugin-testing
/usr/share/javadoc/maven-plugin-testing/allclasses-frame.html
/usr/share/javadoc/maven-plugin-testing/allclasses-noframe.html
/usr/share/javadoc/maven-plugin-testing/constant-values.html
/usr/share/javadoc/maven-plugin-testing/deprecated-list.html
/usr/share/javadoc/maven-plugin-testing/help-doc.html
/usr/share/javadoc/maven-plugin-testing/index-all.html
/usr/share/javadoc/maven-plugin-testing/index.html
/usr/share/javadoc/maven-plugin-testing/javadoc.sh
/usr/share/javadoc/maven-plugin-testing/options
/usr/share/javadoc/maven-plugin-testing/org
/usr/share/javadoc/maven-plugin-testing/org/apache
/usr/share/javadoc/maven-plugin-testing/org/apache/maven
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/AbstractMojoTestCase.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/ArtifactStubFactory.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/ConfigurationException.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/ResolverExpressionEvaluatorStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/SilentLog.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use/AbstractMojoTestCase.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use/ArtifactStubFactory.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use/ConfigurationException.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use/ResolverExpressionEvaluatorStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/class-use/SilentLog.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/package-frame.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/package-summary.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/package-tree.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/package-use.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/ArtifactStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/DefaultArtifactHandlerStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/MavenProjectStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/StubArtifactCollector.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/StubArtifactRepository.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/StubArtifactResolver.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/ArtifactStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/DefaultArtifactHandlerStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/MavenProjectStub.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/StubArtifactCollector.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/StubArtifactRepository.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/class-use/StubArtifactResolver.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/package-frame.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/package-summary.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/package-tree.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/plugin/testing/stubs/package-use.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/BuildTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/ComponentTestTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/PluginTestTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/ProjectTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/RepositoryTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/TestToolsException.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/BuildTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/ComponentTestTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/PluginTestTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/ProjectTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/RepositoryTool.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/class-use/TestToolsException.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/package-frame.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/package-summary.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/package-tree.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/test/plugin/package-use.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/MockManager.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/TestFileManager.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/TestUtils.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/class-use
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/class-use/MockManager.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/class-use/TestFileManager.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/class-use/TestUtils.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/package-frame.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/package-summary.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/package-tree.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/easymock/package-use.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/ReflectiveSetter.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/class-use
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/class-use/ReflectiveSetter.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/package-frame.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/package-summary.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/package-tree.html
/usr/share/javadoc/maven-plugin-testing/org/apache/maven/shared/tools/test/package-use.html
/usr/share/javadoc/maven-plugin-testing/overview-frame.html
/usr/share/javadoc/maven-plugin-testing/overview-summary.html
/usr/share/javadoc/maven-plugin-testing/overview-tree.html
/usr/share/javadoc/maven-plugin-testing/package-list
/usr/share/javadoc/maven-plugin-testing/packages
/usr/share/javadoc/maven-plugin-testing/resources
/usr/share/javadoc/maven-plugin-testing/resources/background.gif
/usr/share/javadoc/maven-plugin-testing/resources/tab.gif
/usr/share/javadoc/maven-plugin-testing/resources/titlebar.gif
/usr/share/javadoc/maven-plugin-testing/resources/titlebar_end.gif
/usr/share/javadoc/maven-plugin-testing/serialized-form.html
/usr/share/javadoc/maven-plugin-testing/stylesheet.css

#------------------------------------------------------------------------
%package	-n maven-plugin-testing-tools
Version:	2.1
Release:	9.2
Summary:	maven-plugin-testing-tools bootstrap version
#Requires:	javapackages-bootstrap
Requires:	java >= 1.5
Requires:	jpackage-utils
Requires:	mvn(org.apache.maven.shared:maven-invoker)
Provides:	maven-plugin-testing-tools = 2.1-9.0:2014.1
Provides:	maven-shared-plugin-testing-tools = 1:2.1-9.0
Provides:	mvn(org.apache.maven.plugin-testing:maven-plugin-testing-tools) = 2.1
Provides:	mvn(org.apache.maven.shared:maven-plugin-testing-tools) = 2.1
Obsoletes:	maven-shared-plugin-testing-tools <= 0:2.1-9.0

%description	-n maven-plugin-testing-tools
maven-plugin-testing-tools bootstrap version.

%files		-n maven-plugin-testing-tools
/usr/share/java/maven-plugin-testing/maven-plugin-testing-tools.jar
/usr/share/maven-effective-poms/JPP.maven-plugin-testing-maven-plugin-testing-tools.pom
/usr/share/maven-fragments/maven-plugin-testing-maven-plugin-testing-tools.xml
/usr/share/maven-poms/JPP.maven-plugin-testing-maven-plugin-testing-tools.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
