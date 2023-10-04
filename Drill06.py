from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    global arrow

    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame
    global t
    global action

    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 1

    # set_new_target_arrow()


def set_new_target_arrow():
    global sx, sy, hx, hy, t
    global action
    global frame
    sx, sy = cx, cy
    # hx, hy = TUK_WIDTH - 50, TUK_HEIGHT - 50
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    t = 0.0
    action = 1 if sx < hx else 0
    frame = 0


def rander_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global cx, cy
    global t

    frame = (frame + 1) % 8

    # if t <= 1.0:
    #     cx = (1 - t) * sx + t * hx
    #     cy = (1 - t) * sy + t * hy
    #     t += 0.001
    # else:
    #     cx, cy = hx, hy
    #     set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    rander_world()
    handle_events()
    update_world()

close_canvas()