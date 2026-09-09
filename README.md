# SubSeven / Sub7 Historical Archive

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

<p align="center"><b>Digital preservation • malware history • defensive cybersecurity education</b></p>

This repository reconstructs the history of **SubSeven / Sub7 / S7**: releases, version differences, interfaces, features, developers and community, EXE/DLL records, Delphi/source-code provenance, old websites, Wayback links, screenshots, historical filenames, documentation, duplicate artifacts and later preservation projects.

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
| **All historical records + duplicates** | [`data/historical-file-inventory.csv`](data/historical-file-inventory.csv) |
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

---

# Release history — 1999 to Legacy

The archive tracks **21 major release/branch records**.

| Version | Date | Major difference / historical landmark |
|---|---:|---|
| **1.0** | Feb 1999 | first public family release; early red-interface generation |
| **1.1** | Mar 1999 | rapid early expansion |
| **1.2** | Mar 1999 | continued early development |
| **1.3** | Mar 1999 | closely spaced incremental build; exact unique delta still under reconstruction |
| **1.4** | Mar 1999 | Registry Manager category confirmed by this branch in surviving catalogs |
| **1.5** | Apr 1999 | major visual transition into the blue/purple **Fatsie** identity |
| **1.6** | Apr 1999 | incremental Fatsie-era revision |
| **1.7** | May 1999 | continued Fatsie-era development |
| **1.8** | May 1999 | webcam capture confirmed by this release in later catalogs |
| **1.9** | Jun 1999 | mature pre-Apocalypse 1.x branch |
| **1.9 Apocalypse** | Aug 1999 | major redesign bridging 1.x and later 2.x/2.1.x presentation |
| **2.0** | Sep 1999 | major 2.x transition; broader system/shell-era feature set |
| **2.1** | Nov 1999 | mature large feature set; IRC/ICQ-era integration becomes especially important |
| **2.1.1 GOLD** | Feb 2000 | named GOLD edition |
| **2.1.2 M.U.I.E** | Apr 2000 | named M.U.I.E edition; important to later source-provenance discussion |
| **2.1.3 BONUS** | Jun 2000 | named BONUS edition; later public source repository identifies itself as 2.1.3 |
| **2.1.4 DEFCON 8** | Jul 2000 | named DEFCON 8 edition |
| **2.2** | Mar 2001 | redesigned interface/server customization; stronger NT/2000 focus; modular plugin architecture |
| **2.1.5 Legends** | Feb 2003 | late original-era 2.1.x release; package records include `ICQMAPI.dll` |
| **2.3** | 2010 | later community continuation/revival, separate from the original 1999–2003 sequence |
| **Legacy** | 2021+ | modern Delphi recreation inspired by the classic UX and separated from the original malware line |

**Detailed release differences → [`docs/version-and-file-history.md`](docs/version-and-file-history.md)**  
**Version × feature matrix → [`data/version-feature-matrix.csv`](data/version-feature-matrix.csv)**

---

# Major change landmarks

| Era | What changed |
|---|---|
| **1.0–1.4** | fast early development; remote file/system/process categories emerge; early red-interface identity |
| **1.5–1.9** | blue/purple Fatsie-era identity; continuing feature expansion; webcam support appears by late 1.x |
| **1.9 Apocalypse** | substantial redesign rather than another ordinary incremental revision |
| **2.0–2.1** | mature 2.x architecture, much larger controller feature set and strong IRC/ICQ-era integration |
| **GOLD → M.U.I.E → BONUS → DEFCON 8** | named 2.1.x editions with increasingly well-preserved screenshots/package/source evidence |
| **2.2** | redesigned UI/editor model, stronger NT/2000-era support and plugin/modular DLL direction |
| **2.1.5 Legends** | return to/continuation of the 2.1.x line; late original-era package with ICQ-related support DLL |
| **2.3** | later 2010 continuation associated with former community members |
| **Legacy** | modern, source-available Delphi homage/recreation documented separately from classic malware artifacts |

---

# What the major features did

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
| **Chat / messages / speech** | visible interaction with the remote desktop/user |
| **Prank / “Fun” controls** | CD tray, mouse, display, window, audio and other visible effects |
| **EditServer** | configuration/editor application associated with later server packages |
| **SIN** | `sin.exe`, identified in 2.2 records as a Static IP Notifier utility |
| **Plugins / DLL extensions** | 2.2-era modular extension/SDK direction |

**Full feature encyclopedia → [`docs/features-and-interface.md`](docs/features-and-interface.md)**

---

# Applications, EXEs, DLLs and project files

| Branch | File | Type | Historical role |
|---|---|---|---|
| **2.2** | `sub7.exe` | EXE | controller/client |
| **2.2** | `EditServer.exe` | EXE | server configuration/editor |
| **2.2** | `server.exe` | EXE | remote server component |
| **2.2** | `sin.exe` | EXE | Static IP Notifier |
| **2.1.5 Legends** | `SubSeven.exe` | EXE | controller/client |
| **2.1.5 Legends** | `server.exe` | EXE | remote server component |
| **2.1.5 Legends** | `editserver.exe` | EXE | server editor/configuration |
| **2.1.5 Legends** | `ICQMAPI.dll` | DLL | ICQ-related support/integration material |

Detailed manifests:

- [`data/manifests/2-2-files.csv`](data/manifests/2-2-files.csv)
- [`data/manifests/2-1-5-legends-files.csv`](data/manifests/2-1-5-legends-files.csv)
- [`data/manifests/legacy-0-1-alpha-files.csv`](data/manifests/legacy-0-1-alpha-files.csv)
- [`data/file-inventory.csv`](data/file-inventory.csv)

---

# Visual history

The main README intentionally avoids embedding questionable local image files. That prevents a malformed image from producing the giant empty/broken block visible in older revisions.

## Reliable visual entry points

| Visual record | Open |
|---|---|
| **Classic releases 1.0–2.1.5** | [Release-by-release screenshot coverage](docs/version-screenshot-status.md) |
| **Full image gallery** | [Image & screenshot gallery](docs/image-gallery.md) |
| **Machine-readable image/source index** | [`data/screenshot-index.csv`](data/screenshot-index.csv) |
| **SubSeven 2.2 README screenshot** | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Sub7_readme_screenshot.png) |
| **Modern SubSeven Legacy screenshots** | [DarkCoderSc/SubSeven](https://github.com/DarkCoderSc/SubSeven) |
| **Classic source-provenance capture** | [Source-code history](docs/source-code-and-development.md) |

### Two reliable examples

<p align="center">
  <a href="https://commons.wikimedia.org/wiki/File:Sub7_readme_screenshot.png"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Sub7_readme_screenshot.png" alt="SubSeven 2.2 README screenshot" width="640"></a>
</p>

<p align="center">
  <a href="https://github.com/DarkCoderSc/SubSeven"><img src="https://raw.githubusercontent.com/DarkCoderSc/SubSeven/main/Assets/screenshots/main.png" alt="Modern SubSeven Legacy viewer" width="640"></a>
</p>

If GitHub temporarily fails to proxy an external image, the image itself is always linked to its source page so the research path remains usable.

---

# February 2001 — Sub7Files.com “About SubSeven”

Important period reference:

**[20 February 2001 Wayback snapshot](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)**  
**[Capture-index fallback](https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml)**

A contemporary SANS/GIAC paper cites the same page and attributes its extensive **SubSeven 2.1 feature list** to that source.

- [`docs/sub7files-about-2001.md`](docs/sub7files-about-2001.md)
- [SANS/GIAC contemporary paper](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)

---

# Source code and development history

Classic SubSeven is historically associated with Delphi/Object Pascal. The archive documents classic source provenance separately from the modern Legacy recreation.

### Classic source provenance

- [illwill/Sub7 on GitLab](https://gitlab.com/illwill/sub7)
- [BSidesCT 2023 — Finding mobman](https://www.bsidesct.org/archives/2023/)
- [`docs/source-code-and-development.md`](docs/source-code-and-development.md)

### Modern Legacy

- [DarkCoderSc/SubSeven](https://github.com/DarkCoderSc/SubSeven)
- [NoorahSmith/DarkCoderSc-SubSeven](https://github.com/NoorahSmith/DarkCoderSc-SubSeven)
- [pawpatrolryder/SubSeven-delphi-rat-](https://github.com/pawpatrolryder/SubSeven-delphi-rat-)
- [rutherfordwj/SubSevenLegacy](https://github.com/rutherfordwj/SubSevenLegacy)

---

# Historical websites and Wayback resources

| Site | Historical role | Archive |
|---|---|---|
| `come.to/subseven` | early vanity/redirect URL | [captures](https://web.archive.org/web/*/http://come.to/subseven) |
| `subseven.slak.org` | early host cited in period material | [captures](https://web.archive.org/web/*/http://subseven.slak.org/) |
| `sub7.net` | major classic project/community domain | [captures](https://web.archive.org/web/*/http://sub7.net/) |
| `sub-7.net` | alternate/related classic domain | [captures](https://web.archive.org/web/*/http://sub-7.net/) |
| `sub7crew.org` | crew/community hub | [captures](https://web.archive.org/web/*/http://sub7crew.org/) |
| `s7help.sub7crew.org` | help/documentation subdomain | [captures](https://web.archive.org/web/*/http://s7help.sub7crew.org/) |
| `sub7files.com` | information/release site | [captures](https://web.archive.org/web/*/http://sub7files.com/) |
| `sub7legends.net` | later revival/community domain | [captures](https://web.archive.org/web/*/http://sub7legends.net/) |

**Deep website reconstruction → [`docs/websites-and-wayback-history.md`](docs/websites-and-wayback-history.md)**

---

# Historical file preservation

Duplicate and alternate records are intentionally preserved in the data instead of silently deleted.

| Data set | Purpose |
|---|---|
| [`historical-file-inventory.csv`](data/historical-file-inventory.csv) | every known historical record including duplicates/variants |
| [`historical-package-records.csv`](data/historical-package-records.csv) | release/package-focused records |
| [`restricted-artifacts-manifest.csv`](data/restricted-artifacts-manifest.csv) | classic runnable/buildable artifacts represented by metadata rather than payloads |
| [`repository-file-status.md`](docs/repository-file-status.md) | what is physically hosted vs metadata-only |

Duplicate labels include **canonical**, **duplicate**, **alternate**, and **variant**.

---

# Repository layout

```text
SubSeven-Historical-Archive/
├── README.md
├── index.html
├── CONTRIBUTING.md
├── assets/
│   └── images/
├── docs/
│   ├── version-and-file-history.md
│   ├── version-screenshot-status.md
│   ├── features-and-interface.md
│   ├── image-gallery.md
│   ├── source-code-and-development.md
│   ├── websites-and-wayback-history.md
│   ├── sub7files-about-2001.md
│   ├── people-and-community.md
│   ├── social-history.md
│   └── link-audit.md
├── data/
│   ├── releases.csv
│   ├── version-feature-matrix.csv
│   ├── screenshot-index.csv
│   ├── file-inventory.csv
│   ├── historical-file-inventory.csv
│   ├── historical-package-records.csv
│   ├── curated-historical-urls.csv
│   └── manifests/
├── archive/
└── tools/
```

---

# Key research links

- [Wikipedia — Sub7](https://en.wikipedia.org/wiki/Sub7)
- [Malware Museum — SubSeven family](https://www.malware.museum/releases/subseven/)
- [SANS/GIAC — What is SubSeven?](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)
- [SANS — SubSeven 2.2](https://www.sans.org/white-papers/958)
- [The Register — New SubSeven Trojan unleashed](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [BSidesCT 2023](https://www.bsidesct.org/archives/2023/)
- [illwill/Sub7](https://gitlab.com/illwill/sub7)
- [DarkCoderSc/SubSeven](https://github.com/DarkCoderSc/SubSeven)

---

## Repository purpose

This project exists for **digital preservation, malware history, cybersecurity education and defensive research**. It is not an official continuation of the original SubSeven project.