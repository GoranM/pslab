pslab
=====

A small Python 3.x media library, with a very simple API.

---

Usage
-----

```py
import pslab

window = pslab.Window(640, 480)               # You have a 640 x 480 window.

window[0] = 0xFF0000                          # Set color of first pixel to red.
window[1] = 0x00FF00                          # Second pixel to blue.
window[2] = 0x0000FF                          # Third to green.

window.update()                               # See the changes (you might have to squint).

window.fill(0xFF0000)                         # Make the whole screen red.

window.update()                               # See the changes (you won't have to squint this time).

slab = pslab.Slab(64, 64)                     # Create a 64 x 64 slab of pixels (black by default).
slab.fill(0xFFFFFF)                           # Make it white.
slab.burnInto(window)                         # Burn the white slab into the red window, at origin.
window.update()                               # See the changes.

slab.fill(0x0000FF)                           # Make slab blue.
slab.burnInto(window, 64, 64)                 # Burn the blue slab into the red window, at x:64, y:64.

for i in range(64 * 32):                      # Color the first half of the slab green.
	slab[i] = 0x00FF00

slab.burnInto(window, 128, 128)               # ... I think you got the idea.
window.update()

window.fill(0)                                # Clear the screen to black.
window.update()

slab = pslab.SlabImg("path/to/image.jpeg")    # Slab of pixels formed from an image.
slab.burnInto(window)                         # Other than that, it's just a regular slab.
window.update()                               # As you can see.


 # Text:

window.fill(0)

font_path = "/path/to/font.ttf"
point_size = 12
color_char = 0xFFFFFF
color_background = 0
text = "Hello World."

slab = pslab.SlabText(font_path, point_size, color_char, color_background, text)
slab.burnInto(window)
window.update()

slab.setColor(0xFF0000)
slab.update()                                 # Changing text requires update - text is rendered to slab.
slab.burnInto(window, 0, 12)
window.update()

slab.setColor(0x0000FF, 0xFF0000)
slab.setText("Hello weird world.")
slab.update()
slab.burnInto(window, 0, 24)
window.update()


 # Sound

sound = pslab.Sound("path/to/sound.wav")
sound.play()


 # Mouse input

import time
import random

mouse = window.mouse

while True:
	window.processEvents()                # Updates the mouse object with relevant data

	if mouse.btnHit("rmb"):               # Clicking right mouse button breaks loop
		break

	if mouse.btnHit("lmb"):               # Clicking left mouse button marks the coordinate

		mx, my = mouse.getPosition()
		slab.setText("mx:{:d}, my:{:d}".format(mx, my))
		slab.setColor(random.randint(0, 0xFFFFFF), 0)
		slab.update()
		slab.burnInto(window, mx, my)
		window.update()

		sound.play()

	time.sleep(1/30)                      # Loop executes at 30 fps
```

---

Install
-------

This library requires SDL 1.2, and complementary libraries (SDL_image, SDL_ttf and SDL_mixer). These are all C shared libraries that must be in your library path.

* __Linux__: you can simply use your package manager to get the respective SDL development packages.
* __Windows__: get the SDL dlls however you can, and make sure they are in your path.
* __OSX__: make sure that the SDL libraries are in your library path.

With that done, you can cd into pslab/demos/minimem, and run `python minimem.py` to test the system.

If everything works right, you can "install" this python library by moving pslab.py and ctypes_sdl into a directory like "site-packages", which is typically used for third party python modules like this one. Although, any directory in your python path should work equally well.

At this point, you should be able to `import pslab` in any Python 3.x program, anywhere on your system.
