from math import radians, sin, cos, tan

ang = float(input('Difite um ângulo: '))

rad = radians(ang)

sen = sin(rad)
cose = cos(rad)
tang = tan(rad)

print('Ângulo {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(ang, sen, cose, tang))
