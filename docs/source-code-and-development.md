# Source Code and Development History

This page separates the original SubSeven development lineage from later source-code claims, mirrors, forks, and the modern SubSeven Legacy recreation.

## Classic implementation language

SubSeven is historically associated with **Borland Delphi / Object Pascal** and the Windows VCL application ecosystem. This is consistent with the form-driven Windows interface style seen in the classic controller/builder applications and with later source-related preservation material.

The archive does not assume a single compiler version across the entire 1999–2003 lifespan unless a surviving project file or contemporaneous document establishes it for a specific branch.

## Classic application model

Later classic releases are documented around three major application roles:

- **Controller/client** — operator-facing Windows GUI used to interact with a connected server.
- **Server component** — the remote component installed/run on the target Windows system.
- **EditServer/builder** — application used to configure a server build.

Additional later components include utilities such as `sin.exe`, ICQ-related support such as `ICQMAPI.dll`, and plugin-extension concepts.

This archive describes those roles historically without publishing deployment, persistence, credential-theft or evasion procedures.

## Why source provenance is complicated

Several different things are commonly described online as "SubSeven source":

1. original/classic source material or claimed leaks;
2. later mirrors/reuploads of claimed classic source;
3. modern forks of those mirrors;
4. complete rewrites or recreations inspired by SubSeven;
5. analysis/decompilation projects that are not original source.

The archive therefore labels source links by **provenance claim**, not simply as "the source code."

## Historical source-code record

A GitLab repository maintained under `illwill/sub7` has been circulated as a historical Sub7 2.1.2/2.1.3-era source-code record. It is useful for provenance research, but its relationship to the original development environment should be verified from project files, commit/import history, embedded strings, contemporaneous releases and independent historical testimony.

Research link:

- https://gitlab.com/illwill/sub7

The public Rice2k archive does not mirror that classic buildable source tree.

## GitHub mirrors / related repositories

Repositories supplied or located during research include:

- https://github.com/NoorahSmith/DarkCoderSc-SubSeven
- https://github.com/pawpatrolryder/SubSeven-delphi-rat-
- https://github.com/xillwillx

These should be treated according to what they actually contain: mirror, fork, preservation copy, derivative or unrelated collection. Repository names alone are not proof of original authorship.

## Modern SubSeven Legacy

The modern DarkCoderSc project is intentionally separated from the classic malware lineage:

- https://github.com/DarkCoderSc/SubSeven

Its repository identifies Jean-Pierre LESUEUR / `DarkCoderSc` and Sub7Crew branding in setup/project material. It is a modern Delphi recreation and its project documentation describes a non-malicious design rather than an attempt to redistribute the original operational RAT.

### Auditable Legacy project structure

The modern repository contains distinct application/project areas corresponding to:

- Viewer
- Service
- Tray / service controller
- Helper
- Certificate generator
- Secure Desktop component
- shared/common libraries
- setup/install definitions

### Setup manifests

The Inno Setup definitions identify build outputs and dependencies for both x86 and x64 variants.

Viewer-side setup references include:

- `Sub7Viewer.exe`
- `CertGenerator.exe`
- `bass.dll`
- OpenSSL `libcrypto` / `libssl` DLLs

Server-side setup references include:

- `Sub7Service.exe`
- `Sub7Helper.exe`
- `Sub7ServerTray.exe`
- `CertGenerator.exe`
- `SecureDesktop.dll`
- `bass.dll`
- OpenSSL `libcrypto` / `libssl` DLLs

These are **modern Legacy build outputs/dependencies**, not evidence that the same filenames existed in classic 1999 releases.

## Dependency distinction

The Legacy repository contains binary dependencies such as x86/x64 BASS and OpenSSL libraries. They are ordinary modern dependencies and are classified separately from classic SubSeven payloads.

The archive records architecture, path, size and repository provenance where verified.

## Delphi project/source artifacts

For historical development research, relevant source/project artifact types include:

- `.pas` — Object Pascal units
- `.dpr` — Delphi project source
- `.dfm` — Delphi form definitions/resources
- `.dproj` — newer Delphi project metadata
- `.res` — Windows/Delphi resources
- `.iss` — Inno Setup installer definitions in the modern Legacy project

The presence of those formats can help reconstruct UI layout, modules, forms and build relationships without requiring malware execution.

## Safe historical analysis approach

Useful development-history questions that can be answered without operating the classic malware include:

- What forms/windows existed in a particular release?
- Which menu categories changed between releases?
- Which files were shipped together?
- Which DLLs were first documented in a branch?
- Which Delphi units/forms corresponded to visible interface features?
- What compiler/project metadata survives?
- How did installer/package naming change?
- Which website or README first mentioned a feature/plugin?
- Which later mirrors contain identical source trees versus modified forks?

## Research rule

Do not merge classic and Legacy evidence into one undifferentiated file list. Every source/component record should carry at least:

- branch/version
- filename/path
- artifact type
- source/repository
- provenance confidence
- whether it is classic, later continuation, mirror, or Legacy

The canonical cross-version inventory is maintained in [`../data/file-inventory.csv`](../data/file-inventory.csv).
