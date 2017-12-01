from opyscad import *


x_beg = -32.0
y2 = -15.0
FN = 32

CHAMBER = 	[
				{
					'point': [x_beg, y2, 0],
					'd_in': 8,
					'd_out': 11
				},
				{
					'point': [-20, y2, 0],
					'd_in': 8,
					'd_out': 11
				},
				{
					'point': [0, 0, 0],
					'd_in': 16,
					'd_out': 19
				},
				{
					'point': [17, 0, 0],
					'd_in': 8,
					'd_out': 11
				},
				{
					'point': [27, 0, 0],
					'd_in': 8,
					'd_out': 11
				},
			]

NEEDLE = 	[
				{
					'point': [x_beg, 0, 0],
					'd_in': 8,
					'd_out': 11
				},
				{
					'point': [-8, 0, 0],
					'd_in': 7,
					'd_out': 10
				},
				{
					'point': [2, 0, 0],
					'd_in': 3,
					'd_out': 5
				},
				{
					'point': [14, 0, 0],
					'd_in': 3,
					'd_out': 4
				},
			]


def section(postfix, beg, end):
	beg_s = sphere(d = beg['d_' + postfix], fn=FN) << beg['point']
	end_s = sphere(d = end['d_' + postfix], fn=FN) << end['point']
	return hull() (beg_s, end_s)

def pipe(path, inner_only = False):
	joints = []
	outer = union()
	inner = union()
	prev = path[0]
	for curr in path[1:]:
		outer += section('out', prev, curr)
		inner += section('in', prev, curr)
		prev = curr

	if inner_only:
		res = inner
	else:
		res = outer - inner

	x, y, z = path[0]['point']
	res -= cube([100, 100, 100]) << [x-100, y - 50, z - 50]
	x, y, z = path[-1]['point']
	res -= cube([100, 100, 100]) << [x, y - 50, z - 50]

	return res

def chamber():
	chamber = pipe(CHAMBER)
	chamber -= pipe(NEEDLE, True)
	chamber += pipe(NEEDLE)
	#chamber -= cube([100,100,100]) << [-50,-50,0]
	#chamber += ~(cylinder(h=27, d=14)/[0,90,0]) << [-50,0,0]
	#chamber += ~(cylinder(h=27, d=14)/[0,90,0]) << [-50,y2,0]
	#chamber += ~(cylinder(h=27, d=14)/[0,90,0]) << [20,0,0]


	return chamber


