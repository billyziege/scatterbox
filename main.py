from visual import *
from random import random
from scatterbox.interupt import listenkeys
from scatterbox.particle import makeparticle, reflect
from scatterbox.physics import collide, move
# ========================================================
# Main program

# Setting up things
#Parameters
# The timestep length (might need to be adjusted)
dt=0.01
# The refresh rate
dtrate=100
# How many particles
number_large_particles=3
number_small_particles=22
# Box size, x_min, x_max, y_min, ...
boxsize=(-2,2,-2,2,-0.5,0.5)
# Maximum velocity
maxvelo=3
#Mass
large_mass = 10
small_mass = 1
#Colors
large_color = vector(0,1,0) #green
small_color = vector(0,0,1) #blue

# Make the box for the video
box(pos=((boxsize[1]+boxsize[0])/2.,
         (boxsize[3]+boxsize[2])/2.,
         (boxsize[5]+boxsize[4])/2.),
    size=(boxsize[1]-boxsize[0],
          boxsize[3]-boxsize[2],
          boxsize[5]-boxsize[4]),
    color=color.white,
    opacity=0.1)

# Make particles with random positions and velocities inside box
# The list of all particles
particles=[]
for i in range(0,number_large_particles):
  particle = makeparticle((boxsize[0]+(boxsize[1]-boxsize[0])*random(),
                  boxsize[2]+(boxsize[3]-boxsize[2])*random(),
                  boxsize[4]+(boxsize[5]-boxsize[4])*random()),
                 (maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random())),
                 large_mass,
                 large_color)
  particles.append(particle)
for i in range(0,number_small_particles):
  particle = makeparticle((boxsize[0]+(boxsize[1]-boxsize[0])*random(),
                  boxsize[2]+(boxsize[3]-boxsize[2])*random(),
                  boxsize[4]+(boxsize[5]-boxsize[4])*random()),
                 (maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random())),
                 small_mass,
                 small_color)
  particles.append(particle)
                               
# Keep the scene from expanding
scene.autoscale=False
# Infinite loop
while True:
    #Video set-up
    #Set the max rate at which the simulation video will refress
    rate(dtrate)
    #A hook to allow key-board interuptive behavior to the video
    listenkeys(scene,particles,small_mass)
    
    #The physics
    #Collide the particles
    collide(particles,dt)
    #Bounce particles off the edge of the simulation
    reflect(particles,boxsize)
    #Move the particles
    move(particles,dt)
