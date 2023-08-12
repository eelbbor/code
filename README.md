# The Code

This monorepo houses the libraries, tools and services.

## Repo Structure

- ./java: Contains all java projects i.e. libraries and services. For more info, look at the [java README.md](java/README.md)
- ./js: Contains all web frontend projects. For more info, look at the [js README.md](js/README.md)

------------
## Quickstart

### Clone the repo
```shell
> git clone https://github.com/eelbbor/code.git eelborr_code
> cd eelborr_code
```

### Install dependencies
At the time of this writing the install tips are specific to development on a Mac using brew.
```shell
> ./setup.sh
```

## Built With
* [Bazelisk] (https://github.com/bazelbuild/bazelisk) Wrapper for [Bazel](https://bazel.build/)
* [OpenJdk17](https://openjdk.org/projects/jdk/17/)
* [REACTJS](https://reactjs.org/)
* [YARN](https://yarnpkg.com/)
* [NPM](https://www.npmjs.com/)