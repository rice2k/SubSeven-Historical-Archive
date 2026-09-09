# Raw Google Drive source records

The Drive preservation collection contains several raw URL-crawl/link-list files that are larger and less curated than the public tables:

| Drive file | Drive ID | Size | Public treatment |
|---|---|---:|---|
| `_sub7crew_org_all_urls.txt` | `1gFZp58rI7rhz9sbodkQg3kzMuQKsdOlw` | 548,749 B | indexed in curated website/history tables; full private source remains in Drive |
| `_sub7_net_all_urls.txt` | `1T-Y4BJpZY72im5afEZ7kfHLNLqea8sZM` | 65,336 B | indexed in curated website/history tables; full private source remains in Drive |
| `_sub7_net_zip_links.txt` | `1G31bApaIZIZPxbrQBE82Bz0mgiqueHlr` | 1,305 B | historical package-URL list; not republished as a live download index |
| `_sub7crew_org_rar_links.txt` | `1UR072XDX_X84_fLePdPxK6NSyMkDxXE8` | 295 B | historical package-URL list; not republished as a live download index |
| `_sub7crew_org_zip_links.txt` | `1SBgYB5g0vcrhhr16q5DrofYFdFyBbzBz` | 119 B | historical package-URL list; not republished as a live download index |

Duplicate copies with the same names/sizes were also found in another preservation tree and are recorded in `../google-drive-master-inventory.csv`.

The raw crawls contain ordinary pages/assets mixed together with old malware/package paths. To keep this public repository useful as a historical archive without functioning as a malware-download directory, the public material is normalized into:

- `../curated-historical-urls.csv`
- `../website-history.csv`
- `../resource-links.csv`
- `../google-drive-master-inventory.csv`

Nothing is deleted from the user's private preservation collection; this file documents the exact private source records and IDs used for the public research tables.
