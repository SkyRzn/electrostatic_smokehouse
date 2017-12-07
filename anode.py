#!/usr/bin/python


from opyscad import *
from box import box



L1 = 390
W1 = 300
L2 = 300
W2 = 300

ANODE = {	'w': 300,
			'h': 1.5,
			't': 5.0,
			'pin': {	'dist': 30.0,
						'd': 4.0,
						'h': 15.0,
						'pit_d': 3.0,
						'pit_h': 3.0 },
		}


def anode(data):
	l = data['l']
	w = data['w']
	h = data['h']
	t = data['t']
	pin = data['pin']

	res = cube([l, w, h]) << [-l/2.0, -w/2.0, 0]
	res -= cube([l - t*2, w - t*2, h + 2]) << [-l/2.0 + t, -w/2.0 + t, -1]
	res += cube([l - t*2, w - t*2, h + 2]) << [-l/2.0 + t, -w/2.0 + t, -1]
	return res


if __name__ == '__main__':
	res = ~box()

	ANODE['l'] = 390
	a1 = anode(ANODE) / [90, 0, 0]
	r = 170
	res += a1 << [0, -r, 200]
	res += a1 << [0, r, 200]

	ANODE['l'] = 300
	a2 = anode(ANODE) / [90, 0, 90]
	r = 220
	res += a2 << [-r, 0, 200]
	res += a2 << [r, 0, 200]

	res.save('box.scad')


