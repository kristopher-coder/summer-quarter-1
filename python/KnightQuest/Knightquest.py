

import pgzrun
import pgzrun
import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keys
# Game constants
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARD_MOVE_INTERVAL = 0.5
PLAYER_MOVE_INTERVAL = 0.1
START_LIVES = 3
# Window size
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# The map (W=Wall, K=Key, G=Guard, P=Player, D=Door)
MAP = [
    "WWWWWWWWWWWWWWWW",
    "W    W      W  W",
    "W WWWWWWWW     W",
    "W W KG   W WWWWW",
    "W W WW WWW   K W",
    "W   W   W W    W",
    "W WWWW P WWWWW W",
    "W     W   W    W",
    "WWWWG WWW   W  W",
    "W   W     WWW  W",
    "W     G     W DW",
    "WWWWWWWWWWWWWWWW"
]
# Game state variables
player = None
playerStartPos = (0, 0)
keysToCollect = []
guards = []
gameOver = False
lives = START_LIVES
win = False
# Converts grid (x, y) to screen pixel coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# Converts Actor's screen pos to grid pos
def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
# Draws the dungeon floor
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x % 2 == y % 2:
                screen.blit("floor2", GetScreenCoords(x, y))
            else:
                screen.blit("floor1", GetScreenCoords(x, y))
# Draws walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
# Draws the player, keys, and guards
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
# Draw lives and game over or win message
def DrawUI():
    screen.draw.text(f"Lives: {lives}", topleft=(10, 10), fontsize=36, color="white", owidth=1)
    if gameOver:
        center = (WIDTH / 2, HEIGHT / 2)
        screen.draw.text("GAME OVER", midbottom=center, fontsize=GRID_SIZE, color="red", owidth=1)
        # Draw restart button
        restart_rect = Rect((WIDTH // 2 - 100, HEIGHT // 2 + 20), (200, 50))
        screen.draw.filled_rect(restart_rect, (50, 50, 50))
        screen.draw.text("RESTART", center=restart_rect.center, fontsize=40, color="white")
    if win:
        center = (WIDTH / 2, HEIGHT / 2)
        screen.draw.text("YOU WIN!", midbottom=center, fontsize=GRID_SIZE, color="lime", owidth=1)
        restart_rect = Rect((WIDTH // 2 - 100, HEIGHT // 2 + 20), (200, 50))
        screen.draw.filled_rect(restart_rect, (50, 50, 50))
        screen.draw.text("RESTART", center=restart_rect.center, fontsize=40, color="white")
# Main draw function
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    DrawUI()
# Setup game actors and variables
def SetupGame():
    global player, playerStartPos, keysToCollect, guards, gameOver, lives, win
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False
    win = False
    lives = START_LIVES
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            pos = GetScreenCoords(x, y)
            if square == "P":
                player.pos = pos
                playerStartPos = pos  # Save starting position
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = pos
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = pos
                guards.append(guard)
    # Reschedule guard movement timer on restart
    clock.unschedule(MoveGuards)
    clock.schedule_interval(MoveGuards, GUARD_MOVE_INTERVAL)
# Handles player movement
def MovePlayer(dx, dy):
    global gameOver, win
    if gameOver or win:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    if MAP[y][x] == "W":
        return
    elif MAP[y][x] == "D":
        if len(keysToCollect) > 0:
            return
        else:
            win = True
            # sounds.win.play() removed
            return
    # Check for key collection
    for key in keysToCollect:
        if GetActorGridPos(key) == (x, y):
            keysToCollect.remove(key)
            # sounds.key.play() removed
            break
        animate(player, pos=GetScreenCoords(x, y),
                duration=PLAYER_MOVE_INTERVAL)
    # Move the player to new position
    player.pos = GetScreenCoords(x, y)
# Handle keyboard input
def on_key_down(key):
    if gameOver or win:
        return  # Ignore key presses after game ends
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.DOWN:
        MovePlayer(0, 1)
# Move a single guard toward the player
def MoveGuard(guard):
    global lives, gameOver
    if gameOver or win:
        return
    playerX, playerY = GetActorGridPos(player)
    guardX, guardY = GetActorGridPos(guard)
    # Simple greedy move toward player
    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -= 1
    #Animate the guard as he moves
    guard.pos = GetScreenCoords(guardX, guardY)
    # If guard catches player
    if (playerX, playerY) == (guardX, guardY):
        # sounds.caught.play() removed
        lives -= 1
        if lives <= 0:
            gameOver = True
        else:
            player.pos = playerStartPos  # Reset player position
# Move all guards
def MoveGuards():
    for guard in guards:
        MoveGuard(guard)
# Handle mouse clicks for restart button
def on_mouse_down(pos):
    if gameOver or win:
        restart_rect = Rect((WIDTH // 2 - 100, HEIGHT // 2 + 20), (200, 50))
        if restart_rect.collidepoint(pos):
            SetupGame()
# Start the game
SetupGame()
clock.schedule_interval(MoveGuards, GUARD_MOVE_INTERVAL)
pgzrun.go()


h







