# Archive Source Provenance Map

This document explains how historical files found locally and public research sources are interpreted inside the SubSeven / Sub7 Historical Archive.

## Why provenance matters

The preservation material mixes several different evidence classes:

1. **Direct Sub7 historical/preservation material** — old URL crawls, screenshots, package records, checksum material and preserved web files.
2. **Duplicate preservation copies** — same-name/same-size files retained in more than one local archive tree.
3. **Alternate/variant package names** — similar version labels whose byte identity has not yet been proven.
4. **Secondary research exports** — bookmark and link collections containing SubSeven references alongside unrelated material.
5. **Modern fan/reconstruction material** — later pages and images about Sub7 that are useful to the preservation story but are not original 1999–2003 artifacts.
6. **Restricted malware packages** — historically important classic archives represented by metadata instead of public runnable payloads.
7. **Public primary/secondary sources** — Wayback captures, contemporary security papers, period news reports, release catalogs and later source repositories.

The repository therefore separates **what an artifact is**, **where it came from**, **what it proves**, and **how confidently it can be tied to a version**.

## Evidence labels used in this archive

### Period-confirmed

A claim supported by a contemporary document, period website capture, period news report, release README or other evidence close to the actual release date.

Examples:

- the February 2001 `sub7files.com/about/index.shtml` source as corroborated by a contemporary SANS/GIAC paper;
- March 2001 reporting on the SubSeven 2.2 public release;
- period documentation identifying the 2.2 controller/editor/server/SIN package roles.

### Retrospectively confirmed

A claim supported by a later preservation catalog, developer retrospective, malware-history database or source repository whose provenance is independently described.

### Historical local-file record

A filename/size/archive relationship preserved locally. This proves that the preservation artifact exists, but does **not by itself** prove that every internal file, release date or feature claim associated with the name is original.

### Historical URL/path record

A path recovered from an old domain crawl. It proves that a URL string was associated with the archived site data, but does not guarantee that the resource was successfully captured, safe, or still downloadable.

### Duplicate

A repeated historical record retained intentionally. Duplicates are grouped and labeled rather than silently deleted.

### Research gap

A detail that is plausible or commonly repeated but is not yet supported strongly enough to be presented as settled fact for a specific version.

## Local historical collection

The canonical inventory is [`../data/historical-file-inventory.csv`](../data/historical-file-inventory.csv). It preserves every current SubSeven-specific local record, including duplicates.

Important source groups include:

- classic release archives from 1.0 through 2.2, Legends and later 2.3 continuation material;
- alternate 1.9/2.0 packages and ancillary archives;
- `sub7.net` and `sub7crew.org` URL/path crawls;
- classic controller imagery and artwork;
- Wayback research/reference images;
- a later GitLab source-provenance capture;
- a 2025 fan/history page preserved separately from original-era material.

## Duplicate and variant handling

The archive never equates “same version label” with “same bytes.”

Examples:

- `ss.1.9.Apocalypse-enc.rar` and `ss.1.9.Apocalypse-enc 2.rar` have the same recorded size and are labeled as a duplicate group.
- `ss.2.1.0-enc.rar` and `ss.2.1.0-enc 2.rar` are likewise retained as duplicate records.
- `sub7legends-enc.rar` and `sub7legends-enc 2.rar` are retained separately in the inventory.
- `ss.2.0-enc.rar`, `s72.0.rar` and `subseven20.zip` are associated with the 2.0 era but are **not** declared byte-identical without hash/content evidence.
- `subpass.zip` and `subpass 2.zip` are same-sized duplicate-name variants.

Image/crawl duplicates are handled the same way: one canonical public asset may be displayed, while all repeated records remain in the inventory.

## Website provenance

The large local path crawls are used to reconstruct old site structure, not to manufacture a new download directory.

### `sub7crew.org`

The crawl preserves evidence for:

- downloads;
- help/reference;
- news;
- IRC/IRC-bot pages;
- UBB/Sub7 forums;
- official mailing-list endpoints;
- galleries;
- navigation/interface graphics;
- member pages;
- historical package/add-on path names.

### `sub7.net`

The crawl preserves project/community paths and old release-package naming. A smaller package-path export supplies evidence for historical distribution filenames from several generations.

## The February 2001 Sub7Files About page

The exact Wayback target is:

- https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml

Because archive replay can be incomplete, the repository does not claim to reproduce missing page markup. A contemporary SANS/GIAC paper cites the same About page and attributes the SubSeven 2.1 feature list to it. That relationship is documented in [`sub7files-about-2001.md`](sub7files-about-2001.md).

## Public source-code provenance

The phrase “SubSeven source code” refers to several distinct things online and they are not merged together:

- **historical classic source provenance:** `illwill/sub7` on GitLab, described there as SubSeven 2.1.2/2.1.3-era source material;
- **modern non-malicious recreation:** `DarkCoderSc/SubSeven` on GitHub, the official SubSeven Legacy source repository;
- **forks/mirrors:** additional GitHub repositories preserved or rehosted by other users.

Repository names alone are not proof of original authorship. See [`source-code-and-development.md`](source-code-and-development.md).

## Secondary discovery sources

Broad bookmark/link exports are indexed in [`../data/secondary-source-index.csv`](../data/secondary-source-index.csv). They are discovery aids, not original SubSeven artifacts. SubSeven-specific links may be extracted from them while unrelated content stays outside this focused archive.

## Safety and historical completeness

“Complete” in this archive means complete **documentation and provenance**, not unrestricted redistribution of executable malware. Classic payloads may be represented by:

- exact historical filename;
- byte size;
- version association;
- duplicate relationship;
- old distribution-path evidence;
- archive/Wayback context;
- verified hashes when available;
- screenshots/readmes/documentation extracted safely;
- source-code provenance links where historically relevant.

This preserves the historical record while keeping the public repository suitable for defensive education and digital preservation.
