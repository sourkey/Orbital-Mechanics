# OrbitalMechanics

A compilation of a few methods used to calculate orbits. This class supports circular and elliptical orbit geometries.

## Implementation
Define an orbital object and use the optional `name` keyword argument.

	sat1 = Orbit('Sat1')

Next, begin to define the orbital parameters, such as the semimajor axis, the semiminor axis, and orbit eccentricity. The program is intended to be used with metric values (i.e. distances in km).

	sat1.calcOrbit(smajor=4000, sminor=0, e=0, steps=50, table='hide', image='hide', summary='hide')
	
Set semimajor and semiminor values. Eccentricity, e, can be specified if the semiminor value is left blank, otherwise it will be calculated. 

Use 'show' for table and image keyword arguments to show the position with the desired step size.

To see the number of objects in orbit use the `showInOrbit` method.

	sat1.showInOrbit()
