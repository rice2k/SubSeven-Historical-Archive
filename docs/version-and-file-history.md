# Version and File History

This page ties each major SubSeven/Sub7 release family to the surviving package names, application names, file/DLL evidence, Google Drive preservation records, and old website records used by this archive.

> The classic packages described below are historical malware artifacts. The public repository documents them but does not redistribute runnable classic payloads.

## 1.x — original generation

### 1.0 — February 1999

The current chronology treats 1.0 as the beginning of the original public family. Drive preservation contains a record named `ss.1.0-enc.rar` and the `sub7.net` URL crawl preserves historical package-name references for `s7.1.0.zip` and `Sub7 v1.0.zip`.

Evidence classes:

- release chronology record
- Drive encrypted archive record
- old `sub7.net` package-path record
- later historical references

The exact original 1.0 internal file manifest remains incomplete and should not be inferred from 2.2/Legends packages.

### 1.1–1.8

These early releases appear in the release chronology and historical website/package references, but the Drive preservation set is less complete than for later versions. Where old package names survive, they are treated as evidence for distribution history rather than proof of an internal file list.

### 1.9 — June 1999

Drive contains `sub7_1_9.zip`, while the old `sub7.net` package-path list preserves references to `s7.1.9.zip`.

### 1.9 Apocalypse — August 1999

Drive contains two duplicate records:

- `ss.1.9.Apocalypse-enc.rar`
- `ss.1.9.Apocalypse-enc 2.rar`

The old `sub7.net` crawl also preserves a historical `s7.1.9.Apocalypse.zip` package path.

The duplicate encrypted archives are represented once in the canonical release record and separately in the Drive inventory so provenance is not lost.

## 2.0 — September 1999

Drive preservation includes:

- `ss.2.0-enc.rar`
- `s72.0.rar`
- `subseven20.zip`

These names show that more than one preservation/distribution naming convention existed. They should not automatically be assumed to be byte-identical without hash confirmation.

## 2.1 generation

### 2.1 / 2.1.0

Drive contains duplicate records for:

- `ss.2.1.0-enc.rar`
- `ss.2.1.0-enc 2.rar`

### 2.1.1 GOLD

Drive contains `ss.2.1.1-enc.rar`.

The GOLD name is preserved in later release catalogs and historical references. Exact package composition should be derived from contemporaneous manifests/readmes when available, not copied backward from 2.2.

### 2.1.2 M.U.I.E

Drive contains `ss.2.1.2-enc.rar`. The old `sub7.net` crawl also preserves a `Sub7 Muie.zip` historical path.

### 2.1.3 BONUS

Drive contains `ss.2.1.3-enc.rar`.

A later GitLab repository claims historical Sub7 source provenance around the 2.1.2/2.1.3 era. The public archive links the repository as a provenance source but does not mirror a buildable classic malware source tree.

### 2.1.4 DEFCON 8

Drive contains `ss.2.1.4-enc.rar`. Historical `sub7.net` path evidence includes names corresponding to 2.1.4 and a 2.1.4 XP package.

This branch is important for Windows-version compatibility history, but the archive keeps package-path evidence distinct from confirmed internal manifests.

## 2.2 — March 2001

This is one of the best-documented classic branches.

Drive preservation includes:

- `ss.2.2.0-enc.rar`

The old website crawl preserves multiple 2.2 package-name/path records, including historical paths containing `s7.2.2.0.zip` and `ss22.zip`.

Surviving period documentation supports the following later-package components:

| File/application | Historical role |
|---|---|
| `sub7.exe` | Operator/controller application in documented 2.2 material. |
| `server.exe` | Server component. |
| `EditServer.exe` | Server configuration/builder-side application. |
| `sin.exe` | Static IP Notifier utility identified in surviving records. |
| plugin DLL system | 2.2 documentation describes optional plugin-style modular extension support. Exact originally distributed plugin DLL names remain incomplete. |

See [`../data/manifests/2-2-files.csv`](../data/manifests/2-2-files.csv).

## 2.1.5 Legends — February 2003

Drive preservation includes duplicate records:

- `sub7legends-enc.rar`
- `sub7legends-enc 2.rar`

The `sub7crew.org` crawl preserves a historical `sub7legends.zip` package path.

Surviving Legends-era documentation supports these associated names:

| File/application | Historical role |
|---|---|
| `SubSeven.exe` | Controller/client naming in Legends-era material. |
| `server.exe` | Server component. |
| `EditServer.exe` | Configuration/builder-side application. |
| `ICQMAPI.dll` | ICQ-related support/integration component named by surviving package documentation. |

See [`../data/manifests/2-1-5-legends-files.csv`](../data/manifests/2-1-5-legends-files.csv).

## 2.3 continuation

Drive contains a record named `SubSeven_2.3.rar`.

The archive treats 2.3 separately from the original 1999–2003 development line because later continuation/community history is frequently mixed with the classic lineage. Exact authorship, date, provenance and relation to earlier source should remain explicitly sourced rather than assumed.

## Modern SubSeven Legacy

The DarkCoderSc/Sub7Crew `SubSeven` repository is treated as a separate modern, non-malicious recreation rather than as proof of the original 1999 package internals.

Its project/setup structure identifies components such as:

- Viewer application
- Windows service component
- Tray/service-controller application
- Helper application
- Certificate generator
- Secure Desktop DLL output
- x86/x64 BASS library dependency
- x86/x64 OpenSSL `libcrypto` / `libssl` dependencies
- Delphi/Object Pascal projects
- Inno Setup installer definitions

See [`../data/manifests/legacy-0-1-alpha-files.csv`](../data/manifests/legacy-0-1-alpha-files.csv).

## Related Drive archives

The Drive collection also contains historical/supporting packages whose names indicate compatibility, documentation, checksum or ancillary-tool purposes:

- `SubSeven And Windows XP.rar`
- `Sub7.net Default md5sum values.rar`
- `Tutorial_Sub7.rar`
- `Tutorial_Sub7_2.rar`
- `sub7-main.rar`
- `subpass.zip`
- `subpass 2.zip`
- `subuster.zip`

These are not silently assigned to a specific release without content-level evidence. Their names, sizes and Drive provenance are preserved in the master inventory.

## Evidence rule used by this archive

A filename appearing in a later package does **not** prove that the same filename existed in every earlier version. The archive therefore distinguishes:

- **confirmed package/component record**
- **historical package-path record**
- **Drive preservation filename**
- **later-source/remake component**
- **unresolved / research gap**

This prevents the common mistake of projecting the well-documented 2.2/Legends layout backward onto the less-documented 1.x line.
