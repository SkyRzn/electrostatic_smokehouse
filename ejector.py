#!/usr/bin/python


from opyscad import *
from chamber import chamber
from coupling import coupling


def main():
	chmb = chamber()
	chmb.save('chamber.scad')
	cpl = coupling(10.0, False, 15.0, True)
	#cpl.save('coupling.scad')
	res = chmb + ((cpl / [0, -90, 0]) << [-22,0,0])
	res += (cpl / [0, -90, 0]) << [-22,-15,0]
	res += (cpl / [0, 90, 0]) << [17,0,0]
	res -= cube([200,200,200]) << [-100,-100,0]
	res.save('coupling.scad')
if __name__ == '__main__':
	main()


