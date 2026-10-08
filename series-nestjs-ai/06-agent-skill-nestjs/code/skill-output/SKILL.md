---
name: nest-feature
description: >
  Scaffold or extend a TaskFlow NestJS business feature module.
  Use when creating or modifying modules, controllers, services, DTOs,
  repository contracts and Prisma adapters within src/modules/.
  Do NOT use for one-line fixes, README edits, infrastructure-only changes,
  config-only changes, or CI/CD pipeline work.
---

## Before you start

1. Read `references/architecture.md` for the target directory layout and
   dependency diagram.
2. Read the nearest completed feature module (e.g. `src/modules/users/` or
   `src/modules/auth/`) to absorb the established patterns.

## Workflow

3. Present the file plan and dependency direction **before editing any file**.
   Wait for explicit approval.
4. After approval, implement in this order: contract → types/DTOs → service →
   controller → module registration → tests.

## Architecture rules

5. **Controllers are thin.** They parse the request, call the service, and
   return the response. No business logic.
6. **Business rules live in services or use cases.** Each feature has its own
   explicit service — no shared business logic across features.
7. **Never create generic business CRUD abstractions** (`BaseCrudService`,
   `CommonService<T>`, or similar). Even when CRUD method names look
   identical, the business rules behind create/update/delete differ per
   feature.
8. **Repository contracts are pure interfaces** — no Prisma imports, no
   database types. They define what the feature needs, not how it's stored.
9. **Prisma adapters implement contracts**, receive the Prisma 8 database
   facade via DI token, and live near `src/database/`.
10. **Domain-specific code stays in its module.** Do not move feature-specific
    logic into `common/`. Only cross-cutting concerns with 2+ consumers
    belong in `common/`.

## Prisma 8 — mandatory

11. Before any database change, check the
    [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status)
    and read the relevant
    [Prisma 8 documentation](https://www.prisma.io/docs/orm).
12. Use `contract.prisma`, emitted contract artifacts (`contract.json`,
    `contract.d.ts`), and the database facade (`src/prisma/db.ts`).
13. **Never use** `@prisma/client`, `PrismaClient`, `prisma generate`,
    `schema.prisma`, `migrate dev`, or `migrate deploy`. These are Prisma 7
    patterns.
14. Use the Prisma 8 migration workflow: edit contract → `prisma contract emit`
    → `prisma migration plan --name <name>` → review → apply → verify.

## Verification (after every change)

15. Run `prisma contract emit` and `prisma migration check` when the contract
    changes.
16. Run lint, tests (`npm test`), and show the diff summary scoped to the
    changed files.
