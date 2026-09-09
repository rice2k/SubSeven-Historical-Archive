# Preservation and Research Access

This repository is intended to preserve the historical record around SubSeven / Sub7 for malware-history research, defensive cybersecurity education, software-history research, and digital preservation.

## What is preserved directly

The repository can directly preserve and expose research-safe material such as:

- screenshots, artwork, icons, banners, old website captures, and interface images;
- historical HTML/CSS/JavaScript pages that are non-operational research artifacts;
- README files, changelogs, FAQs, mailing-list excerpts, documentation, and release notes;
- URL crawls and Wayback path indexes;
- version matrices, file manifests, EXE/DLL filename inventories, release/package metadata, and duplicate relationships;
- checksums/hashes and byte sizes when known;
- source-code provenance notes, repository links, screenshots, and project-tree documentation;
- modern non-malicious SubSeven Legacy source references and documentation;
- research notes that explain what each component or feature did historically.

## Historical executable/source artifacts

Classic SubSeven packages and buildable classic RAT source trees are historically important, but this public repository does not redistribute runnable payloads or readily recoverable weaponized source. Instead, the repository preserves the research value through:

- exact filename;
- version/edition association;
- size;
- duplicate/alternate-copy status;
- hashes when independently verified;
- original site/path or archive reference;
- package/application role;
- associated README/documentation references;
- source-code provenance and repository history;
- screenshots and static directory/file listings where available.

The canonical list is maintained in `data/restricted-artifacts-manifest.csv`.

## If original samples are removed from local storage

Deleting the original malware archives means this repository will preserve the **historical evidence and research metadata**, but not a recoverable copy of the executable malware itself. Researchers can still identify releases, compare versions, follow contemporary documentation, inspect screenshots, study source provenance, compare file layouts, and locate public historical references.

For long-term preservation of original live malware samples, use an appropriately controlled malware-research or institutional preservation environment with access controls and handling procedures rather than a general public source-code repository.

## Duplicate policy

Duplicates are not silently discarded from the historical record. Each duplicate or alternate package name is retained as a separate metadata row and points to the canonical artifact relationship. This is useful for reconstructing how files were copied, renamed, re-packed, mirrored, or preserved over time.
