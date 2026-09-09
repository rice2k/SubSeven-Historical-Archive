# SubSeven / Sub7 Image Gallery

This page is the canonical index for images that are physically hosted in this repository. The goal is to keep image links stable, identify what each image actually shows, and avoid silently reusing an image for the wrong version.

> **Image rule:** a screenshot is labeled with a specific SubSeven version only when the evidence supports that identification. Otherwise it is described more generally as classic-family, later-source, website/archive, or modern Legacy material.

## Repository-hosted images

### Classic SubSeven controller/interface

[Open the image file](../assets/images/classic-subseven-interface.jpg)

![Classic SubSeven controller/interface](../assets/images/classic-subseven-interface.jpg)

**Repository path:** `assets/images/classic-subseven-interface.jpg`

**Use in the archive:** representative classic controller/interface image. It is used on the main README and visual history page. It should not be assigned to an exact release unless additional provenance identifies the version.

---

### Historical SubSeven artwork / icon sheet

[Open the image file](../assets/images/subseven-art-gallery.png)

![SubSeven historical artwork and icon sheet](../assets/images/subseven-art-gallery.png)

**Repository path:** `assets/images/subseven-art-gallery.png`

**Use in the archive:** historical artwork/icon reference. Individual graphics may originate from different preservation contexts, so the sheet is presented as a visual archive rather than as one specific release screen.

---

### Wayback / website-reference image

[Open the image file](../assets/images/wayback-sub7-reference.jpg)

![SubSeven Wayback reference image](../assets/images/wayback-sub7-reference.jpg)

**Repository path:** `assets/images/wayback-sub7-reference.jpg`

**Use in the archive:** website/Wayback research reference. It is not presented as an original SubSeven application screenshot.

## Additional unique visual records documented in the preservation inventory

The local historical collection also records additional unique research screenshots, including:

- a GitLab `illwill/Sub7` source-repository capture showing the project tree and its “Source code for SubSeven 2.1.3” description;
- a `sub7crew.org` Wayback/retry reference image;
- a `sub7.org` Wayback/retry reference image;
- a `users.otenet.gr` Sub7 files/extras Wayback/retry reference image;
- duplicate-format or duplicate-copy versions of some of those screenshots.

Those records remain listed in [`../data/historical-file-inventory.csv`](../data/historical-file-inventory.csv) and [`local-archive-findings.md`](local-archive-findings.md). Duplicate copies are kept in the historical inventory instead of being presented as separate unique screenshots.

## Screenshot research priorities

The archive still needs strongly sourced, version-specific screenshots for:

- 1.0–1.4 early red-interface builds;
- 1.5–1.9 Fatsie-era builds;
- 1.9 Apocalypse;
- 2.0;
- 2.1;
- GOLD, M.U.I.E, BONUS and DEFCON 8 editions;
- 2.2 controller, EditServer, SIN and plugin-related screens;
- 2.1.5 Legends controller/EditServer;
- original `sub7.net`, `sub7crew.org` and `sub7files.com` page captures by date;
- modern SubSeven Legacy interface screenshots.

When a new image is added, record its source, capture date if known, historical interpretation, exact repository path, duplicate relationship, and confidence level.

## Link reliability

Repository-local image paths are checked automatically by:

- [`../tools/check_internal_links.py`](../tools/check_internal_links.py)
- [`.github/workflows/internal-link-check.yml`](../.github/workflows/internal-link-check.yml)

The workflow runs on pushes and pull requests so a renamed or deleted image cannot silently leave a broken README or documentation image link.
