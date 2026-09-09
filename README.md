# SubSeven / Sub7 Historical Archive

<p align="center">
  <a href="docs/image-gallery.md"><img src="assets/images/classic-subseven-interface.jpg" alt="Classic SubSeven controller interface" width="760"></a>
</p>

<p align="center">
  <a href="docs/archive-source-provenance.md"><img alt="Historical archive" src="https://img.shields.io/badge/type-historical%20archive-7c3aed"></a>
  <a href="docs/version-and-file-history.md"><img alt="Coverage" src="https://img.shields.io/badge/coverage-1999%E2%86%92present-2563eb"></a>
  <a href="docs/source-code-and-development.md"><img alt="Language" src="https://img.shields.io/badge/classic%20language-Delphi%20%2F%20Object%20Pascal-d97706"></a>
  <a href="docs/safety-and-scope.md"><img alt="Purpose" src="https://img.shields.io/badge/purpose-cybersecurity%20history-059669"></a>
  <a href="data/historical-file-inventory.csv"><img alt="Duplicates" src="https://img.shields.io/badge/duplicates-preserved%20%26%20labeled-475569"></a>
  <a href="docs/image-gallery.md"><img alt="Screenshots" src="https://img.shields.io/badge/screenshots-open%20gallery-0ea5e9"></a>
  <a href="docs/repository-file-status.md"><img alt="File status" src="https://img.shields.io/badge/files-hosted%20vs%20not%20hosted-334155"></a>
</p>

> **Educational / historical cybersecurity archive.** This repository reconstructs the history of **SubSeven / Sub7**, one of the best-known Windows remote-access trojans of the late 1990s and early 2000s: releases, features, interfaces, developers/community, applications, EXE/DLL records, source-code provenance, websites, Wayback captures, screenshots, old documentation, distribution history and defensive context.
>
> Safe historical research material is preserved directly. Classic runnable malware and buildable weaponized classic RAT source are documented through exact filenames, sizes, hashes/provenance, old distribution paths, screenshots, readmes, source references and technical history rather than being republished as executable payloads.

---

## Quick navigation

| Research area | Page / data |
|---|---|
| **What SubSeven was / how it worked** | [Overview below](#what-was-subseven) |
| **Every version and what changed** | [`docs/version-and-file-history.md`](docs/version-and-file-history.md) |
| **Version × feature comparison** | [`data/version-feature-matrix.csv`](data/version-feature-matrix.csv) |
| **Detailed feature encyclopedia** | [`docs/features-and-interface.md`](docs/features-and-interface.md) |
| **February 2001 Sub7Files About page** | [`docs/sub7files-about-2001.md`](docs/sub7files-about-2001.md) |
| **Old websites / Wayback history** | [`docs/websites-and-wayback-history.md`](docs/websites-and-wayback-history.md) |
| **Source code / Delphi / development** | [`docs/source-code-and-development.md`](docs/source-code-and-development.md) |
| **People and community** | [`docs/people-and-community.md`](docs/people-and-community.md) |
| **AOL / ICQ / IRC / social history** | [`docs/social-history.md`](docs/social-history.md) |
| **Historical files found locally** | [`docs/local-archive-findings.md`](docs/local-archive-findings.md) |
| **What is actually hosted vs not hosted** | [`docs/repository-file-status.md`](docs/repository-file-status.md) |
| **Image / screenshot gallery** | [`docs/image-gallery.md`](docs/image-gallery.md) |
| **Link and image audit** | [`docs/link-audit.md`](docs/link-audit.md) |
| **Preservation / research access** | [`docs/preservation-and-research-access.md`](docs/preservation-and-research-access.md) |
| **All historical records + duplicate relationships** | [`data/historical-file-inventory.csv`](data/historical-file-inventory.csv) |
| **Historical package records** | [`data/historical-package-records.csv`](data/historical-package-records.csv) |
| **Restricted artifact manifest** | [`data/restricted-artifacts-manifest.csv`](data/restricted-artifacts-manifest.csv) |
| **EXE / DLL / source / project inventory** | [`data/file-inventory.csv`](data/file-inventory.csv) |
| **Old URL / Wayback catalog** | [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv) |
| **Secondary discovery sources** | [`data/secondary-source-index.csv`](data/secondary-source-index.csv) |
| **Visual website** | [`index.html`](index.html) |
| **Evidence / provenance rules** | [`docs/archive-source-provenance.md`](docs/archive-source-provenance.md) |
| **Open research gaps** | [`docs/research-gaps.md`](docs/research-gaps.md) |

---

# What was SubSeven?

**SubSeven** — usually shortened to **Sub7** or **S7** — was a Windows **remote-access trojan / backdoor** family first released in 1999. It combined a graphical controller with a remote server component and, over time, accumulated a very large set of remote-management, surveillance, credential-related, networking and prank functions.

The classic family is historically associated with **Borland Delphi / Object Pascal** and the Windows VCL ecosystem.

SubSeven became especially visible during the era of Windows 95/98/ME, NT/2000, dial-up Internet, AOL/AIM, ICQ, IRC, email attachments, personal websites, file-sharing and early consumer webcams. Its cultural reputation came from the unusual mixture of serious remote-control/surveillance features and visible prank controls: the same controller that could display a message or open a CD tray also exposed file access, keylogging, password/account-data functions, screen/webcam monitoring and remote execution categories.

## High-level architecture

Classic SubSeven followed a **controller / server** model:

```text
┌──────────────────────────┐
│ Controller / Client      │
│ operator-facing GUI      │
└────────────┬─────────────┘
             │ remote connection
             ▼
┌──────────────────────────┐
│ Server component         │
│ remote Windows process   │
└────────────┬─────────────┘
             │
             ├─ file / system information
             ├─ process / application controls
             ├─ screen / webcam / audio categories
             ├─ keyboard / clipboard monitoring
             ├─ network / connection features
             └─ prank / visible desktop controls
```

Later releases also used a separate **EditServer** application for server configuration/customization.

### Confirmed later-package components

| Component | Version evidence | Historical purpose |
|---|---|---|
| `sub7.exe` | 2.2 | controller/client application |
| `SubSeven.exe` | 2.1.5 Legends | controller/client application |
| `server.exe` | 2.2 / Legends | remote server component |
| `EditServer.exe` / `editserver.exe` | later classic releases | server editor/configuration application |
| `sin.exe` | 2.2 | Static IP Notifier utility |
| `ICQMAPI.dll` | Legends | ICQ-related support/integration library |
| plugin DLL architecture | 2.2 | modular extension/SDK concept |

See the [complete EXE/DLL/source inventory](data/file-inventory.csv).

---

# Release history and major differences

The archive currently tracks **21 major release / branch records**.

| Version | Date | Major historical distinction |
|---|---|---|
| **1.0** | Feb 1999 | first public family release; early red-interface generation |
| **1.1** | Mar 1999 | rapid early feature expansion |
| **1.2** | Mar 1999 | continued March development |
| **1.3** | Mar 1999 | closely spaced incremental release; exact delta still being reconstructed |
| **1.4** | Mar 1999 | Registry Manager category confirmed by this branch |
| **1.5** | Apr 1999 | major visual transition to blue/purple **Fatsie** identity |
| **1.6** | Apr 1999 | incremental Fatsie-era release |
| **1.7** | May 1999 | incremental Fatsie-era release |
| **1.8** | May 1999 | webcam capture confirmed by this release |
| **1.9** | Jun 1999 | mature pre-Apocalypse 1.x branch |
| **1.9 Apocalypse** | Aug 1999 | radical redesign bridging 1.x and later 2.x/2.1.x design |
| **2.0** | Sep 1999 | major 2.x transition; shell-access category confirmed in surviving catalogs |
| **2.1** | Nov 1999 | enormous mature feature set; IRC/ICQ-era integration becomes central |
| **2.1.1 GOLD** | Feb 2000 | named GOLD edition |
| **2.1.2 M.U.I.E** | Apr 2000 | named M.U.I.E edition; important to later source provenance |
| **2.1.3 BONUS** | Jun 2000 | named BONUS edition; later source repo labels itself 2.1.3 |
| **2.1.4 DEFCON 8** | Jul 2000 | named DEFCON 8 edition; later XP-labeled package path also survives |
| **2.2** | Mar 2001 | redesigned UI/server customization, stronger NT/2000 support, expanded networking, plugin architecture |
| **2.1.5 Legends** | Feb 2003 | late original-era release; package includes `ICQMAPI.dll` |
| **2.3** | Mar 2010 reported | later community continuation; separated from original 1999–2003 lineage |
| **Legacy** | 2021+ | modern non-malicious Delphi recreation inspired by the 2.2.x UX |

The detailed release guide explains the features, files, screenshots, package evidence and confidence level **for each version individually**:

### ➜ [`docs/version-and-file-history.md`](docs/version-and-file-history.md)

Machine-readable comparison:

### ➜ [`data/version-feature-matrix.csv`](data/version-feature-matrix.csv)

---

# Major feature families

SubSeven accumulated dozens of individual controls. The archive explains what they did historically without reproducing an abuse manual.

### Remote management

File Manager · Process Manager · Application/Window Manager · System Information · Registry Manager · remote shell/terminal category · screen/desktop viewing

### Surveillance / privacy-invasive functions

Keylogger · Clipboard Manager · password/account-data recovery categories · webcam capture · microphone/voice recording · instant-messaging observation categories

### Network / connection functions

Host/IP tools · connection notification · Network Manager · port redirect/tunnel concepts · FTP/service categories · IRC/ICQ integration · 2.2-era proxy/network-observation expansion

### Communication / visible interaction

Chat · messages/questions · text-to-speech · browser/URL-oriented controls

### Prank / “Fun” functions

CD-tray controls · mouse/UI effects · desktop/window manipulation · screen/display effects · visible messages/audio effects

### Configuration / ecosystem

EditServer · controller preferences · server customization · connection notification · `sin.exe` · 2.2 plugin/SDK architecture · Legends-era `ICQMAPI.dll`

**Feature-by-feature encyclopedia:** [`docs/features-and-interface.md`](docs/features-and-interface.md)

---

# February 2001: Sub7Files.com “About SubSeven”

One of the most valuable period references is this exact Wayback snapshot:

### [SubSeven — `www.sub7files.com/about/index.shtml` — 20 February 2001](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)

Wayback replay can be intermittent, so the archive also provides the capture index:

### [Browse all captures of the About page](https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml)

The archived page does not always replay cleanly today. A contemporary SANS/GIAC paper independently cites the same About page (accessed 13 February 2001) and explicitly attributes its large **SubSeven 2.1 feature list** to it.

That relationship is reconstructed here:

- [Detailed source study](docs/sub7files-about-2001.md)
- [SANS/GIAC contemporary paper](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)

---

# 2.2 — the major 2001 redesign

SubSeven **2.2**, publicly released in March 2001, is one of the best-documented classic branches. Contemporary reporting describes a more flexible/redesigned interface, revamped server customization, smoother Windows NT/2000 operation, a client not backward-compatible with older servers, expanded network capabilities and plugin/modular extension architecture.

Confirmed package applications:

- `sub7.exe`
- `EditServer.exe`
- `server.exe`
- `sin.exe`

Research:

- [The Register — New SubSeven Trojan unleashed, 13 Mar 2001](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [SANS — SubSeven 2.2: New Flavor of an Old Favorite](https://www.sans.org/white-papers/958)
- [Malware Museum — SubSeven 2.2](https://www.malware.museum/release/subseven/22/)

---

# 2.1.5 Legends — February 2003

Legends is the late original-era release in the familiar 2.1.x line.

Known distributed files/applications include:

- `server.exe`
- `SubSeven.exe`
- `editserver.exe`
- `ICQMAPI.dll`

Its preserved feature catalog includes the large classic management/surveillance family plus Voice Recorder and Application / Window Manager.

- [Malware Museum — SubSeven 2.1.5 Legends](https://www.malware.museum/release/subseven/215-legends/)

---

# Source code and development history

## Classic source provenance

A public GitLab repository maintained by **illwill** is an important classic-source research record:

### https://gitlab.com/illwill/sub7

A preserved source-repository screenshot identifies the project as **“Source code for SubSeven 2.1.3.”** Its visible README describes source received as **Sub7 2.1.2-era material** directly from mobman and released publicly around the **30 September 2023 BSidesCT** event. The visible repository tree includes `Keylogger`, `[BINS]`, `client`, `editserver.new`, `server`, `Compile_Test.gif`, `README.md` and `rxlib275.zip`.

The 2.1.2-vs-2.1.3 labeling discrepancy is preserved as part of the provenance record rather than silently simplified.

The official BSidesCT 2023 schedule describes illwill’s **“Finding mobman”** talk as covering the acquisition of Sub7 2.1.3’s source code:

- [BSidesCT 2023 archive](https://www.bsidesct.org/archives/2023/)

## Modern SubSeven Legacy

Official source:

### https://github.com/DarkCoderSc/SubSeven

The project states that Legacy is written in Delphi like the original but **does not include malicious features**. Its documented benign functions include a 2.2.x-inspired UX, File Manager, Process Manager, Remote Terminal, Windows Session Manager, modern socket/OpenSSL communication and multithreading/concurrency.

Verified public GitHub mirrors/derivatives tracked separately:

- https://github.com/NoorahSmith/DarkCoderSc-SubSeven
- https://github.com/pawpatrolryder/SubSeven-delphi-rat-
- https://github.com/rutherfordwj/SubSevenLegacy

Additional researcher/profile reference:

- https://github.com/xillwillx

**Full development/source research:** [`docs/source-code-and-development.md`](docs/source-code-and-development.md)

---

# Historical files found locally

A substantial local preservation collection contains release/package records, URL crawls, screenshots, artwork, checksum/tutorial material and later preservation artifacts. **Duplicate records are intentionally retained in the inventory.**

### Example package records

| Scope | Filename | Size | Duplicate status |
|---|---|---:|---|
| 1.0 | `ss.1.0-enc.rar` | 545,132 B | canonical |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc.rar` | 914,392 B | canonical |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc 2.rar` | 914,392 B | duplicate |
| 2.0 | `ss.2.0-enc.rar` | 1,978,683 B | canonical |
| 2.1.0 | `ss.2.1.0-enc.rar` | 1,394,230 B | canonical |
| 2.1.0 | `ss.2.1.0-enc 2.rar` | 1,394,230 B | duplicate |
| 2.1.1 GOLD | `ss.2.1.1-enc.rar` | 2,751,465 B | canonical |
| 2.1.2 M.U.I.E | `ss.2.1.2-enc.rar` | 1,661,300 B | canonical |
| 2.1.3 BONUS | `ss.2.1.3-enc.rar` | 1,429,077 B | canonical |
| 2.1.4 DEFCON 8 | `ss.2.1.4-enc.rar` | 1,417,607 B | canonical |
| 2.2 | `ss.2.2.0-enc.rar` | 2,921,188 B | canonical metadata record |
| Legends | `sub7legends-enc.rar` | 1,339,783 B | canonical |
| Legends | `sub7legends-enc 2.rar` | 1,339,783 B | duplicate |
| 2.3 | `SubSeven_2.3.rar` | — | later continuation record |

Additional records include `sub7_1_9.zip`, `subseven20.zip`, `SubSeven And Windows XP.rar`, `Sub7.net Default md5sum values.rar`, two historical tutorial archives, `sub7-main.rar`, `subpass.zip` / duplicate and `subuster.zip`.

- [Detailed local archive findings](docs/local-archive-findings.md)
- [What is hosted vs not hosted](docs/repository-file-status.md)
- [Every historical record including duplicates](data/historical-file-inventory.csv)
- [Package-only table](data/historical-package-records.csv)
- [Restricted artifact manifest](data/restricted-artifacts-manifest.csv)

---

# Duplicate policy

Duplicates are **not removed from the historical record**. Every known record is labeled as one of:

- `canonical`
- `duplicate`
- `alternate`
- `variant`

For identical safe visual/text content the repository may display one canonical copy while still retaining every duplicate provenance row. Alternate filenames are **not** assumed byte-identical unless hashes/content prove it.

---

# Historical websites and Wayback resources

The archive tracks at least these major domains/URLs:

| Domain / URL | Historical role | Wayback |
|---|---|---|
| `come.to/subseven` | early vanity/redirect URL | [captures](https://web.archive.org/web/*/http://come.to/subseven) |
| `subseven.slak.org` | early host cited in period material | [captures](https://web.archive.org/web/*/http://subseven.slak.org/) |
| `sub7.net` | major classic project/community domain | [captures](https://web.archive.org/web/*/http://sub7.net/) |
| `sub-7.net` | alternate/related classic domain | [captures](https://web.archive.org/web/*/http://sub-7.net/) |
| `sub7crew.org` | crew/community hub | [captures](https://web.archive.org/web/*/http://sub7crew.org/) |
| `s7help.sub7crew.org` | help/documentation subdomain | [captures](https://web.archive.org/web/*/http://s7help.sub7crew.org/) |
| `sub7files.com` | information/release distribution site | [captures](https://web.archive.org/web/*/http://sub7files.com/) |
| `sub7legends.net` | later revival/community domain | [captures](https://web.archive.org/web/*/http://sub7legends.net/) |

Historical local URL crawls preserve old paths for help/reference, IRC, forums, mailing lists, galleries, navigation graphics, CSS/JS, member directories and historical package names.

**Deep reconstruction:** [`docs/websites-and-wayback-history.md`](docs/websites-and-wayback-history.md)

---

# Visual archive

The main README intentionally shows only a small preview. The full gallery contains repository-hosted images plus version-specific classic screenshots and modern Legacy screenshots with source-page fallbacks.

<p align="center">
  <a href="docs/image-gallery.md"><img src="assets/images/subseven-art-gallery.png" alt="SubSeven historical artwork and icons" width="760"></a>
</p>

<p align="center">
  <a href="https://www.malware.museum/release/subseven/22/"><img src="https://www.malware.museum/media/resources/2024/03/12/910392e5-f67f-489b-8b6e-17adc0290ff4.png" alt="SubSeven 2.2 screenshot" width="360"></a>
  <a href="https://github.com/DarkCoderSc/SubSeven"><img src="https://raw.githubusercontent.com/DarkCoderSc/SubSeven/main/Assets/screenshots/main.png" alt="SubSeven Legacy main viewer" width="360"></a>
</p>

**Preview above:** classic 2.2 source-page image and the modern non-malicious Legacy viewer. If a remote image fails, click it to open its source page.

<p align="center">
  <a href="docs/image-gallery.md"><img src="assets/images/wayback-sub7-reference.jpg" alt="SubSeven Wayback research reference" width="520"></a>
</p>

- [Open the full screenshot/image gallery](docs/image-gallery.md)
- [See what image/files are physically hosted](docs/repository-file-status.md)
- [Open the link/image audit](docs/link-audit.md)
- [View duplicate image records](data/historical-file-inventory.csv)

---

# Preservation status

Safe historical material is being copied into this repository wherever practical. The preservation inventory distinguishes:

- **mirrored** — research file itself is present in GitHub;
- **canonical safe copy** — one copy is mirrored while duplicate provenance is recorded separately;
- **metadata-only restricted artifact** — classic runnable malware or buildable weaponized code is not mirrored;
- **secondary discovery source** — a large mixed bookmark/link collection used to discover SubSeven material without importing unrelated content wholesale.

If the original local preservation set is going to be deleted, keep a separate offline copy of every **metadata-only restricted artifact**; GitHub is not intended to be the sole backup of those runnable originals.

See [`docs/preservation-and-research-access.md`](docs/preservation-and-research-access.md) and [`docs/repository-file-status.md`](docs/repository-file-status.md).

---

# Research principles

This archive does not collapse uncertain claims into facts. Each finding should be traceable to one or more of:

1. period documentation / website capture;
2. contemporary security research/news;
3. surviving package/file evidence;
4. later developer/source provenance;
5. later preservation catalog;
6. clearly labeled unresolved research gap.

A filename in a later package does not prove it shipped with an earlier version. A later source tree does not automatically prove original authorship. A duplicate archive does not become a separate release merely because it has a second filename.

See [`docs/archive-source-provenance.md`](docs/archive-source-provenance.md).

---

# Link and image reliability

Repository-local README/document/image paths were audited against the current `main` branch. The main external GitHub source/mirror links were also checked through GitHub's repository API.

The repository includes a standalone relative-link/image validator:

```text
python tools/check_internal_links.py
```

Audit details, image fallbacks, and Wayback fallback guidance are maintained in [`docs/link-audit.md`](docs/link-audit.md).

---

# Key research links

- [Wikipedia — Sub7](https://en.wikipedia.org/wiki/Sub7)
- [Malware Museum — SubSeven release family](https://www.malware.museum/releases/subseven/)
- [SANS/GIAC — What is SubSeven?](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)
- [SANS — SubSeven 2.2: New Flavor of an Old Favorite](https://www.sans.org/white-papers/958)
- [The Register — New SubSeven Trojan unleashed](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [BSidesCT 2023 — Finding mobman](https://www.bsidesct.org/archives/2023/)
- [illwill/Sub7 — classic source provenance](https://gitlab.com/illwill/sub7)
- [DarkCoderSc/SubSeven — modern Legacy source](https://github.com/DarkCoderSc/SubSeven)

---

## Repository purpose

This project exists for **digital preservation, malware history, cybersecurity education and defensive research**. It is not an official continuation of the original SubSeven project and is not intended as an operational malware distribution repository.