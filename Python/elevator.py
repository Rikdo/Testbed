// There are three elevators.
// The building is 33 floors tall
// The left elevator can also descend to the two basement levels

class Elevator:
  def __init__(self, name):
    self.name = name
    self.rest_flr = 1
    self.current_flr = 1
    self.direction = 
  def call(self, destination):        # Method
      return f"{self.name} headed to {destination}."
