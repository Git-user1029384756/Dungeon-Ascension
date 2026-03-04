
# Dungeon Ascension

A Modular Command-Line RPG Engine in Python

---

## Version History

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

### v2 — Equipment & Loot Expansion (Current)

v2 expands the dungeon prototype into a systemic RPG foundation.

This version introduces a full item ecosystem and loot architecture while preserving modular boundaries.

#### Implemented in v2

### Item System

* `Item` base class
* `Equipment` subclass
* `Consumable` subclass
* Polymorphic `use()` behavior
* Type-aware reconstruction via `item_from_dict()`
* Explicit `type` field in serialization
* Save/load compatibility per item type

Items now serialize and deserialize cleanly with type-aware reconstruction.

---

### Inventory System

* Inventory is a container of item objects (not a dict of counters)
* Consumables stack by `template_id`
* Equipment remains unique object instances
* Stacking logic handled inside `Inventory`
* Inventory handles storage only; items handle behavior

This structure supports future:

* Enchantments
* Durability
* Unique modifiers
* Metadata per item

---

### Consumable Mechanics

* Supports multiple effect types (`heal_flat`, `heal_percent`)
* Quantity-based stacking
* Prevents overheal
* Blocks usage at full HP
* Reduces quantity upon use
* Clean separation between effect logic and storage logic

---

### Equipment System

* Slot-based equipment system (`weapon`, `armor`)
* Equip/unequip mechanics
* Automatic swapping
* Equipment removed from inventory when equipped
* Equipment returned to inventory when unequipped
* Save/load persistence of equipped items

Equipment does not permanently mutate player stats.

---

### Dynamic Stat Recalculation

Player stats are computed dynamically from:

* Base stats
* Equipped item modifiers

Stats are exposed through properties (`max_hp`, `attack`, `defense`).

This prevents:

* Permanent stat drift
* Stacking bugs
* Unequip inconsistencies
* Save corruption issues

Combat reads computed stats directly from the player.

---

### Rarity System

* Equipment includes a `rarity` attribute
* Rarity-based modifier scaling
* Rarity-based name coloring
* Config-driven rarity configuration

Rarity is implemented structurally and visually, without overcomplicating loot weighting.

---

### Loot System

* Centralized `generate_loot()` function
* Category-based template pools (`consumables`, `equipment`)
* Data-driven templates (`item_templates.py`)
* Random category selection
* Random template selection within category
* All item creation routed through factory system

Loot generation is unified across future systems (combat, exploration, events).

---

## Current Architectural Philosophy

### Core Principles

#### 1. Separation of Responsibilities

* **Item** → Defines behavior
* **Inventory** → Stores and stacks
* **Player** → Orchestrates actions
* **Combat** → Owns damage calculation
* **GameEngine** → Controls high-level flow

No system mutates another system's internal structure directly.

---

#### 2. Data-Driven Templates

Items are defined via structured template pools.

This enables:

* Rapid content expansion
* Safe balancing
* Version-safe serialization
* Clear separation between logic and data

---

#### 3. Dynamic Stat Architecture

Stats are derived, not mutated.

This allows future expansion into:

* Advanced modifiers
* Status effects
* Buff/debuff systems
* Conditional effects

Without refactoring the stat core.

---

#### 4. Object-Based Inventory

Inventory intentionally stores objects instead of key-value counters.

This preserves future flexibility for:

* Unique enchantments
* Randomized modifiers
* Individual item state
* Metadata expansion

---

## Core Gameplay Loop (Current State)

1. Create or load a character.
2. Explore dungeon floors via randomized events.
3. Engage in automated combat.
4. Generate loot via centralized loot system.
5. Equip or store items.
6. Use consumables strategically.
7. Gain XP and level up.
8. Progress floors and face bosses.
9. Reset dungeon progression after completion.

---

## Planned v2.5 Refinements

- (future/planned)

No new gameplay systems will be introduced in v2.5.
---

## Technical Structure

```
game.py              # GameEngine orchestrator
art.py               # ASCII art and presentation mappings
player.py            # Player class and XP system
inventory.py         # Inventory container logic
item.py              # Item, Equipment, Consumable classes
item_templates.py    # Data-driven item definitions
loot.py              # Centralized loot generator
combat.py            # Turn-based combat logic
enemy.py             # Enemy and boss definitions
config.py            # Balance parameters
save_load.py         # Persistence layer
character.py         # Shared base for Player and Enemy
data/                # JSON save files
requirements.txt     # Dependencies
```

---

## Combat System

* Automated turn-based combat
* Combat owns damage calculation
* Dynamic stat resolution
* XP rewards
* Boss archetypes
* Floor-based difficulty scaling

Combat remains deterministic but extensible.

---

## Design Goals

Dungeon Ascension is evolving toward:

* Clean architectural boundaries
* Extensible systems
* Data-driven expansion
* Maintainable code structure
* Version-aware persistence
* Scalable RPG mechanics

The project is transitioning from game prototype to RPG engine foundation.

---

## Installation

Install dependencies:


`pip install -r requirements.txt`

---

## Running the Game

`python game.py`

if game does not run, try deleting the old data (`characters.json`).

---

## Dependencies

* colorama

(Defined in `requirements.txt`)

---

## Project Origin

Originally developed as the final project for CS50P.

The project has evolved into a structured system-driven RPG architecture.

---

## Closing Note

Dungeon Ascension now represents:

* Progressive refactoring
* Iterative system design
* Applied object-oriented architecture
* Long-term scalability thinking

Each version strengthens structural foundations before expanding mechanics.

The dungeon grows deeper...