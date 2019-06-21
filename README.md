# Orbital-Mechanics

A compilation of a few methods used to calculate orbits. This class supports circular and elliptical orbit geometries. The script is intended to be used with metric values (i.e. distances in km).

## Implementation

Initialize an orbital object and use the optional `name` keyword argument.

	sat1 = Orbit('Sat1')

### Circular Orbit

Define the orbital parameters: 

	sat1.calcOrbit(smajor=4000, steps=50, table='hide', image='hide', summary='hide')
	
The number of steps in the calculation is set to 50 by default. 

For a circular orbit, the true anomoly, mean anomoly, and eccentric anomoly are by definition the same value. Furthermore, the eccentricity is zero.

### Elliptical Orbit

:rocket: Coming soon!

### Optional Keyword Arguments

Several keyword arguments have been included which provide a table with positions, an image of the orbit, and a summary of the orbital parameters. 
  * Use 'table="show"' to print orbital positions.
  * Use 'image="show"' to display an image of the orbit.
  * Use 'summary="show"' to print a summary of the orbital parameters (e.g. semimajor axis, eccentricity, etc).

### Objects in Orbit

To see the the names and number of objects in orbit use the `showInOrbit` method.

	sat1.showInOrbit()
