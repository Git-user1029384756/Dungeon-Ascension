
# Dungeon Ascension

A Modular Command-Line RPG Engine in Python

---

## Version History

- Current v4
- Next planned: v4.5

---

## Features

- Modular Python RPG engine
- Turn-based tactical combat
- Event-driven combat resolution
- State-driven combat (status effects)
- Data-driven item and ability templates
- JSON save persistence
- Equipment and inventory system
- Resource-based abilities (mana)
- Persistent status effects with duration and modifiers

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

### v2.5 — Engine Stabilization & Combat Decoupling

v2.5 focuses on internal stability, structural tightening, and long-term maintainability.
No new gameplay systems were introduced.

## Major Refinements

## Combat Refactor

* Introduced `BattleResult` object
* Combat logic no longer prints directly
* Combat no longer applies loot
* Combat now functions as a pure simulation module
* Presentation handled exclusively by `GameEngine`

This decouples simulation from UI and progression logic.

---

## Player & XP Improvements

* XP system now supports multi-level progression in a single reward
* Level-up logic returns structured feedback
* Eliminated hardcoded XP subtraction values
* Improved separation between logic and presentation

---

## Inventory & Persistence Fixes

* Fixed encapsulation bug in `Inventory.from_list()`
* Ensured proper object reconstruction during load
* Confirmed v2 save compatibility
* Prevented silent inventory corruption

---

## Item Interface Standardization

* Unified item interface (all items now expose `rarity`)
* Removed type-based branching in GameEngine
* Strengthened polymorphic design across item subclasses

---

## Architectural Outcome

v2.5 transforms Dungeon Ascension from a functional prototype into a structurally disciplined RPG engine foundation.

The system is now:

* Simulation-safe
* Version-stable
* Internally consistent
* Ready for systemic expansion

---

## v3 — Combat Ability System & Resource Mechanics

v3 introduces player abilities, resource management, and expanded combat decision-making.

This version transitions combat from a purely automated system into a system where players actively choose abilities and manage resources.

---

## Ability System

* Introduced `Ability` class
* Data-driven `ability_templates`
* Ability factory creation from templates
* Ability resource costs
* Ability damage and healing effects
* Ability validation and resource checks before execution

Abilities are designed to remain fully data-driven and extensible.

---

## Ability Result System

* Introduced `AbilityResult` object
* Abilities now return structured results rather than mutating combat state directly
* Combat engine applies results after validation
* Enables future expansion into status effects and advanced mechanics

This maintains separation between ability logic and combat resolution.

---

## Resource System

* Player now supports dynamic resource pools
* Initial implementation includes `mana`
* Resources stored in flexible dictionary structure
* Abilities consume resources through the player resource API
* Resources automatically restore on level-up

This system is designed to support future resource types (stamina, rage, energy).

---

## Combat Expansion

Combat now supports:

* Basic attacks
* Ability usage
* Resource consumption
* Tactical decision making
* Ability-driven damage

---

## Consumable Expansion

Consumables now support additional effect types:

* `heal_flat`
* `heal_percent`
* `restore_mana` (new)

New consumables introduced:

* Minor Mana Potion
* Major Mana Potion

This allows players to recover combat resources without requiring character defeat.

---

## Architectural Outcome

v3 transforms Dungeon Ascension combat from a deterministic loop into a tactical resource-driven system.

The engine now supports:

* Data-driven abilities
* Resource-based mechanics
* Expanded consumable effects
* Tactical player decision making

All systems maintain strict modular boundaries and template-driven configuration.

---

## v3.5 — Combat Resolution Refactor

v3.5 focuses on stabilizing the internal combat architecture introduced in v3.

No new gameplay systems were added. Instead, this version refines how abilities interact with combat resolution and prepares the engine for future mechanics such as status effects.

### Major Refinements

#### Event-Driven Combat Resolution

* Ability execution now produces structured **events**
* Combat resolves events rather than abilities mutating targets directly
* Damage and healing are applied through a centralized resolver

This ensures that combat rules remain consistent regardless of ability complexity.

---

#### Ability Result Improvements

* Ability events now include explicit **source** and **target** references
* Supports future mechanics such as:
  * damage reflection
  * lifesteal
  * status effect triggers
  * conditional effects

---

#### Damage Mitigation Unification

* Combat now centralizes damage mitigation logic
* Both basic attacks and ability damage pass through the same combat rules
* Prevents divergence between attack damage and ability damage

---

#### Combat Architecture Outcome

v3.5 completes the transition to an **event-driven combat architecture**.

Abilities now describe **what happens**, while the combat engine determines **how it is resolved**.

This separation prepares the engine for future mechanics including:

* status effects (implemented in v4)
* conditional triggers
* advanced damage modifiers
* turn-based effect processing

(save compatible with v2 and above)

---

## v4 — Status Effects & State-Driven Combat (Current)

v4 introduces a full status effect system and completes the transition from event-driven combat into a state-driven combat model.

This version focuses on **deepening combat mechanics vertically** rather than expanding feature breadth.

---

## Status Effect System

* Introduced `StatusEffect` base class
* Effects persist across turns with duration tracking
* Effects execute through:
  * `on_apply`
  * `on_turn_start`
  * `on_turn_end`
  * `on_expire`
* Effects are processed in a stable iteration model (safe against mutation)

This establishes a flexible foundation for all future combat modifiers.

---

## Effect Types

### Damage Over Time (DoT)

* Implemented via `DamageOverTime`
* Applies damage each turn
* Non-stackable by default
* Refreshes duration instead of duplicating
* Displays remaining duration in combat logs

---

### Stat Modifiers

* Implemented via `StatModifier`
* Dynamically modifies:
  * attack
  * defense
  * max HP
* Fully integrated with the stat property system
* Effects apply and expire without permanently mutating base stats

---

## Status Effect Lifecycle Management

* Effects tick down each turn
* Expired effects are removed safely
* Expiration triggers explicit feedback (`on_expire`)
* All effect updates are centrally managed through `Character`

This ensures deterministic and debuggable behavior.

---

## Stacking & Refresh Logic

* Effects define their own stacking rules (`stackable`)
* Non-stackable effects refresh duration instead of stacking
* Prevents unintended exponential scaling
* Maintains combat readability and balance

---

## Combat Integration

* Status effects are applied through the existing event system
* `AbilityResult` now supports `status_effect` events
* Combat engine remains the sole authority for applying outcomes
* Status effects interact seamlessly with:
  * damage mitigation
  * stat calculation
  * turn processing

---

## Dynamic Stat Pipeline Completion

v4 completes the stat architecture by combining:

* Base stats
* Equipment modifiers
* Status effect modifiers

All resolved dynamically at runtime through property access.

This ensures:

* No stat drift
* No desynchronization
* No permanent mutation bugs

---

## Combat Feedback & Logging Improvements

* Introduced consistent combat log formatting
* Added explicit feedback for:
  * effect application
  * effect refresh
  * damage over time ticks
  * effect expiration
* Improved clarity of combat state transitions

---

## Architectural Outcome

v4 transforms combat into a **state-aware system** where entities carry ongoing effects that influence future turns.

The engine now supports:

* Persistent combat states
* Turn-based effect processing
* Dynamic stat modification layers
* Clean separation between logic and presentation

---

## Design Impact

v4 prioritizes **vertical system depth** over feature expansion.

Instead of adding more abilities or content, this version strengthens:

* System consistency
* Mechanical expressiveness
* Long-term extensibility

This prepares the engine for future systems such as:

* ability scaling
* effect synergies
* enemy abilities
* progression mechanics

(save compatible with v2 and above)
---

## v4.5

- (Future/Planned)

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
This system now fully integrates status effects as part of stat computation.

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
3. Engage in tactical turn-based combat using attacks and abilities and status effects.
4. Generate loot via centralized loot system.
5. Equip or store items.
6. Use consumables strategically.
7. Gain XP and level up.
8. Progress floors and face bosses.
9. Reset dungeon progression after completion.

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

* Turn-based combat
* Basic attacks and player abilities
* Event-driven ability resolution
* Persistent status effects (DoT and stat modifiers)
* Dynamic stat calculation (base + equipment + effects)
* Effect duration and lifecycle management
* Centralized damage mitigation
* XP rewards
* Boss archetypes
* Floor-based difficulty scaling

Combat now operates as a **state-driven system**, where actions create lasting effects that influence future turns.

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

---

## License

Dungeon Ascension is licensed under the GNU GPL v3.

You are free to study, modify, and redistribute the code,
but any distributed derivative work must also remain open-source
under the same license.