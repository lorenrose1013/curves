from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    x0 = cx + r * math.sin( math.radians(t) )
    y0 = cy + r * math.cos( math.radians(t) )
    while(t < 360):
    	rad = math.radians(t) 
        x = r * math.sin(rad) + cx
        y = r * math.cos(rad) + cy
        add_edge( points, x0, y0, 0, x, y, 0 )
        x0 = x
        y0 = y
        t += step
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
	#for hermit(points, x0, y0, dx0, dy0, x1, y1, dx1, dy1, step, curve_type )
    if (curve_type == "hermite"):
    	dx0 = x2
    	dy0 = y2
    	dx1 = x3
    	dy1 = y3
        t = 0
        mx = generate_curve_coefs(x0, x1, dx0, dx1, "hermite")
        my = generate_curve_coefs(y0, y1, dy0, dy1, "hermite")
        while(t < 1):
        	ax = mx[0][0]
        	bx = mx[0][1]
        	cx = mx[0][2]
        	dx = mx[0][3]
        	ay = my[0][0]
        	by = my[0][1]
        	cy = my[0][2]
        	dy = my[0][3]
        	x = ((ax) * t ** 3) + ((bx) * t ** 2 ) + ((cx) * t ) + (dx) 
        	y = (3 * ay * t ** 2 ) + (2 * by * t ) + cy
        	add_edge(points, x0, y0, 0, x, y, 0)
        	x0 = x
        	y0 = y
        	t += step
    elif(curve_type == "bezier"):
        t = 0
        mx = generate_curve_coefs(x0, x1, x2, x3, "bezier")
        my = generate_curve_coefs(y0, y1, y2, y3, "bezier")
        while(t < 1):
        	ax = mx[0][0]
        	bx = mx[0][1]
        	cx = mx[0][2]
        	dx = mx[0][3]
        	ay = my[0][0]
        	by = my[0][1]
        	cy = my[0][2]
        	dy = my[0][3]
        	x = ((ax) *  t ** 3) + ((bx) * t ** 2 ) + ((cx) * t ) + (dx) 
        	y = ((ay) *  t ** 3) + ((by) * t ** 2 ) + ((cy) * t ) + (dy) 
        	add_edge(points, x0, y0, 0, x, y, 0)
        	x0 = x
        	y0 = y
        	t += step

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

