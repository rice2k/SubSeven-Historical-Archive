# Websites and Wayback History

This page reconstructs the historical SubSeven/Sub7 web footprint from public references plus Google Drive URL-crawl preservation.

## Domain evolution overview

### `come.to/subseven`

An early vanity/redirect-style URL associated with SubSeven references. Because redirect services could change destinations over time, preserved captures should be interpreted by capture date rather than treated as a stable canonical host.

Wayback lookup:

- https://web.archive.org/web/*/http://come.to/subseven

### `subseven.slak.org`

An early host cited in period material and later histories.

Wayback lookup:

- https://web.archive.org/web/*/http://subseven.slak.org/

### `sub7.net`

One of the major classic project/community domains.

The Drive crawl `_sub7_net_all_urls.txt` preserves a broad set of paths and hostnames associated with `sub7.net`. A smaller `_sub7_net_zip_links.txt` preserves historical package-name/path records. The archive uses the former to reconstruct site history and the latter as package-distribution metadata without converting it into a live malware download directory.

Wayback lookup:

- https://web.archive.org/web/*/http://sub7.net/
- https://web.archive.org/web/*/http://www.sub7.net/

Drive evidence includes old package-path names corresponding to releases such as 1.0, 1.9, 1.9 Apocalypse, 2.1.4, an XP-labeled 2.1.4 package and 2.2.

### `sub-7.net`

Alternate/related historical domain found in later references and preservation material.

Wayback lookup:

- https://web.archive.org/web/*/http://sub-7.net/

### `sub7crew.org`

The Drive crawl shows that `sub7crew.org` functioned as much more than a single project homepage. Preserved historical paths include:

- `/downloads.html`
- `/downloads/`
- `/help.shtml`
- `/reference.shtml`
- `/irc.shtml`
- `/ircbots.html`
- `/subseven.shtml`
- `/sub7list.shtml`
- `/gallery/`
- `/images/`
- `/ubb/`
- `/cgi-bin/s7forum/ultimatebb.cgi`
- mailing-list archive endpoints under `/cgi-bin/mojo/mojo.cgi`
- member areas including `~azzazzin`, `~fc`, `~mistahq`, and `~qroject`

The crawl also preserves old interface assets such as GIF/JPG buttons, tabs, logos, banners, CSS and JavaScript.

Wayback lookup:

- https://web.archive.org/web/*/http://sub7crew.org/
- https://web.archive.org/web/*/http://www.sub7crew.org/

### `s7help.sub7crew.org`

A help/documentation subdomain present in the Drive URL crawl.

Wayback lookup:

- https://web.archive.org/web/*/http://s7help.sub7crew.org/

### `sub7files.com`

A release/documentation distribution site referenced in surviving period material.

Wayback lookup:

- https://web.archive.org/web/*/http://sub7files.com/

### `sub7legends.net`

A later preservation/revival domain associated with Legends-era community history.

Wayback lookup:

- https://web.archive.org/web/*/http://sub7legends.net/

## `sub7crew.org` site structure recovered from Drive

### Main navigation / content areas

The URL crawl contains evidence for classic content categories such as:

- news
- downloads
- help/reference
- SubSeven-specific pages
- IRC
- forums
- mailing lists
- gallery
- links
- member pages
- tutorials

### Mailing list

The crawl preserves endpoints whose query strings identify both a generic `sub7crew` list and a `SubSeven_Official_Mailing_List` archive. These are useful evidence for reconstructing the community/support ecosystem even when individual messages are not locally preserved.

### Forums

Historical UBB/Sub7 forum endpoints appear in the crawl, including `cgi-bin/s7forum/ultimatebb.cgi` and related UBB assets.

### IRC

`irc.shtml` and `ircbots.html` appear in the crawl, supporting the role of IRC as part of the community/support scene around the site.

### Gallery and interface assets

The crawl preserves filenames for:

- old logos
- navigation button images
- tab images
- header images
- gallery screenshots
- CSS files
- GIF/JPG interface elements

These filenames are valuable for future Wayback recovery because individual archived assets can often be located even when a complete page capture renders badly.

## Member-area evidence

The crawl contains user/member directories under `sub7crew.org`, including paths for:

- `~azzazzin`
- `~fc`
- `~mistahq`
- `~qroject`

These areas included personal pages, utilities, tutorials, links, scene material and Sub7-adjacent content. The archive records their existence and safe historical page paths. Executable/tool package paths are treated as metadata-only.

## Historical package-path evidence

The URL crawls preserve old filenames/paths that help identify how releases and add-ons were distributed. Examples include records corresponding to:

- SubSeven 1.0
- SubSeven 1.9
- 1.9 Apocalypse
- 2.1.4
- 2.1.4 XP
- 2.2
- Legends

The `sub7crew.org` crawl also contains scene-era add-on/tool package names in member directories. These names are useful for historical reconstruction but are not surfaced as live executable-download links in this public archive.

## How to use the Wayback Machine for this archive

For historical research, use capture-index URLs rather than assuming one snapshot date is authoritative. A useful pattern is:

`https://web.archive.org/web/*/http://HOST/PATH`

This lets a researcher compare multiple captures and determine when a page, filename or site design first/last appears.

For image/CSS recovery, searching the exact historical asset path can be more successful than loading the parent page. The Drive crawl therefore preserves path-level evidence even where the original HTML is missing.

## Drive-preserved screenshot records

Drive search found several later screenshots or browser captures related to this research, including duplicate Wayback reference images and a GitLab/source-reference capture. They are documented in [`drive-source-provenance.md`](drive-source-provenance.md). Duplicate screenshots are not uploaded repeatedly.

## Data files

- [`../data/curated-historical-urls.csv`](../data/curated-historical-urls.csv) — normalized historical path catalog
- [`../data/website-history.csv`](../data/website-history.csv) — domain evolution summary
- [`../data/google-drive-master-inventory.csv`](../data/google-drive-master-inventory.csv) — Drive provenance

The raw crawl sources remain represented by metadata/provenance and curated safe paths because the original lists mix ordinary web assets with historical malware-package URLs.
