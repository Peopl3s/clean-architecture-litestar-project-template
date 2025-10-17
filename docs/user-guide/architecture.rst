Architecture
============

This project follows **Clean Architecture** principles to maintain separation of concerns and ensure the application remains testable, maintainable, and independent of external concerns.

Overview
--------

Clean Architecture organizes code into concentric layers, with the business logic at the center and infrastructure details at the outer layers. This ensures that:

- Business rules don't depend on external frameworks or databases
- The application can be tested without UI, database, or external services
- Business logic is isolated from technical implementation details

Layer Structure
---------------

Domain Layer (Innermost)
~~~~~~~~~~~~~~~~~~~~~~~~

The domain layer contains the core business logic and is completely independent of external concerns.

**Components:**

- **Entities** (`src/{{cookiecutter.project_slug}}/domain/entities/`): Core business objects with enterprise-wide business rules
  - ``Artifact``: Main business entity representing museum artifacts

- **Value Objects** (`src/{{cookiecutter.project_slug}}/domain/value_objects/`): Immutable objects with no identity
  - ``Era``: Represents historical periods
  - ``Material``: Represents artifact materials

- **Domain Exceptions** (`src/{{cookiecutter.project_slug}}/domain/exceptions/`): Business rule violations

**Key Principles:**
- No external dependencies
- Pure Python objects
- Contains only business logic

Application Layer
~~~~~~~~~~~~~~~~~

The application layer contains use cases and application-specific business rules.

**Components:**

- **Use Cases** (`src/{{cookiecutter.project_slug}}/application/use_cases/`): Application-specific business rules
  - ``ProcessArtifactUseCase``: Main orchestration use case
  - ``FetchArtifactFromMuseumAPI``: External API integration
  - ``GetArtifactFromCache``/``SaveArtifactToCache``: Cache operations
  - ``GetArtifactFromRepo``/``SaveArtifactToRepo``: Database operations
  - ``PublishArtifactToBroker``/``PublishArtifactToCatalog``: Publishing operations

- **DTOs** (`src/{{cookiecutter.project_slug}}/application/dtos/`): Data Transfer Objects for inter-layer communication
  - ``ArtifactDTO``: Main data transfer object
  - ``EraDTO``/``MaterialDTO``: Value object DTOs

- **Interfaces** (`src/{{cookiecutter.project_slug}}/application/interfaces/`): Abstractions for infrastructure components
  - ``Repositories``: Data access abstractions
  - ``Serialization``: Data transformation abstractions
  - ``MessageBroker``/``Cache``/``HTTPClients``: External service abstractions

**Key Principles:**
- Depends only on Domain layer
- Contains application orchestration logic
- Defines interfaces for infrastructure implementations

Infrastructure Layer
~~~~~~~~~~~~~~~~~~~~

The infrastructure layer contains implementations of application interfaces and external concerns.

**Components:**

- **Database** (`src/{{cookiecutter.project_slug}}/infrastructures/db/`):
  - ``Models``: SQLAlchemy ORM models
  - ``Repositories``: Repository pattern implementations
  - ``Mappers``: Database entity to domain object mapping
  - ``UnitOfWork``: Transaction management

- **Cache** (`src/{{cookiecutter.project_slug}}/infrastructures/cache/`):
  - ``RedisClient``: Redis cache implementation

- **HTTP Clients** (`src/{{cookiecutter.project_slug}}/infrastructures/http/`):
  - External API client implementations

- **Message Broker** (`src/{{cookiecutter.project_slug}}/infrastructures/broker/`):
  - ``Publisher``: Kafka/message queue publisher

- **Infrastructure Mappers** (`src/{{cookiecutter.project_slug}}/infrastructures/mappers/`):
  - ``InfrastructureArtifactMapper``: Serialization for external APIs and caching

**Key Principles:**
- Implements application interfaces
- Contains all external dependencies
- Handles technical implementation details

Presentation Layer (Outermost)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The presentation layer handles user interfaces and external communication.

**Components:**

- **REST API** (`src/{{cookiecutter.project_slug}}/presentation/api/rest/`):
  - ``Controllers``: Litestar endpoint handlers
  - ``Schemas``: Pydantic models for request/response validation
  - ``Mappers``: DTO to schema transformation

- **Response Schemas** (`src/{{cookiecutter.project_slug}}/presentation/api/rest/v1/schemas/`):
  - ``ArtifactResponseSchema``: Main API response model
  - ``EraResponseSchema``/``MaterialResponseSchema``: Value object response models

- **Presentation Mappers** (`src/{{cookiecutter.project_slug}}/presentation/api/rest/v1/mappers/`):
  - ``ArtifactPresentationMapper``: Converts DTOs to API response schemas

**Key Principles:**
- Depends only on Application layer
- Handles HTTP concerns
- Manages request/response transformation

Key Architectural Patterns
--------------------------

Dependency Inversion
~~~~~~~~~~~~~~~~~~~~~

All dependencies point inward, following the Dependency Inversion Principle:

- Domain layer has no dependencies
- Application layer depends only on Domain
- Infrastructure layer implements Application interfaces
- Presentation layer depends on Application

This is enforced through dependency injection using ``dishka`` container.

Mapper Pattern
~~~~~~~~~~~~~~

Multiple mapper types handle data transformation between layers:

1. **Infrastructure Mappers**: DTO ↔ Dictionary (for JSON serialization)
2. **Database Mappers**: Domain Entity ↔ ORM Model
3. **Presentation Mappers**: DTO ↔ Response Schema

Each mapper has a single responsibility and maintains separation between layers.

Repository Pattern
~~~~~~~~~~~~~~~~~~

Data access is abstracted through repository interfaces:

- ``ArtifactRepository`` interface defined in Application layer
- ``ArtifactRepositoryImpl`` implementation in Infrastructure layer
- Enables testing with mock repositories
- Allows switching database implementations

Unit of Work Pattern
~~~~~~~~~~~~~~~~~~~~~

Transaction management is handled through Unit of Work:

- ``UnitOfWork`` interface defines transaction boundaries
- ``SqlAlchemyUnitOfWork`` provides database transaction management
- Ensures atomic operations across multiple repositories

Data Flow Example
-----------------

Here's how a typical request flows through the architecture:

1. **HTTP Request** → Presentation Layer
   - Litestar controller receives request
   - Validates request schema

2. **Controller** → Application Layer
   - Calls use case with dependency-injected dependencies
   - Passes input DTOs

3. **Use Case** → Domain + Infrastructure
   - Executes business logic using domain entities
   - Uses repositories for data persistence
   - Uses external services for integration

4. **Response Flow** (reverse order)
   - Domain entities → DTOs
   - DTOs → Response schemas
   - Response schemas → HTTP response

InfrastructureMapper Analysis
------------------------------

The ``InfrastructureArtifactMapper`` is a **necessary and architecturally sound** component:

**Purpose:**
- Converts Application DTOs to dictionaries for JSON serialization
- Handles transformation for external APIs, caching, and message brokers
- Implements ``SerializationMapperProtocol`` from Application layer

**Clean Architecture Compliance:**
✅ **Follows Dependency Inversion**: Implements Application interface
✅ **Single Responsibility**: Only handles serialization concerns
✅ **Isolation**: Keeps Application layer clean from JSON/serialization details

**Usage Examples:**
- HTTP client request/response serialization
- Redis cache key-value storage
- Message broker payload formatting
- External catalog API integration

**Why It's Necessary:**
- Application DTOs shouldn't know about JSON serialization
- Different external systems may require different formats
- Enables testing without actual serialization
- Maintains clean separation between business logic and technical concerns

Schema Naming Convention
------------------------

All response schemas now follow the ``*Schema`` naming convention for clarity:

- ``ArtifactResponseSchema`` (was ``ArtifactResponse``)
- ``EraResponseSchema`` (was ``EraResponse``)
- ``MaterialResponseSchema`` (was ``MaterialResponse``)

This naming convention:
- Clearly distinguishes schemas from DTOs and entities
- Indicates these are Pydantic validation models
- Maintains consistency across the presentation layer
- Improves code readability and maintainability

Benefits of This Architecture
----------------------------

**Testability:**
- Each layer can be tested in isolation
- Business logic can be tested without external dependencies
- Easy to mock infrastructure components

**Maintainability:**
- Clear separation of concerns
- Changes to external systems don't affect business logic
- Each component has a single responsibility

**Flexibility:**
- Easy to swap implementations (databases, caches, APIs)
- Can add new presentation layers (GraphQL, gRPC) without changing core
- Supports incremental migration and evolution

**Scalability:**
- Layers can be scaled independently
- Clear boundaries help with team organization
- Enables microservice decomposition if needed

See Also
--------

* :doc:`../development/code-quality` - Code standards
* :doc:`testing` - Testing strategies
* :doc:`../advanced/best-practices` - Advanced patterns
