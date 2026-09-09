# SubSeven / Sub7 Historical Archive

> **Educational / historical cybersecurity archive.** This repository documents SubSeven (Sub7), its releases, interfaces, websites, developers, file structure, related utilities, historical abuse, source-code provenance, and defensive research. Classic malware binaries and weaponized packages are **not redistributed here**; those artifacts are preserved as metadata records with version, filename, size, Drive provenance, archive references, hashes when independently verified, and historical context.

![Classic SubSeven interface](assets/images/classic-subseven-interface.jpg)

## Archive purpose

SubSeven was one of the best-known Windows remote-access trojans of the late 1990s and early 2000s. This project reconstructs the historical record around it: what versions existed, what the operator and server-side applications looked like, how the project websites changed, which EXE/DLL/project files were associated with releases, how add-ons/plugins were described, what contemporary documentation said, and how users and defenders encountered it during the AOL/ICQ/IRC/dial-up era.

The archive keeps four frequently confused histories separate:

1. **Original SubSeven releases (1999–2003)** — the classic malware family and its distribution/community ecosystem.
2. **Later continuations and preservation packages** — including the reported 2.3-era continuation and archival mirrors.
3. **Historical source-code records** — documented for provenance without republishing weaponized original malware code.
4. **SubSeven Legacy** — the modern Delphi recreation by DarkCoderSc/Sub7Crew whose project documentation describes the removal/omission of malicious functionality.

## Start here

- **[Open the full visual history site](index.html)**
- **[Release chronology](data/releases.csv)**
- **[EXE / DLL / source inventory](data/file-inventory.csv)**
- **[Google Drive master inventory](data/google-drive-master-inventory.csv)**
- **[Historical Drive package records](data/drive-historical-packages.csv)**
- **[Old website / Wayback path catalog](data/curated-historical-urls.csv)**
- **[Research/source ledger](data/resource-links.csv)**
- **[Google Drive findings](docs/google-drive-findings.md)**

## What this archive contains

- Full working chronology from 1.0 through 2.1.5 Legends, the later reported 2.3 continuation, and modern SubSeven Legacy.
- Version-specific file/DLL records including `SubSeven.exe`, `sub7.exe`, `server.exe`, `EditServer.exe`, `sin.exe`, `ICQMAPI.dll`, classic plugin-DLL architecture, and modern Legacy project/dependency files.
- Historical package metadata recovered from Google Drive for 1.0, 1.9 Apocalypse, 2.0, 2.1.0–2.1.4, 2.2, Legends, 2.3, tutorials, compatibility/checksum material, and ancillary Sub7 archives.
- Historical site/domain reconstruction for `come.to/subseven`, `subseven.slak.org`, `sub7.net`, `sub-7.net`, `sub7crew.org`, `s7help.sub7crew.org`, `sub7files.com`, and `sub7legends.net`.
- Curated Wayback lookup paths derived from large private Google Drive URL crawls for `sub7crew.org` and `sub7.net`.
- Old paths for help/reference pages, mailing-list archives, IRC, forums, galleries, member pages, CSS/GIF/JPG assets, and historical package-name records.
- Drive-recovered classic controller imagery, SubSeven artwork/icons, and a Wayback reference screenshot.
- A preserved **2025 fan/history HTML page** from Drive, explicitly labeled so it cannot be confused with an original 1999–2003 site.
- CSV research datasets and separate per-version file manifests.

## Release chronology

| Version | Date | Branch | Codename / Edition |
|---|---|---|---|
| 1.0 | February 1999 | Original 1.x | — |
| 1.1 | March 1999 | Original 1.x | — |
| 1.2 | March 1999 | Original 1.x | — |
| 1.3 | March 1999 | Original 1.x | — |
| 1.4 | March 1999 | Original 1.x | — |
| 1.5 | April 1999 | Original 1.x | — |
| 1.6 | April 1999 | Original 1.x | — |
| 1.7 | May 1999 | Original 1.x | — |
| 1.8 | May 1999 | Original 1.x | — |
| 1.9 | June 1999 | Original 1.x | — |
| 1.9 Apocalypse | August 1999 | Original 1.x | Apocalypse |
| 2.0 | September 1999 | Original 2.x | — |
| 2.1 | November 1999 | Original 2.1.x | — |
| 2.1.1 GOLD | February 2000 | Original 2.1.x | GOLD |
| 2.1.2 M.U.I.E | April 2000 | Original 2.1.x | M.U.I.E |
| 2.1.3 BONUS | June 2000 | Original 2.1.x | BONUS |
| 2.1.4 DEFCON 8 | July 2000 | Original 2.1.x | DEFCON 8 |
| 2.2 | March 2001 | Original 2.2.x | — |
| 2.1.5 Legends | February 2003 | Original 2.1.x | Legends |
| 2.3 | March 2010 (reported) | Community continuation | — |
| Legacy 0.1 Alpha | 2021–2023 project activity | Non-malicious remake | Legacy |

The detailed release table records confidence, summaries, inventory status, and unresolved questions in [`data/releases.csv`](data/releases.csv).

## Application/package architecture

Classic SubSeven packages commonly revolved around three core roles:

- **Controller / client** — operator-facing Windows GUI. Later verified names include `sub7.exe` (2.2) and `SubSeven.exe` (Legends-era material).
- **Server component** — remotely installed component commonly named `server.exe` in documented later packages.
- **EditServer** — `EditServer.exe`, a server configuration/builder-side application documented across multiple later branches.

Additional historically documented components include:

- **`sin.exe`** — identified in 2.2 records as a Static IP Notifier utility.
- **Plugin DLL architecture** — surviving 2.2 documentation describes optional plugin-style extensions; exact original distributed DLL names remain a research gap.
- **`ICQMAPI.dll`** — named by surviving Legends-era package documentation as ICQ support/integration material.

The archive documents these applications without providing a procedure for deploying the classic server/payload.

## Programming language / implementation history

Classic SubSeven is associated with **Borland Delphi / Object Pascal** and the Windows VCL GUI ecosystem. A later repository claims historical 2.1.3 source provenance; it is linked for research but is not mirrored here as buildable weaponized malware source.

Modern **SubSeven Legacy** is separately auditable and Delphi-based. Its repository exposes distinct Viewer, Service, Tray, Helper, certificate-generation, Secure Desktop and setup projects. Its installer manifests identify x86/x64 BASS and OpenSSL dependencies. That modern structure is documented in the Legacy manifest rather than being projected backward onto 1999-era packages.

### Version-specific application/file manifests

- **[SubSeven 2.2 files](data/manifests/2-2-files.csv)** — `sub7.exe`, `EditServer.exe`, `server.exe`, `sin.exe`, plugin architecture record.
- **[SubSeven 2.1.5 Legends files](data/manifests/2-1-5-legends-files.csv)** — `SubSeven.exe`, `server.exe`, `EditServer.exe`, `ICQMAPI.dll`.
- **[SubSeven Legacy files/dependencies](data/manifests/legacy-0-1-alpha-files.csv)** — Viewer/Service/Tray/Helper projects, Secure Desktop DLL output, BASS/OpenSSL dependencies, Delphi project files and Inno Setup manifests.

Safe modern Legacy dependency/project download URLs are included in the detailed manifest where verified. Classic malware executables are marked `record-only` rather than being linked as live downloads.

## Google Drive preservation findings

The connected Drive archive contains several Sub7 preservation trees. The public master inventory currently records **47+ Sub7-specific folder/file records**, including duplicates, safe visual/web material and historical package records.

One collection preserves package records for **1.0, 1.9 Apocalypse, 2.0, 2.1.0, 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.2, Legends, and 2.3**. It also contains:

- `SubSeven And Windows XP.rar`
- `Sub7.net Default md5sum values.rar`
- `Tutorial_Sub7.rar`
- `Tutorial_Sub7_2.rar`
- `sub7-main.rar`
- `sub7_1_9.zip`
- `subseven20.zip`
- `subpass.zip`
- `subuster.zip`

Those files are cataloged in [`data/google-drive-master-inventory.csv`](data/google-drive-master-inventory.csv) and [`data/drive-historical-packages.csv`](data/drive-historical-packages.csv). Classic executable/archive payloads are not copied into this public repository.

### Raw URL-crawl sources

Drive also contains:

- `_sub7crew_org_all_urls.txt` — **548,749 bytes**
- `_sub7_net_all_urls.txt` — **65,336 bytes**
- smaller historical ZIP/RAR URL lists

The private raw crawls mix ordinary website/assets with historical malware package paths. Their exact Drive IDs/sizes are documented in [`data/raw/README.md`](data/raw/README.md) and the master inventory. The public archive publishes normalized safe historical paths in [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv) instead of becoming a live malware-download directory.

## Historical website reconstruction

The Drive crawl establishes a much richer `sub7crew.org` footprint than a simple homepage snapshot. Recovered historical paths include:

- `downloads.html`, `downloads/`
- `reference.shtml`
- `help.shtml`
- `irc.shtml`, `ircbots.html`
- `subseven.shtml`, `sub7list.shtml`
- the SubSeven Official Mailing List archive endpoint
- UBB / Sub7 forum endpoints
- gallery JPGs and old interface GIFs/CSS
- member areas under `~azzazzin`, `~fc`, `~mistahq`, `~qroject`, and others
- historical package-name/path records associated with 2.2, Legends and scene-era add-on tools

### Major domains

| Domain / URL | Historical role | Wayback |
|---|---|---|
| `come.to/subseven` | Early redirect / vanity URL | [captures](https://web.archive.org/web/*/http://come.to/subseven) |
| `subseven.slak.org` | Early hosting cited in period references | [captures](https://web.archive.org/web/*/http://subseven.slak.org/) |
| `sub7.net` | Major classic project/community domain | [captures](https://web.archive.org/web/*/http://sub7.net/) |
| `sub-7.net` | Alternate/related historical domain | [captures](https://web.archive.org/web/*/http://sub-7.net/) |
| `sub7crew.org` | Crew/community hub with downloads, help, mailing lists, gallery, IRC and member pages | [captures](https://web.archive.org/web/*/http://sub7crew.org/) |
| `s7help.sub7crew.org` | Help/documentation subdomain found in the Drive crawl | [captures](https://web.archive.org/web/*/http://s7help.sub7crew.org/) |
| `sub7files.com` | Release/documentation distribution site referenced by surviving material | [captures](https://web.archive.org/web/*/http://sub7files.com/) |
| `sub7legends.net` | Later community revival/preservation domain | [captures](https://web.archive.org/web/*/http://sub7legends.net/) |

## Images and visual preservation

### Classic controller

![Classic SubSeven controller](assets/images/classic-subseven-interface.jpg)

### SubSeven art / icon sheet

![SubSeven art gallery](assets/images/subseven-art-gallery.png)

### Drive-preserved Wayback reference

![Drive-preserved Wayback reference](assets/images/wayback-sub7-reference.jpg)

The visual site at [`index.html`](index.html) also references the official modern Legacy repository for an additional contemporary Legacy interface example.

## Preserved later fan/history artifact

[`archive/fan-pages/sub7-2025.html`](archive/fan-pages/sub7-2025.html) preserves the small `sub7.html` file found in Drive. A prominent provenance notice was added because the file is a **modern 2025 fan/history page**, not an original Mobman/Sub7 Crew webpage. Its historical statements should be corroborated before being treated as primary evidence.

## Repository map

- [`index.html`](index.html) — full visual historical site
- [`assets/images/`](assets/images/) — recovered screenshots/artwork
- [`data/releases.csv`](data/releases.csv) — canonical release chronology
- [`data/file-inventory.csv`](data/file-inventory.csv) — EXE/DLL/source/project inventory
- [`data/google-drive-master-inventory.csv`](data/google-drive-master-inventory.csv) — Drive IDs, sizes, duplicates and public-treatment classification
- [`data/resource-links.csv`](data/resource-links.csv) — research/source ledger
- [`data/drive-historical-packages.csv`](data/drive-historical-packages.csv) — Drive package evidence
- [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv) — old website / Wayback path map
- [`data/website-history.csv`](data/website-history.csv) — domain evolution
- [`data/manifests/`](data/manifests/) — version-specific file manifests
- [`data/raw/README.md`](data/raw/README.md) — provenance for private raw URL-crawl sources
- [`docs/google-drive-findings.md`](docs/google-drive-findings.md) — Drive audit notes
- [`docs/research-gaps.md`](docs/research-gaps.md) — unresolved targets
- [`docs/safety-and-scope.md`](docs/safety-and-scope.md) — archival scope
- [`archive/fan-pages/`](archive/fan-pages/) — later preservation/fan artifacts with provenance labels

## Core research references

- [Wikipedia — Sub7](https://en.wikipedia.org/wiki/Sub7)
- [Malware Museum — SubSeven release index](https://www.malware.museum/releases/subseven/)
- [DarkCoderSc — SubSeven Legacy](https://github.com/DarkCoderSc/SubSeven)
- [GitLab — historical Sub7 source-code record](https://gitlab.com/illwill/sub7)
- [Darknet Diaries EP 150 — mobman 2](https://darknetdiaries.com/episode/150/)
- [Wayback — sub7crew.org](https://web.archive.org/web/*/http://sub7crew.org/)
- [Wayback — sub7.net](https://web.archive.org/web/*/http://sub7.net/)
- [Wayback — sub7files.com](https://web.archive.org/web/*/http://sub7files.com/)
- [Wayback — sub7legends.net](https://web.archive.org/web/*/http://sub7legends.net/)

More leads and source classifications are in [`data/resource-links.csv`](data/resource-links.csv).

## Safety / archival scope

This repository is for historical study, malware-history research, digital preservation and defensive cybersecurity education. It does not provide deployment instructions, credential-theft procedures, persistence/evasion recipes, or runnable classic SubSeven payloads. Where a classic package exists in the private Drive archive, the public repository records the artifact and its provenance rather than redistributing it.
