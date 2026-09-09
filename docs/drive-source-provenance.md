# Google Drive Source Provenance Map

This document records how the connected Google Drive material was interpreted for the public SubSeven / Sub7 Historical Archive.

## Why provenance matters

The Drive collection mixes several different kinds of material:

1. **Direct Sub7 preservation material** — files and folders explicitly named Sub7/SubSeven, old URL crawls, screenshots, release/package records, tutorial archives, checksum material and preserved web files.
2. **Duplicate preservation copies** — identical or near-identical files stored in more than one Drive folder or imported at different times.
3. **Secondary research exports** — bookmark collections, link directories and reports that contain Sub7 references among unrelated material.
4. **Modern fan/reconstruction material** — later HTML pages or images about Sub7 that are useful to the history but are not original 1999–2003 artifacts.
5. **Restricted malware packages** — historical archives whose names, sizes and provenance are historically important but whose executable payloads are not republished by this public repository.

The repository therefore preserves **metadata and provenance separately from executable content**.

## Direct Sub7 collections located in Drive

Multiple folders named `Sub7` and one `Other Sub7` folder were located during the Drive audit. One principal `Sub7` folder includes URL-crawl exports, a classic controller image and a small later `sub7.html` history/fan page. A larger preservation tree contains historical package records covering the classic release family.

### URL crawl exports

The following Drive artifacts are important primary preservation evidence for the old web presence:

| File | Size | Historical value |
|---|---:|---|
| `_sub7crew_org_all_urls.txt` | 548,749 bytes | Large crawl/index of historical `sub7crew.org` paths including site assets, help/reference pages, forums, mailing-list endpoints, IRC areas, member pages and historical download-path records. |
| `_sub7_net_all_urls.txt` | 65,336 bytes | Crawl/index of historical `sub7.net` paths. |
| `_sub7_net_zip_links.txt` | 1,305 bytes | Historical package-name/path evidence for releases hosted or linked from `sub7.net`; treated as metadata rather than a public malware download list. |
| `_sub7crew_org_zip_links.txt` | 119 bytes | Historical package URL evidence from `sub7crew.org`; record-only. |
| `_sub7crew_org_rar_links.txt` | 295 bytes | Historical RAR/add-on path evidence from `sub7crew.org`; record-only. |

The large crawls have duplicate Drive copies with different import/modified timestamps. The GitHub archive records one canonical copy in the master inventory and marks the others as duplicates rather than presenting them as separate historical sources.

## Release/package evidence found in Drive

The preservation tree contains named archives corresponding to many classic versions. The public archive records their filenames, byte sizes, Drive provenance and version association without redistributing their executable payloads.

Known records include:

- `ss.1.0-enc.rar`
- `ss.1.9.Apocalypse-enc.rar`
- `ss.1.9.Apocalypse-enc 2.rar`
- `ss.2.0-enc.rar`
- `ss.2.1.0-enc.rar`
- `ss.2.1.0-enc 2.rar`
- `ss.2.1.1-enc.rar`
- `ss.2.1.2-enc.rar`
- `ss.2.1.3-enc.rar`
- `ss.2.1.4-enc.rar`
- `ss.2.2.0-enc.rar`
- `sub7legends-enc.rar`
- `sub7legends-enc 2.rar`
- `SubSeven_2.3.rar`
- `s72.0.rar`
- `sub7_1_9.zip`
- `subseven20.zip`

Additional related archives include:

- `SubSeven And Windows XP.rar`
- `Sub7.net Default md5sum values.rar`
- `Tutorial_Sub7.rar`
- `Tutorial_Sub7_2.rar`
- `sub7-main.rar`
- `subpass.zip`
- `subpass 2.zip`
- `subuster.zip`

See [`../data/drive-historical-packages.csv`](../data/drive-historical-packages.csv) and [`../data/google-drive-master-inventory.csv`](../data/google-drive-master-inventory.csv) for the normalized inventory.

## Old website evidence recovered from the crawl

The `sub7crew.org` crawl preserves evidence for a much broader site than a single download page. Historical paths include:

- `downloads.html` and `downloads/`
- `help.shtml`
- `reference.shtml`
- `irc.shtml`
- `ircbots.html`
- `subseven.shtml`
- `sub7list.shtml`
- a SubSeven Official Mailing List archive endpoint
- UBB/Sub7 forum endpoints
- gallery JPG files
- old GIF/JPG navigation/interface assets
- CSS and JavaScript assets
- member areas such as `~azzazzin`, `~fc`, `~mistahq` and `~qroject`

The crawl also contains historical package and add-on filenames. Those names are useful for reconstructing the site and community ecosystem, but the public archive does not turn them into live executable download links.

## Visual material found in Drive

Drive search identified multiple screenshots and web-reference images associated with Sub7 research, including:

- `1698323969143.jpg` — preserved classic SubSeven interface image; duplicate copies exist.
- `art.png` — large SubSeven art/icon sheet used by the archive gallery.
- `web.archive.org-4bd740875f.jpg` — Wayback-related reference image; duplicate copies exist.
- `web.archive.org-e47480a787.jpg` — additional Wayback reference image; duplicate copies exist.
- `web.archive.org-5cad8207bd.jpg` — additional Wayback reference image; duplicate copies exist.
- `gitlab.com-80bbfaea50.png` / `.jpg` — source-repository/reference captures useful for documenting later source-code provenance.

Only unique, relevant visual records should be exposed in the public gallery. Duplicate image copies remain represented in the Drive inventory rather than being uploaded repeatedly.

## Modern `sub7.html` preservation artifact

Drive contains a small HTML page named `sub7.html` describing Sub7 history and linking later source/remake projects. Its content and timestamps identify it as a **modern fan/history artifact**, not an original 1999–2003 Sub7 Crew page. The archive preserves it under `archive/fan-pages/` with an explicit provenance warning.

It should not be cited as primary evidence for exact release dates, developer identity or historical claims unless those claims are independently corroborated.

## Secondary link/bookmark sources

Drive searches for `SubSeven`, `mobman` and `sub7crew.org` also return larger unrelated research collections such as:

- `links.md`
- large `README.md` link exports
- `links (7).html`
- `links_directory_pro.xlsx`
- `Rice_Master_Bookmarks.html`
- `favorites_7_8_26.html`
- `favorites_7_8_26_organized.html`
- `favorites_7_29_25.html`
- `bookmark_binder_report.html`

These are **secondary discovery sources**, not SubSeven artifacts by themselves. They are useful for finding additional URLs and historical references, but should not be copied wholesale into this repository because they contain large amounts of unrelated material.

## Public-treatment rules

Each Drive record is assigned one of these public treatments:

- **publish-safe** — screenshots, non-operational historical HTML, documentation, normalized research data.
- **metadata-only** — classic malware archives, executable payloads and archives containing them.
- **curated-links-only** — raw crawls containing a mixture of ordinary site history and old malware-package URLs.
- **duplicate** — redundant Drive copy represented by a canonical record.
- **secondary-source** — broad bookmark/link collections used for discovery but not copied wholesale.

This lets the repository remain a detailed historical and educational archive without becoming a distribution point for runnable classic SubSeven malware.
