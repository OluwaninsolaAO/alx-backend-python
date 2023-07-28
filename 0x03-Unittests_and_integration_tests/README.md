# 0x03. Unittests and Integration Tests

`Unit tests` in software testing are designed to test individual units or components of code in isolation. Their primary purpose is to ensure that each unit functions correctly and independently of other parts of the application. Typically, unit tests are written for functions, methods, or small classes to validate their behavior with various inputs. These tests are fast, focused, and ideal for rapid testing during development.

On the other hand, `integration tests` check how different parts of the application work together. They focus on testing the interaction and integration between components, modules, or external services, often requiring actual dependencies or using mock objects that resemble those dependencies. Integration tests are broader in scope and can identify issues that may not be apparent in isolated unit tests, though they may take longer to execute and are run less frequently.

A well-balanced testing strategy includes both unit tests and integration tests, providing a comprehensive approach to ensuring code quality and application behavior.

### Learning Objectives

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures
