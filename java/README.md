# Overview
The java package of the codebase contains services and libraries. Unit tests live here as well.

### Background Reading:
- [JUNIT](https://junit.org/junit5/docs/current/user-guide/#overview)

### Core Pattern
Services consume libraries and should provide servable entity. Libraries should be a well-defined foundational bits to 
build on.

TODO Generate a script to enable easy scaffolding based on type.

### Structure:
- ./libs: General libraries for usage in the java package.
- ./components: All business logic lies here.
- ./services: Wraps components and constructs a service with an endpoint to be hit.
- ./sandbox: General play area but not considered for use in libraries or services. 
View its [README](sandbox/README.md) for more info.
