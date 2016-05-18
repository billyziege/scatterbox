from visual import *
# ========================================================
# ========================================================
#
# Listen for keys
# Modify this for interactions with the program
#
def listenkeys(scene,particles,mass):
  # Was a key pressed?
  if scene.kb.keys:
    # Yes, which one?
    s=scene.kb.getkey()
    # This is where you have to add all your keys
    # "x" exits
    if s=='x':
      exit()
    # "s" prints all your stats
    if s=="s":
      print_stats(particles)
    if s=="v":
      switch_visible(particles,mass)

#
# Little routine that calculates total energy and momentum
# Just for demo
def print_stats(particles):
  energy=0
  momentum=vector(0,0,0)
  for particle in particles:
    momentum+=particle.mass*particle.velocity
    energy+=.5*particle.mass*mag2(particle.velocity)
  print "Momentum",momentum
  print "Energy",energy

def switch_visible(particles,mass):
  """
  Tells the program to hide or show the particles with the given mass.
  """
  for particle in particles:
    if particle.mass == mass:
      if particle.visible is True:
        particle.visible = False
      else:
        particle.visible = True
