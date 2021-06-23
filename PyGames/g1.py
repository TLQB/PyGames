from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

khois = []

class Ground(Button):
	"""docstring for Ground"""	
	Entity(model="cube",x = 15,z=15,y=.5,texture = "wall",scale=(1,2,1))
	Entity(model="cube",x = 4,z=12,y=.5,texture = "brick",scale=(1,3,1))
	Entity(model="cube",x = 8,z=10,y=.5,texture = "brick",scale=(1,5,1))
	Entity(model="cube",x = 2,z=1,y=.5,texture = "wall",scale=(1,5,1))
	Entity(model="cube",x = 18,z=3,y=.5,texture = "brick",scale=(1,5,1))
	Entity(model="cube",x = 5,z=13,y=.5,texture = "wall",scale=(1,5,1))
	Entity(model="cube",x = 8,z=3,y=.5,texture = "brick",scale=(1,4,1))
	Entity(model="cube",x = 20,z=16,y=.5,texture = "wall",scale=(1,2,1))
	def __init__(self,position = (0,0,0)):
		super().__init__(
			parent = scene,
			model = "cube",
			position = position,
			color = color.gray,
			origin_y = .5,
			origin_x = 10,
			origin_z = 10,
			texture = "grass"

			)
		
for z in range(30):
	for x in range(30):
		g = Ground(position = (x,0,z))

class Gun(Entity):
	"""docstring for Gun"""
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = "cube",
			scale = .4,
			position = (0, -.4, .1),
			texture = "gun2"

			)

class Khoi(Button):
	i = 0
	"""docstring for khoi"""
	def __init__(self):
		super().__init__(
			parent = scene,
			model = "cube",
			#texture ="monter1",
			y = .5,
			x=random.randint(20, 30),
			z=random.randint(20, 30),
			#x = random.randrange(30,20,1),
			#z = random.randrange(40,30,1),
			color = color.red,
			)
	def input(self,key):
		if key == "left mouse down":
			Audio(sound_file_name='gun.mp3', autoplay=True)	
		if self.hovered:
			if key == "left mouse down":
				Audio(sound_file_name='gun.mp3', autoplay=True)					
				destroy(khoi)
						
def input(key):			
	if key == "1":
		Audio(sound_file_name='gunconvert.mp3', autoplay=True)
		gun.texture = "gun2"
	if key == "2":
		Audio(sound_file_name='gunconvert.mp3', autoplay=True)
		gun.texture = "gun3"
	if key == "3":
		Audio(sound_file_name='gunconvert.mp3', autoplay=True)
		gun.texture = "gun4"	
			
def update():
	try:
		khoi.x -= time.dt
		khoi.z -= time.dt
	except:
		pass											

khoi = Khoi()			
gun = Gun()	
sky = Sky()
player = FirstPersonController()
app.run()