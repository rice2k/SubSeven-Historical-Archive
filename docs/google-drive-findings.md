# Google Drive preservation findings

The connected Google Drive contains multiple SubSeven/Sub7 collections assembled for historical preservation. This document records what was found and how each class of material is handled in the public archive.

## 1. Historical release collection

The primary release collection contains encrypted/package archives whose filenames map to major SubSeven branches and editions. Observed records include:

| Historical scope | Drive filename | Size | Public archive treatment |
|---|---:|---:|---|
| 1.0 | `ss.1.0-enc.rar` | 545,132 B | metadata only |
| 1.9 Apocalypse | `ss.1.9.Apocalypse-enc.rar` | 914,392 B | metadata only; duplicate present |
| 2.0 | `ss.2.0-enc.rar` | 1,978,683 B | metadata only |
| 2.0 alternate | `s72.0.rar` | size not returned in search result | metadata only |
| 2.1.0 | `ss.2.1.0-enc.rar` | 1,394,230 B | metadata only; duplicate present |
| 2.1.1 | `ss.2.1.1-enc.rar` | 2,751,465 B | metadata only |
| 2.1.2 | `ss.2.1.2-enc.rar` | 1,661,300 B | metadata only |
| 2.1.3 | `ss.2.1.3-enc.rar` | 1,429,077 B | metadata only |
| 2.1.4 | `ss.2.1.4-enc.rar` | 1,417,607 B | metadata only |
| 2.2 | `ss.2.2.0-enc.rar` | 2,921,188 B | metadata only; Google explicitly blocked raw download as malware |
| Legends | `sub7legends-enc.rar` | 1,339,783 B | metadata only; duplicate present |
| 2.3 continuation | `SubSeven_2.3.rar` | size not returned in captured listing | metadata only |

These package records are important because they establish that the user's Drive preservation collection contains a broad version sequence rather than only one or two releases. They are **not** copied into the public GitHub repository as runnable malware.

## 2. Additional/ancillary Sub7 packages

A nested `Other Sub7` folder contains additional historical filenames:

- `sub7_1_9.zip` — 1,299,523 B
- `subseven20.zip` — 1,035,557 B
- `subpass.zip` — 6,319 B
- `subpass 2.zip` — 6,319 B (duplicate-name variant)
- `subuster.zip` — 29,663 B

The broader collection also includes:

- `SubSeven And Windows XP.rar` — 283,843 B
- `Sub7.net Default md5sum values.rar` — 17,361 B
- `Tutorial_Sub7.rar` — 1,254,718 B
- `Tutorial_Sub7_2.rar` — 1,530,900 B
- `sub7-main.rar` — 3,012,065 B

These are cataloged as historical evidence. Their contents are not assumed to be benign merely because a filename says "tutorial", "MD5", or "Windows XP"; where safe text or images can be independently extracted/verified, those can be preserved separately.

## 3. Website and URL-crawl collection

A separate `Sub7` Drive folder contains URL crawl material for old SubSeven domains. Two especially important source files are:

- `_sub7crew_org_all_urls.txt` — 548,749 bytes
- `_sub7_net_all_urls.txt` — 65,336 bytes

The crawl preserves old project/community paths for pages and assets that are otherwise difficult to reconstruct from memory. Examples include:

- `downloads.html`, `downloads.shtml`, and `/downloads/`
- `reference.shtml`
- `help.shtml`
- `irc.shtml`
- `subseven.shtml`
- `sub7list.shtml`
- SubSeven Official Mailing List archive endpoints
- UBB/forum paths
- gallery image paths
- old GIF/JPG/CSS interface assets
- member pages under `~azzazzin`, `~fc`, `~mistahq`, `~qroject`, and others
- historical package URL records such as `s7.2.2.0.zip` and `sub7legends.zip`
- associated utility paths for binders, web downloaders, infectors, scanners and other scene-era tools

The public repository preserves the raw URL lists as historical text data and also provides a curated/normalized table for easier research. A historical URL record is not treated as proof that the referenced file is safe or still downloadable.

## 4. Historical images found in Drive

The Drive audit located visual material that can safely be included directly in the archive:

- `1698323969143.jpg` — 129,938 B — classic SubSeven controller/interface screenshot (duplicate copy also present)
- `art.png` — 1,111,935 B — SubSeven artwork/icon sheet
- `web.archive.org-bda1c48231.jpg` — Wayback-related screenshot
- `web.archive.org-4bd740875f.jpg` — Wayback-related screenshot
- `gitlab.com-80bbfaea50.png` — GitLab/source-code-page screenshot

The two clearest SubSeven visual assets are mirrored under `assets/images/` and displayed on the repository homepage/site.

## 5. Fan/history HTML preserved in Drive

The file `sub7.html` (3,029 B; duplicate copy also present) is a **2025 fan/history page**, not an original 1999–2003 SubSeven website. It is useful as provenance for the user's later preservation work, but its statements should be verified against period sources before being treated as primary historical evidence.

## 6. Deduplication

Several Drive items appear in two preservation trees with identical names and sizes. The GitHub archive keeps one canonical public copy of safe data/assets and records duplicate Drive entries in `data/google-drive-master-inventory.csv` rather than publishing redundant copies.

## 7. Public archive policy

The GitHub repository mirrors safe historical material such as screenshots, artwork, HTML/CSS research pages, CSV/JSON indexes, documentation, and URL crawls. Classic SubSeven malware archives and potentially weaponized source packages are represented by metadata, provenance, historical filenames, release association, archive/Wayback references and hashes when verified—not by executable downloads.

See:

- [`../data/google-drive-master-inventory.csv`](../data/google-drive-master-inventory.csv)
- [`../data/drive-historical-packages.csv`](../data/drive-historical-packages.csv)
- [`../data/curated-historical-urls.csv`](../data/curated-historical-urls.csv)
- [`../data/raw/`](../data/raw/)
