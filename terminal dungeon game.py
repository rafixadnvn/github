import random
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

WIDTH = 20
HEIGHT = 10

player_x = 1
player_y = 1
health = 30

enemies = []

def spawn_enemies(count=5):
    for _ in range(count):
        ex = random.randint(2, WIDTH - 2)
        ey = random.randint(2, HEIGHT - 2)
        enemies.append([ex, ey])

def draw():
    clear()
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += "@"
            elif [x, y] in enemies:
                row += "&"
            elif x == 0 or y == 0 or x == WIDTH - 1 or y == HEIGHT - 1:
                row += "#"
            else:
                row += " "
        print(row)
    print(f"\nHealth: {health}")

def move(direction):
    global player_x, player_y
    if direction == "w" and player_y > 1:
        player_y -= 1
    elif direction == "s" and player_y < HEIGHT - 2:
        player_y += 1
    elif direction == "a" and player_x > 1:
        player_x -= 1
    elif direction == "d" and player_x < WIDTH - 2:
        player_x += 1

def move_enemies():
    global health
    for enemy in enemies:
        # Move horizontally
        if enemy[0] < player_x:
            enemy[0] += 1
        elif enemy[0] > player_x:
            enemy[0] -= 1

        # Move vertically
        if enemy[1] < player_y:
            enemy[1] += 1
        elif enemy[1] > player_y:
            enemy[1] -= 1

        # Attack
        if enemy[0] == player_x and enemy[1] == player_y:
            health -= 2

spawn_enemies()

while health > 0:
    draw()
    move_input = input("Move (W A S D): ").lower()

    if move_input in ["w", "a", "s", "d"]:
        move(move_input)
        move_enemies()
    else:
        print("Invalid move, bro.")
        time.sleep(1)

clear()
print("💀 You died in the dungeon...")
