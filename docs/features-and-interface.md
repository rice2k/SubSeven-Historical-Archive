# SubSeven Feature Encyclopedia and Interface Guide

This page explains what the major SubSeven/Sub7 features **did historically**, where they appear in the release lineage, and why they mattered. It is intentionally written as a malware-history/defensive reference rather than an operating manual.

For exact per-version status, use [`../data/version-feature-matrix.csv`](../data/version-feature-matrix.csv).

## How SubSeven worked at a high level

Classic SubSeven followed a **controller / server** model:

1. The **controller/client** was the Windows GUI used by the remote operator.
2. The **server** was the remote component running on the other Windows system.
3. Later packages used **EditServer** as a separate configuration/editor application for the server package.
4. Some branches added companion utilities or support DLLs, such as `sin.exe` in 2.2 and `ICQMAPI.dll` in Legends-era material.
5. Version 2.2 introduced a more explicitly modular/plugin-oriented architecture.

The controller presented remote functions through menus, trees, lists, dialogs and status panels. The exact organization changed substantially across the 1.x, Apocalypse, 2.0/2.1 and 2.2 visual generations.

## Interface generations

### 1.0–1.4 — early red interface

Developer-retrospective material describes the earliest public releases as using a predominantly red visual design. These builds established the controller/server concept and rapidly accumulated remote-management and surveillance functions.

### 1.5–1.9 — blue/purple “Fatsie” identity

Version 1.5 is an important visual marker. The more recognizable blue/purple Sub7 look and “Fatsie” identity belong to this later 1.x generation rather than the first 1.0-era interface.

### 1.9 Apocalypse — experimental redesign

Apocalypse was a named redesign rather than just another point build. Later developer history describes it as an important visual/structural bridge toward the 2.0/2.1 family.

### 2.0 / 2.1.x — mature classic controller

The 2.1 line became the best-known classic interface generation: a dense utility-style Windows GUI with a very large remote-management feature set.

### 2.2 — modular redesign

Contemporary reporting describes a more flexible UI and revamped server-customization mechanism. 2.2 also broke client compatibility with older servers and emphasized modular/plugin support.

### 2.1.5 Legends — return to the 2.1.x lineage

Legends is the late original-era release and uses 2.1.x numbering rather than continuing the 2.2 line.

### Modern Legacy — 2.2.x-inspired recreation

The modern DarkCoderSc/Sub7Crew Legacy project recreates a 2.2.x-style experience in Delphi while explicitly omitting classic malicious features.

---

# Core applications and components

## Controller / client

**What it was:** the operator-facing GUI. It kept connection information and exposed the various feature modules.

**Known executable names:**

- `sub7.exe` — documented in 2.2 material.
- `SubSeven.exe` — documented in Legends-era material.

**Why it mattered:** SubSeven’s unusually broad graphical controller made complex remote functions accessible without requiring a command-line-only workflow, which contributed to its popularity.

## Server component

**What it was:** the remote side of the classic controller/server architecture.

**Known later filename:** `server.exe`.

**Why it mattered:** the server’s existence is what made the classic package a remote-access trojan when installed without authorization. This archive describes its role but does not provide deployment or persistence instructions.

## EditServer

**What it was:** a server editor/configuration application in later classic releases.

**Known filename:** `EditServer.exe` / `editserver.exe`.

**What the interface historically controlled:** broad categories of server identity, connection/notification behavior, packaging and startup/customization settings.

**Why it mattered:** EditServer separated configuration from the main controller and made server customization a defining part of the SubSeven ecosystem.

## SIN — Static IP Notifier

**Known filename:** `sin.exe` in documented 2.2 material.

**What it did:** acted as a connection/address-notification utility in an era when home users frequently changed IP addresses.

**Why it mattered:** dial-up and dynamic addressing were practical problems for remote-access tools, so notification/address helpers became part of the surrounding ecosystem.

## `ICQMAPI.dll`

**Version evidence:** Legends-era package documentation.

**What it represented:** ICQ-related support/integration material.

**Why it mattered:** ICQ was central to the era’s communications culture, and SubSeven’s history repeatedly intersects with ICQ/IRC notification and account-related features.

## Plugin DLL system

**Version evidence:** 2.2 period documentation and contemporary reporting.

**What it was:** a modular extension concept intended to separate optional functionality from the core program and support an SDK/plugin ecosystem.

**Why it mattered:** 2.2’s plugin direction was a meaningful architectural departure from the earlier monolithic controller style. The exact complete list of original distributed plugin DLL filenames remains a research gap.

---

# Feature encyclopedia

## Address Book / target management

**What it did:** stored or organized connection entries so the controller could keep track of remote systems and associated connection details.

**Strongest version evidence:** mature 2.1-era feature documentation.

**Historical significance:** useful context for understanding how the GUI evolved from a single connection utility into a management console.

## Host lookup / IP information tools

**What they did:** exposed host/IP lookup and basic network-information functions inside the controller.

**Strongest evidence:** 2.1-era period feature list.

**Historical significance:** bundled network utilities reduced the need for separate tools and reflected the networking culture of the era.

## Connection notification

**What it did:** alerted the operator when a server became reachable/online using era-appropriate communication services such as ICQ, IRC or email.

**Strongest evidence:** mature 2.1-era documentation and later connection-notification utilities.

**Historical significance:** particularly relevant to dial-up and changing IP addresses.

## System Information

**What it did:** displayed information about the remote Windows environment — computer/user identity, Windows/platform information, important directories, screen characteristics, processor/storage information and other host details.

**Earliest confirmed family evidence:** early 1.x.

**Historical significance:** transformed the controller into a remote inventory console and provided information useful for deciding which other modules were applicable.

## File Manager

**What it did:** let the controller browse remote drives/directories/files and perform ordinary remote file-management actions such as transfer, rename, deletion, viewing/editing or launching a selected file.

**Earliest confirmed family evidence:** early 1.x.

**Historical significance:** one of the most persistent core features across the classic lineage and also retained in benign form by modern Legacy.

**Defensive significance:** unauthorized remote file access creates theft, alteration and disruption risk.

## File search / bookmarks / transfer queue concepts

**What they did:** supplemented the File Manager with ways to locate files, remember paths and manage transfers.

**Strongest evidence:** mature 2.1-era feature lists.

**Historical significance:** shows how far the GUI had evolved beyond a minimal send/receive utility.

## Process Manager

**What it did:** enumerated running processes and exposed process-management controls.

**Earliest confirmed family evidence:** early 1.x catalogs.

**Historical significance:** gave the remote operator insight into running software and became a standard RAT feature category. Modern Legacy retains a benign Process Manager.

## Application / Window Manager

**What it did:** listed active applications/windows and exposed controls affecting focus, visibility, enabled state or closure.

**Strong evidence:** mature 2.1 period list; explicitly represented in Legends-era feature cataloging.

**Historical significance:** one of the features that made SubSeven feel like an interactive Windows-control console rather than a purely hidden command channel.

## Remote Shell / Terminal

**What it did:** provided a remote command-execution/terminal category through the controller.

**Confirmed by:** 2.0 and later high-level feature catalogs.

**Historical significance:** greatly expanded administrative/control power. This archive records the capability but does not reproduce commands or abuse procedures.

**Modern Legacy:** retains a Remote Terminal as a benign administration feature.

## Remote Desktop / Screen Capture

**What it did:** captured or displayed the remote desktop, including full-screen and thumbnail-style viewing concepts in mature versions.

**Earliest confirmed family evidence:** early 1.x.

**Historical significance:** visually demonstrated the level of access and made surveillance/control immediately understandable to nontechnical users.

## Screen/desktop manipulation

**What it did:** altered visible desktop elements, display characteristics, wallpaper or other UI presentation.

**Strong evidence:** mature 2.1 feature documentation.

**Historical significance:** some controls had legitimate remote-administration analogues, while others were primarily disruptive or prank-oriented.

## Mouse controls

**What they did:** remotely influenced mouse movement/buttons or added novelty visual effects.

**Strong evidence:** mature 2.1 period documentation and older feature lists.

**Historical significance:** part of SubSeven’s distinctive mixture of serious remote control and conspicuous pranks.

## Keyboard / input controls

**What they did:** monitored or manipulated keyboard/input behavior.

**Strong evidence:** keylogging exists across much of the classic family; broader input controls are especially visible in mature feature lists.

**Defensive significance:** covert keyboard monitoring can expose credentials, private messages and other sensitive information.

## Keylogger

**What it did:** recorded keystrokes/user typing; some generations included offline/log-oriented collection concepts.

**Earliest confirmed family evidence:** early 1.x.

**Historical significance:** a major reason SubSeven is classified as credential/surveillance malware rather than merely a remote-prank tool.

## Clipboard Manager

**What it did:** exposed clipboard contents/control through the remote interface.

**Strong evidence:** mature 2.1 and later catalogs.

**Defensive significance:** clipboard contents may include passwords, messages or copied sensitive data.

## Password Recovery / cached account information

**What it did:** exposed password/account-data recovery categories associated with Windows and applications of the era.

**Earliest confirmed family evidence:** early 1.x.

**Historical significance:** greatly increased the security impact of infection.

**Archive boundary:** this repository documents the category but does not provide credential-extraction procedures.

## Registry Manager

**What it did:** allowed remote viewing/editing of Windows Registry information.

**Confirmed by:** at least 1.4 in surviving feature cataloging and later releases.

**Historical significance:** added deep Windows configuration/control and became a recurring RAT capability.

## Webcam Capture

**What it did:** accessed webcam imagery/video-related capture functionality where hardware was present.

**Confirmed by:** at least 1.8 in surviving release catalogs and throughout later classic branches.

**Historical significance:** became one of SubSeven’s most notorious privacy-invasive functions as webcams became common.

## Voice / microphone recording

**What it did:** captured audio from a remote system where supported.

**Evidence:** audio/voice-related features appear in early catalogs; Voice Recorder is explicitly cataloged in 2.2 and Legends.

**Historical significance:** expanded surveillance beyond screen/keyboard/webcam capture.

## Chat

**What it did:** opened or supported a text interaction channel with the remote user.

**Strong evidence:** mature 2.1 period list and older feature descriptions.

**Historical significance:** made some SubSeven sessions visibly interactive and fed its “hacker toy” reputation.

## Popup messages / questions

**What they did:** displayed user-visible dialogs/messages on the remote desktop.

**Historical significance:** commonly used for pranks or intimidation and visually demonstrated remote control.

## Text-to-speech

**What it did:** caused text to be spoken using available Windows speech functionality.

**Strong evidence:** mature 2.1 feature documentation.

**Historical significance:** another example of novelty functionality living beside serious surveillance features.

## Browser / URL-oriented controls

**What they did:** influenced browser/web behavior or opened web content on the remote desktop.

**Historical significance:** useful for pranks, forced navigation or visible demonstrations of control.

## Network Manager

**What it did:** displayed/manipulated network-connection information and exposed network-oriented functions.

**Strong evidence:** 2.1-era and later release catalogs.

**Historical significance:** helped evolve SubSeven from host control into a platform with network-proxy/relay potential.

## Port redirect / tunneling concepts

**What they did:** allowed network traffic to be relayed/redirection-oriented through the remote host.

**Strong evidence:** mature classic documentation; 2.2-era reporting emphasizes broader networking capability.

**Defensive significance:** an infected host could be abused as an intermediary. Operational configuration details are intentionally omitted.

## SOCKS/proxy functionality

**Version significance:** contemporary 2.2 reporting highlights proxy-style networking as part of the expanded network feature set.

**Historical significance:** made the remote host more useful as a network intermediary and is one reason 2.2 attracted defensive attention.

## Packet-sniffing / network observation

**Version significance:** contemporary 2.2 reporting discusses packet-sniffing capability.

**Historical significance:** extended surveillance from local user activity to network traffic.

## FTP/service functions

**What they did:** exposed file/service-oriented network capabilities from the remote host.

**Strong evidence:** mature classic descriptions.

**Historical significance:** contributed to the “remote administration suite” feel of the controller while creating obvious unauthorized-access risks.

## IRC control / IRC bot integration

**What it did:** integrated SubSeven control/notification concepts with IRC, a major communication platform of the period.

**Version significance:** 2.1 is strongly associated with the beginning of IRC-control support in later historical summaries.

**Historical significance:** IRC channels could act as coordination/notification infrastructure and tied SubSeven deeply to contemporary hacker/scene culture.

## ICQ integration / ICQ-related functions

**What they did:** used or interacted with ICQ for notification/account-related features.

**Version significance:** 2.1-era history and later Legends package evidence; `ICQMAPI.dll` is named in Legends material.

**Historical significance:** ICQ was one of the dominant instant-messaging platforms of the era.

## AIM / Yahoo / MSN messenger observation categories

**What they did:** mature feature lists include instant-messaging observation/spy categories for popular chat clients of the era.

**Historical significance:** illustrates how the program followed the communication habits of contemporary Windows users.

## Server restart / reconnect controls

**What they did:** controlled the remote server/session state and reconnection behavior.

**Strong evidence:** mature 2.1 period list.

**Historical significance:** part of normal remote-session management in the controller architecture.

## Client preferences

**What they did:** configured the local controller UI — colors, hints, local download directory, chat appearance and other operator-side preferences.

**Strong evidence:** 2.1 period feature list.

**Historical significance:** shows how polished/customizable the controller had become.

## Server customization / EditServer options

**What they did historically:** configured broad server/package identity, connection/notification and startup/customization behavior.

**Version significance:** mature 2.1 and especially 2.2 reporting describe extensive server customization; 2.2 is noted for a revamped mechanism.

**Archive boundary:** stealth, persistence and delivery settings are documented only as historical categories, not as a step-by-step configuration guide.

## Prank / “Fun” controls

These were not one feature but a collection of visible effects. Historical descriptions include things such as:

- opening/closing the CD tray;
- visible desktop/window changes;
- mouse effects;
- messages/chat;
- speaker/audio effects;
- hiding/showing interface elements;
- altering screen/display behavior.

**Historical significance:** these functions explain much of SubSeven’s cultural reputation as a “hacker toy.” They also helped obscure the fact that the same controller exposed serious credential, surveillance, filesystem and remote-execution capabilities.

---

# Version-specific feature landmarks

## Early 1.x

Core remote file, screen, system, process, credential/keylogging and prank functions developed rapidly. Registry management is confirmed by 1.4; the major 1.5 milestone is a visual redesign; webcam capture is confirmed by 1.8.

## 1.9 Apocalypse

The key landmark is the experimental redesign that foreshadowed the 2.x/2.1.x interface generation.

## 2.0

A major branch change; shell-access capability is explicitly represented in surviving feature catalogs.

## 2.1

The most fully documented mature classic feature generation before 2.2. The February 2001 Sub7Files About page and contemporary SANS/GIAC paper provide an unusually large period feature record.

## 2.1.1–2.1.4 named editions

GOLD, M.U.I.E, BONUS and DEFCON 8 are distinct preserved editions. Their broad feature family is clear, but the archive avoids inventing precise point-by-point deltas where original changelogs have not yet been recovered.

## 2.2

Major differences include a redesigned/more flexible interface, revamped server customization, improved NT/2000 compatibility, non-backward-compatible client, broader networking and plugin/SDK architecture. Confirmed package applications: `sub7.exe`, `EditServer.exe`, `server.exe`, `sin.exe`.

## 2.1.5 Legends

Late original-era 2.1.x release. Confirmed files include `SubSeven.exe`, `server.exe`, `editserver.exe` and `ICQMAPI.dll`; feature cataloging explicitly includes Voice Recorder and Application/Window Manager.

## Modern Legacy

The official modern recreation deliberately omits classic malicious features. Its documented benign functions include File Manager, Process Manager, Remote Terminal and Windows Session Manager, implemented in a modern Delphi project with separate Viewer/Service/Tray/Helper components.

---

# Research sources

- [Sub7Files About — exact 20 Feb 2001 Wayback target](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)
- [SANS/GIAC — What is SubSeven? Giving away control of your machine!](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)
- [SANS — SubSeven 2.2: New Flavor of an Old Favorite](https://www.sans.org/white-papers/958)
- [The Register — New SubSeven Trojan unleashed, 13 Mar 2001](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [Malware Museum — SubSeven release family](https://www.malware.museum/releases/subseven/)
- [Malware Museum — SubSeven 2.2](https://www.malware.museum/release/subseven/22/)
- [Malware Museum — SubSeven 2.1.5 Legends](https://www.malware.museum/release/subseven/215-legends/)
- [DarkCoderSc/SubSeven — modern Legacy source](https://github.com/DarkCoderSc/SubSeven)
