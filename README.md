# SubSeven / Sub7 Historical Archive

<p align="center">
  <a href="docs/image-gallery.md"><img src="assets/images/classic-subseven-interface.jpg" alt="Classic SubSeven controller interface" width="780"></a>
</p>

<p align="center">
  <a href="docs/archive-source-provenance.md"><img alt="Historical archive" src="https://img.shields.io/badge/type-historical%20archive-7c3aed"></a>
  <a href="docs/version-and-file-history.md"><img alt="Coverage" src="https://img.shields.io/badge/coverage-1999%E2%86%92present-2563eb"></a>
  <a href="docs/source-code-and-development.md"><img alt="Classic language" src="https://img.shields.io/badge/classic%20language-Delphi%20%2F%20Object%20Pascal-d97706"></a>
  <a href="docs/image-gallery.md"><img alt="Screenshots" src="https://img.shields.io/badge/screenshots-open%20gallery-0ea5e9"></a>
  <a href="docs/version-screenshot-status.md"><img alt="Screenshot coverage" src="https://img.shields.io/badge/visual%20coverage-by%20version-0284c7"></a>
  <a href="data/historical-file-inventory.csv"><img alt="Duplicates" src="https://img.shields.io/badge/duplicates-preserved%20%26%20labeled-475569"></a>
  <a href="docs/repository-file-status.md"><img alt="File status" src="https://img.shields.io/badge/files-hosted%20vs%20not%20hosted-334155"></a>
  <a href="docs/safety-and-scope.md"><img alt="Purpose" src="https://img.shields.io/badge/purpose-cybersecurity%20history-059669"></a>
</p>

> **Digital preservation • malware history • defensive cybersecurity education**  
> This repository reconstructs the history of **SubSeven / Sub7 / S7**: releases, version differences, interfaces, features, developers and community, EXE/DLL records, Delphi/source-code provenance, old websites, Wayback links, screenshots, historical filenames, documentation, duplicate artifacts and later preservation projects.
>
> Classic runnable malware and directly buildable weaponized classic RAT material are **not republished as payloads here**. Their historical record is preserved through filenames, sizes, hashes/provenance where available, package manifests, screenshots, readmes, archived URLs and technical documentation.

---

## Start here

| Research area | Canonical page |
|---|---|
| **What SubSeven was / how it worked** | [Overview below](#what-was-subseven) |
| **Every version and what changed** | [`docs/version-and-file-history.md`](docs/version-and-file-history.md) |
| **Version × feature matrix** | [`data/version-feature-matrix.csv`](data/version-feature-matrix.csv) |
| **Screenshots / images** | [`docs/image-gallery.md`](docs/image-gallery.md) |
| **Screenshot coverage by release** | [`docs/version-screenshot-status.md`](docs/version-screenshot-status.md) |
| **Machine-readable screenshot index** | [`data/screenshot-index.csv`](data/screenshot-index.csv) |
| **Detailed feature encyclopedia** | [`docs/features-and-interface.md`](docs/features-and-interface.md) |
| **Files / EXEs / DLLs / source artifacts** | [`data/file-inventory.csv`](data/file-inventory.csv) |
| **What GitHub physically hosts vs metadata-only** | [`docs/repository-file-status.md`](docs/repository-file-status.md) |
| **Historical package records** | [`data/historical-package-records.csv`](data/historical-package-records.csv) |
| **All local historical records + duplicates** | [`data/historical-file-inventory.csv`](data/historical-file-inventory.csv) |
| **Old websites / Wayback history** | [`docs/websites-and-wayback-history.md`](docs/websites-and-wayback-history.md) |
| **Sub7Files February 2001 source study** | [`docs/sub7files-about-2001.md`](docs/sub7files-about-2001.md) |
| **Source code / Delphi / development history** | [`docs/source-code-and-development.md`](docs/source-code-and-development.md) |
| **People / crew / authorship research** | [`docs/people-and-community.md`](docs/people-and-community.md) |
| **AOL / AIM / ICQ / IRC era context** | [`docs/social-history.md`](docs/social-history.md) |
| **Research provenance / confidence rules** | [`docs/archive-source-provenance.md`](docs/archive-source-provenance.md) |
| **Link & image audit** | [`docs/link-audit.md`](docs/link-audit.md) |
| **Open research gaps** | [`docs/research-gaps.md`](docs/research-gaps.md) |
| **Visual standalone site** | [`index.html`](index.html) |

---

# What was SubSeven?

**SubSeven**, usually shortened to **Sub7** or **S7**, was a Windows remote-access trojan/backdoor family first released in 1999. It became one of the most recognizable RAT families of the Windows 9x / NT / 2000 era and is closely associated with the dial-up Internet, IRC, ICQ, AOL/AIM, personal-site and early-webcam period.

The classic family is historically associated with **Borland Delphi / Object Pascal** and the Windows VCL application ecosystem.

Its controller combined ordinary remote-management concepts with surveillance, credential-related, networking and prank functions. That mixture made Sub7 culturally memorable while also making unauthorized installations a serious privacy and security threat.

## High-level architecture

```text
┌──────────────────────────────┐
│ Controller / Client          │
│ graphical operator interface │
└──────────────┬───────────────┘
               │ network connection
               ▼
┌──────────────────────────────┐
│ Server component             │
│ remote Windows process       │
└──────────────┬───────────────┘
               │
               ├─ file / system information
               ├─ process / window management
               ├─ screen / webcam / audio categories
               ├─ keyboard / clipboard monitoring
               ├─ network / messaging integration
               └─ visible prank / desktop controls
```

Later classic releases also used **EditServer** as a separate server-configuration/editor application. SubSeven 2.2 additionally emphasized a more modular plugin/DLL direction.

> This archive explains the architecture historically. It does not provide deployment, persistence, evasion or unauthorized-access instructions.

---

# Release history — 1999 to Legacy

The archive tracks **21 major release/branch records**. Month-level dates below follow the current preservation catalog; exact day claims are kept separate when stronger evidence exists.

| Version | Date | Major difference / historical landmark | Visual evidence |
|---|---:|---|---|
| **1.0** | Feb 1999 | first public family release; early red-interface generation | [coverage](docs/version-screenshot-status.md) |
| **1.1** | Mar 1999 | rapid early expansion | [coverage](docs/version-screenshot-status.md) |
| **1.2** | Mar 1999 | continued early development | [coverage](docs/version-screenshot-status.md) |
| **1.3** | Mar 1999 | closely spaced incremental build; exact unique delta still under reconstruction | [coverage](docs/version-screenshot-status.md) |
| **1.4** | Mar 1999 | Registry Manager category confirmed by this branch in surviving catalogs | [coverage](docs/version-screenshot-status.md) |
| **1.5** | Apr 1999 | major visual transition into the blue/purple **Fatsie** identity | [coverage](docs/version-screenshot-status.md) |
| **1.6** | Apr 1999 | incremental Fatsie-era revision | [coverage](docs/version-screenshot-status.md) |
| **1.7** | May 1999 | continued Fatsie-era development | [coverage](docs/version-screenshot-status.md) |
| **1.8** | May 1999 | webcam capture confirmed by this release in later catalogs | [coverage](docs/version-screenshot-status.md) |
| **1.9** | Jun 1999 | mature pre-Apocalypse 1.x branch | [coverage](docs/version-screenshot-status.md) |
| **1.9 Apocalypse** | Aug 1999 | major redesign bridging 1.x and later 2.x/2.1.x presentation | [coverage](docs/version-screenshot-status.md) |
| **2.0** | Sep 1999 | major 2.x transition; broader system/shell-era feature set | [coverage](docs/version-screenshot-status.md) |
| **2.1** | Nov 1999 | mature large feature set; IRC/ICQ-era integration becomes especially important | [coverage](docs/version-screenshot-status.md) |
| **2.1.1 GOLD** | Feb 2000 | named GOLD edition | [coverage](docs/version-screenshot-status.md) |
| **2.1.2 M.U.I.E** | Apr 2000 | named M.U.I.E edition; important to later source-provenance discussion | [coverage](docs/version-screenshot-status.md) |
| **2.1.3 BONUS** | Jun 2000 | named BONUS edition; later public source repository identifies itself as 2.1.3 | [coverage](docs/version-screenshot-status.md) |
| **2.1.4 DEFCON 8** | Jul 2000 | named DEFCON 8 edition; XP-labeled later package-path evidence also survives | [coverage](docs/version-screenshot-status.md) |
| **2.2** | Mar 2001 | redesigned interface/server customization; stronger NT/2000 focus; modular plugin architecture | [coverage](docs/version-screenshot-status.md) |
| **2.1.5 Legends** | Feb 2003 | late original-era 2.1.x release; package records include `ICQMAPI.dll` | [coverage](docs/version-screenshot-status.md) |
| **2.3** | 2010 | later community continuation/revival, kept separate from the original 1999–2003 lineage | [coverage](docs/version-screenshot-status.md) |
| **Legacy** | 2021+ | modern Delphi recreation inspired by the classic UX and explicitly separated from the original malware line | [official source](https://github.com/DarkCoderSc/SubSeven) |

### Detailed differences

The release table above is intentionally compact. The full release guide records **version-specific files, feature changes, screenshots, evidence confidence, package names and research links** without copying the mature 2.1/2.2 feature set backward into every early build:

**→ [`docs/version-and-file-history.md`](docs/version-and-file-history.md)**  
**→ [`data/version-feature-matrix.csv`](data/version-feature-matrix.csv)**

---

# Major change landmarks

| Era | What changed |
|---|---|
| **1.0–1.4** | fast early development; recognizable remote file/system/process categories emerge; early red-interface identity |
| **1.5–1.9** | blue/purple Fatsie-era visual identity; feature set continues expanding; webcam support appears by the late 1.x line |
| **1.9 Apocalypse** | substantial redesign rather than another plain-number incremental revision |
| **2.0–2.1** | mature 2.x architecture and a much larger controller feature set; IRC/ICQ-era connectivity becomes central to the historical record |
| **GOLD → M.U.I.E → BONUS → DEFCON 8** | named 2.1.x editions; increasingly well-preserved screenshots/package/source evidence |
| **2.2** | redesigned UI/editor model, stronger Windows NT/2000-era support and plugin/modular DLL direction |
| **2.1.5 Legends** | return to/continuation of the 2.1.x line; late original-era package with ICQ-related support DLL |
| **2.3** | later 2010 continuation associated with former community members rather than the original 1999–2003 release sequence |
| **Legacy** | modern, source-available Delphi homage/recreation; documented separately from classic malware artifacts |

---

# What the major features did

SubSeven accumulated many individual controls. The archive documents what they represented **historically and defensively**, not how to abuse them.

| Feature family | Historical function |
|---|---|
| **File Manager** | remote drive, directory and file browsing/management |
| **System Information** | displayed operating-system, user, directory, hardware/display and environment information |
| **Process / Application / Window Manager** | enumerated and managed running processes, applications and windows |
| **Registry Manager** | exposed remote Windows Registry management |
| **Screen / Desktop** | captured or displayed the remote desktop and related display controls |
| **Webcam / Audio** | later branches included webcam and microphone/voice surveillance categories |
| **Keylogger / Clipboard** | captured typed or clipboard data; historically significant because of credential/privacy risk |
| **Password / account-data recovery** | exposed credential/account-information categories in mature releases |
| **Network Manager / redirect / proxy concepts** | network-management and relay/redirection categories expanded across mature releases |
| **IRC / ICQ / messaging integration** | reflected the communication environment of the late-1990s/early-2000s Internet |
| **Chat / messages / speech** | allowed visible interaction with the remote desktop/user |
| **Prank / “Fun” controls** | CD tray, mouse, display, window, audio and other visible effects |
| **EditServer** | configuration/editor application associated with later server packages |
| **SIN** | `sin.exe`, identified in 2.2 records as a Static IP Notifier utility |
| **Plugins / DLL extensions** | 2.2-era modular extension/SDK direction |

**Full feature encyclopedia → [`docs/features-and-interface.md`](docs/features-and-interface.md)**

---

# Applications, EXEs, DLLs and project files

## Confirmed later-classic package records

| Branch | File | Type | Historical role | Research manifest |
|---|---|---|---|---|
| **2.2** | `sub7.exe` | EXE | controller/client | [`2-2-files.csv`](data/manifests/2-2-files.csv) |
| **2.2** | `EditServer.exe` | EXE | server configuration/editor | [`2-2-files.csv`](data/manifests/2-2-files.csv) |
| **2.2** | `server.exe` | EXE | remote server component | [`2-2-files.csv`](data/manifests/2-2-files.csv) |
| **2.2** | `sin.exe` | EXE | Static IP Notifier | [`2-2-files.csv`](data/manifests/2-2-files.csv) |
| **2.1.5 Legends** | `SubSeven.exe` | EXE | controller/client | [`2-1-5-legends-files.csv`](data/manifests/2-1-5-legends-files.csv) |
| **2.1.5 Legends** | `server.exe` | EXE | remote server component | [`2-1-5-legends-files.csv`](data/manifests/2-1-5-legends-files.csv) |
| **2.1.5 Legends** | `editserver.exe` | EXE | server editor/configuration | [`2-1-5-legends-files.csv`](data/manifests/2-1-5-legends-files.csv) |
| **2.1.5 Legends** | `ICQMAPI.dll` | DLL | ICQ-related support/integration material | [`2-1-5-legends-files.csv`](data/manifests/2-1-5-legends-files.csv) |

## Modern Legacy records

The official modern repository identifies separate Viewer, Service, Helper, Tray, certificate-generator, Secure Desktop and shared/common project areas. Its installer definitions reference outputs/dependencies including `Sub7Viewer.exe`, `Sub7Service.exe`, `Sub7Helper.exe`, `Sub7ServerTray.exe`, `CertGenerator.exe`, `SecureDesktop.dll`, BASS and OpenSSL libraries.

These are **modern Legacy names**, not evidence for original 1999 package filenames.

- [Official Legacy source](https://github.com/DarkCoderSc/SubSeven)
- [Legacy file manifest](data/manifests/legacy-0-1-alpha-files.csv)
- [Complete cross-version file inventory](data/file-inventory.csv)

---

# Visual history

## Repository-hosted classic/interface material

<p align="center">
  <a href="docs/image-gallery.md"><img src="assets/images/subseven-art-gallery.png" alt="Historical SubSeven artwork and icon reference" width="720"></a>
</p>

The repository physically hosts multiple preservation images and separately catalogs externally sourced, version-specific controller screenshots.

### Hosted source-provenance capture

<p align="center">
  <a href="docs/source-code-and-development.md"><img src="assets/images/illwill-sub7-source-provenance.jpg" alt="illwill Sub7 public source repository provenance screenshot" width="760"></a>
</p>

### Current screenshot coverage

The screenshot catalog now records visual evidence for the major classic release sequence, including **1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, Apocalypse, 2.0, GOLD, M.U.I.E, DEFCON 8, 2.2 and Legends**, source-page evidence for **1.3, base 2.1 and BONUS**, a retrospective 2.3 visual reference, and the official modern Legacy screenshot set.

- **[Open the full screenshot gallery](docs/image-gallery.md)**
- **[See coverage by version](docs/version-screenshot-status.md)**
- **[Download/view the screenshot index](data/screenshot-index.csv)**

Repository-hosted Wayback/research images are also preserved, but archive-retry screenshots are explicitly labeled as **research-attempt evidence**, not original website layouts.

---

# February 2001 — Sub7Files.com “About SubSeven”

A particularly valuable period target is the archived `sub7files.com` About page immediately before the 2.2 release:

**[20 February 2001 archived About page](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)**  
**[All Wayback captures / fallback](https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml)**

A contemporary SANS/GIAC paper independently cites the same About page and attributes a large **SubSeven 2.1 feature list** to it.

- [Archive source study](docs/sub7files-about-2001.md)
- [SANS/GIAC contemporary paper](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)

---

# Historical websites and web-community footprint

| Domain / URL | Historical role | Archive entry point |
|---|---|---|
| `come.to/subseven` | early vanity/redirect URL | [Wayback](https://web.archive.org/web/*/http://come.to/subseven) |
| `subseven.slak.org` | early hosting cited in period references | [Wayback](https://web.archive.org/web/*/http://subseven.slak.org/) |
| `sub7.net` | major classic project/community domain | [Wayback](https://web.archive.org/web/*/http://sub7.net/) |
| `sub-7.net` | alternate/related historical domain | [Wayback](https://web.archive.org/web/*/http://sub-7.net/) |
| `sub7crew.org` | community/crew hub: downloads, help, IRC, forums, mailing lists, galleries, member pages | [Wayback](https://web.archive.org/web/*/http://sub7crew.org/) |
| `s7help.sub7crew.org` | help/documentation subdomain | [Wayback](https://web.archive.org/web/*/http://s7help.sub7crew.org/) |
| `sub7files.com` | release/documentation/information site | [Wayback](https://web.archive.org/web/*/http://sub7files.com/) |
| `sub7legends.net` | later Legends-era revival/community/preservation domain | [Wayback](https://web.archive.org/web/*/http://sub7legends.net/) |

Historical URL/path records preserve evidence for old help/reference pages, mailing-list endpoints, UBB forums, IRC pages, galleries, CSS/JavaScript, logos/buttons/tabs and member directories.

**Deep website reconstruction → [`docs/websites-and-wayback-history.md`](docs/websites-and-wayback-history.md)**  
**Normalized URL catalog → [`data/curated-historical-urls.csv`](data/curated-historical-urls.csv)**

---

# Source code and development provenance

Classic SubSeven is historically associated with Delphi/Object Pascal. A major modern provenance record is the public **`illwill/sub7`** GitLab project:

**https://gitlab.com/illwill/sub7**

Its public project description identifies it as **“Source code for SubSeven 2.1.3,”** while preserved README material discusses **2.1.2-era source** received from mobman. This 2.1.2-vs-2.1.3 discrepancy is retained rather than silently flattened into one claim.

The repository hosts a screenshot of that public source page for historical provenance, while the classic buildable source tree itself is linked/documented rather than copied into this archive.

The official BSidesCT 2023 schedule for illwill’s **“Finding mobman”** presentation provides additional context for the source-acquisition/public-release story:

- [BSidesCT 2023 archive](https://www.bsidesct.org/archives/2023/)
- [Full source/development history](docs/source-code-and-development.md)

## Modern Legacy

The modern project is intentionally treated separately:

- **Official:** https://github.com/DarkCoderSc/SubSeven
- [NoorahSmith fork](https://github.com/NoorahSmith/DarkCoderSc-SubSeven)
- [pawpatrolryder fork](https://github.com/pawpatrolryder/SubSeven-delphi-rat-)
- [rutherfordwj fork](https://github.com/rutherfordwj/SubSevenLegacy)

Repository names alone are not treated as proof of original classic authorship; provenance is evaluated separately.

---

# Historical files found locally

The preservation collection contains release/package records, URL crawls, screenshots, artwork, checksum/tutorial material and later preservation artifacts. **Duplicates are intentionally retained and labeled.**

Example package records include:

| Scope | Historical filename | Known size | Record status |
|---|---|---:|---|
| 1.0 | `ss.1.0-enc.rar` | 545,132 B | canonical metadata record |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc.rar` | 914,392 B | canonical metadata record |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc 2.rar` | 914,392 B | duplicate record |
| 2.0 | `ss.2.0-enc.rar` | 1,978,683 B | canonical metadata record |
| 2.1.0 | `ss.2.1.0-enc.rar` | 1,394,230 B | canonical metadata record |
| 2.1.0 | `ss.2.1.0-enc 2.rar` | 1,394,230 B | duplicate record |
| 2.1.1 GOLD | `ss.2.1.1-enc.rar` | 2,751,465 B | metadata record |
| 2.1.2 M.U.I.E | `ss.2.1.2-enc.rar` | 1,661,300 B | metadata record |
| 2.1.3 BONUS | `ss.2.1.3-enc.rar` | 1,429,077 B | metadata record |
| 2.1.4 DEFCON 8 | `ss.2.1.4-enc.rar` | 1,417,607 B | metadata record |
| 2.2 | `ss.2.2.0-enc.rar` | 2,921,188 B | metadata record |
| Legends | `sub7legends-enc.rar` | 1,339,783 B | canonical metadata record |
| Legends | `sub7legends-enc 2.rar` | 1,339,783 B | duplicate record |
| 2.3 | `SubSeven_2.3.rar` | not yet established in canonical table | continuation record |

Additional cataloged names include `sub7_1_9.zip`, `subseven20.zip`, `SubSeven And Windows XP.rar`, `Sub7.net Default md5sum values.rar`, historical tutorial archives, `sub7-main.rar`, `subpass.zip` / duplicate and `subuster.zip`.

### What is actually backed up by GitHub?

Do **not** assume that every filename in the historical inventory is physically stored here.

- [Hosted vs not-hosted status](docs/repository-file-status.md)
- [Complete historical inventory](data/historical-file-inventory.csv)
- [Package-only records](data/historical-package-records.csv)
- [Restricted artifact manifest](data/restricted-artifacts-manifest.csv)

---

# Duplicate policy

Duplicates are **not erased from the research record**. Each known record can be classified as:

- `canonical`
- `duplicate`
- `alternate`
- `variant`

For identical safe text/image material, the repository can display one canonical file while still retaining all duplicate provenance rows. Alternate filenames are not assumed byte-identical unless hashes/content establish that relationship.

---

# Repository-hosted preservation images

The repository currently physically hosts:

- `assets/images/classic-subseven-interface.jpg`
- `assets/images/subseven-art-gallery.png`
- `assets/images/illwill-sub7-source-provenance.jpg`
- `assets/images/wayback-sub7-reference.jpg`
- `assets/images/wayback-sub7-org-2001-retry.jpg`
- `assets/images/wayback-sub7crew-org-2001-retry.jpg`
- `assets/images/wayback-otenet-sub7-files-2002-retry.jpg`

See [`docs/image-gallery.md`](docs/image-gallery.md) for the images themselves, external version-specific screenshots and source-page fallbacks.

---

# Repository layout

```text
SubSeven-Historical-Archive/
├── README.md                     # this research homepage
├── index.html                    # standalone visual archive
├── assets/
│   ├── styles.css
│   └── images/                   # repository-hosted preservation images
├── docs/
│   ├── version-and-file-history.md
│   ├── version-screenshot-status.md
│   ├── features-and-interface.md
│   ├── image-gallery.md
│   ├── websites-and-wayback-history.md
│   ├── source-code-and-development.md
│   ├── sub7files-about-2001.md
│   ├── people-and-community.md
│   ├── social-history.md
│   ├── repository-file-status.md
│   └── ...
├── data/
│   ├── releases.csv
│   ├── version-feature-matrix.csv
│   ├── file-inventory.csv
│   ├── screenshot-index.csv
│   ├── website-history.csv
│   ├── curated-historical-urls.csv
│   ├── historical-file-inventory.csv
│   ├── historical-package-records.csv
│   └── manifests/
├── archive/
└── tools/
    └── check_internal_links.py
```

---

# Link and image reliability

Repository-local links use relative paths so they work on GitHub without depending on commit-specific URLs. Externally hosted screenshots always have a source-page fallback where possible.

The repository includes a local validator:

```text
python tools/check_internal_links.py
```

Audit status and maintenance rules are recorded in [`docs/link-audit.md`](docs/link-audit.md).

GitHub Camo can temporarily cache a failed external image request. A Camo failure does **not** necessarily mean the source page is gone; use the clickable source page in the screenshot gallery when that happens.

---

# Key historical / research links

- [Sub7Files.com About page — 20 Feb 2001 Wayback snapshot](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)
- [Malware Museum — SubSeven release family](https://www.malware.museum/releases/subseven/)
- [SANS/GIAC — contemporary SubSeven research](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)
- [SANS — SubSeven 2.2: New Flavor of an Old Favorite](https://www.sans.org/white-papers/958)
- [The Register — New SubSeven Trojan unleashed](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [BSidesCT 2023 archive](https://www.bsidesct.org/archives/2023/)
- [illwill/Sub7 — classic source provenance](https://gitlab.com/illwill/sub7)
- [DarkCoderSc/SubSeven — modern Legacy source](https://github.com/DarkCoderSc/SubSeven)
- [Wikimedia Commons — SubSeven 2.2 README screenshot](https://commons.wikimedia.org/wiki/File:Sub7_readme_screenshot.png)

---

## Archive purpose

This repository exists for **digital preservation, malware history, cybersecurity education and defensive research**. It is not an official continuation of the original SubSeven project.

Research claims are kept traceable to period documentation, archived websites, contemporary security research/news, surviving package/file evidence, later developer/source provenance or clearly labeled secondary catalogs. Unresolved claims remain unresolved instead of being silently converted into facts.
