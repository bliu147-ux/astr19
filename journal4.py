class Animal:
	
	def __init__(self, arm_length=3.0, 
					   leg_length=9.9,
					   eye_number=2,
					   has_tail=True,
					   furry=True):
	
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.eye_number = eye_number
		self.has_tail = has_tail
		self.furry = furry

	def description(self):
		print(f"My animal has an arm length of {self.arm_length}")
		print(f"My animal has a leg length of {self.leg_length}")
		print(f"My animal has {self.eye_number} eyes")
		print(f"{self.has_tail}, my animal has a tail")
		print(f"{self.furry}, my animal is furry")

test = Animal()
test.description()
