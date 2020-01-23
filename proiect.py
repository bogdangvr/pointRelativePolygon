import matplotlib.pyplot as plt

def ecuatiaDreptei(pct1, pct2):
    #Aflam ecuatia dreptei
    a = pct1[1] - pct2[1]
    b = pct2[0] - pct1[0]
    c = pct1[0] * (-a) - pct1[1] * b

    return (a,b,c)

def extremitati(polygon):
    #Determinam cel mai din stanga si din dreapta X
    #Determinam cel mai de sus si de jos Y
    xmin=polygon[0][0]
    xmax=polygon[0][0]

    ymin=polygon[0][1]
    ymax=polygon[0][1]

    for i in range(1, len(polygon)):
        if polygon[i][0] > xmax:
            xmax = polygon[i][0]
        if polygon[i][0] < xmin:
            xmin = polygon[i][0]
        if polygon[i][1] > ymax:
            ymax = polygon[i][1]
        if polygon[i][1] < ymin:
            ymin = polygon[i][1]
    return (xmin, xmax, ymin, ymax)

def testIncluziune(mypct, extrem):
    if mypct[0] < extrem[0] or mypct[0] > extrem[1] or mypct[1] > extrem[3] or mypct[1] < extrem[2]:
        print("Point is located outside the polygon's area")
        return -1

def findmax(p1, p2, index):
	if p1[index] > p2[index]:
		return p1[index], p2[index]
	return p2[index], p1[index]

def intersectie(a, b, c, d):
    dr1 = ecuatiaDreptei(a, b)
    dr2 = ecuatiaDreptei(c, d)
    determinant = dr1[0] * dr2[1] - dr1[1] * dr2[0]
    if determinant != 0:
        xInt = ((-dr1[2]) * dr2[1] + dr1[1] * dr2[2])/determinant
        yInt = ((-dr2[2]) * dr1[0] + dr1[2] * dr2[0])/determinant

        (x1dr, x1st) = findmax(a, b, 0)
        (x2dr, x2st) = findmax(c, d, 0)

        (y1sus, y1jos) = findmax(a, b, 1)
        (y2sus, y2jos) = findmax(c, d, 1)

        if xInt >= x1st and xInt <= x1dr and xInt >= x2st and xInt <= x2dr and yInt >= y1jos and yInt <= y1sus and yInt >= y2jos and yInt <= y2sus:
            if xInt == a[0] and yInt == a[1]:
                print("Point is located outside the polygon's area")
                return 2;
            return True
        else:
            return False
    else:
        if dr1[0] * dr2[1] - dr1[1] * dr2[0] != 0 or dr1[0] * dr2[2] - dr1[2] * dr2[0] != 0 or dr1[1] * dr2[2] - dr1[2] * dr1[1] != 0:
            return -1
        else:
            if a[0] > b[0]:
                a, b = b, a
            if c[0] > d[0]:
                c, d = d, c
            if a[0] >= c[0] and a[0] <= d[0]:
                print ("Point is located outside the polygon's area")
                return 2
            if c[0] >= a[0] and c[0] <= b[0]:
                print ("Point is located outside the polygon's area")
                return 2

def draw(polygon, startPct):
	x = [a[0] for a in polygon]
	y = [a[1] for a in polygon]

	plt.plot(x, y, 'ro')

	plt.plot(startPct[0], startPct[1], 'bo')

	for i in range(len(x)-1):
		connectPoints(x,y,i,i+1)
	
	connectPoints(x,y,0,len(x)-1)

	plt.axis('equal')
	plt.show()

def connectPoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

def main():
	#Date de intrare
	polygon = ((0, 0), (2, 0), (2, 2), (0,2))
	myPct = (3,0)

	draw(polygon, myPct)

	xmin, xmax, ymin, ymax = extremitati(polygon)

	if testIncluziune(myPct, (xmin, xmax, ymin, ymax)) == -1:
		return

	capatDreapta = (xmax+1, myPct[1])
	capatStanga = (xmin-1, myPct[1])

	pctMax = (xmax+1, myPct[1])
	pctMin = (xmin-1, myPct[1])

	pctDreapta = 0
	pctStanga = 0

	for i in range(len(polygon)-1):
		rasp = intersectie(myPct, pctMax, polygon[i], polygon[i+1])
		if rasp == 1:
			pctDreapta += 1
		if rasp == 2:
			return
		rasp = intersectie(myPct, pctMin, polygon[i], polygon[i+1])
		if rasp == 1:
			pctStanga += 1
		if rasp == 2:
			return

	rasp = intersectie(myPct, pctMax, polygon[0], polygon[len(polygon)-1])

	if rasp == 1:
		pctDreapta += 1
	if rasp == 2:
		return
		
	rasp = intersectie(myPct, pctMin, polygon[0], polygon[len(polygon)-1])

	if rasp == 1:
		pctStanga += 1
	if rasp == 2:
		return

	if pctDreapta == 0 or pctStanga == 0:
		print("Point is located outside the polygon's area")
	else:
		print("Point is located inside the polygon's area")


if __name__ == '__main__':
	main()