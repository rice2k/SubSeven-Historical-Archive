# Link and Image Audit

This page records the repository's navigation, image, and source-link checks so broken paths are easier to detect and repair as the archive grows.

**Last GitHub/API audit:** 2026-09-09

## Current result

**PASS for the primary repository navigation and all seven repository-hosted image paths checked through the GitHub API.**

The `main` tree contains the README, visual site, docs, datasets, manifests, local-link checker, archive material, CSS, and the hosted image files referenced by the main research pages.

---

## Main README navigation

The primary README targets below are present on `main`:

- `docs/version-and-file-history.md`
- `data/version-feature-matrix.csv`
- `docs/features-and-interface.md`
- `docs/sub7files-about-2001.md`
- `docs/websites-and-wayback-history.md`
- `docs/source-code-and-development.md`
- `docs/people-and-community.md`
- `docs/social-history.md`
- `docs/local-archive-findings.md`
- `docs/repository-file-status.md`
- `docs/image-gallery.md`
- `docs/link-audit.md`
- `docs/preservation-and-research-access.md`
- `docs/archive-source-provenance.md`
- `docs/research-gaps.md`
- `data/historical-file-inventory.csv`
- `data/historical-package-records.csv`
- `data/restricted-artifacts-manifest.csv`
- `data/file-inventory.csv`
- `data/curated-historical-urls.csv`
- `data/secondary-source-index.csv`
- `index.html`

Image metadata is also maintained in [`../data/screenshot-index.csv`](../data/screenshot-index.csv).

The visual `index.html` uses repository-relative paths for local content rather than fragile commit-specific URLs.

---

## Repository-hosted images

All of the following paths were confirmed present on `main`:

| Repository path | Main use | Status |
|---|---|---|
| `assets/images/classic-subseven-interface.jpg` | representative classic controller / README hero | **verified present** |
| `assets/images/subseven-art-gallery.png` | historical artwork/icon reference | **verified present** |
| `assets/images/illwill-sub7-source-provenance.jpg` | classic-source provenance capture | **verified present** |
| `assets/images/wayback-sub7-reference.jpg` | Wayback/website research reference | **verified present** |
| `assets/images/wayback-sub7-org-2001-retry.jpg` | Sub7.org archive-retry record | **verified present** |
| `assets/images/wayback-sub7crew-org-2001-retry.jpg` | Sub7Crew.org archive-retry record | **verified present** |
| `assets/images/wayback-otenet-sub7-files-2002-retry.jpg` | users.otenet.gr archive-retry record | **verified present** |

Canonical gallery: [`image-gallery.md`](image-gallery.md)

Machine-readable visual map: [`../data/screenshot-index.csv`](../data/screenshot-index.csv)

### Relative-path rule

From the repository root / README:

```text
assets/images/filename.ext
```

From a document under `docs/`:

```text
../assets/images/filename.ext
```

For a clickable Markdown/HTML image, link the image to its local file or its source page rather than leaving it as a dead decorative image.

---

## Badge/link rule

README Shields badges are wrapped in `<a href="...">` elements. The badge graphic itself is supplied by Shields/GitHub Camo, while the click target is a repository page/data file.

Current badge destinations include:

| Badge | Destination |
|---|---|
| Historical archive | `docs/archive-source-provenance.md` |
| Coverage | `docs/version-and-file-history.md` |
| Classic language: Delphi / Object Pascal | `docs/source-code-and-development.md` |
| Purpose | `docs/safety-and-scope.md` |
| Duplicates | `data/historical-file-inventory.csv` |
| Screenshots | `docs/image-gallery.md` |
| Files hosted vs not hosted | `docs/repository-file-status.md` |

This fixes the earlier behavior where the shield itself rendered correctly but did not navigate anywhere when clicked.

---

## External screenshot reliability

The gallery contains external version-specific screenshots from Malware Museum, a Wikimedia Commons SubSeven 2.2 README screenshot, and modern Legacy screenshots from the official `DarkCoderSc/SubSeven` repository.

Each externally hosted visual includes a **source-page fallback**. If GitHub Camo caches a failed image request or the direct media URL changes, the researcher can still open the release/source page.

External image/source status is tracked separately from repository-hosted status in `data/screenshot-index.csv`.

---

## Verified public GitHub source/reference links

These GitHub destinations were checked through GitHub's repository API:

| Link | Type | Result |
|---|---|---|
| https://github.com/DarkCoderSc/SubSeven | official modern Legacy repository | **exists; public; `main`** |
| https://github.com/NoorahSmith/DarkCoderSc-SubSeven | Legacy fork | **exists; public; `main`** |
| https://github.com/pawpatrolryder/SubSeven-delphi-rat- | Legacy fork | **exists; public; `main`** |
| https://github.com/rutherfordwj/SubSevenLegacy | Legacy fork | **exists; public; `main`** |
| https://github.com/xillwillx | researcher/profile reference | profile reference; not treated as a specific SubSeven repository |

The archive labels forks as forks rather than presenting every similarly named repository as an independent original source.

---

## Important non-GitHub research links

Current major research destinations include:

- `https://gitlab.com/illwill/sub7`
- `https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094`
- `https://www.sans.org/white-papers/958`
- `https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377`
- `https://www.malware.museum/releases/subseven/`
- `https://www.bsidesct.org/archives/2023/`

External sites can change independently of this repository. Historical claims should therefore retain source titles/URLs and, where possible, repository-hosted screenshots or Wayback fallbacks.

---

## Wayback reliability rule

Wayback replay can fail temporarily even when captures exist. Important historical pages should expose both:

1. an **exact dated snapshot** when known; and
2. a **capture-index fallback**.

For the February 2001 Sub7Files About page:

- Exact: `https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml`
- Capture index: `https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml`

The same method is used for important `sub7.net`, `sub7crew.org`, `sub7files.com`, `sub7legends.net`, early vanity URLs, images, CSS, and page records.

The hosted `*-retry.jpg` files are explicitly labeled as **archive-research attempt evidence**, not screenshots of the original website design.

---

## Local internal-link checker

The repository contains [`../tools/check_internal_links.py`](../tools/check_internal_links.py). It validates Markdown/HTML relative links, local images, and HTML fragment targets without fetching external websites.

Run from a local repository clone:

```text
python tools/check_internal_links.py
```

External image URLs, archive replay, and third-party research sites require separate periodic checking because they can change independently of the GitHub repository.

---

## Maintenance checklist

When a file or image is added, moved, renamed, or replaced:

1. update README navigation when appropriate;
2. update `index.html` if it links to the item;
3. update cross-links under `docs/`;
4. update `docs/image-gallery.md` for visual changes;
5. update `data/screenshot-index.csv` for image hosting/source changes;
6. keep duplicate historical records labeled rather than silently deleting provenance;
7. run `python tools/check_internal_links.py` from a local clone;
8. recheck edited GitHub source/fork URLs;
9. use both exact and capture-index Wayback links for important archived pages.
