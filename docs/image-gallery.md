# SubSeven / Sub7 Image Gallery

This is the canonical index for images physically hosted in the repository. Every hosted image below uses a repository-relative path so it renders correctly on GitHub without depending on an external image host.

> **Image identification rule:** a screenshot is assigned to a specific SubSeven version only when the surviving evidence supports that identification. Otherwise it is labeled as classic-family, source-code research, website/archive, or modern Legacy material.

**Image-path audit:** 2026-09-09 — all three currently hosted image paths below were confirmed present on the `main` branch through GitHub's repository API.

---

## Classic SubSeven controller / interface

[Open full image](../assets/images/classic-subseven-interface.jpg)

[![Classic SubSeven controller/interface](../assets/images/classic-subseven-interface.jpg)](../assets/images/classic-subseven-interface.jpg)

**Repository path:** `assets/images/classic-subseven-interface.jpg`  
**Status:** verified present  
**Used on:** `README.md`, `index.html`, this gallery

**Historical use:** representative classic controller/interface image. It should not be assigned to one exact release until stronger provenance identifies the version.

---

## Historical SubSeven artwork / icon sheet

[Open full image](../assets/images/subseven-art-gallery.png)

[![SubSeven historical artwork and icon sheet](../assets/images/subseven-art-gallery.png)](../assets/images/subseven-art-gallery.png)

**Repository path:** `assets/images/subseven-art-gallery.png`  
**Status:** verified present

**Historical use:** artwork/icon reference containing preserved SubSeven-related visual material. Because individual graphics can come from different preservation contexts, it is presented as an archive sheet rather than one release screenshot.

---

## Wayback / website-reference image

[Open full image](../assets/images/wayback-sub7-reference.jpg)

[![SubSeven Wayback reference image](../assets/images/wayback-sub7-reference.jpg)](../assets/images/wayback-sub7-reference.jpg)

**Repository path:** `assets/images/wayback-sub7-reference.jpg`  
**Status:** verified present

**Historical use:** website/Wayback research reference. It is not presented as an original SubSeven application screenshot.

---

# Additional unique visual records in the historical inventory

The historical collection also records several distinct research screenshots that are not currently represented as separate public image files:

- an `illwill/Sub7` source-repository capture showing the source tree and its **“Source code for SubSeven 2.1.3”** description;
- a Sub7Crew.org Wayback/retry reference image;
- a Sub7.org Wayback/retry reference image;
- a `users.otenet.gr` Sub7 files/extras Wayback/retry reference image;
- duplicate-format or duplicate-copy versions of some of the above.

They remain documented in:

- [`../data/historical-file-inventory.csv`](../data/historical-file-inventory.csv)
- [`local-archive-findings.md`](local-archive-findings.md)
- [`archive-source-provenance.md`](archive-source-provenance.md)

Duplicate image records remain in the inventory rather than being silently discarded.

---

# Verified GitHub visual/source references

The following GitHub repositories are live and were checked through GitHub's repository API during the 2026-09-09 audit:

- [DarkCoderSc/SubSeven](https://github.com/DarkCoderSc/SubSeven) — official modern SubSeven Legacy repository
- [NoorahSmith/DarkCoderSc-SubSeven](https://github.com/NoorahSmith/DarkCoderSc-SubSeven) — fork
- [pawpatrolryder/SubSeven-delphi-rat-](https://github.com/pawpatrolryder/SubSeven-delphi-rat-) — fork
- [rutherfordwj/SubSevenLegacy](https://github.com/rutherfordwj/SubSevenLegacy) — fork

These are used as modern/reference material and are not treated as proof of the contents of every original 1999–2003 package.

---

# Screenshot research priorities

The archive still needs strongly sourced, version-specific screenshots for:

- 1.0–1.4 early red-interface builds;
- 1.5–1.9 Fatsie-era builds;
- 1.9 Apocalypse;
- 2.0;
- 2.1;
- GOLD, M.U.I.E, BONUS and DEFCON 8 editions;
- 2.2 controller, EditServer, SIN and plugin-related screens;
- 2.1.5 Legends controller/EditServer;
- original `sub7.net`, `sub7crew.org` and `sub7files.com` pages by date;
- modern SubSeven Legacy interface screenshots.

For each newly added image, record:

1. source URL / archive capture;
2. capture or release date when known;
3. exact repository path;
4. version identification and confidence;
5. duplicate relationship, if any;
6. what the screenshot visibly demonstrates.

---

# Link reliability

Repository-local image paths are intentionally relative:

- from root/README: `assets/images/...`
- from `docs/`: `../assets/images/...`

The repository includes:

- [`../tools/check_internal_links.py`](../tools/check_internal_links.py)
- [`link-audit.md`](link-audit.md)

Run from a local repository clone:

```text
python tools/check_internal_links.py
```

The checker validates local Markdown/HTML links, images, and HTML fragment targets. External research sites and Wayback captures are audited separately because they can change or replay intermittently even when the repository itself is correct.
