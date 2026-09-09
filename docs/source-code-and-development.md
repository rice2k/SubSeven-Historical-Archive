# SubSeven Source Code, Programming Language and Development History

This page separates **classic SubSeven source provenance**, later mirrors/forks, reverse-engineering/preservation material and the modern **SubSeven Legacy** recreation. They are not all the same codebase.

## Quick source-provenance table

| Source / repository | What it represents | Archive classification |
|---|---|---|
| [`illwill/sub7` on GitLab](https://gitlab.com/illwill/sub7) | Publicly released classic Sub7 source-provenance tree associated with the 2.1.2/2.1.3 era | historical classic source provenance; linked, not mirrored as a buildable malware tree |
| [`DarkCoderSc/SubSeven`](https://github.com/DarkCoderSc/SubSeven) | Official modern **SubSeven Legacy** recreation | modern non-malicious source; official Legacy project |
| [`NoorahSmith/DarkCoderSc-SubSeven`](https://github.com/NoorahSmith/DarkCoderSc-SubSeven) | Later GitHub preservation/fork record | mirror/fork; not original classic authorship evidence |
| [`pawpatrolryder/SubSeven-delphi-rat-`](https://github.com/pawpatrolryder/SubSeven-delphi-rat-) | Later GitHub preservation/derivative record | mirror/derivative; content must be evaluated separately |
| [`xillwillx` GitHub profile](https://github.com/xillwillx) | Public account associated with illwill’s broader preservation/security work | researcher/source-provenance lead, not itself a Sub7 source tree |

> **Safety / preservation rule:** this archive documents and links source provenance but does not republish the classic source tree as a turnkey buildable malware package.

---

# Programming language

Classic SubSeven is historically associated with **Borland Delphi / Object Pascal** and the Windows VCL ecosystem.

This is consistent with:

- the form-driven Windows GUI visible in the classic controller/editor applications;
- historical `.pas`, `.dpr`, `.dfm`-style project evidence associated with Delphi applications;
- the later source-provenance material;
- the modern Legacy recreation, which intentionally continues the Delphi lineage.

The archive does **not** assume that every 1999–2003 release used exactly the same Delphi IDE/compiler version unless a specific project file, README or contemporary statement proves it.

## Common Delphi artifact types

| Extension | Historical development role |
|---|---|
| `.pas` | Object Pascal unit/source file |
| `.dpr` | Delphi project program/source |
| `.dfm` | Delphi form/resource definition; valuable for reconstructing UI layout |
| `.res` | compiled Windows/Delphi resources |
| `.dcu` | compiled Delphi unit; binary build artifact |
| `.dpk` | Delphi package project in some component ecosystems |
| `.bpl` | Delphi runtime/design package output in some component ecosystems |
| `.dproj` | newer Delphi project metadata used in modern Delphi generations |
| `.iss` | Inno Setup definition used by the modern Legacy installer projects |

`.dfm` files are especially useful to historians because they can reveal form names, controls, menus, captions and layout relationships without running a historical executable.

---

# Classic application architecture

Later well-documented classic releases revolve around three main application roles:

## Controller / client

The operator-facing Windows GUI that exposed connection information and remote feature modules.

Known later executable names include:

- `sub7.exe` — 2.2 material;
- `SubSeven.exe` — Legends-era material.

## Server

The remote component in the classic client/server architecture.

Known later filename:

- `server.exe`.

## EditServer / builder/editor

The server configuration/editor application used by later packages.

Known name:

- `EditServer.exe` / `editserver.exe`.

Additional later components include `sin.exe`, ICQ support material such as `ICQMAPI.dll`, and 2.2’s plugin-extension design.

---

# Historical classic source-code provenance: `illwill/sub7`

Public research link:

- **https://gitlab.com/illwill/sub7**

A locally preserved screenshot of the repository identifies it as **“Source code for SubSeven 2.1.3.”** The visible repository tree includes areas named:

- `Keylogger`
- `[BINS]`
- `client`
- `editserver.new`
- `server`
- `Compile_Test.gif`
- `README.md`
- `rxlib275.zip`

The visible README text in that capture describes the material as **Sub7 2.1.2 source received directly from mobman**, and says it was released publicly to coincide with the **BSidesCT event on 30 September 2023**. It also discusses missing Delphi 4-era components and historical compilation work in a Windows 98/Delphi 4 environment.

That apparent 2.1.2-vs-2.1.3 naming discrepancy is historically important and is preserved here rather than “corrected” into one simplified claim.

## Independent conference corroboration

The official **BSidesCT 2023** schedule lists illwill’s talk **“Finding mobman”** on 30 September 2023 and describes the presentation as covering the history of SubSeven, the search for mobman and the acquisition of **Sub7 2.1.3’s source code**.

- [BSidesCT 2023 archive — Finding mobman](https://www.bsidesct.org/archives/2023/)

This independently supports the public-release/source-acquisition event, even though detailed branch labeling in the repository itself still deserves careful source-level study.

## Preserved screenshot

The archive includes a locally found capture of the source repository under `assets/images/source-code/` so future researchers can see how the public source-provenance page was presented at the time of preservation.

## What this source can help historians answer

Without turning it into a build guide, source/form analysis can help reconstruct:

- form/window names;
- menu organization;
- relationships between controller, server and EditServer projects;
- UI resources and images;
- Delphi unit names;
- feature-module boundaries;
- library/component dependencies;
- protocol/message naming at a descriptive level;
- differences between the public source tree and surviving binary release screenshots;
- whether later mirrors contain identical or modified trees.

---

# Modern SubSeven Legacy source

Official repository:

- **https://github.com/DarkCoderSc/SubSeven**

The official README states that SubSeven Legacy is written in **Delphi** like the original project but **does not include malicious features**.

Its documented goals/features include:

- a SubSeven **2.2.x-inspired VCL/WinAPI UX**;
- direct socket communication with modern OpenSSL support;
- multithreading/concurrency;
- File Manager;
- Process Manager;
- Remote Terminal;
- Windows Session Manager.

## Modern Legacy project structure

The repository/setup material exposes distinct project areas corresponding to:

- Viewer/controller;
- Windows Service;
- Server Tray / service-controller UI;
- Helper application;
- certificate generator;
- Secure Desktop component;
- shared/common source;
- resources;
- setup/install definitions.

## Known modern build outputs / dependencies

Viewer-side setup material references:

- `Sub7Viewer.exe`
- `CertGenerator.exe`
- `bass.dll`
- OpenSSL `libcrypto` / `libssl` DLLs

Server-side setup material references:

- `Sub7Service.exe`
- `Sub7Helper.exe`
- `Sub7ServerTray.exe`
- `CertGenerator.exe`
- `SecureDesktop.dll`
- `bass.dll`
- OpenSSL `libcrypto` / `libssl` DLLs

These names belong to the **modern Legacy project**. They must not be projected backward as evidence that those filenames existed in original 1999 releases.

See [`../data/manifests/legacy-0-1-alpha-files.csv`](../data/manifests/legacy-0-1-alpha-files.csv).

---

# Mirrors and forks

A repository being named “SubSeven” does not automatically make it original source. Each candidate is classified by:

- upstream repository relationship;
- commit/import history;
- README provenance claims;
- file-tree similarity;
- embedded project/version strings;
- Delphi project metadata;
- whether it is classic source, a Legacy fork, a reupload or a derivative.

## `NoorahSmith/DarkCoderSc-SubSeven`

- https://github.com/NoorahSmith/DarkCoderSc-SubSeven

Treat as a later mirror/fork record unless its commit history establishes something more specific.

## `pawpatrolryder/SubSeven-delphi-rat-`

- https://github.com/pawpatrolryder/SubSeven-delphi-rat-

Treat as a later preservation/derivative record and inspect content/provenance before assigning it to a classic branch.

## `rutherfordwj/SubSevenLegacy`

- https://github.com/rutherfordwj/SubSevenLegacy

A later Legacy-related fork/archive that may be useful for comparing modern project history, dependencies and README changes.

---

# Source-code timeline

| Period | Source/development significance |
|---|---|
| 1999 | Original Delphi SubSeven development begins; rapid 1.x releases. |
| 1999–2000 | 2.0/2.1.x generation expands controller and feature architecture. |
| 2001 | 2.2 redesign introduces stronger modular/plugin direction. |
| 2003 | 2.1.5 Legends becomes the late original-era release. |
| 2010 | Later 2.3 continuation/revival appears in historical summaries. |
| 2021+ | DarkCoderSc/Sub7Crew develops modern non-malicious SubSeven Legacy in Delphi. |
| 30 Sep 2023 | BSidesCT “Finding mobman” presentation documents acquisition of classic source; `illwill/sub7` becomes a public source-provenance reference. |

---

# What is and is not mirrored here

## Mirrored/preserved directly

- screenshots of source-repository pages;
- safe project metadata/inventories;
- modern Legacy repository links and non-malicious project documentation;
- source-provenance timelines;
- filenames/project names;
- research notes about forms, dependencies and version relationships.

## Linked/documented but not republished as buildable classic malware

- the classic `illwill/sub7` source tree;
- classic server/client payload source where it would turn this archive into a malware build/distribution package;
- operational deployment/evasion/persistence instructions.

This preserves the historical source record while keeping the repository focused on education, digital preservation and defensive research.

---

# Research checklist for future source comparison

For each source/mirror candidate, record:

1. claimed SubSeven version;
2. repository/import date;
3. upstream/fork relationship;
4. Delphi compiler/project clues;
5. top-level project folders;
6. `.dpr` project names;
7. `.dfm` form names;
8. notable component/library dependencies;
9. version strings in forms/resources;
10. whether the tree contains controller, server and EditServer projects;
11. differences from `illwill/sub7` or official Legacy;
12. screenshot/UI correspondence with known releases;
13. provenance confidence.

The canonical cross-version file inventory remains [`../data/file-inventory.csv`](../data/file-inventory.csv), while locally preserved historical package/source records are in [`../data/historical-file-inventory.csv`](../data/historical-file-inventory.csv).
