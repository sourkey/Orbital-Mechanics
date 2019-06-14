# OrbitalMechanics

A compilation of a few methods used to calculate orbits. This class supports circular and elliptical orbit geometries.

## Implementation
Define an orbital object and use the optional 'name' keyword argument.

	sat1 = Orbit('Sat1')

Next, begin to define the orbital parameters, such as the semimajor axis, the semiminor axis, and orbit eccentricity. 

	calcOrbit(major=4000, minor=0, e=0, step=0.05, table='hide', image='hide')
	
Set semimajor and semiminor values. Eccentricity, e, can be specified if the semiminor value is left blank, otherwise it will be calculated. 

Use 'show' for table and image keyword arguments to show the position with the desired step size.
