# TaskFlow

Task management REST API built with NestJS 12, TypeScript 5.9+, Prisma 8 and
PostgreSQL. Runs on Node 24 with ESM. Architecture: modular monolith organized
by business domain. Authentication uses JWT access tokens with refresh token
rotation.

## Directory layout

```text
src/
├── main.ts              # Bootstrap
├── app.module.ts        # Root module
├── prisma/              # Prisma 8 contract, emitted artifacts, db facade
├── common/              # Cross-cutting utilities (2+ consumers, domain-free)
├── config/              # App/database config + Zod env validation
├── database/            # DatabaseModule, Prisma provider, repository adapters
└── modules/
    ├── users/           # User registration, profile
    ├── auth/            # JWT auth, refresh tokens, session
    ├── access-control/  # Roles, Permissions, assignments, guards
    └── tasks/           # Business feature: task CRUD with ownership
migrations/app/          # Prisma 8 migration history
prisma.config.ts         # Prisma CLI config
```

## Dependency rules

1. Dependencies flow one direction:
   `controller → service/use-case → repository contract ← adapter → db facade`
2. Controllers handle transport only — no business logic.
3. Business rules stay in service or use case, explicit per feature.
4. Repository contracts are pure interfaces — no Prisma imports.
5. `common/` does not import from `modules/`, `config/`, or `database/`.
6. No generic business CRUD service (`BaseCrudService<T>`). Even when method
   names match, business semantics differ.
7. Feature-specific code (guards, decorators, policies) stays in its module.

## Database — Prisma 8

- **Contract:** `src/prisma/contract.prisma` (PSL source of truth)
- **Emitted:** `contract.json`, `contract.d.ts` (committed to git)
- **Facade:** `src/prisma/db.ts` (query API entry point)
- **Migrations:** `migrations/app/`

### Workflow

```text
Edit contract.prisma
→ prisma contract emit
→ prisma migration plan --name <name>
→ Review migration + DDL
→ prisma db migrate --advance-ref db
→ prisma db verify
→ Run tests
```

### Banned (Prisma 7)

Do NOT use: `@prisma/client`, `PrismaClient`, `prisma generate`,
`schema.prisma`, `migrate dev`, `migrate deploy`.

Always check [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status)
and [Prisma 8 docs](https://www.prisma.io/docs/orm) before writing database code.

## Environment

- `.env` is gitignored. `.env.example` has placeholders only.
- All env vars validated at startup via ConfigModule + Zod.
- Docker Compose uses required variable interpolation.

## Testing

- **Framework:** Vitest 4 (`globals: true`)
- **Unit:** mock repository contracts, test service logic
- **E2E:** Supertest against real PostgreSQL
- **Run:** `npm test` (unit), `npm run test:e2e` (integration)

## Agent workflow

1. Read the nearest completed feature before creating a new one.
2. Present file plan and dependency direction. Wait for approval.
3. After implementation, run verification:
   - `prisma contract emit` + `prisma migration check` (if contract changed)
   - Lint, test, diff summary scoped to changed files
4. Reference Prisma 8 docs directly — do not use search-result snippets from
   Prisma 6/7.
