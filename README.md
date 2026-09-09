# SubSeven / Sub7 Historical Archive

> **Educational / historical cybersecurity archive.** This repository documents SubSeven (Sub7), its releases, interfaces, websites, developers, file structure, related utilities, historical abuse, and defensive research. Classic malware binaries and weaponized packages are **not redistributed here**; those artifacts are preserved as metadata records (name, version, size, source/provenance, archive references, hashes when verified, and historical links).

![Classic SubSeven interface](assets/images/classic-subseven-interface.jpg)

## Archive purpose

SubSeven was one of the best-known Windows remote-access trojans of the late 1990s and early 2000s. This project reconstructs the historical record around it: what versions existed, what the operator and server-side applications looked like, how the project websites changed, which files/DLLs were associated with releases, how add-ons and plugins were described, what contemporary documentation said, and how defenders and users encountered it.

The repository intentionally separates four different things that are often mixed together online:

1. **Original SubSeven releases (1999–2003)** — historical malware family and its official/community distribution ecosystem.
2. **Later continuations and preservation packages** — including the reported 2.3-era continuation and archival mirrors.
3. **Released/leaked source-code records** — documented for provenance without republishing weaponized original malware code.
4. **SubSeven Legacy** — the modern Delphi recreation by DarkCoderSc/Sub7Crew that explicitly removed malicious functionality.

## What this archive contains

- Full release chronology from 1.0 through 2.1.5 Legends, later 2.3 continuation, and the modern non-malicious SubSeven Legacy remake.
- Version-by-version file and DLL records, including `SubSeven.exe`, `sub7.exe`, `server.exe`, `EditServer.exe`, `sin.exe`, `ICQMAPI.dll`, plugin DLL architecture, and modern Legacy project/dependency files.
- Historical package metadata recovered from Google Drive for 1.0, 1.9 Apocalypse, 2.0, 2.1.0–2.1.4, 2.2, Legends, 2.3, tutorials, compatibility material, checksum references, and ancillary tools.
- Original website/domain history for `come.to/subseven`, `subseven.slak.org`, `sub7.net`, `sub-7.net`, `sub7crew.org`, `s7help.sub7crew.org`, `sub7files.com`, and `sub7legends.net`.
- Raw historical URL crawls recovered from Google Drive for `sub7crew.org` and `sub7.net`, plus curated Wayback lookup tables.
- Historical site paths for downloads, help/reference pages, mailing lists, IRC, gallery files, member pages, forum endpoints, CSS, GIF/JPG assets, and old package filenames.
- Screenshots and artwork from the historical collection.
- A searchable visual website in [`index.html`](index.html).
- CSV/JSON research datasets so the history can be audited and extended.

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

## Applications and package model

Classic SubSeven releases commonly revolved around an **operator-side client/controller**, a **server/payload component**, and configuration/builder tooling such as **EditServer**. Contemporary and later records also refer to auxiliary utilities such as **SIN**, ICQ-related components, plugins, and release-specific add-ons. The exact filename set changed between branches, so this archive keeps filenames tied to the version/evidence that supports them rather than presenting one blended list.

See [`data/file-inventory.csv`](data/file-inventory.csv) and the per-release manifests under [`data/manifests/`](data/manifests/).

## Programming language and implementation

Classic SubSeven is associated with **Borland Delphi / Object Pascal** and the Windows VCL GUI ecosystem. The modern SubSeven Legacy recreation is also Delphi-based. The Legacy repository exposes a much more auditable project structure, including separate viewer, service, tray, helper, certificate-generation, secure-desktop and setup projects, plus x86/x64 BASS and OpenSSL dependencies. These modern files are documented separately so they are not mistaken for original 1999–2003 binaries.

## Google Drive preservation findings

The connected Drive archive contains multiple historical Sub7 collections. One collection preserves encrypted or packaged releases for **1.0, 1.9 Apocalypse, 2.0, 2.1.0, 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.2, Legends, and 2.3**. It also contains `SubSeven And Windows XP.rar`, `Sub7.net Default md5sum values.rar`, `Tutorial_Sub7.rar`, `Tutorial_Sub7_2.rar`, `sub7-main.rar`, `sub7_1_9.zip`, `subseven20.zip`, `subpass.zip`, and `subuster.zip`, among other duplicates/alternate package names.

Those packages are **cataloged, not mirrored as runnable malware**. See [`data/drive-historical-packages.csv`](data/drive-historical-packages.csv) and [`docs/google-drive-findings.md`](docs/google-drive-findings.md).

A second Drive collection preserves historical URL crawls. The `sub7crew.org` list contains old project/community paths such as:

- `downloads.html` / `downloads/`
- `reference.shtml`
- `help.shtml`
- `irc.shtml`
- `subseven.shtml`
- SubSeven Official Mailing List archive endpoints
- old UBB/forum paths
- gallery JPGs and interface GIFs
- member pages for `~azzazzin`, `~fc`, `~mistahq`, and others
- historical package URL records such as `s7.2.2.0.zip` and `sub7legends.zip`

The raw crawl data is preserved under [`data/raw/`](data/raw/) and the most useful records are normalized in [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv).

## Major historical websites

| Domain / URL | Historical role | Wayback |
|---|---|---|
| `come.to/subseven` | Early redirect / vanity URL associated with the project | [captures](https://web.archive.org/web/*/http://come.to/subseven) |
| `subseven.slak.org` | Early hosting cited in period references | [captures](https://web.archive.org/web/*/http://subseven.slak.org/) |
| `sub7.net` | Major project/community domain; Drive crawl preserves historical paths | [captures](https://web.archive.org/web/*/http://sub7.net/) |
| `sub-7.net` | Alternate/related historical domain | [captures](https://web.archive.org/web/*/http://sub-7.net/) |
| `sub7crew.org` | Crew/community hub with downloads, help, mailing lists, gallery, IRC and member pages | [captures](https://web.archive.org/web/*/http://sub7crew.org/) |
| `s7help.sub7crew.org` | Help/documentation subdomain recovered from Drive URL crawl | [captures](https://web.archive.org/web/*/http://s7help.sub7crew.org/) |
| `sub7files.com` | Release/documentation distribution site referenced by period README material | [captures](https://web.archive.org/web/*/http://sub7files.com/) |
| `sub7legends.net` | Later community revival associated with Legends-era preservation | [captures](https://web.archive.org/web/*/http://sub7legends.net/) |

## Images

### Classic controller

![Classic SubSeven controller](assets/images/classic-subseven-interface.jpg)

### SubSeven art / icon sheet

![SubSeven art gallery](assets/images/subseven-art-gallery.png)

## Repository map

- [`index.html`](index.html) — visual historical site
- [`data/releases.csv`](data/releases.csv) — canonical release chronology
- [`data/file-inventory.csv`](data/file-inventory.csv) — EXE/DLL/source/project inventory
- [`data/resource-links.csv`](data/resource-links.csv) — version-specific research links
- [`data/drive-historical-packages.csv`](data/drive-historical-packages.csv) — Drive evidence for historical archives
- [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv) — curated old URL/Wayback map
- [`data/website-history.csv`](data/website-history.csv) — domain evolution
- [`data/manifests/`](data/manifests/) — release-specific file manifests
- [`data/raw/`](data/raw/) — raw historical URL crawl preservation
- [`docs/google-drive-findings.md`](docs/google-drive-findings.md) — Drive audit notes
- [`docs/research-gaps.md`](docs/research-gaps.md) — unresolved research targets
- [`docs/safety-and-scope.md`](docs/safety-and-scope.md) — archival/safety policy

## Core references

- [Wikipedia — Sub7](https://en.wikipedia.org/wiki/Sub7)
- [Malware Museum — SubSeven release index](https://www.malware.museum/releases/subseven/)
- [DarkCoderSc — SubSeven Legacy](https://github.com/DarkCoderSc/SubSeven)
- [GitLab — historical Sub7 source-code record](https://gitlab.com/illwill/sub7)
- [Darknet Diaries EP 150 — mobman 2](https://darknetdiaries.com/episode/150/)
- [Wayback — sub7crew.org](https://web.archive.org/web/*/http://sub7crew.org/)
- [Wayback — sub7.net](https://web.archive.org/web/*/http://sub7.net/)
- [Wayback — sub7files.com](https://web.archive.org/web/*/http://sub7files.com/)
- [Wayback — sub7legends.net](https://web.archive.org/web/*/http://sub7legends.net/)

## Safety / archival scope

This repository is designed for historical study, malware-history research, digital preservation, and defensive cybersecurity education. It does not provide deployment instructions, credential theft procedures, persistence/evasion recipes, or runnable classic SubSeven payloads. Where an original malware package exists in the private Drive archive, the public repository records the artifact rather than redistributing it.
