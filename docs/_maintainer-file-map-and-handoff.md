# Maintainer File Map & Project Handoff

> **Maintainer note — intentionally unlinked from the public README/navigation.**
>
> This repository is public, so this page is **not private**. It is only *unlinked*. Anyone who discovers the path can still read it.
>
> Purpose: preserve the project state, file locations, provenance map, known historical filenames, source locations, and current research/fix status so the working context survives even if the original chat is deleted.

Last maintained from the SubSeven archive workstream: **2026-09-09**.

---

# 1. Canonical repository

Repository:

- `https://github.com/rice2k/SubSeven-Historical-Archive`
- Default branch: `main`

Primary public entry points:

- `README.md` — main GitHub research homepage
- `index.html` — standalone visual archive
- `docs/version-and-file-history.md` — detailed version-by-version history
- `docs/features-and-interface.md` — feature encyclopedia
- `docs/image-gallery.md` — screenshot/image catalog
- `docs/source-code-and-development.md` — Delphi/source provenance
- `docs/websites-and-wayback-history.md` — domains, old sites, Wayback research
- `docs/repository-file-status.md` — hosted vs metadata-only status
- `docs/research-access-warning.md` — research-access/safety explanation

This maintainer page is deliberately **not linked** from those public entry points.

---

# 2. Repository-hosted files and locations

## Root

- `README.md`
- `index.html`
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/historical-source.md`

## Visual assets

- `assets/styles.css`
- `assets/images/classic-subseven-interface.jpg`
- `assets/images/subseven-art-gallery.png`
- `assets/images/illwill-sub7-source-provenance.jpg`
- `assets/images/wayback-sub7-reference.jpg`
- `assets/images/wayback-sub7-org-2001-retry.jpg`
- `assets/images/wayback-sub7crew-org-2001-retry.jpg`
- `assets/images/wayback-otenet-sub7-files-2002-retry.jpg`

Important rendering note:

- Some locally preserved image files have rendered unreliably in GitHub Markdown.
- The main README no longer embeds the problematic local hero image.
- `docs/image-gallery.md` links questionable local files instead of embedding them until revalidated.
- The Wikimedia 2.2 README screenshot is linked to its source page instead of hotlinked because GitHub/Camo repeatedly failed to render the direct image URL.
- Official modern Legacy screenshots from `DarkCoderSc/SubSeven` currently render reliably.

## Main documentation

- `docs/archive-source-provenance.md`
- `docs/features-and-interface.md`
- `docs/image-gallery.md`
- `docs/link-audit.md`
- `docs/local-archive-findings.md`
- `docs/people-and-community.md`
- `docs/preservation-and-research-access.md`
- `docs/repository-file-status.md`
- `docs/research-access-warning.md`
- `docs/research-gaps.md`
- `docs/safety-and-scope.md`
- `docs/social-history.md`
- `docs/source-code-and-development.md`
- `docs/sub7files-about-2001.md`
- `docs/version-and-file-history.md`
- `docs/version-screenshot-status.md`
- `docs/websites-and-wayback-history.md`

## Structured research data

- `data/releases.csv`
- `data/version-feature-matrix.csv`
- `data/file-inventory.csv`
- `data/historical-file-inventory.csv`
- `data/historical-package-records.csv`
- `data/restricted-artifacts-manifest.csv`
- `data/resource-links.csv`
- `data/curated-historical-urls.csv`
- `data/secondary-source-index.csv`
- `data/screenshot-index.csv`
- `data/website-history.csv`

## Per-version manifests

- `data/manifests/2-2-files.csv`
- `data/manifests/2-1-5-legends-files.csv`
- `data/manifests/legacy-0-1-alpha-files.csv`

## Safe/defanged raw material

- `data/raw/README.md`
- `data/raw/_sub7_net_zip_links-defanged.txt`

## Later preservation artifact

- `archive/fan-pages/sub7-2025.html`

## Validation utility

- `tools/check_internal_links.py`

---

# 3. Known historical package records — originals are NOT backed up by GitHub

**Critical preservation warning:** the files below are represented by metadata/history only. If the original copies are deleted elsewhere, this GitHub repository will **not** contain the actual archive bytes.

Canonical metadata locations:

- `data/restricted-artifacts-manifest.csv`
- `data/historical-package-records.csv`
- `data/historical-file-inventory.csv`
- `docs/repository-file-status.md`
- `docs/version-and-file-history.md`

Known historical filenames currently tracked:

| Scope | Historical filename | Known size / note | GitHub status |
|---|---|---:|---|
| 1.0 | `ss.1.0-enc.rar` | 545,132 B | metadata only |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc.rar` | 914,392 B | metadata only |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc 2.rar` | 914,392 B | duplicate record; metadata only |
| 2.0 | `ss.2.0-enc.rar` | 1,978,683 B | metadata only |
| 2.0 alternate | `s72.0.rar` | size unresolved in current public record | metadata only |
| 2.1.0 | `ss.2.1.0-enc.rar` | 1,394,230 B | metadata only |
| 2.1.0 | `ss.2.1.0-enc 2.rar` | 1,394,230 B | duplicate record; metadata only |
| 2.1.1 GOLD | `ss.2.1.1-enc.rar` | 2,751,465 B | metadata only |
| 2.1.2 M.U.I.E | `ss.2.1.2-enc.rar` | 1,661,300 B | metadata only |
| 2.1.3 BONUS | `ss.2.1.3-enc.rar` | 1,429,077 B | metadata only |
| 2.1.4 DEFCON 8 | `ss.2.1.4-enc.rar` | 1,417,607 B | metadata only |
| 2.2 | `ss.2.2.0-enc.rar` | 2,921,188 B | metadata only |
| 2.1.5 Legends | `sub7legends-enc.rar` | 1,339,783 B | metadata only |
| 2.1.5 Legends | `sub7legends-enc 2.rar` | 1,339,783 B | duplicate record; metadata only |
| 2.3 continuation | `SubSeven_2.3.rar` | size unresolved in current public record | metadata only |
| 1.9 alternate | `sub7_1_9.zip` | 1,299,523 B | metadata only |
| 2.0 alternate | `subseven20.zip` | 1,035,557 B | metadata only |
| compatibility/history | `SubSeven And Windows XP.rar` | historical ancillary archive | metadata only |
| checksum/reference | `Sub7.net Default md5sum values.rar` | historical checksum/reference archive | metadata only |
| tutorial/history | `Tutorial_Sub7.rar` | historical tutorial archive | metadata only |
| tutorial/history | `Tutorial_Sub7_2.rar` | historical tutorial archive | metadata only |
| source/collection | `sub7-main.rar` | source/collection-related archive record | metadata only |
| ancillary | `subpass.zip` | historical ancillary archive | metadata only |
| ancillary | `subpass 2.zip` | duplicate/variant record | metadata only |
| ancillary | `subuster.zip` | historical ancillary archive | metadata only |

Do **not** assume these are backed up because their names appear in GitHub.

---

# 4. Public source-code / development locations

Classic source provenance:

- `https://gitlab.com/illwill/sub7`
  - public source-provenance project
  - repository page identifies itself as `Source code for SubSeven 2.1.3`
  - preserved screenshot in this archive: `assets/images/illwill-sub7-source-provenance.jpg`
  - project tree visible in preserved research included names such as `Keylogger`, `[BINS]`, `client`, `editserver.new`, `server`, `Compile_Test.gif`, `README.md`, `rxlib275.zip`
  - provenance discrepancy between 2.1.2 and 2.1.3 labeling is intentionally preserved rather than silently resolved

Conference provenance:

- `https://www.bsidesct.org/archives/2023/`
  - BSidesCT 2023 `Finding mobman` research reference

Modern Legacy source:

- `https://github.com/DarkCoderSc/SubSeven`

Tracked modern forks/derivatives:

- `https://github.com/NoorahSmith/DarkCoderSc-SubSeven`
- `https://github.com/pawpatrolryder/SubSeven-delphi-rat-`
- `https://github.com/rutherfordwj/SubSevenLegacy`
- researcher/profile reference: `https://github.com/xillwillx`

Archive research page:

- `docs/source-code-and-development.md`

---

# 5. Historical websites / Wayback locations

Key historical domains/locations tracked:

- `come.to/subseven`
- `subseven.slak.org`
- `sub7.net`
- `sub-7.net`
- `www.sub-7.net`
- `sub7crew.org`
- `sub7crew.com` / `www.sub7crew.com`
- `sub7files.com`
- `sub7legends.net`

Exact important period source:

- `https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml`
- capture-index fallback: `https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml`

Known fixed Sub7Crew snapshot retained in research:

- `https://web.archive.org/web/20010825081000/http://sub7crew.org/`

Canonical GitHub research files:

- `docs/websites-and-wayback-history.md`
- `docs/sub7files-about-2001.md`
- `data/curated-historical-urls.csv`
- `data/website-history.csv`
- `data/resource-links.csv`

---

# 6. Major research/source URLs supplied or used during this project

Core source/research locations:

- `https://github.com/DarkCoderSc/SubSeven`
- `https://github.com/NoorahSmith/DarkCoderSc-SubSeven`
- `https://gitlab.com/illwill/sub7`
- `https://github.com/xillwillx`
- `https://github.com/pawpatrolryder/SubSeven-delphi-rat-`
- `https://exetools.com/showthread.php?t=20235`
- `http://www.sub7files.com/`
- `http://websites.milonic.com/sub-7.net`
- `https://iss4cf0ng.github.io/2026/02/18/2026-2-18-Subseven/`
- current Wikipedia article for Sub7/SubSeven
- Malware Museum SubSeven release catalog and version pages
- SANS/GIAC historical papers
- Security Incidents / seclists 2001 SubSeven 2.2 README and architecture reposts
- Darknet Diaries episodes/transcripts discussing mobman/authorship history
- BSidesCT 2023 historical research
- Wikimedia Commons SubSeven 2.2 README screenshot

The public archive should distinguish:

1. primary/period evidence;
2. contemporary security reporting;
3. modern archival catalogs;
4. later community/fan material;
5. source-provenance repositories;
6. claims that remain uncertain.

---

# 7. Release chronology currently represented

Current canonical release/branch records:

- 1.0 — Feb 1999
- 1.1 — Mar 1999
- 1.2 — Mar 1999
- 1.3 — Mar 1999
- 1.4 — Mar 1999
- 1.5 — Apr 1999
- 1.6 — Apr 1999
- 1.7 — May 1999
- 1.8 — May 1999
- 1.9 — Jun 1999
- 1.9 Apocalypse — Aug 1999
- 2.0 — Sep 1999
- 2.1 — Nov 1999
- 2.1.1 GOLD — Feb 2000
- 2.1.2 M.U.I.E — Apr 2000
- 2.1.3 BONUS — Jun 2000
- 2.1.4 DEFCON 8 — Jul 2000
- 2.2 — Mar 2001
- 2.1.5 Legends — Feb 2003
- 2.3 continuation — 2010
- Legacy — 2021+

Canonical files:

- `data/releases.csv`
- `docs/version-and-file-history.md`
- `data/version-feature-matrix.csv`

---

# 8. Version-specific application/file evidence

Well-documented 2.2 package/application names:

- `sub7.exe` — controller/client
- `EditServer.exe` — server configuration/editor
- `server.exe` — remote server component
- `sin.exe` — Static IP Notifier

Manifest:

- `data/manifests/2-2-files.csv`

Well-documented 2.1.5 Legends package/application names:

- `SubSeven.exe` — controller/client
- `server.exe` — remote server component
- `editserver.exe` — server configuration/editor
- `ICQMAPI.dll` — ICQ-related support/integration material

Manifest:

- `data/manifests/2-1-5-legends-files.csv`

Modern Legacy project/output/dependency evidence:

- Viewer/controller project
- Windows Service
- Server Tray / service controller UI
- Helper application
- certificate generator
- Secure Desktop component
- shared/common source
- BASS dependency
- OpenSSL dependencies

Manifest:

- `data/manifests/legacy-0-1-alpha-files.csv`

Cross-version inventory:

- `data/file-inventory.csv`

---

# 9. Feature documentation state

The archive currently documents these major feature families at a historical/defensive level:

- File Manager
- System Information
- Process Manager
- Application/Window Manager
- Registry Manager
- Screen/Desktop
- Webcam
- Audio/Voice Recorder
- Keylogger
- Clipboard
- Password/account-data categories
- network management / redirect / proxy concepts
- IRC integration
- ICQ integration
- chat/messages/speech
- prank/fun controls
- EditServer
- SIN
- plugin/DLL architecture

Canonical feature page:

- `docs/features-and-interface.md`

Machine-readable comparison:

- `data/version-feature-matrix.csv`

Important rule retained from the project: do not copy the mature 2.1/2.2 feature set backward into early 1.x releases unless source evidence confirms it.

---

# 10. Screenshot / image research state

Canonical screenshot index:

- `data/screenshot-index.csv`

Canonical gallery:

- `docs/image-gallery.md`

Per-version coverage:

- `docs/version-screenshot-status.md`

Release-specific visual source pages have been identified for most classic versions through Malware Museum, including 1.0, 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, Apocalypse, 2.0, GOLD, M.U.I.E, DEFCON 8, 2.2 and Legends.

Direct image-media indexing still needs improvement for:

- 1.3
- base 2.1
- 2.1.3 BONUS

2.3 has a retrospective visual reference cataloged, but original-period 2.3 imagery remains desirable.

Additional high-value visual targets:

- EditServer screens
- SIN screens
- plugin/module screens
- File Manager/Registry/Process/Network subwindows
- original `sub7.net` / `sub7crew.org` / `sub7files.com` site-layout captures

---

# 11. Recent GitHub fixes preserved from this chat

Completed fixes:

- Main README was reorganized to remove repeated material.
- All top badges were changed from dead images into clickable links.
- Broken local hero image was removed from the README after it created a huge blank/broken area on GitHub.
- `docs/image-gallery.md` was rebuilt to prefer source-page links over fragile hotlinks.
- Wikimedia 2.2 README direct-image embed was removed after repeated GitHub/Camo rendering failure; source/license page link remains.
- Working modern Legacy screenshots remain inline.
- Broken `rutherfordwj/SubSevenLegacy` README link was corrected.
- Source-code history page’s stale nonexistent `assets/images/source-code/` path was corrected to the actual hosted provenance image.
- Provider-specific public wording such as `Google Drive` was removed from repository research pages.
- Duplicate records are retained and labeled instead of silently removed.
- Contribution guide and historical-source issue template were added.
- Research-access warning page was added.

Relevant recent commits from this workstream included:

- `2fb36032...` — removed broken README hero dependency
- `ccf16291...` — rebuilt image gallery for safer rendering
- `789ba3c4...` — removed broken Wikimedia README image embed from README
- `9ffaf6cb...` — removed broken Wikimedia embed from gallery
- `7379512c...` — corrected SubSevenLegacy external repository link
- `fd98c0a7...` — added research-access warning page

Do not rely on commit abbreviations as the only provenance; the repository history is authoritative.

---

# 12. Safety / preservation boundary currently applied

Public repository may directly preserve:

- historical text documentation
- README/changelog material
- screenshots and artwork
- hashes and metadata
- package filenames/sizes
- non-operational project/file structure descriptions
- website archives / URL records
- safe research notes
- modern non-malicious Legacy documentation/source links

Public repository does **not** directly republish through this project:

- runnable classic SubSeven malware payloads
- readily recoverable classic malware archives
- buildable weaponized classic RAT source trees
- operational deployment/persistence/evasion instructions

Public third-party research/source pages may be linked as provenance/reference pages, but the archive should not turn them into direct payload-download buttons.

---

# 13. Important project language/style decisions

Public-facing wording should use:

- `historical files found locally`
- `local preservation collection`
- `historical preservation records`

Avoid provider-specific wording in public pages.

Use explicit statuses where possible:

- **AVAILABLE HERE** — safe file physically downloadable from this repository
- **PUBLIC RESEARCH SOURCE** — external research/source page
- **HISTORICAL ARTIFACT — METADATA ONLY** — historical file is known/cataloged but not physically hosted

---

# 14. Remaining high-priority work

1. Revalidate/re-encode the locally hosted images that currently render unreliably on GitHub.
2. Physically mirror more safe historical screenshots with source/license notes so the archive depends less on third-party hotlinks.
3. Recover/index direct screenshot URLs for 1.3, base 2.1 and 2.1.3 BONUS.
4. Recover stronger original-period 2.3 screenshots/provenance.
5. Recover original old-site visual layouts and assets for `sub7.net`, `sub7crew.org`, `sub7files.com` and related domains.
6. Expand version-specific change logs and original README evidence.
7. Expand safe source-code archaeology: Delphi unit/form/project names, DFM/UI structure, dependencies and branch differences without creating a build/deployment guide.
8. Verify additional 2.2 plugin DLL names/versions through period sources.
9. Expand trusted hash provenance where available.
10. Continue link/image audits after every rename or new visual addition.

---

# 15. Before deleting the original chat

The important research state from the conversation has now been copied into GitHub through:

- the public README and deep research pages;
- the structured CSV inventories/manifests;
- the screenshot/source indexes;
- the research-access warning;
- this unlinked maintainer handoff page.

What is **not** preserved by deleting the chat:

- the actual bytes of metadata-only historical malware archives listed above;
- any private/local/cloud storage path that was intentionally not published;
- transient screenshots uploaded only to demonstrate GitHub rendering bugs unless separately committed to the repository.

Therefore, **do not delete your only copy of any historical artifact marked `metadata only` if you still want the original bytes preserved.**

This file is intended to be the maintainer restart point for future work.