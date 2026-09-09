# Repository File Status

This page answers two questions directly:

1. **What is physically hosted in this GitHub repository?**
2. **What historical material is known from the local preservation collection but is not physically uploaded?**

The distinction matters because the public archive preserves research material directly where practical while keeping runnable classic malware and directly buildable weaponized classic RAT material out of the repository.

---

# Physically hosted on GitHub

## Main site / navigation

- `README.md` — primary GitHub landing page
- `index.html` — visual archive site
- `assets/styles.css` — visual-site stylesheet
- `tools/check_internal_links.py` — repository-local link/image validator

## Repository-hosted images

The following are physically stored under `assets/images/`:

| File | Type / use |
|---|---|
| `classic-subseven-interface.jpg` | representative classic controller/interface image |
| `subseven-art-gallery.png` | historical artwork/icon reference |
| `wayback-sub7-reference.jpg` | Wayback/archive research reference |
| `wayback-sub7-org-2001-retry.jpg` | Sub7.org 2001 archive retry record |
| `wayback-sub7crew-org-2001-retry.jpg` | Sub7Crew.org 2001 archive retry record |
| `wayback-otenet-sub7-files-2002-retry.jpg` | users.otenet.gr Sub7 Files/Extras 2002 archive retry record |

The three `retry` images are preserved as evidence of archive-research attempts. They are **not** presented as screenshots of the original historical site designs.

Canonical visual index: [`image-gallery.md`](image-gallery.md)

## Historical / research documentation

- `docs/archive-source-provenance.md`
- `docs/features-and-interface.md`
- `docs/image-gallery.md`
- `docs/link-audit.md`
- `docs/local-archive-findings.md`
- `docs/people-and-community.md`
- `docs/preservation-and-research-access.md`
- `docs/repository-file-status.md`
- `docs/research-gaps.md`
- `docs/safety-and-scope.md`
- `docs/social-history.md`
- `docs/source-code-and-development.md`
- `docs/sub7files-about-2001.md`
- `docs/version-and-file-history.md`
- `docs/websites-and-wayback-history.md`

## Structured research data

- `data/curated-historical-urls.csv`
- `data/file-inventory.csv`
- `data/historical-file-inventory.csv`
- `data/historical-package-records.csv`
- `data/releases.csv`
- `data/resource-links.csv`
- `data/restricted-artifacts-manifest.csv`
- `data/secondary-source-index.csv`
- `data/version-feature-matrix.csv`
- `data/website-history.csv`

## Version / file manifests

- `data/manifests/2-2-files.csv`
- `data/manifests/2-1-5-legends-files.csv`
- `data/manifests/legacy-0-1-alpha-files.csv`

## Safe raw / defanged material

- `data/raw/README.md`
- `data/raw/_sub7_net_zip_links-defanged.txt`

## Later preservation / fan artifact

- `archive/fan-pages/sub7-2025.html`

This is labeled as a modern fan/history artifact rather than an original 1999–2003 SubSeven website.

---

# Externally sourced screenshots linked by the repository

The image gallery also contains source-backed screenshot links for classic releases including 1.0, 1.4, 1.9, 1.9 Apocalypse, 2.1.2 M.U.I.E, 2.1.4 DEFCON 8, 2.2 and 2.1.5 Legends, plus a Wikimedia Commons 2.2 README screenshot and modern SubSeven Legacy screenshots.

Those are not yet all mirrored as repository-hosted files. Each has a source-page fallback so a remote-image failure does not destroy the research trail.

See [`image-gallery.md`](image-gallery.md).

---

# Known visual record not yet physically uploaded

- `illwill/Sub7` source-repository capture showing the public source-project tree and its `Source code for SubSeven 2.1.3` project description.

The source page remains documented at:

- https://gitlab.com/illwill/sub7

Duplicate visual records remain in `data/historical-file-inventory.csv`.

---

# Known historical files that are **not** physically uploaded

These records remain documented in `data/restricted-artifacts-manifest.csv`, `data/historical-package-records.csv`, and the version-history pages.

## Classic release / package archives

| Version / scope | Historical filename | Known size | Public GitHub status |
|---|---|---:|---|
| 1.0 | `ss.1.0-enc.rar` | 545,132 B | metadata only |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc.rar` | 914,392 B | metadata only |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc 2.rar` | 914,392 B | duplicate record; metadata only |
| 2.0 | `ss.2.0-enc.rar` | 1,978,683 B | metadata only |
| 2.0 | `s72.0.rar` | unknown in current record | alternate package record; metadata only |
| 2.1.0 | `ss.2.1.0-enc.rar` | 1,394,230 B | metadata only |
| 2.1.0 | `ss.2.1.0-enc 2.rar` | 1,394,230 B | duplicate record; metadata only |
| 2.1.1 GOLD | `ss.2.1.1-enc.rar` | 2,751,465 B | metadata only |
| 2.1.2 M.U.I.E | `ss.2.1.2-enc.rar` | 1,661,300 B | metadata only |
| 2.1.3 BONUS | `ss.2.1.3-enc.rar` | 1,429,077 B | metadata only |
| 2.1.4 DEFCON 8 | `ss.2.1.4-enc.rar` | 1,417,607 B | metadata only |
| 2.2 | `ss.2.2.0-enc.rar` | 2,921,188 B | metadata only |
| 2.1.5 Legends | `sub7legends-enc.rar` | 1,339,783 B | metadata only |
| 2.1.5 Legends | `sub7legends-enc 2.rar` | 1,339,783 B | duplicate record; metadata only |
| 2.3 continuation | `SubSeven_2.3.rar` | unknown in current record | metadata only |
| 1.9 alternate | `sub7_1_9.zip` | 1,299,523 B | metadata only |
| 2.0 alternate | `subseven20.zip` | 1,035,557 B | metadata only |

## Related historical archives not uploaded

- `SubSeven And Windows XP.rar` — compatibility/tutorial record
- `Sub7.net Default md5sum values.rar` — checksum/reference archive record
- `Tutorial_Sub7.rar` — historical tutorial archive
- `Tutorial_Sub7_2.rar` — historical tutorial archive
- `sub7-main.rar` — source/collection-related archive record
- `subpass.zip`
- `subpass 2.zip` — duplicate/variant record
- `subuster.zip`

These files are cataloged so researchers can identify them, compare filenames/sizes and understand their relationship to the historical collection even though the archives themselves are not hosted here.

## Classic source-code material

The repository links and documents the public `illwill/sub7` source-provenance project and related mirrors/derivatives, but this repository does not import a directly buildable classic RAT source tree into its own file hierarchy.

See [`source-code-and-development.md`](source-code-and-development.md).

---

# Duplicate handling

Duplicates are not erased from the historical record. A duplicate can appear as a second filename with the same known size, a duplicate local copy of a crawl/image/archive, or an alternate package name whose byte identity is not yet proven.

The public repository may host one canonical safe copy of identical image/text content while retaining every known duplicate relationship in `data/historical-file-inventory.csv`.

---

# Preservation rule

Before deleting local originals, compare them against this page and `data/restricted-artifacts-manifest.csv`. A file marked **metadata only** is **not backed up by the GitHub repository itself**; only its research record is preserved here.
