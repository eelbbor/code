# Overview
The java package of the codebase contains services and components. Unit tests live here as well.

### Core Pattern
Services consume one or more libraries to provide encapsulated functionality. Libraries are intended to be discrete 
capabilities with narrow focus. As this is part of a monorepo the libraries are not necessarily intended to be built
as library binaries.

NOTE: As more areas of distinctions arrise the sandbox exists for playing but should not be considered ready for use.

### Structure:
- ./libs: General libraries for usage in the java package. View its [README](libs/README.md) for more info
- ./sandbox: Playground for testing and experimenting. View its [README](services/README.md) for more info
- ./services: Wraps components and constructs a service with an endpoint to be hit. View its [README](services/README.md) for more info