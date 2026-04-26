---
name: dotnet-conventions
description: 'Ensure .NET/C# code meets best practices for the solution/project. Delegates CLI commands to the dotnet-cli sub-skill.'
---

# .NET/C# Best Practices

Routes build, test, and tooling requests to the appropriate sub-skill before applying code conventions.

> ⚠️ **CRITICAL**: Always validate code practices and API usage against **Microsoft Learn** using the `microsoft-learn` MCP. Do not rely on assumptions about SDK patterns, APIs, or best practices — check the official documentation.

## Sub-skill Delegate Map

| Request type                                                | Sub-skill to invoke                   |
| ----------------------------------------------------------- | ------------------------------------- |
| Build, test, run, publish, format, or manage NuGet packages | [`dotnet-cli`](references/net-cli.md) |

> Always use the dotnet CLI for package management and project operations — never edit `.csproj` files directly to add or remove packages.

---

Your task is to ensure .NET/C# code in ${selection} meets the best practices specific to this solution/project. This includes:

## Naming Conventions

- Use `PascalCase` for all public classes, methods, and properties
- Use `camelCase` for private fields and local variables

## Documentation & Structure

- Create comprehensive XML documentation comments for all public classes, interfaces, methods, and properties
- Include parameter descriptions and return value descriptions in XML comments
- Follow the established namespace structure: {Core|Console|App|Service}.{Feature}

## Design Patterns & Architecture

- Use .NET primary constructors with no private backing fields unless additional logic is required; migrate existing classes to primary constructors where feasible
- Use primary constructor syntax for dependency injection (e.g., `public class MyClass(IDependency dependency)`)
- Implement the Command Handler pattern with generic base classes (e.g., `CommandHandler<TOptions>`)
- Use interface segregation with clear naming conventions (prefix interfaces with 'I')
- Follow the Factory pattern for complex object creation.

## Dependency Injection & Services

- Use constructor dependency injection with null checks via ArgumentNullException
- Register services with appropriate lifetimes (Singleton, Scoped, Transient)
- Use Microsoft.Extensions.DependencyInjection patterns
- Implement service interfaces for testability

## Resource Management & Localization

- Use ResourceManager for localized messages and error strings
- Separate LogMessages and ErrorMessages resource files
- Access resources via `_resourceManager.GetString("MessageKey")`

## Async/Await Patterns

- Use async/await for all I/O operations and long-running tasks
- Return Task or Task<T> from async methods
- Use ConfigureAwait(false) where appropriate
- Handle async exceptions properly

## Testing Standards

- Use MSTest framework with FluentAssertions for assertions
- Follow AAA pattern (Arrange, Act, Assert)
- Use Moq for mocking dependencies
- Test both success and failure scenarios
- Include null parameter validation tests

## Configuration & Settings

- Use strongly-typed configuration classes with data annotations
- Implement validation attributes (Required, NotEmptyOrWhitespace)
- Use IConfiguration binding for settings
- Support appsettings.json configuration files

## Microsoft Foundry & Microsoft Agent Framework

- Use Microsoft Agent Framework for building and hosting AI agents
- Deploy and manage agents via Microsoft Foundry (not direct SK kernel wiring)
- Use the `microsoft-foundry` MCP for all agent deployment, evaluation, and management workflows
- Use `Microsoft.Extensions.AI` abstractions for chat completion and embeddings
- Register agents and tools through the Microsoft Agent Framework's service registration patterns
- Use structured output patterns for reliable AI responses

## Error Handling & Logging

- Use structured logging with Microsoft.Extensions.Logging
- Include scoped logging with meaningful context
- Throw specific exceptions with descriptive messages
- Use try-catch blocks for expected failure scenarios

## Performance & Security

- Use C# 12+ features and .NET 8 optimizations where applicable
- Implement proper input validation and sanitization
- Use parameterized queries for database operations
- Follow secure coding practices for AI/ML operations

## Application Lifecycle

- Before starting the application, check if an instance is already running; if it is running under `dotnet watch run`, reuse that instance instead of starting a new one
- Never start the application as a background process
- Always dispose of resources properly when the application closes

## Code Quality

- Ensure SOLID principles compliance
- Avoid code duplication through base classes and utilities
- Use meaningful names that reflect domain concepts
- Keep methods focused and cohesive
- Implement proper disposal patterns (`IDisposable` / `IAsyncDisposable`) for all resources
