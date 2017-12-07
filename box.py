#!/usr/bin/python


from opyscad import *


H = 400.0
L1 = 450.0
W1 = 350.0
L2 = 500.0
W2 = 400.0
T = 2.0


def part(dt, dh):
	global H, L1, W1, L2, W2
	r1 = cube([L1 + dt*2, W1 + dt*2, 1]) << [-L1/2.0 - dt, -W1/2.0 - dt, dh]
	r2 = cube([L2 + dt*2, W2 + dt*2, 1]) << [-L2/2.0 - dt, -W2/2.0 - dt, H + dh]

	return hull() (r1, r2)

def box():
	return part(T, -T) - part(0, 0)


if __name__ == '__main__':
	box().save('box.scad')


