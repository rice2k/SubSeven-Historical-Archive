# Contributing to the SubSeven Historical Archive

Contributions are welcome when they improve the historical record, provenance, screenshots, documentation or defensive understanding of SubSeven/Sub7.

## Useful contributions

Good research contributions include:

- original or period-correct screenshots with a source URL and date;
- Wayback captures of `sub7.net`, `sub7crew.org`, `sub7files.com`, `sub7legends.net` or related historical pages;
- original READMEs, FAQs, help text, release notes or mailing-list announcements;
- version-specific feature evidence;
- package filenames, file sizes and published hashes;
- EXE/DLL/project-file inventories;
- Delphi compiler/component clues;
- source-code provenance evidence;
- corrections to release dates or version relationships supported by a source;
- old logos, buttons, tabs, banners, CSS or other website assets with provenance;
- duplicate/alternate-file relationships;
- period security papers, books, news reports or vendor analyses.

## What to include with a finding

Please provide as much of the following as possible:

1. **Version / branch** — for example `1.9 Apocalypse`, `2.2`, `2.1.5 Legends` or `Legacy`.
2. **Artifact type** — screenshot, README, HTML page, source reference, EXE/DLL metadata, release announcement, etc.
3. **Source URL** — original URL, Wayback URL, repository URL or publication page.
4. **Date** — release date, capture date, publication date or best-known timeframe.
5. **What it demonstrates** — describe the specific historical claim supported by the artifact.
6. **Filename / size / hash** — when relevant and known.
7. **Duplicate relationship** — whether it appears identical to something already cataloged.
8. **Confidence** — confirmed, likely, secondary-source claim or unresolved.

## Screenshot rules

A screenshot should be assigned to a specific release only when its source supports that identification. Similar-looking interfaces are not enough by themselves.

For visual material, record:

- source page;
- direct image URL when available;
- version claim;
- capture/publication date;
- whether it is original-period, later preservation, retrospective or modern Legacy;
- what can actually be seen in the image.

The current visual map is in:

- [`docs/image-gallery.md`](docs/image-gallery.md)
- [`docs/version-screenshot-status.md`](docs/version-screenshot-status.md)
- [`data/screenshot-index.csv`](data/screenshot-index.csv)

## Evidence and confidence

The archive prefers primary or contemporary evidence, but later preservation catalogs can still be useful when clearly labeled.

Do not silently turn a repeated claim into a fact. When sources conflict, preserve the disagreement and cite both sides.

See [`docs/archive-source-provenance.md`](docs/archive-source-provenance.md).

## Safety boundary

This repository is for digital preservation, cybersecurity history and defensive research.

Please do **not** submit:

- runnable classic SubSeven malware binaries;
- archives intended to distribute classic payloads;
- directly buildable weaponized classic RAT source trees;
- deployment, persistence, evasion or concealment instructions;
- master/universal password values;
- operational command/protocol strings intended to control compromised systems;
- instructions for unauthorized access.

Historical filenames, hashes, sizes, screenshots, readmes, public source-provenance links and defensive descriptions are appropriate.

## Before opening a new finding

Check the following first:

- [`docs/version-and-file-history.md`](docs/version-and-file-history.md)
- [`data/file-inventory.csv`](data/file-inventory.csv)
- [`data/historical-file-inventory.csv`](data/historical-file-inventory.csv)
- [`data/screenshot-index.csv`](data/screenshot-index.csv)
- [`docs/research-gaps.md`](docs/research-gaps.md)

Duplicates are welcome as **provenance records**; just label them as duplicates rather than presenting them as a new release.
