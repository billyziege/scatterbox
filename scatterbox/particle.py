from visual import *
#Creates, destroys, and sets up boundary conditions for the particles.

def makeparticle(position,velocity,mass,col,visible=True):
  # Make a new particle
  newparticle=sphere(pos=position,radius=0.2*mass**(1./3.),color=col)
  # Give it mass
  newparticle.mass=mass
  # Give it velocity
  newparticle.velocity=vector(velocity)
  #Tell the program if it will be visible or not.
  newparticle.visible=visible
  return newparticle

#
# The following removes the particle in the argument
#
def destroyparticle(particles,thisparticle):
  # Remove it from the list of particles to take care of
  particles.remove(thisparticle)
  # Make it invisible
  thisparticle.visible=false
  # Delete it
  del thisparticle
  return particles
            
def reflect(particles,boxsize):
  """
  Sets up the reflect boundary condition on the particles in the box.
  Reflects the particle elastically back into the box.
  """
  for particle in particles:
    if particle.pos.x>=boxsize[1] or particle.pos.x<=boxsize[0]:
      particle.velocity.x=-particle.velocity.x
    if particle.pos.y>=boxsize[3] or particle.pos.y<=boxsize[2]:
      particle.velocity.y=-particle.velocity.y
    if particle.pos.z>=boxsize[5] or particle.pos.z<=boxsize[4]:
      particle.velocity.z=-particle.velocity.z
