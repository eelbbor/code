"""Common dependencies for Java rules."""

JAVA_REPOS = [
    "https://repo.maven.apache.org/maven2/",
]

JAVA_VERSIONS = {
    "guava": "32.1.2-jre",
    "junit-jupiter": "5.10.0",
    "junit-platform": "1.10.0",
}

JAVA_DEPENDENCIES = [
    "com.google.guava:guava:{}".format(JAVA_VERSIONS["guava"]),
    "org.junit.platform:junit-platform-launcher:{}".format(JAVA_VERSIONS["junit-platform"]),
    "org.junit.platform:junit-platform-reporting:{}".format(JAVA_VERSIONS["junit-platform"]),
    "org.junit.jupiter:junit-jupiter-api:{}".format(JAVA_VERSIONS["junit-jupiter"]),
    "org.junit.jupiter:junit-jupiter-params:{}".format(JAVA_VERSIONS["junit-jupiter"]),
    "org.junit.jupiter:junit-jupiter-engine:{}".format(JAVA_VERSIONS["junit-jupiter"]),
]