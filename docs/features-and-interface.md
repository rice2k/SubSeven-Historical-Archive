# Features, interface, and application layout

This page documents the **historical function categories and user-interface organization** of SubSeven without reproducing a deployment/abuse manual. Exact menus and labels varied across versions, so features are tied to the broader classic family unless a version-specific source establishes otherwise.

## Classic controller layout

The classic Windows controller used a dense, utility-style GUI typical of Delphi/VCL applications of the period. Surviving screenshots show an operator application organized around a target connection and groups of remote-management actions rather than a command-line-only workflow.

Common visual elements across later controller generations included:

- connection/target information;
- a tree/list or grouped navigation area;
- status and activity information;
- panels/dialogs for individual remote-management functions;
- file/path selectors;
- process/window lists;
- system information displays;
- surveillance/media-related dialogs;
- prank/visual-effect controls;
- server/configuration settings handled separately through EditServer in documented releases.

See the repository's recovered screenshot at `assets/images/classic-subseven-interface.jpg`.

## Major historical feature categories

### System information

SubSeven could query information about a remote Windows system. Historical catalogs describe retrieval of host/system details and information useful for managing a connected machine.

### File management

The controller family included remote file-management functions. At a high level these covered browsing remote storage and performing normal file operations. This archive does not reproduce steps for using file access to steal or plant data.

### Process and application management

Later versions exposed information about running processes/applications and remote-control functions associated with them. Modern SubSeven Legacy deliberately retains benign process-management concepts in a non-malicious recreation.

### Window / desktop interaction

Classic feature lists contain numerous controls affecting the Windows desktop and visible UI. Some became memorable because they were used as pranks, such as manipulating visible Windows elements or producing visual effects.

### Remote terminal / command execution category

Classic RAT functionality included remote execution/control capabilities. The archive records that this category existed but does not provide commands, persistence steps, or abuse recipes.

### Keyboard / input-related functions

Historical SubSeven descriptions include keyboard/input monitoring or manipulation functions. Because those capabilities can enable credential theft or covert surveillance, this archive documents them only as a historical capability category.

### Screen / webcam surveillance

Later 1.x/2.x feature catalogs include screen-viewing and webcam-related capabilities. Their presence helped make SubSeven notable during the period when consumer webcams were becoming more common.

### Audio / media

Some versions exposed audio/media-related functionality. The modern Legacy project also includes the BASS audio library as a dependency, but that modern dependency should not be projected backward as proof of the exact classic implementation.

### Password / credential-related functions

Historical descriptions of SubSeven contain password-recovery/theft capabilities. These are significant to malware history and detection, but operational procedures are intentionally omitted from this archive.

### Network / connection information

SubSeven needed to deal with the realities of late-1990s/early-2000s home connectivity: changing IP addresses, dial-up connections, and consumer NAT/network setups. The 2.2 package is documented with `sin.exe`, a Static IP Notifier utility, illustrating the project's surrounding connection-management ecosystem.

### ICQ integration

ICQ was central to the era's communication culture. Legends-era package documentation names `ICQMAPI.dll`, and historical material also describes ICQ-related notification/integration behavior. The DLL is cataloged by name rather than redistributed.

### Prank / novelty controls

SubSeven became culturally memorable partly because its controller mixed serious remote-control functions with prank-like actions. Historical descriptions include things such as changing desktop behavior, manipulating visible UI elements, opening the CD tray, and displaying messages/effects. These features helped it spread by word of mouth but did not make the underlying unauthorized-access use benign.

## EditServer

`EditServer.exe` is one of the most important applications for understanding package architecture. In later documented branches it acted as the server configuration/editor side of the package.

Historically, builder/editor interfaces allowed release-specific server properties to be configured before the server component was produced/distributed. This archive records the existence and purpose of those settings but does not reproduce evasion, persistence, credential-theft, or delivery instructions.

## SubSeven 2.2 package layout

The 2.2 release is particularly useful because multiple surviving sources identify four principal executable names:

| File | Historical role |
|---|---|
| `sub7.exe` | Controller/client |
| `EditServer.exe` | Server editor/configuration application |
| `server.exe` | Remote server component |
| `sin.exe` | Static IP Notifier utility |

A separate 2.2 manifest is in `data/manifests/2-2-files.csv`.

## 2.2 plugin architecture

Period documentation describes SubSeven 2.2 as supporting plugin-style extensions implemented through DLLs, with SDK/plugin work discussed around the release. This mattered historically because it separated optional functionality from the monolithic core.

The archive does **not yet have a trustworthy complete list of the original distributed plugin DLL filenames**. Rather than inventing names from later third-party packs, that remains listed in `docs/research-gaps.md`.

## Legends package layout

Surviving Legends-era documentation names:

| File | Historical role |
|---|---|
| `SubSeven.exe` | Controller/client |
| `server.exe` | Remote server component |
| `EditServer.exe` | Server editor/configuration application |
| `ICQMAPI.dll` | ICQ support/integration library |

See `data/manifests/2-1-5-legends-files.csv`.

## Modern SubSeven Legacy interface

SubSeven Legacy deliberately recreates a **2.2.x-style UX theme** using Delphi/VCL/WinAPI while removing classic malicious features. Its official README lists benign remote-administration functions such as:

- File Manager;
- Process Manager;
- Remote Terminal;
- Windows Session Manager;
- direct socket/TLS communication;
- multithreading/concurrency.

The modern codebase is split into Viewer, Service, Tray, Helper, CertGen, SecureDesktop, Shared, Resources and Setup areas. That architecture is documented in `data/manifests/legacy-0-1-alpha-files.csv`.

## What still needs primary screenshots

The visual archive would benefit from dated, version-specific screenshots of:

- early 1.0–1.4 interfaces;
- 1.9 and 1.9 Apocalypse;
- 2.0 and 2.1;
- GOLD, M.U.I.E, BONUS and DEFCON 8 editions;
- EditServer dialogs by version;
- SIN;
- plugin management screens;
- Legends controller and editor;
- original website download/help pages alongside each release.

Those are tracked as preservation/research targets rather than filled with unlabeled images from unknown versions.
