# OrbitalMechanics

A compilation of a few methods used to calculate orbits. This class supports circular and elliptical orbit geometries.

Implementation
Define an orbital object:

	sat1 = Orbit('Sat1')

Define orbital parameters:

	calcOrbit(major=4000, minor=0, e=0, step=0.05, table='hide', image='hide')
	
Set semimajor and semiminor values. Eccentricity, e, can be specified if the semiminor value is left blank, otherwise it will be calculated. Use 'show' for table and image keywords to show the position with the desired step size.
