
---

# Dungeon Ascension
#### Description:

## Version History

### v1 - Foundation
Established the primary gameplay loop, combat system, floor progression, persistence, and modular structure.

- Core combat
- Floors
- XP system

### v1.5
--(future/planned)

**Dungeon Ascension** is a modular command-line RPG implemented in Python.
The game simulates structured dungeon progression in which a player explores floors, encounters enemies, gains experience, levels up, and ultimately faces one of two randomized boss encounters.

The project emphasizes clean architecture, separation of concerns, testability, and data-driven design while maintaining immersive terminal presentation through ASCII art and color-enhanced output.

This application was developed as the final project for CS50P (Introduction to Programming with Python).

---

## Concept

Beneath the surface of a forgotten kingdom lies a descending dungeon known only as The Deep Vault. No maps survive. No records explain its origin. What is known is simple: those who descend grow stronger — or never return.

Each floor of the dungeon feels constructed rather than natural, populated by creatures that appear placed, not born. Goblins guard upper corridors. Heavier brutes roam the deeper chambers. And at the lowest level, a powerful entity waits — one of two ancient wardens whose presence suggests the dungeon was built to imprison something… or to protect something.

Adventurers enter seeking power, answers, or survival. Few reach the final floor. Fewer still return to tell what they saw.

In Dungeon Ascension, the player is one such adventurer — climbing through danger, forced backward by defeat, and gradually uncovering strength through repetition and persistence.

---

## Technical Architecture

```
project.py          # Entry point, gameplay loop coordination
combat.py           # Turn-based battle resolution
player.py           # Player class, XP and leveling system
enemy.py            # Enemy class (including bosses)
character.py        # Shared base class for Player and Enemy
config.py           # Game constants and balance configuration
art.py              # ASCII art and presentation mappings
save_load.py        # Persistent character storage (JSON-based)
test_project.py     # Pytest unit tests
data/               # JSON save data
requirements.txt    # Project dependencies
```

## Architectural Principles

### Separation of Concerns

Game mechanics, persistence, configuration, and presentation are separated into dedicated modules.

### Data-Driven Design

Enemy stats, floor distribution, victory requirements, and scaling values are centralized in `config.py`, enabling balance adjustments without modifying combat logic.

### Presentation Decoupling

ASCII art and visual effects are stored and mapped in `art.py`, preventing UI logic from polluting core gameplay systems.

---

## Core Gameplay Loop

1. Create or load a persistent character.
2. Explore the current dungeon floor.
3. Trigger randomized events:

   * Combat encounter
   * Potion discovery
   * Empty chamber
4. Engage in automated turn-based combat.
5. Gain XP and level up.
6. Descend after reaching required victories.
7. Face one of two randomized bosses on the final floor.
8. Upon clearing the dungeon, progression resets while character stats persist.

If defeated:

* The player is revived.
* Progress regresses by one floor.
* HP is restored.
* Victories reset.

---

## Presentation Layer

The project includes a dedicated presentation module (`art.py`) responsible for ASCII art and visual enhancements.

### Visual Features

* Green intro banner
* Blue-colored boss art
* Red Grim Reaper death art
* Dynamic boss reveal sequences
* Terminal clearing for cinematic transitions
* Color-enhanced combat messaging using `colorama`

Presentation logic is separated from gameplay logic, maintaining architectural clarity while enhancing immersion.

---

## Required CS50P Functions

The following functions are defined in `project.py` and tested using pytest:

* `create_enemy_for_floor(floor)`
* `should_descend_floor(victories_on_floor, current_floor)`
* `calculate_new_floor_on_defeat(current_floor)`

These functions isolate deterministic game logic from side effects, ensuring proper unit test coverage.

---

## Combat System

Combat is fully automated and turn-based.

Damage is calculated using attack and defense attributes, with a minimum damage threshold ensuring progression.

Enemy categories include:

* Baseline units (Goblin)
* Mid-tier units (Orc, Skeleton)
* Heavy units (Strong Orc)
* Two distinct boss archetypes with unique stat distributions

Boss encounters trigger unique messaging and visual presentation, representing the peak difficulty of a dungeon cycle.

---

## Features

* Persistent character saves (JSON-based)
* XP progression and level scaling
* Floor-based structured advancement
* Randomized encounters
* Randomized final boss selection
* Color-enhanced terminal output
* ASCII art boss and death sequences
* Modular architecture
* Pytest-based unit testing

---

## Installation

Install dependencies:

pip install -r requirements.txt

---

## Running the Game

python project.py

---

## Running Tests

pytest test_project.py

---

## Dependencies

* `colorama`

(Defined in `requirements.txt`)

---

## Conclusion

Dungeon Ascension demonstrates structured program design, modular architecture, deterministic testing practices, and applied object-oriented principles within an interactive terminal application.

The project balances gameplay structure with maintainable engineering practices while incorporating immersive presentation elements uncommon in typical CLI-based coursework.

---
