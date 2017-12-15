#!/usr/bin/python


from opyscad import *


BASE_H = 200
BASE_Z = 10
BASE_W_IN = 13
BASE_W_OUT = 16
BASE_LEG_L = 150
BASE_LEG_H = 4
LEG_L	= 100
LEG_W = 5
LEG_H1	= 8
LEG_Z1	= BASE_Z + 0.5
LEG_H2	= 5
LEG_Z2	= 2

ROD_H = 200
ROD_W_IN = 10
ROD_W_OUT = 12


def leg():
	points = [	[0, LEG_Z1],
				[LEG_L - LEG_W, LEG_Z2],
				[LEG_L - LEG_W, 0],
				[LEG_L, 0],
				[LEG_L, LEG_Z2],
				[LEG_L, LEG_Z2 + LEG_H2],
				[0, LEG_Z1 + LEG_H1] ]
	poly = polygon(points)
	res = linear_extrude(LEG_W)(poly)
	return (res / [90, 0, 0]) << [0, LEG_W/2.0, 0]


def base():
	res = leg()
	res += leg() / [0, 0, 120]
	res += leg() / [0, 0, 240]

	res += cube([BASE_W_OUT, BASE_W_OUT, BASE_H]) << [-BASE_W_OUT/2.0, -BASE_W_OUT/2.0, BASE_Z]
	res -= cube([BASE_W_IN, BASE_W_IN, BASE_H + BASE_Z + 2]) << [-BASE_W_IN/2.0, -BASE_W_IN/2.0, -1]
	return res

def rod():
	res = cube([ROD_W_OUT, ROD_W_OUT, ROD_H]) << [-ROD_W_OUT/2.0, -ROD_W_OUT/2.0, 0]
	res -= cube([ROD_W_IN, ROD_W_IN, ROD_H+2]) << [-ROD_W_IN/2.0, -ROD_W_IN/2.0, -1]
	return res

def main():
	res = base()
	res += rod() << [0, 0, 150]
	res.save('hanger.scad')


if __name__ == '__main__':
	main()


