# Demon Slayer Text Adventure

## Overview

This project is a Python text-based adventure game for IT-140 Intro to Scripting. The player starts in the Living room and must collect six items before confronting the Demon King in the Great Hall.

If the player reaches the Demon King before collecting all required items, the game ends. After all six items are collected, the player can enter the Great Hall and begin the final battle.

## Game Objective

Collect all six items and defeat the Demon King.

Required items:

- Holy Water
- Sword
- Armor
- Medical Kit
- Sutra Book
- Lotus

Villain:

- Demon King

## Room Map

The game has eight rooms:

| Room | Item or Role | Connected Rooms |
| --- | --- | --- |
| Living room | Starting point | East to Mess Hall |
| Mess Hall | Holy Water | West to Living room, North to Armory, South to Basement, East to Pond |
| Armory | Sword | South to Mess Hall, East to Shrine |
| Shrine | Armor | West to Armory |
| Basement | Medical Kit | North to Mess Hall, East to Library |
| Library | Sutra Book | West to Basement |
| Pond | Lotus | West to Mess Hall, East to Great Hall |
| Great Hall | Demon King | West to Pond |

## How to Play

Run the game with Python:

```bash
python TextGameStoryboard.py
```

The game accepts two command types:

```text
move East
move West
move North
move South
pickup Holy Water
```

Use `move` followed by a direction to travel between rooms. Use `pickup` followed by the item name to collect an item in the current room.

## Suggested Winning Path

One possible route is:

1. Move East to the Mess Hall and pick up Holy Water.
2. Move North to the Armory and pick up Sword.
3. Move East to the Shrine and pick up Armor.
4. Move West to the Armory.
5. Move South to the Mess Hall.
6. Move South to the Basement and pick up Medical Kit.
7. Move East to the Library and pick up Sutra Book.
8. Move West to the Basement.
9. Move North to the Mess Hall.
10. Move East to the Pond and pick up Lotus.
11. Move East to the Great Hall to confront the Demon King.

## Game Logic

The game uses a dictionary named `floor_layout` to store each room, its available directions, and any item located there. The player inventory is stored in a list, and a counter tracks how many items have been collected.

Main features:

- Displays the player's current location and inventory.
- Detects items in the current room.
- Allows movement using dictionary lookups.
- Adds collected items to the inventory.
- Removes collected items from rooms.
- Prevents invalid movement.
- Ends the game if the player enters the Great Hall too early.
- Starts a final number-guessing battle after all six items are collected.

## Files

- `TextGameStoryboard.py`: Main Python game file.
- `README.md`: Project documentation generated from the storyboard.
