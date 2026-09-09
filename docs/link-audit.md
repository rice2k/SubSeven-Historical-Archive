# Link and Image Audit

This page records the repository's navigation, image, and GitHub-link checks so broken paths are easier to detect and repair as the archive grows.

**Last GitHub/API audit:** 2026-09-09

## Current result

**PASS for the primary repository navigation and repository-hosted image paths checked through the GitHub API.**

The repository tree on `main` contains the README, visual site, docs, datasets, manifests, local-link checker, archive material, CSS, and the image files referenced by the main pages.

## Main README navigation

The primary README links below resolve to files present on `main`:

- `docs/version-and-file-history.md`
- `data/version-feature-matrix.csv`
- `docs/features-and-interface.md`
- `docs/sub7files-about-2001.md`
- `docs/websites-and-wayback-history.md`
- `docs/source-code-and-development.md`
- `docs/people-and-community.md`
- `docs/social-history.md`
- `docs/local-archive-findings.md`
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

The visual `index.html` also references repository-local documentation/data targets by relative path rather than by fragile branch-specific absolute URLs.

## Repository-hosted images

The following image files are physically present in `assets/images/` and the relative paths used by README/docs match the repository tree:

| Repository path | Main use | Status |
|---|---|---|
| `assets/images/classic-subseven-interface.jpg` | Main README and visual-site classic controller image | **verified present** |
| `assets/images/subseven-art-gallery.png` | Historical artwork/icon gallery | **verified present** |
| `assets/images/wayback-sub7-reference.jpg` | Wayback/website research reference | **verified present** |

Canonical gallery: [`image-gallery.md`](image-gallery.md)

### Relative-path rule

From the repository root / README, use:

```text
assets/images/filename.ext
```

From a page inside `docs/`, use:

```text
../assets/images/filename.ext
```

This keeps images rendering correctly on normal GitHub Markdown pages and avoids dependency on a raw-content host URL.

## Verified public GitHub source/reference links

These destinations were checked against GitHub's repository API during the latest audit:

| Link | Type | Result |
|---|---|---|
| https://github.com/DarkCoderSc/SubSeven | official modern Legacy repository | **exists; public; `main`** |
| https://github.com/NoorahSmith/DarkCoderSc-SubSeven | Legacy fork | **exists; public; `main`** |
| https://github.com/pawpatrolryder/SubSeven-delphi-rat- | Legacy fork | **exists; public; `main`** |
| https://github.com/rutherfordwj/SubSevenLegacy | Legacy fork | **exists; public; `main`** |
| https://github.com/xillwillx | researcher/profile reference | profile reference; not treated as a specific SubSeven repository |

The archive identifies forks as forks rather than presenting every similarly named repository as an independent historical source.

## Important non-GitHub research links

The archive currently points researchers to resources including:

- `https://gitlab.com/illwill/sub7`
- `https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094`
- `https://www.sans.org/white-papers/958`
- `https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377`
- `https://www.malware.museum/releases/subseven/`
- `https://www.bsidesct.org/archives/2023/`

External sites can change independently of this repository. A research URL being temporarily unavailable should not cause a repository-local image or navigation failure.

## Wayback reliability rule

Wayback replay links can fail temporarily even when captures exist. Important historical pages therefore should expose both:

1. an **exact dated snapshot** when known; and
2. a **capture-index fallback**.

For the February 2001 Sub7Files About page:

- Exact: `https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml`
- Capture index: `https://web.archive.org/web/*/http://www.sub7files.com/about/index.shtml`

The same approach is used for important `sub7.net`, `sub7crew.org`, `sub7files.com`, `sub7legends.net`, early vanity-URL, image, CSS, and page records.

## Full repository tree check

The recursive `main` tree was checked through GitHub's API during this audit. It confirms the presence of the core structure:

```text
README.md
index.html
assets/styles.css
assets/images/
docs/
data/
data/manifests/
data/raw/
archive/fan-pages/
tools/check_internal_links.py
```

## Local internal-link checker

The repository contains [`../tools/check_internal_links.py`](../tools/check_internal_links.py). It validates Markdown/HTML relative links, local images, and HTML fragment targets without fetching external websites.

Run from a local clone of the repository root:

```text
python tools/check_internal_links.py
```

The current ChatGPT execution environment cannot resolve `github.com` through its container network, so a fresh clone-and-run was not possible during this audit. The GitHub connector/API was used instead to validate the repository tree, primary internal targets, hosted image paths, and named GitHub repository links.

## Maintenance checklist

Whenever a file is renamed, moved, or replaced:

1. update the README quick-navigation table;
2. update `index.html`;
3. update cross-links under `docs/`;
4. update `docs/image-gallery.md` for image changes;
5. keep duplicate historical records labeled rather than silently deleting provenance;
6. run `python tools/check_internal_links.py` from a local clone;
7. recheck edited GitHub source/fork URLs;
8. provide both exact and capture-index Wayback links for important archived pages.
