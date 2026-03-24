
# Dungeon Ascension

A Modular Command-Line RPG Engine in Python

---

## Version History

* Current v4.5
* Next planned: v5

---

## Features

* Modular Python RPG engine
* Turn-based tactical combat
* Event-driven combat resolution
* State-driven combat (status effects)
* Data-driven item and ability templates
* JSON save persistence
* Equipment and inventory system
* Resource-based abilities (mana)
* Persistent status effects with duration and modifiers
* Mid-combat consumable usage
* Scalable effect system (supports stat-based scaling)

---

### v1 — Foundation

Established the primary gameplay loop, combat system, floor progression, persistence, and modular structure.

* Core automated combat
* Floor progression system
* XP and leveling system
* Persistent character saves
* Boss encounters
* Risk–reward floor regression on defeat

v1 proved the core loop was stable and replayable.

---

### v1.5 — Structural Refactor

Focused purely on architectural clarity and long-term scalability.

* Introduced `GameEngine` (centralized orchestration)
* Renamed `project.py` → `game.py`
* Encapsulated lifecycle management
* Separated exploration logic
* Save file version tagging
* Backward-compatible save loading
* Removed testing scaffolding
* Improved state ownership boundaries

No gameplay changes — structural evolution only.

---

### v2 — Equipment & Loot Expansion

Expanded the system into a full item-driven RPG foundation.

#### Core Additions

* Item hierarchy (`Item`, `Equipment`, `Consumable`)
* Inventory system with stacking rules
* Equipment slots and modifiers
* Loot generation system
* Rarity system with scaling and visuals

---

### v2.5 — Engine Stabilization

Focused on internal consistency and decoupling.

* Introduced `BattleResult`
* Combat became simulation-only
* UI handled by `GameEngine`
* Fixed persistence and reconstruction issues
* Unified item interfaces

---

### v3 — Ability & Resource System

Introduced tactical combat decisions.

* Ability system (data-driven)
* Resource system (mana)
* AbilityResult abstraction
* Expanded consumables (mana recovery)

---

### v3.5 — Event-Driven Combat Completion

Finalized combat architecture.

* Abilities produce structured events
* Combat resolves events centrally
* Unified mitigation pipeline
* Clean separation of “intent vs resolution”

Prepared the engine for status effects.

---

## v4 — Status Effects & State-Driven Combat

v4 introduces persistent combat states and completes the transition to a **state-driven combat model**.

---

### Status Effect System

* `StatusEffect` base class
* Turn lifecycle hooks:

  * `on_apply`
  * `on_turn_start`
  * `on_turn_end`
  * `on_expire`
* Duration-based persistence
* Safe iteration and cleanup

---

### Effect Types

#### Damage Over Time (DoT)

* Turn-based damage
* Non-stackable by default (refresh behavior)
* Duration-aware logging

#### Stat Modifiers

* Modify attack, defense, max HP dynamically
* Fully integrated into stat properties
* No permanent stat mutation

---

### Combat Integration

* Status effects applied via event system
* Effects processed each turn
* Fully compatible with:

  * damage mitigation
  * stat calculation
  * ability system

---

### Dynamic Stat System (Completed)

Stats now resolve from:

* Base stats
* Equipment
* Status effects

Ensures:

* No stat drift
* No desync
* Fully deterministic outcomes

---

### Combat Feedback Improvements

* Duration-aware logs
* Effect application and expiration messages
* Clear state transitions

---

### Architectural Outcome

Combat becomes **state-aware and persistent**, enabling:

* Ongoing effects
* Multi-turn strategy
* Extensible combat mechanics

---

## v4.5 — Combat Depth & System Refinement (Current)

v4.5 builds on v4 by improving **flexibility, usability, and system depth** without introducing feature bloat.

---

### Effect Scaling System

* Status effects can now scale using stats
* Supports:

  * stat-based potency (e.g. attack scaling)
  * multipliers
  * flat bonuses
* Aligns DoT and effects with ability system design

This unifies how **all combat values are calculated**.

---

### Mid-Combat Consumables

* Players can now use consumables during combat
* Integrated into combat menu
* Reuses inventory logic (no duplication of item behavior)

Adds tactical flexibility without breaking architecture.

---

### Combat Flow Improvements

* Cleaner integration between:

  * abilities
  * effects
  * consumables
* Improved player decision space
* Maintains deterministic resolution

---

### Design Philosophy Reinforced

v4.5 continues the project philosophy:

> **Deepen systems vertically before expanding horizontally**

No unnecessary features added — only meaningful system extensions.

---

## Current Architectural Philosophy

### Core Principles

#### 1. Separation of Responsibilities

* **Item** → Defines behavior
* **Inventory** → Stores and stacks
* **Player** → Orchestrates actions
* **Combat** → Resolves outcomes
* **GameEngine** → Controls flow

---

#### 2. Data-Driven Templates

* Abilities and items defined via templates
* Logic separated from data
* Enables safe scaling and balancing

---

#### 3. Dynamic Stat Architecture

Stats are derived, not stored.

Now includes:

* Base stats
* Equipment modifiers
* Status effects

---

#### 4. Event → State Evolution

* v3.5: Event-driven combat
* v4+: State-driven combat

The system now supports **persistent combat state** layered over event resolution.

---

#### 5. Object-Based Inventory

* Items stored as objects
* Supports future:

  * enchantments
  * metadata
  * unique instances

---

## Core Gameplay Loop

1. Create or load a character
2. Explore dungeon floors
3. Engage in turn-based combat
4. Use attacks, abilities, and consumables
5. Apply and manage status effects
6. Collect and equip loot
7. Gain XP and level up
8. Progress floors and defeat bosses

---

## Technical Structure

```
game.py              # GameEngine (flow control & UI)
combat.py            # Combat loop & resolution
abilities.py         # Ability system & event generation
ability_templates.py # Ability definitions (data layer)

status_effect.py     # Status effect system (state layer)

player.py            # Player logic, equipment, resources
character.py         # Base stats & effect processing
enemy.py             # Enemy definitions

inventory.py         # Inventory container
item.py              # Item classes
item_templates.py    # Item definitions
loot.py              # Loot generation

config.py            # Game balance values
save_load.py         # Persistence system

art.py               # ASCII/UI elements
data/                # Save files
requirements.txt     # Dependencies
```

---

## Combat System

* Turn-based combat
* Basic attacks, abilities, consumables
* Event-driven ability resolution
* State-driven status effects
* Dynamic stat computation
* Centralized damage mitigation
* Effect lifecycle management

Combat now functions as a **layered system**:

> Events → State → Resolution → Feedback

---

## Design Goals

Dungeon Ascension is evolving toward:

* Deep systemic mechanics
* Clean architecture
* Data-driven scalability
* Maintainable codebase
* Extensible RPG engine design

---

## Installation

```
pip install -r requirements.txt
```

---

## Running the Game

```
python game.py
```

If issues occur, delete old save data (`characters.json`).

---

## Dependencies

* colorama

---

## Project Origin

Originally developed as a CS50P final project.
Now evolved into a structured RPG engine.

---

## Closing Note

Dungeon Ascension now represents:

* System-first design
* Iterative refinement
* Strong architectural discipline

Each version deepens the foundation before expanding outward.

The dungeon grows deeper…

---

## License

GNU GPL v3

You are free to study, modify, and redistribute the code,
but any distributed derivative work must also remain open-source
under the same license.