import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "ctypes_sdl"))

from sdl import *
import sdlimage
import sdlttf
import sdlmixer
import ctypes as ct


c_str = lambda s: ct.c_char_p(bytes(s, "ascii"))


class Slab:
	
	def __init__(self, width=10, height=10, p_surface=None):

		if p_surface != None:
			self.p_surface = p_surface
		else:
			self.p_surface = SDL_CreateRGBSurface(
				SDL_SWSURFACE, width, height, 24, 0, 0, 0, 0)

		self.surface = self.p_surface.contents
		
		self.pixels = ct.cast(self.surface.pixels, ct.POINTER(c_char))

		self.rect = SDL_Rect(0, 0, 0, 0)
	

	def __del__(self):
		
		if hasattr(self, "p_surface"):
			SDL_FreeSurface(self.p_surface)
	

	def __getitem__(self, idx):

		color = 0

		for b in self.pixels[idx * 3 : idx * 3 + 3][::-1]:
			color = color << 8
			color = color ^ b

		return color


	def __setitem__(self, idx, color):

		int_bgr = lambda col: (col & 0x0000ff, (col & 0x00ff00) >> 8, (col & 0xff0000) >> 16)

		for i, c in enumerate(int_bgr(color)):
			self.pixels[idx * 3 + i] = c


	def getWidth(self):
		
		return self.surface.w

	
	def getHeight(self):

		return self.surface.h
	

	def fill(self, color):
		
		SDL_FillRect(self.p_surface, 0, color)	
	

	def burnInto(self, slab, x=0, y=0):
		
		self.rect.x = x
		self.rect.y = y
		
		SDL_BlitSurface(self.p_surface, 0, slab.p_surface, ct.byref(self.rect))	




class SlabImg(Slab):

	def __init__(self, file_path):

		ascii_path = bytes(file_path, "ascii")

		p_surface = sdlimage.IMG_Load(ct.c_char_p(ascii_path))

		if not p_surface:
			msg = "Failed to load \"{:s}\" - Make sure the file path is correct."
			raise Exception(msg.format(file_path))

		p_surface_optimized = SDL_DisplayFormat(p_surface)
		SDL_FreeSurface(p_surface)

		super().__init__(p_surface=p_surface_optimized)



class SlabText(Slab):

	def __init__(self, font_path, point_size, fgc, bgc, text):
		
		ascii_path = bytes(font_path, "ascii")

		self.font = sdlttf.TTF_OpenFont(ct.c_char_p(ascii_path), point_size)
		
		if not self.font:
			msg = "Failed to load \"{:s}\" - Make sure the file path is correct."
			raise Exception(msg.format(file_path))

		self.setText(text)

		self.setColor(fgc, bgc)
		
		self.update()
	

	def setText(self, text):
		
		self.text = c_str(text)


	def setColor(self, fgc, bgc=0):

		int_rgb = lambda col: ((col & 0xff0000) >> 16, (col & 0x00ff00) >> 8, col & 0x0000ff)

		r, g, b = int_rgb(fgc)
		self.fgc = sdlttf.SDL_Color(r, g, b, 0xFF)
		r, g, b = int_rgb(bgc)
		self.bgc = sdlttf.SDL_Color(r, g, b, 0xFF)


	def update(self):
		
		p_surface = sdlttf.TTF_RenderText_Shaded(self.font, self.text, self.fgc, self.bgc)

		super().__del__()

		super().__init__(p_surface=p_surface)
	


class Sound:

	def __init__(self, file_path):
		
		self.chunk = sdlmixer.Mix_LoadWAV(c_str(file_path))
		
		if not self.chunk:
			msg = "Failed to load \"{:s}\" - Make sure the file path is correct."
			raise Exception(msg.format(file_path))
	
	
	def __del__(self):

		sdlmixer.Mix_FreeChunk(self.chunk)

	
	def play(self):
		
		sdlmixer.Mix_PlayChannel(-1, self.chunk, 0)

		

class Mouse:
	
	def __init__(self):

		self.position = (0, 0)
		self.btn_state = {"lmb": 0, "rmb": 0}
	

	def btnDown(self, btn):
		
		return self.btn_state[btn]


	def btnHit(self, btn):
		
		return self.btn_state[btn] == 2

	
	def getPosition(self):
		
		return self.position



class Window(Slab):

	
	def __init__(self, width, height):

		super().__init__(p_surface=SDL_SetVideoMode(width, height, 24, SDL_SWSURFACE))
		
		self.event = SDL_Event()

		self.mouse = Mouse()

	
	def update(self):
		
		SDL_Flip(self.p_surface)

	
	def processEvents(self):

		HIT = 2
		DOWN = 1
		UP = 0

		for btn, state in self.mouse.btn_state.items():
			if state == HIT:
				self.mouse.btn_state[btn] = DOWN

		while SDL_PollEvent(ct.byref(self.event)):

			if self.event.type == SDL_MOUSEBUTTONDOWN:
				self.__setMouseBtnState(self.event.button, HIT)
			elif self.event.type == SDL_MOUSEBUTTONUP:
				self.__setMouseBtnState(self.event.button, UP)
	

	def __setMouseBtnState(self, event, state):

		if event.button == SDL_BUTTON_LEFT:
			self.mouse.btn_state["lmb"] = state
		elif event.button == SDL_BUTTON_RIGHT:
			self.mouse.btn_state["rmb"] = state

		self.mouse.position = (event.x, event.y)
		

SDL_Init(SDL_INIT_EVERYTHING)
sdlttf.TTF_Init()

rate = 44100
fmt = AUDIO_S16SYS
channels = 2
buffers = 4096

sdlmixer.Mix_OpenAudio(rate, fmt, channels, buffers)
