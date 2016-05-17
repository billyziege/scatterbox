from visual import *
from random import random
# The list of all particles
particles=[]
# The timestep length (might need to be adjusted)
dt=0.01
# The rate
dtrate=100
# How many particles
number_particles=100
# Box size, x_min, x_max, y_min, ...
boxsize=(-10,4,-5,8,-3,6)
# Maximum velocity
maxvelo=3
# Maximum mass
maxmass=10
#
# ========================================================
# ================================== Some useful functions
# Probably do not need to be changed
#
# The following function makes a particle
# at the given position and with the given
# velocity.
# Assume constant density, radius proportional
# to m^(1/3).
# col determines color
#
def makeparticle(position,velocity,mass,col):
# Make a new particle
    newparticle=sphere(pos=position,radius=0.2*mass**(1./3.),color=col)
# Give it mass
    newparticle.mass=mass
# Give it velocity
    newparticle.velocity=vector(velocity)
# Put it into the list of particles to take care of
    particles.append(newparticle)
#
# The following removes the particle in the argument
#
def destroyparticle(thisparticle):
# Remove it from the list of particles to take care of
    particles.remove(thisparticle)
# Make it invisible
    thisparticle.visible=false
# Delete it
    del thisparticle
            
#
# Classical hard sphere scattering
# The following scatters two particles elastically
# Modifies their velocities
#
def scatter_particles(p1,p2):
# Difference vector
    diff=p2.pos-p1.pos
    distance=mag(diff)
# Do they even touch?
    if distance<=p1.radius+p2.radius:
# Yes, they do
# Only scatter them if they are actually
# moving toward each other
        nextpos1=p1.pos+p1.velocity*dt
        nextpos2=p2.pos+p2.velocity*dt
        if mag(nextpos2-nextpos1)<distance:
# Time to colide!
# Direction of difference vector
            rhat=norm(diff)
# Momenta
            mv1=p1.mass*p1.velocity
            mv2=p2.mass*p2.velocity
# Calculate the momentum transfer
            transfer=2.*dot(p1.mass*mv2-p2.mass*mv1,rhat)/(p1.mass+p2.mass)*rhat
# Get new velocities
            p1.velocity=(mv1+transfer)/p1.mass
            p2.velocity=(mv2-transfer)/p2.mass

#
# Do scattering of particles
#
def scatter():
# Go over all particles
    for i in range(0,len(particles)):
# Go over all possible scattering partners
        for j in range(i+1,len(particles)):
            scatter_particles(particles[i],particles[j])
#
# Do reflection of particles
#
def reflect():
    global boxsize
    for particle in particles:
        if particle.pos.x>=boxsize[1] or particle.pos.x<=boxsize[0]:
            particle.velocity.x=-particle.velocity.x
        if particle.pos.y>=boxsize[3] or particle.pos.y<=boxsize[2]:
            particle.velocity.y=-particle.velocity.y
        if particle.pos.z>=boxsize[5] or particle.pos.z<=boxsize[4]:
            particle.velocity.z=-particle.velocity.z
#
# Move particles to next timestep
#
def move():
    for particle in particles:
        particle.pos+=particle.velocity*dt
#
# ========================================================
# ========================================================
#
# Listen for keys
# Modify this for interactions
#
def listenkeys():
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
            print_stats()


#
# Litte routine that calculates total energy and momentum
# Just for demo
def print_stats():
    energy=0
    momentum=vector(0,0,0)
    for particle in particles:
        momentum+=particle.mass*particle.velocity
        energy+=.5*particle.mass*mag2(particle.velocity)
    print "Momentum",momentum
    print "Energy",energy
    
# ========================================================
# Main program
# Setting up things
# Make the box

box(pos=((boxsize[1]+boxsize[0])/2.,
         (boxsize[3]+boxsize[2])/2.,
         (boxsize[5]+boxsize[4])/2.),
    size=(boxsize[1]-boxsize[0],
          boxsize[3]-boxsize[2],
          boxsize[5]-boxsize[4]),
    color=color.white,
    opacity=0.1)

# Make a bunch of totally random particles inside box

for i in range(0,number_particles):
    makeparticle((boxsize[0]+(boxsize[1]-boxsize[0])*random(),
                  boxsize[2]+(boxsize[3]-boxsize[2])*random(),
                  boxsize[4]+(boxsize[5]-boxsize[4])*random()),
                 (maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random()),
                  maxvelo*(1.-2.*random())),
                 1.+(maxmass-1.)*random(),
                 (random(),random(),random()))

                                 
# Keep the scene from expanding
scene.autoscale=False
# Infinite loop
while True:
    rate(dtrate)
    listenkeys()
    scatter()
    reflect()
    move()
                              



