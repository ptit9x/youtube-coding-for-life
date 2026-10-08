# TaskFlow — Target Architecture Reference

> This file is loaded by the `nest-feature` skill when scaffolding or extending
> a business feature. It describes the current directory layout and dependency
> rules of the TaskFlow project.

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
│   ├── decorators/                  # @CurrentUser, @Public, etc.
│   ├── filters/                     # Global exception filters
│   ├── guards/                      # Global guards (if any)
│   ├── interceptors/                # Logging, transform response
│   ├── pipes/                       # AppValidationPipe
│   ├── constants/                   # App-wide constants
│   └── utils/                       # Pure utility functions
├── config/
│   ├── app.config.ts                # App configuration factory
│   ├── database.config.ts           # Database URL config
│   └── env.validation.ts            # Zod schema for .env
├── database/
│   ├── database.module.ts           # Prisma provider registration
│   ├── prisma.provider.ts           # DI token + factory
│   └── repositories/               # Prisma adapters implement contracts
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
    │   ├── guards/                  # JwtAuthGuard
    │   └── strategies/              # JwtStrategy
    ├── access-control/              # Roles, Permissions, assignments
    │   ├── roles/
    │   ├── permissions/
    │   ├── assignments/
    │   ├── decorators/              # @RequirePermissions
    │   ├── guards/                  # PermissionGuard
    │   └── types/
    └── tasks/
        ├── tasks.module.ts
        ├── tasks.controller.ts
        ├── tasks.service.ts
        ├── dto/
        └── tasks.repository.ts

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

## Prisma 8 workflow

```text
Edit contract.prisma
  → prisma contract emit
  → prisma migration plan --name <migration-name>
  → Review migration.ts + ops.json + DDL preview
  → prisma db migrate --advance-ref db
  → prisma db verify
  → Run tests
```

## Banned patterns (Prisma 7)

- `@prisma/client`
- `PrismaClient`
- `prisma generate`
- `schema.prisma`
- `prisma migrate dev`
- `prisma migrate deploy`
- `prisma.user.findMany()` style queries
