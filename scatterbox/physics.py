from visual import *

#Contains the functions that do the physics of the simulation.

def move(particles,dt):
  """
  Move particles to next timestep under the assumption of constant 0 acceleration
  """
  for particle in particles:
    particle.pos+=particle.velocity*dt


def collision_in_1D(v1,v2,m1,m2):
  """
  Returns the final velocities for the given particle initial velocities
  and particle masses.
  """
  v1_final = (m1-m2)*v1/(m1+m2)+2*m2*v2/(m1+m2)
  v2_final = 2*m1*v1/(m1+m2) - (m1-m2)*v2/(m1+m2)
  return (v1_final,v2_final)

def collide_particles(p1,p2,dt):
  """
  Checks to see if particle 1 (p1) and
  particle 2 (p2) are close enough to collide.
  If so, reduces the collision to a 1 D problem.
  """
  # Displacement vector
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
      # Project the collision to a 1D problem
      v1=dot(p1.velocity,rhat)
      v2=dot(p2.velocity,rhat)
      #Feed the 1D velocities to the collision_in_1D function
      (v1_final,v2_final) = collision_in_1D(v1,v2,p1.mass,p2.mass)
      #Update the velocity with this chang in velocity
      delta_v1 = (v1_final-v1)*rhat
      delta_v2 = (v2_final-v2)*rhat
      p1.velocity = p1.velocity + delta_v1
      p2.velocity = p2.velocity + delta_v2

#
# Do scattering of particles
#
def collide(particles,dt):
  """
  Collides each particle against every other particle
  """
  # Go over all particles
  for i in range(0,len(particles)):
    # Go over all possible scattering partners
    for j in range(i+1,len(particles)):
      collide_particles(particles[i],particles[j],dt)

