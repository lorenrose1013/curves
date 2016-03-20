from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    file_contents = f.readlines()
    i = 0
    while (i < len(file_contents) ):
        line = file_contents[i]
        print line
        line.replace("\n", "")
        if ("line" in line):
        	#add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
            args = file_contents[i+1]
            print args
            args = args.split(" ")
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            i += 1
        elif("circle" in line):
        	#add_circle( points, cx, cy, cz, r, step ):
            args = file_contents[i+1]
            args = args.split(" ")
            add_circle(points, int(args[0]), int(args[1]), int(args[2]), 0, 1)
            i+=1
        elif("hermite" in line):
        	#add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
        	#for hermit(points, x0, y0, dx0, dy0, x1, y1, dx1, dy1, step, curve_type )
            args = file_contents[i+1]
            args = args.split(" ")
            add_circle(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]), 1, "hermite")
            i += 1
        elif("b" in line):
            #add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
        	#for bezier(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type )
            args = file_contents[i+1]
            args = args.split(" ")
            add_circle(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]), int(args[6]), int(args[7]), 1, "bezier")
            i += 1
        elif("ident" in line):
            ident(transform)
        elif("scale" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            scalar = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(scalar, transform)
            i += 1
        elif("translate" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            trans = make_translate(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(trans, transform)
            i += 1
        elif("xrotate" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            xRot = make_rotX(int(args[0]))
            matrix_mult(xRot, transform)
            i += 1      
        elif("yrotate" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            yRot = make_rotY(int(args[0]))
            matrix_mult(yRot, transform)
            i += 1      
        elif("zrotate" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            zRot = make_rotZ(int(args[0]))
            matrix_mult(zRot, transform)
            i += 1       
        elif("apply" in line):
            matrix_mult(transform, points)      
        elif("display" in line):
            draw_lines(points, screen, color) 
            #display(screen) 
            print screen   
        elif("save" in line):
            args = file_contents[i+1]
            args = args.split(" ")
            draw_lines(points, screen, color)
            save_ppm(screen, args[0])
            i+=1
        i+=1

