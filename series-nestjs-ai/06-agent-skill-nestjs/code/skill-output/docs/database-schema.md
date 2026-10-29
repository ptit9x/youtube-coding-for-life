# Database Schema — nestjs-base-with-ai

> Cold Memory: read when changing models, relations, or migrations.

## Current models (from `contract.prisma`)

### User

| Field | Type | Constraints |
|---|---|---|
| id | String | `@id @default(cuid())` |
| email | String | `@unique` |
| name | String | |
| password | String | Hashed with bcrypt |
| createdAt | DateTime | `@default(now())` |
| updatedAt | DateTime | `@updatedAt` |

## Migration workflow

```text
Edit contract.prisma
  → prisma contract emit
  → prisma migration plan --name <migration-name>
  → Review migration.ts + ops.json + DDL preview
  → prisma db migrate --advance-ref db
  → prisma db verify
  → Run tests
```

### Commands reference

```bash
# Emit contract artifacts (contract.json, contract.d.ts)
npx prisma contract emit

# Plan a new migration
npx prisma migration plan --name <migration-name>

# Apply migration
npx prisma db migrate --advance-ref db

# Verify database matches contract
npx prisma db verify
```

## Patterns in use

- **Contract-first:** `contract.prisma` is the single source of truth
- **Emitted artifacts committed:** `contract.json` and `contract.d.ts` are tracked in git
- **Database facade:** `src/prisma/db.ts` provides the typed query API
- **DI token:** `DB_FACADE` token in `DatabaseModule` — adapters receive the facade via constructor injection
- **cuid IDs:** all models use `@default(cuid())` for primary keys

## Banned patterns (Prisma 7)

| ❌ WRONG (Prisma 7) | ✅ CORRECT (Prisma 8) |
|---|---|
| `import { PrismaClient } from '@prisma/client'` | `import { db } from '../prisma/db'` |
| `new PrismaClient()` | Inject via `DB_FACADE` token |
| `prisma generate` | `prisma contract emit` |
| `schema.prisma` | `contract.prisma` |
| `prisma migrate dev` | `prisma migration plan --name <name>` |
| `prisma migrate deploy` | `prisma db migrate --advance-ref db` |
| `prisma.user.findMany()` | `db.user.findMany()` |

