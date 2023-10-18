class FaveAnimal:
	def __init__(self, armlength,leglength,eyenum,tailpresence,furriness):
		self.armlength = armlength
		self.leglength = leglength
		self.eyenum = eyenum
		self.tailpresence = tailpresence
		self.furriness = furriness
	def words(self):
		print("Bee arms are " + self.armlength)
		print("Bee legs are " + self.leglength)
		print(f"Bees have {self.eyenum} eyes")
		print(f"Do bees have tails? {self.tailpresence}")
		print(f"Are bees furry? {self.furriness}")

bee = FaveAnimal("...short","also very short. Sorry these aren't floats, I genuinely couldn't find out how long bee legs are.",5,False,True)
bee.words()