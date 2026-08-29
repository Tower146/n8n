# CLAUDE.md

Guidance for Claude Code (and other AI assistants) working in this repository.

## What this is

n8n is a fair-code workflow automation platform. This repo is a **pnpm + Turborepo
monorepo** (`n8n-monorepo`) containing the backend, the Vue editor UI, the ~300 built-in
integration nodes, and the shared libraries that tie them together.

- **Node.js** `>=20.15`, **pnpm** `>=10.2.1` (pinned via `packageManager: pnpm@10.2.1`)
- `npm install` / `yarn install` are **blocked** by `scripts/block-npm-install.js`. Always use `pnpm`.
- Workspace globs live in `pnpm-workspace.yaml`: `packages/*`, `packages/@n8n/*`,
  `packages/frontend/**`, `cypress`. Shared dependency versions are pinned in that file's
  `catalog:` / `catalogs.frontend:` blocks — add new shared deps there rather than
  version-by-version in each package.

## Package map

### Backend / core
| Package | Path | Purpose |
| --- | --- | --- |
| `n8n` | `packages/cli` | The CLI and server: REST controllers, DB layer, auth, scaling, execution lifecycle |
| `n8n-core` | `packages/core` | Workflow execution engine, active webhooks, binary data. **Contact n8n maintainers before changing** |
| `n8n-workflow` | `packages/workflow` | Shared interfaces, expression evaluation, node helpers used by both front- and backend |
| `n8n-node-dev` | `packages/node-dev` | CLI for scaffolding custom nodes |

### Nodes
| Package | Path | Purpose |
| --- | --- | --- |
| `n8n-nodes-base` | `packages/nodes-base` | ~300 built-in nodes + ~381 credential types |
| `@n8n/n8n-nodes-langchain` | `packages/@n8n/nodes-langchain` | AI / LangChain nodes (agents, chains, vector stores) |

### Frontend
| Package | Path | Purpose |
| --- | --- | --- |
| `n8n-editor-ui` | `packages/frontend/editor-ui` | The Vue 3 workflow editor |
| `@n8n/design-system` | `packages/frontend/@n8n/design-system` | Shared Vue component library |
| `@n8n/composables` | `packages/frontend/@n8n/composables` | Shared Vue composables |
| `@n8n/chat` | `packages/frontend/@n8n/chat` | Embeddable chat widget |

### Shared `@n8n/*` libraries (`packages/@n8n/`)
`api-types` (request/response DTOs), `config` (typed env config), `di` (dependency-injection
container), `permissions` (scopes/roles), `utils`, `client-oauth2`, `imap`,
`codemirror-lang` (n8n expression language), `json-schema-to-zod`, `task-runner`
(sandboxed code execution), `benchmark`, plus tooling configs: `eslint-config`,
`typescript-config`, `vitest-config`, `storybook`.

### Other top-level dirs
- `cypress/` — E2E test suite (its own workspace package, `n8n-cypress`)
- `docker/images/` — Dockerfiles
- `scripts/` — repo maintenance scripts (`reset.mjs`, `format.mjs`, `prepare.mjs`)
- `patches/` — pnpm `patchedDependencies` (bull, pyodide, vue-tsc, several `@types/*`)

## Commands

All root commands fan out through Turborepo, so they respect the dependency graph.

### Setup and run
```bash
pnpm install          # install everything
pnpm build            # build all packages (turbo run build)
pnpm start            # run n8n from packages/cli/bin
pnpm dev              # watch-mode for backend + editor (excludes design-system, chat, task-runner)
pnpm dev:be           # backend only
pnpm dev:fe           # editor UI + design system
pnpm dev:ai           # langchain nodes + cli + core
pnpm reset            # nuke build artifacts / node_modules and start clean
```

### Verify — run these before pushing
```bash
pnpm typecheck        # tsc --noEmit across packages (vue-tsc for editor-ui)
pnpm lint             # eslint
pnpm lintfix          # eslint --fix
pnpm format           # biome format + prettier
pnpm format:check     # CI-equivalent format check
pnpm test             # all tests
```

Scoped variants exist for each: `build:backend|frontend|nodes`,
`lint:backend|frontend|nodes`, `test:backend|frontend|nodes`. The scoped test tasks run
with `--concurrency=1`.

Prefer running checks in the package you touched — it is far faster than the root task:

```bash
cd packages/cli && pnpm test          # jest, sqlite by default
cd packages/cli && pnpm typecheck
cd packages/frontend/editor-ui && pnpm test   # vitest
```

### Running a single test
```bash
# Backend / nodes (jest)
cd packages/cli && pnpm jest src/services/__tests__/foo.service.test.ts
cd packages/cli && pnpm jest -t "returns 404 when missing"
cd packages/nodes-base && pnpm jest nodes/Switch

# Frontend (vitest)
cd packages/frontend/editor-ui && pnpm vitest run src/components/Foo.test.ts
cd packages/frontend/editor-ui && pnpm test:dev    # watch mode
```

### Alternative databases (backend)
`packages/cli` tests default to sqlite. Other backends need a running server:
```bash
pnpm test:postgres    # DB_TYPE=postgresdb, alt_schema, test_ prefix
pnpm test:mysql
pnpm test:mariadb
```

### E2E
```bash
pnpm cypress:install        # once, from cypress/ — required before first run
pnpm dev:e2e                # interactive, dev mode (reacts to code changes)
cd cypress && pnpm test:e2e:ui     # interactive against built UI
cd cypress && pnpm test:e2e:all    # headless, full suite
```

## Code style

Formatting is tool-enforced; don't hand-format.

- **Indentation: tabs**, width 2. **Single quotes**. **Semicolons**. Trailing commas
  everywhere. Line width **100**. LF endings. (`.editorconfig`, `biome.jsonc`, `.prettierrc.js`)
- **Biome** formats `.js`, `.ts`, `.json`. **Prettier** formats `.vue`, `.yml`, `.md`,
  `.css`, `.scss`. Biome's linter is disabled — linting is ESLint's job.
- **Lefthook** runs both on staged files at pre-commit (`lefthook.yml`) and re-stages
  fixes, so a commit normally formats itself.
- ESLint configs live in `packages/@n8n/eslint-config` (`base`, `node`, `frontend`) plus
  custom rules in `local-rules.js` — e.g. no uncaught `JSON.parse`, no
  `JSON.parse(JSON.stringify(...))`, no unneeded backticks.

## Architecture notes

### Dependency injection (backend)
`packages/cli` and `packages/core` use `@n8n/di` (an in-house fork of `typedi`, ~283
import sites in `packages/cli/src` alone). Services are classes decorated with `@Service()`
and dependencies arrive through the constructor:

```ts
import { Service } from '@n8n/di';

@Service()
export class MyService {
	constructor(private readonly userRepository: UserRepository) {}
}
```

This requires `experimentalDecorators` + `emitDecoratorMetadata`, already set in the
backend tsconfigs. In tests, resolve via the container rather than constructing by hand
where the surrounding tests do so.

### REST controllers
Routes are declarative decorators from `@/decorators` — `@RestController('/path')` on the
class, `@Get` / `@Post` / `@Put` / `@Patch` / `@Delete` on methods, with `@Body`, `@Param`, `@Query`
for binding, and `@Licensed` / `@GlobalScope` for gating. Request/response DTOs come from
`@n8n/api-types`. See `packages/cli/src/controllers/me.controller.ts` for the canonical shape.

### Database layer
Under `packages/cli/src/databases/`: `entities/` (TypeORM entities), `repositories/`
(injectable repositories — controllers/services depend on these, never on raw
connections), `migrations/{common,sqlite,postgresdb,mysqldb}/`, `subscribers/`, `dsl/`.
**A schema change needs a migration in every DB dialect directory**, named
`<timestamp>-DescriptiveName.ts` (exporting a class named
`DescriptiveName<timestamp>`) and registered in that directory's `index.ts`.

### Nodes
A node lives in `packages/nodes-base/nodes/<Name>/` and typically contains:
- `<Name>.node.ts` — the implementation (`description` + `execute`)
- `<Name>.node.json` — codex metadata (categories, docs links)
- `<name>.svg` — icon
- `test/` — unit and/or declarative workflow tests
- `V1/`, `V2/`, … — **versioned** nodes keep old behavior intact; add a new version
  directory rather than changing an existing one when behavior would break users
- `__schema__/` — response schemas, where present

Credentials live in `packages/nodes-base/credentials/`. `pnpm lint` in that package also
runs `scripts/validate-load-options-methods.js`.

### Path aliases
Backend packages map `@/*` to `src/*`, `@test/*` to `test/shared/*`, and
`@test-integration/*` to `test/integration/shared/*`. Jest resolves these from the
tsconfig automatically (`jest.config.js` at the root).

### Enterprise-licensed code
Files with `.ee.` in the filename or directories ending in `.ee` (e.g.
`packages/cli/src/sso.ee/`, `ldap.ee/`, `external-secrets.ee/`, `permissions.ee/`) are
**not** covered by the Sustainable Use License — they fall under `LICENSE_EE.md`. Keep
enterprise-only features inside those paths and don't move `.ee` code into
generally-licensed files.

## Testing conventions

- **Backend and nodes: Jest** (`ts-jest`). Test files match `\.(test|spec)\.(js|ts)$`,
  usually in a sibling `__tests__/` directory or a node's `test/` directory.
  `jest-mock-extended` and `nock` are the standard mocking/HTTP-stubbing tools.
- **Frontend: Vitest** (`vitest.workspace.ts` covers `packages/frontend`) with
  `@testing-library/vue`.
- **E2E: Cypress** in `cypress/` — page objects in `pages/`, specs in `e2e/`.
- Node behavior is often tested declaratively with workflow JSON fixtures; see
  `packages/nodes-base/nodes/Switch/V3/test` for the pattern to copy.
- Tests are not optional here: per `CONTRIBUTING.md`, community PRs without tests are
  auto-closed after 14 days. A bug fix needs a regression test; a feature needs coverage.

## Git and PR conventions

**PR titles are validated in CI** (`.github/workflows/check-pr-title.yml`) and feed the
changelog. Format follows the Angular convention:

```
<type>(<scope>): <Summary>
```

- **type**: `feat` | `fix` | `perf` | `test` | `docs` | `refactor` | `build` | `ci` | `chore`
  (only `feat`, `fix`, `perf` and breaking changes appear in the changelog)
- **scope** (optional, only if it fits exactly): `API` | `benchmark` | `core` | `editor` |
  `* Node` (e.g. `Mattermost Node`, `Microsoft To Do Node`)
- **summary**: imperative present tense, capitalized, no trailing period, no ticket IDs
- Suffix with `(no-changelog)` to keep it out of release notes
- Breaking changes go in the footer as `BREAKING CHANGE: <summary>`

Examples from recent history:
```
feat(editor): Add variables and context section to schema view (#13875)
fix(core): Do not use `url.includes` to check for domain names (#13802)
refactor(core): Add strong typing for `INodeTypeBaseDescription['group']` (no-changelog)
```

Full rules: `.github/pull_request_title_conventions.md`. PR body should follow
`.github/pull_request_template.md` (summary, linked ticket/issue, review checklist).

## Gotchas

- Use `pnpm`, never `npm` or `yarn` — the preinstall hook will reject it.
- `packages/core` handles workflow execution; the contributing guide asks you to contact
  n8n before making changes there.
- `packages/cli` compiles with `strict: false` — don't assume strict-null semantics when
  reading that code, and match the surrounding style rather than tightening types ad hoc.
- Building the editor UI needs headroom; its build already sets
  `NODE_OPTIONS=--max-old-space-size=8192`.
- `CHANGELOG.md` is generated (and ~830KB) — never edit it by hand. It's excluded from
  Biome formatting.
- Adding a shared dependency? Put the version in the `pnpm-workspace.yaml` catalog and
  reference it as `catalog:` from the package.
- Only the `master` branch is licensed; content of other branches is not (see `LICENSE.md`).
