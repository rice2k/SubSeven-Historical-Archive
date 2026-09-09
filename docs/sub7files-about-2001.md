# Sub7Files.com “About SubSeven” — February 2001 historical source

> **Primary archive target:** [20 February 2001 Wayback capture of `www.sub7files.com/about/index.shtml`](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)

This page is one of the most important period references for reconstructing what SubSeven looked like immediately before the public 2.2 release in March 2001. The Wayback replay is not always reliably renderable today, so this archive does **not** invent missing HTML or claim to reproduce the original page verbatim.

A contemporary SANS/GIAC paper, **“What is SubSeven? Giving away control of your machine!”**, cites the same `sub7files.com/about/index.shtml` page (accessed 13 February 2001) and explicitly attributes its SubSeven **2.1 feature list** to that source. That makes the paper a valuable contemporary corroborating record when the original archived page does not replay cleanly.

Research links:

- [Wayback — exact 2001-02-20 Sub7Files About capture](https://web.archive.org/web/20010220171345/http://www.sub7files.com/about/index.shtml)
- [SANS/GIAC — What is SubSeven? Giving away control of your machine!](https://www.giac.org/paper/gsec/453/subseven-giving-control-machine/101094)
- [Sub7Files.com capture index](https://web.archive.org/web/*/http://www.sub7files.com/)

## What the period description says SubSeven was

The contemporary SANS/GIAC description presents SubSeven as a Windows remote-access/backdoor program with three broad functional areas:

1. **File control** — remotely viewing and managing files and folders.
2. **Monitoring / surveillance** — observing the screen and user activity and collecting information from the remote Windows system.
3. **Network / remote control** — managing connections and using network-oriented functions from the connected machine.

That framing is useful because it describes SubSeven as much more than a single “trojan executable.” It was a controller/server ecosystem with a Windows GUI, configuration tools and a large set of modules exposed through one operator interface.

## Reconstructed SubSeven 2.1 feature families

The contemporary feature list is very long. Rather than reproducing it verbatim, the archive groups its functions by purpose. The items below describe **what the historical controls did**, not instructions for using them against a system.

### Connection and address tools

The 2.1 controller included address-book and target-management concepts, host/IP lookup utilities and connection-notification options. These existed to help an operator keep track of remote systems during an era when many home users were on dial-up connections and frequently changed IP addresses.

Historical significance: this helps explain why later releases also included connection-notification utilities and why ICQ, IRC and email appeared so often in Sub7 documentation.

### System information

The controller could display a broad profile of the remote Windows machine: computer/user identity, Windows version/platform, important folders, screen resolution, processor information, storage/drive information and other environment details.

Historical significance: this turned the GUI into a remote inventory console and gave later malware analysts a recognizable set of host-enumeration behaviors.

### File Manager

The file-management interface exposed remote drives, directories and files and supported common management actions such as locating, transferring, renaming, deleting, viewing or launching files.

Historical significance: file management was one of the core functions present across much of the SubSeven lineage and is one of the easiest features to recognize in surviving screenshots and feature catalogs.

### Process, application and window management

SubSeven could enumerate running programs/windows and expose controls that changed the state or visibility of selected windows and applications.

Historical significance: later releases and modern SubSeven Legacy both retain recognizable process/application-management concepts, although Legacy intentionally omits the classic malicious functions.

### Screen and desktop control

The feature list includes screen-capture and desktop-viewing functions plus controls that affected visible Windows user-interface elements.

Historical significance: remote screen viewing helped SubSeven resemble legitimate remote-administration software at the interface level, while its unauthorized use and surveillance functions made the classic program malware.

### Keyboard, clipboard and user-activity monitoring

The classic controller exposed keystroke and clipboard-monitoring categories and other user-activity observation features.

Historical significance: these functions created serious credential/privacy risks and are a major reason SubSeven is studied as surveillance malware rather than merely a prank tool.

### Webcam and audio

Period feature records include webcam-related monitoring and audio/recording capabilities in parts of the classic lineage.

Historical significance: these functions became particularly notorious as webcams and multimedia hardware became more common on consumer PCs.

### Password / account information

The 2.1-era feature catalog includes password/account-recovery and cache-related capabilities.

Historical significance: these functions elevated SubSeven from remote-control software to credential-stealing malware. This archive documents their existence but does not reproduce procedures for extracting credentials.

### Messaging and communication

The controller offered chat/message and speech-related novelty or communication features, allowing visible interaction with the person at the remote machine.

Historical significance: these controls contributed to SubSeven’s reputation as both a serious RAT and a “hacker toy,” because the same interface mixed covert surveillance with conspicuous pranks.

### ICQ / IRC / instant-messaging ecosystem

SubSeven’s feature history intersects heavily with ICQ and IRC, and later documentation also mentions other instant-messaging observation features.

Historical significance: these services were central to the late-1990s/early-2000s scene. SubSeven 2.1 is widely associated with IRC-control support, while later package documentation names `ICQMAPI.dll` in the Legends era.

### Network and service functions

The period list includes networking utilities, redirection/proxy-style concepts and service-oriented functions.

Historical significance: by the 2.2 era, contemporary reporting specifically highlighted broader networking capabilities and a more modular architecture. These features also made infected systems useful as intermediaries in larger abuse campaigns.

### Prank / novelty controls

SubSeven exposed numerous controls that altered the visible desktop or hardware behavior: messages, mouse/keyboard effects, screen/UI changes and well-known novelty actions such as opening the CD tray.

Historical significance: the prank controls made the program memorable and helped it spread culturally, but they existed beside credential theft, surveillance and remote execution capabilities.

### Client preferences and server configuration

The 2.1 feature list also documents extensive client preferences and server-configuration options. The classic package family later exposed these through a dedicated **EditServer** application.

Historical significance: customization was a defining part of SubSeven’s architecture. This archive records the categories of configuration that existed but intentionally does not reproduce stealth, persistence or delivery recipes.

## What changed when 2.2 arrived

The February 2001 About page is best understood as a snapshot of the mature **2.1 generation** just before SubSeven 2.2. Contemporary March 2001 reporting describes 2.2 as a substantial transition rather than a simple point release:

- a redesigned/more flexible user interface;
- a revamped server-customization system;
- improved Windows NT/2000 behavior;
- loss of backward compatibility between the new client and older servers;
- broader network functionality;
- plugin/modular extension architecture and SDK discussion.

See:

- [The Register — “New SubSeven Trojan unleashed,” 13 March 2001](https://www.theregister.com/security/2001/03/13/new-subseven-trojan-unleashed/855377)
- [SANS — “SubSeven 2.2: New Flavor of an Old Favorite,” 29 May 2001](https://www.sans.org/white-papers/958)

## Evidence rule

This archive distinguishes three levels of certainty:

- **Period-confirmed:** explicitly supported by contemporary documentation or a surviving release record.
- **Retrospectively confirmed:** supported by later preservation/research sources that identify a specific version.
- **Not yet confirmed for that version:** known elsewhere in the family but not safely projected backward or forward without evidence.

That rule is especially important for early 1.x releases, where surviving screenshots and package manifests are much less complete than for 2.1, 2.2 and Legends.
