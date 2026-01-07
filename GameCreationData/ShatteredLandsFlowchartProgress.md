Shattered Lands Flowchart\Progress from scratch to Alpha stage.
Progress indicators:

* ✅ **Completed**
* 🔄 **In Progress**
* 🕓 **Not Started Yet**


---

## **🧱 PHASE 1: FOUNDATION (Pre-Production & Core Setup)**

🔄 **1. Game Concept & Documentation**

* Define core gameplay loop, world design, faction/class system, attribute framework.
* Document races, lore, leveling systems, resource mechanics (mana, fatigue, momentum).

**2. Unreal Engine 5 Project Setup**

* Create new UE5 project (blank or MMO starter kit if available).
* Enable key plugins: Online Subsystem, Gameplay Tags, Enhanced Input, etc.
* Set up source control (e.g., Git + Git LFS).

**3. Initial Folder & Module Structure**

* Standardize folder layout: `/Plugins`, `/Core`, `/Characters`, `/World`, `/UI`, `/Systems`.
* Create a modular plugin template for systems: combat, attributes, inventory, etc.

---

## **🧠 PHASE 2: CORE SYSTEMS DEVELOPMENT (Engine-Ready Architecture)**

**1. Character System**

* C++ Plugin: Attributes, leveling, stat caps, fatigue, stamina, class framework.
* Blueprint Integration: Creation screen, preview stats.
* Data-Driven: Use DataAssets for race/class templates.

**2. Input & Movement**

* Set up Enhanced Input system (C++) for modular binding support.
* Blueprint UI for keybinding and movement option toggles.

**3. Combat System**

* C++ Plugin for hit detection, damage resolution, stance logic, and Momentum.
* Blueprint layer: animations, visual hit feedback, UI triggers.

**4. Inventory & Equipment**

* C++ Plugin: Item structure, weight, durability, sockets.
* Blueprint: Drag-and-drop inventory UI, tooltip overlays.

**5. UI Framework**

* UMG Blueprints: Health bars, hotbars, chat, quest log, inventory.
* Backend: C++ data sync, update triggers, animation handling.

---

## **🌐 PHASE 3: NETWORKING & MULTIPLAYER SETUP**

**1. Multiplayer Framework**

* C++ base: Dedicated server, client authority, replicated variables.
* Test: Movement, damage, chat, inventory sync across clients.

**2. Account & Character Management**

* External DB (MySQL/Postgres) or Unreal SaveGame DB bridge.
* Plugin: Login auth, character select/create, data persistence.

**3. Party & Threat Systems**

* Plugin: Threat calculations, group targeting logic.
* Blueprint: Group frames, threat indicators.

---

## **🧩 PHASE 4: WORLD BUILDING & AI**

**1. Procedural/Hand-Built Zone Prototypes**

* Use Landscape, Foliage, Water, World Partition.
* Setup Level Streaming and World Composition.

**2. AI Prototypes**

* Behavior Trees + Blackboards.
* C++ plugin logic: patrols, aggro, group response.
* Blueprint layer: AI perception visualization, debug controls.

**3. NPC & Quest System**

* Plugin: Quest objectives, state tracking, reward system.
* Blueprint: Dialogue UI, map markers.

---

## **🧪 PHASE 5: INTERNAL PLAYABLE BUILD**

**1. Core Loop Integration**

* Player can: create character → spawn in world → accept quest → fight enemies → level up → gain loot.

**2. Stability Testing**

* Unit tests for core plugins.
* Blueprint failover cases.
* Network desync/recovery handling.

**3. Internal Debug & GM Tools**

* Spawn entities, grant items, teleport.
* Log capture, error output, performance benchmarks.

---

## **🧪 PHASE 6: CLOSED ALPHA TEST PREP**

**1. Alpha Build Branch**

* Create an alpha testing branch with tagged version.
* Disable unfinished features behind dev flags.

**2. Installer & Patching**

* Build deployable installer or launcher.
* Auto-update system prototype (e.g., via Amazon S3 + manifest).

**3. Alpha Feedback Tools**

* In-game bug report UI.
* Logging to server + client.

**4. Internal/Invite-Only Closed Alpha**

* Small test group (friends, developers, QA).
* Focus: major systems integration, crash/logic bugs, server performance.

---

## **Optional Tools to Build Alongside**

* **Metrics Collector Plugin**: Track time spent in combat, map movement heatmaps.
* **Localization/Strings DB**: If targeting multilingual support.
* **Modular Expansion Framework**: Base plugin to register new classes, abilities, gear types by external mods.

---

Would you like this converted into a **text-only indented hierarchy** or a visual flowchart next? Or should I break it into tasks for project management software like Trello or Notion?
