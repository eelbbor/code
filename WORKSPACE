load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


### Java External
JVM_EXTERNAL_VERSION = "4.5"
JVM_EXTERNAL_SHA = "b17d7388feb9bfa7f2fa09031b32707df529f26c91ab9e5d909eb1676badd9a6"

http_archive(
    name = "rules_jvm_external",
    strip_prefix = "rules_jvm_external-%s" % JVM_EXTERNAL_VERSION,
    sha256 = JVM_EXTERNAL_SHA,
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/%s.zip" % JVM_EXTERNAL_VERSION,
)

load("@rules_jvm_external//:repositories.bzl", "rules_jvm_external_deps")
rules_jvm_external_deps()

load("@rules_jvm_external//:setup.bzl", "rules_jvm_external_setup")
rules_jvm_external_setup()

# Load external dependencies from maven.
load("//java:DEPENDENCIES.bzl", "JAVA_REPOS", "JAVA_DEPENDENCIES")
load("@rules_jvm_external//:defs.bzl", "maven_install")
maven_install(
    artifacts = JAVA_DEPENDENCIES,
    fetch_sources = True,
    repositories = JAVA_REPOS,
)

# Contrib Java
CONTRIB_RULES_JAVA_VERSION = "0.18.0"
CONTRIB_RULES_JAVA_SHA = "bd0f82def1879df85ff0a80767e6455911e1c9c1eac5db1de8f68dcccd4a3d7a"
http_archive(
    name = "contrib_rules_jvm",
    sha256 = CONTRIB_RULES_JAVA_SHA,
    strip_prefix = "rules_jvm-%s" % CONTRIB_RULES_JAVA_VERSION,
    url = "https://github.com/bazel-contrib/rules_jvm/archive/v%s.tar.gz" % CONTRIB_RULES_JAVA_VERSION,
)

load("@contrib_rules_jvm//:repositories.bzl", "contrib_rules_jvm_deps")
contrib_rules_jvm_deps()

load("@contrib_rules_jvm//:setup.bzl", "contrib_rules_jvm_setup")
contrib_rules_jvm_setup()

