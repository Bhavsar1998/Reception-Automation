import pyglet
from pyglet.window import Platform
import time
global sprite
monitor = Platform().get_default_display().get_default_screen()
pyglet.gl.glClearColor(1, 1, 1, 1)

cab=''
def intialize_map(cabin):
    cab=cabin
    drawMap(cab)

    @window.event
    def on_draw():
        import time

        window.clear()
        if time.time() - t1 > 10:
            pyglet.app.exit()
        sprite.draw()
        pyglet.clock.schedule_once(update, 10)

    t1 = time.time()
    pyglet.app.run()
    window.close()
    # print("time up")



def drawMap(cab):
    global sprite
    # cab = 'collegeMap.png'
    sprite = pyglet.sprite.Sprite(pyglet.resource.animation(cab))
    H_ratio = sprite.height
    W_ratio = sprite.width
    global window
    window = pyglet.window.Window(width=1920, height=1080, fullscreen=True)


def update(dt):
    # print("END")
    dt = pyglet.clock.tick()
    if dt == 10:
        return 0

# cabin='canteen.gif'
# intialize_map(cabin)