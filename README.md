
---

# Dungeon Ascension
#### Description:

## Version History

### v1 - Foundation
Established the primary gameplay loop, combat system, floor progression, persistence, and modular structure.

- Core automated combat
- Floor progression system
- XP and leveling system
- Persistent character saves
- Boss encounters
- Risk–reward floor regression on defeat

v1 proved the core loop was stable and replayable.

### v1.5 - Structural Refactor
Reorganized the architecture around a centralized GameEngine class.
Encapsulated state ownership, lifecycle management, and exploration flow.
Fixed Defense being used twice during damage calculation.
Added version tag in save file.

- Introduced GameEngine (centralized orchestration)
- Renamed project.py → game.py
- Encapsulated lifecycle management
- Separated exploration logic
- Save file version tagging
- Removed testing scaffolding
- Improved state ownership boundaries
- Backward-compatible save loading
- Fixed damage calculation

No gameplay changes — structural evolution only.

### v2 - System Expansion

- (future/planned)

## Overview

**Dungeon Ascension** is a modular command-line RPG implemented in Python.
The game simulates a structured dungeon progression system in which a player explores floors, encounters enemies, gains experience, levels up, and ultimately faces randomized boss encounters.

The project is evolving toward stricter separation of engine logic and presentation and data-driven design.

This application was developed as the final project for CS50P (Introduction to Programming with Python).

---

## Concept/Lore

Beneath the surface of a forgotten kingdom lies a descending dungeon known only as The Deep Vault. No maps survive. No records explain its origin. What is known is simple: those who descend grow stronger — or never return.

Each floor of the dungeon feels constructed rather than natural, populated by creatures that appear placed, not born. Goblins guard upper corridors. Heavier brutes roam the deeper chambers. And at the lowest level, a powerful entity waits — one of two ancient wardens whose presence suggests the dungeon was built to imprison something… or to protect something.

Adventurers enter seeking power, answers, or survival. Few reach the final floor. Fewer still return to tell what they saw.

In Dungeon Ascension, the player is one such adventurer — climbing through danger, forced backward by defeat, and gradually uncovering strength through repetition and persistence.

---

## Core Gameplay Loop

The player:

1. Creates or loads a persistent character.
2. Explores dungeon floors through randomized events.
3. Engages in automated combat encounters.
4. Gains experience and levels up.
5. Progresses deeper into the dungeon after meeting victory thresholds.
6. Faces one of two randomized bosses on the final floor.
7. Resets progression after clearing the dungeon, with the player stats still being intact.

If defeated, the player is revived on the previous floor, creating a structured risk–reward loop.

---

## Technical Design

The project is organized into modular components:

```
game.py             # Orchestrator through the GameEngine class.
art.py              # Art for bosses, art for death screen and intro banner.
combat.py           # Handles turn-based battle resolution logic.
player.py           # Implements the Player class, XP system, and leveling mechanics.
enemy.py            # Defines the Enemy class and boss variants.
config.py           # Centralizes game constants and balancing parameters.
save_load.py        # Manages persistent storage and retrieval of character data.
character.py        # Provides shared logic used by both Player and Enemy classes.
data/               # Saved character data inside JSON
requirements.txt    # Project dependencies
```

### Architectural Principles

* **Separation of Concerns**
  Combat logic, player state management, configuration, and persistence are separated into independent modules.

* **Data-Driven Design**
  Enemy stats, floor configurations, and progression thresholds are defined in `config.py`, allowing balance adjustments without altering logic.

* **Persistence Layer**
  Character progress is saved and loaded using a structured dictionary-based storage system.

---


## Combat System

Combat is automated and turn-based.
Damage calculation incorporates attack and defense attributes.
Enemy archetypes are designed to create distinct combat pacing:

* Baseline enemies (e.g., Goblin)
* Scaling mid-tier enemies (e.g., Orc, Skeleton)
* Heavy units (e.g., Strong Orc)
* Two distinct boss archetypes with different stat distributions

Boss encounters include unique messaging and represent the peak difficulty of a dungeon cycle.

---

## Features

* Persistent character saves
* XP and level progression system
* Floor-based dungeon advancement
* Randomized encounters and boss selection
* Structured difficulty escalation
* Color-enhanced CLI output (via colorama)
* Modular code architecture

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Running the Game

python game.py

---

## Dependencies

* colorama

(Defined in `requirements.txt`)

---

## Conclusion

Dungeon Ascension demonstrates structured program design, modular architecture, and applied object-oriented principles within a game-driven context.

The project balances gameplay structure with maintainable software engineering practices.

---
