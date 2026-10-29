# Architecture — nestjs-base-with-ai

> Cold Memory: read when changing module boundaries or dependency direction.

## Directory layout

```text
src/
├── main.ts                          # Bootstrap, global pipes/filters
├── app.module.ts                    # Root module, imports all feature modules
├── prisma/
│   ├── contract.prisma              # PSL source of truth
│   ├── contract.json                # Emitted contract (committed)
│   ├── contract.d.ts                # Emitted types (committed)
│   └── db.ts                        # Database facade (Prisma 8)
├── common/                          # Cross-cutting, domain-independent
│   ├── filters/                     # Global exception filters
│   ├── pipes/                       # AppValidationPipe
│   └── utils/                       # Pure utility functions
├── config/
│   ├── app.config.ts                # App configuration factory
│   ├── database.config.ts           # Database URL config
│   └── env.validation.ts            # Zod schema for .env
├── database/
│   ├── database.module.ts           # Prisma provider registration
│   ├── db-facade.token.ts           # DI token for Prisma 8 facade
│   ├── index.ts                     # Barrel export
│   └── prisma-*.repository.ts       # Prisma adapters implement contracts
└── modules/
    ├── users/
    │   ├── users.module.ts
    │   ├── users.controller.ts      # Thin: parse request, call service
    │   ├── users.service.ts         # Business logic
    │   ├── dto/                     # CreateUserDto, UpdateUserDto
    │   └── users.repository.ts      # Contract (pure interface)
    ├── auth/
    │   ├── auth.module.ts
    │   ├── auth.controller.ts
    │   ├── auth.service.ts
    │   ├── dto/
    │   └── jwt-auth.provider.ts     # JwtBearerProvider (credential validation)
    └── ...                          # Future feature modules

migrations/
└── app/                             # Prisma 8 migration history
prisma.config.ts                     # Prisma CLI configuration
```

## Dependency direction

```text
Controller
  │  (parse request, return response — NO business logic)
  ▼
Service / Use Case
  │  (business rules, validation, orchestration)
  ▼
Repository Contract  ◄────  Prisma Adapter
  (pure interface,           (implements contract,
   no Prisma imports)         receives db facade via DI)
                                      │
                                      ▼
                              Database Facade (db.ts)
                              (Prisma 8 query API)
```

## Layer responsibilities

| Layer | Responsibility | Forbidden |
|---|---|---|
| **Controller** | HTTP transport: parse params/body, call service, return DTO | Business logic, direct DB access |
| **Service** | Business rules, authorization checks, orchestration | Direct Prisma calls, HTTP concerns |
| **Repository Contract** | Define data access interface as pure TypeScript | Import Prisma, database types |
| **Prisma Adapter** | Implement contract using Prisma 8 facade | Business logic, HTTP concerns |
| **common/** | Cross-cutting utilities used by 2+ consumers | Import from modules/, config/, database/ |

## Module dependency map

```text
AppModule
├── ConfigModule (global)
├── DatabaseModule (global — provides db facade token)
├── UsersModule
│   └── imports DatabaseModule (uses adapter via DI token)
└── AuthModule
    └── imports UsersModule (uses UsersService for credential check)
```

- `UsersModule` does NOT import `AuthModule` — no circular dependency.
- `AuthModule` depends on `UsersModule` for user lookup during authentication.
- Both modules receive the Prisma 8 facade via the `DB_FACADE` injection token from `DatabaseModule`.

