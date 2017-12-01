from opyscad import *
import math


R_IN = 11.0/2
R_OUT = 14.0/2
WAVE_DH_MIN = 0
WAVE_DH_MAX = 0.5
PART_R_IN = 8.0/2
PART_L = 4.0
WAVE_ANGLE = 20/180.0*math.pi
FN = 32


def wave(x0, l, space_beg):
	period = (WAVE_DH_MAX - WAVE_DH_MIN)/math.tan(WAVE_ANGLE)*2
	n = int(l/period)
	dl = l - n*period

	res = []

	res.append([x0, R_IN + WAVE_DH_MAX])
	x = x0
	if space_beg and dl > 0:
		x += dl
		res.append([x, R_IN + WAVE_DH_MAX])

	for i in range(n):
		x += period/2
		res.append([x, R_IN + WAVE_DH_MIN])

		x += period/2
		res.append([x, R_IN + WAVE_DH_MAX])

	if (not space_beg) and dl > 0:
		x += dl
		res.append([x, R_IN + WAVE_DH_MAX])

	return res

def coupling(l1, wave1, l2, wave2):
	bevel_l = WAVE_DH_MAX/math.tan(WAVE_ANGLE)
	l = l1 + PART_L + l2

	if wave1:
		res = wave(0, l1, False)
	else:
		res = [[0, R_IN + WAVE_DH_MAX], [bevel_l, R_IN], [l1, R_IN]]

	res.append([l1 + PART_L/2.0, PART_R_IN])

	if wave2:
		res += wave(l1 + PART_L, l2, True)
	else:
		res += [[l - l2, R_IN], [l - bevel_l, R_IN], [l, R_IN + WAVE_DH_MAX]]

	res.append([l, R_OUT])
	res.append([0, R_OUT])

	poly = polygon(res)
	return rotate_extrude(fn=FN)(poly/[0, 0, 90])


	return res

