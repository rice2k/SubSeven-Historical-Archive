# Link and Image Audit

This page records the repository's navigation/image checks so broken paths are easier to detect and repair as the archive grows.

**Last manual/API audit:** 2026-09-09

## Repository-local navigation

The main README currently links to repository files that exist on the `main` branch, including:

- `docs/version-and-file-history.md`
- `data/version-feature-matrix.csv`
- `docs/features-and-interface.md`
- `docs/sub7files-about-2001.md`
- `docs/websites-and-wayback-history.md`
- `docs/source-code-and-development.md`
- `docs/people-and-community.md`
- `docs/social-history.md`
- `docs/local-archive-findings.md`
- `docs/archive-source-provenance.md`
- `docs/research-gaps.md`
- `data/historical-file-inventory.csv`
- `data/historical-package-records.csv`
- `data/file-inventory.csv`
- `data/curated-historical-urls.csv`
- `data/secondary-source-index.csv`
- `index.html`

The visual `index.html` also references repository-local documentation/data targets using paths that exist on `main`.

## Repository-hosted images

The following image paths exist in `assets/images/` and are suitable for stable relative linking from README/docs:

| Path | Used for |
|---|---|
| `assets/images/classic-subseven-interface.jpg` | Main README/visual-site classic controller image |
| `assets/images/subseven-art-gallery.png` | Historical artwork/icon gallery |
| `assets/images/wayback-sub7-reference.jpg` | Wayback/website research reference |

Canonical gallery: [`image-gallery.md`](image-gallery.md)

## Verified GitHub repositories / profiles

These GitHub destinations were checked through GitHub's repository/search API during the 2026-09-09 audit:

| Link | Audit result |
|---|---|
| https://github.com/DarkCoderSc/SubSeven | Public repository exists; default branch `main` |
| https://github.com/NoorahSmith/DarkCoderSc-SubSeven | Public repository exists; default branch `main` |
| https://github.com/pawpatrolryder/SubSeven-delphi-rat- | Public repository exists; default branch `main` |
| https://github.com/rutherfordwj/SubSevenLegacy | Public repository exists; default branch `main` |
| https://github.com/xillwillx | Account exists; public repositories are discoverable. This is a profile link, not a specific SubSeven repository. |

Repository names alone do not establish historical authenticity; provenance is handled separately in [`source-code-and-development.md`](source-code-and-development.md).

## Other critical research links checked

The following research destinations responded during the audit:

- https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094
- https://www.sans.org/white-papers/958
- https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377
- https://www.malware.museum/releases/subseven/
- https://www.bsidesct.org/archives/2023/
- https://gitlab.com/illwill/sub7

## Wayback reliability rule

Wayback replay links can fail temporarily even when captures exist. For historically important pages, the archive should provide both:

1. an **exact dated snapshot** when known; and
2. a **capture-index fallback** so researchers can choose another archived date.

For the February 2001 Sub7Files About page:

- Exact snapshot: https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml
- Capture index: https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml

The same rule should be used for `sub7.net`, `sub7crew.org`, `sub7files.com`, `sub7legends.net`, early vanity URLs, images, CSS and individual historical paths.

## Local checker

The repository includes [`../tools/check_internal_links.py`](../tools/check_internal_links.py), which scans Markdown/HTML relative links, local image references and HTML anchors.

Run from the repository root:

```text
python tools/check_internal_links.py
```

The script intentionally does not fetch external websites. External archival/research links require a separate periodic audit because domains and archive replay behavior change over time.

## Maintenance rule

When renaming or moving any file:

- update README navigation;
- update `index.html` links;
- update cross-links in `docs/`;
- update image paths in `docs/image-gallery.md`;
- run the local checker;
- recheck any external source link that was edited.
