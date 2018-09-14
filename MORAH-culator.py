
#Name: Morah David
#Phone Number: 08146139053,09078820715
#E-mail: nzubechukwumorah@gmail.com


#This is an attempt to combine programs, while treating them as seperate programs, but maintaining a link between them, somehow
#Constructive criticism is highly encouraged.
#Please send any observations to """"nzubechukwumorah@gmail.com""""


#AUTHORS NOTE : The sleep() function was used to provide a "feel" for the user to enhance User Experience.

#___________________________________________________PROGRAM___________________________________________________________


#Import Required Libraries that will be used later in the program
import time
import math
from math import pi

#defining functions to process requests
def program_request_options():
    print("Select the operation to be carried out by entering the corresponding number.")
    print("          1 --------- Calculate PERIMETER")
    print("          2 --------- Calculate AREA")
    print("          3 --------- Calculate VOLUME")
    print("          4 --------- Calculate SURFACE AREA")
    print("          9 --------- Exit 'MORAH-culator'")
    
def perimeter_shapes():
    print(" 1 ----- Square")
    print(" 2 ----- Rectangle")
    print(" 3 ----- Triangle")
    print(" 4 ----- Circle")
    print(" 5 ----- Parallelogram")
    print(" 6 ----- Rhombus")
    print(" 7 ----- Trapezoid")
    print("enter any other number to Return to previous menu")

def volume_shapes():
    print("1 ----- Cube")
    print("2 ----- Rectangular Prism")
    print("3 ----- Cylinder")
    print("4 ----- Cone")
    print("5 ----- Sphere")
    print("6 ----- Ellipsoid")

def area_shapes():
    print("1 ----- Square")
    print("2 ----- Rectangle")
    print("3 ----- Trapezoid")
    print("4 ----- Parallelogram")
    print("5 ----- Circle")
    print("6 ----- Ellipse")
    print("7 ----- Triangle")
    print("8 ----- Sphere")

def square_perimeter():
    length = float(input("Length of a side:\n"))
    result = (4*length)
    result = round(result,3)
    return result

def rectangle_perimeter():
    length = float(input("Length  :  "))
    breadth = float(input("Breadth  :  "))
    result = ((2*length)+(2*breadth))
    result = round(result,3)
    return result

def triangle_perimeter():
    a = float(input("Length of side 'A'  :  "))
    b = float(input("Length of side 'B'  :  "))
    c = float(input("Length of side 'C'  :  "))
    result = (a + b + c)
    result = round(result,3)
    return result

def circle_perimeter():
    radius = float(input("Enter the radius of the circle"))
    result = (2*pi)*(radius)
    result = round(result,3)
    return result

def parallelogram_perimeter():
    base_length = float(input("Enter length of base  :  "))
    side_length = float(input("Enter length of side  :  "))
    result = 2(base_length + side_length)
    result = round(result,3)
    return result

def rhombus_perimeter():
    side = float(input("Length of a side   :   "))
    result = (4*side)
    result = round(result,3)
    return result
    
def trapezoid_perimeter():
    a = float(input("Length of side A   :   "))
    b = float(input("Length of side B   :   "))
    c = float(input("Length of side C   :   "))
    d = float(input("Length of side D   :   "))
    result = (a + b + c + d)
    result = round(result,3)
    return result

def square_area():
    L = float(input("Enter the length of the square   :  "))
    result = L**2
    result = round(result,3)
    return result

def rectangle_area():
    L = float(input("Enter the length of the rectangle     :     "))
    B = float(input("Enter the breadth of the rectangle    :     "))
    result = L*B
    result = round(result,3)
    return result

def parallelogram_area():
    b = float(input("Base of parallelogram    :     "))
    h = float(input("Height of parallelogram   :     "))
    result = b*h
    result = round(result,3)
    return result

def trapezoid_area():
    a = float(input("Enter length of one side   :   "))
    b = float(input("Enter length of opposite side    :    "))
    h = float(input("Enter height of the trapezoid   :      "))
    result = (0.5* (a + b) * h)
    result = round(result,3)
    return result

def circle_area():
    radius = float(input("Radius of the citrcle:"))
    result = (pi * (radius**2))
    result = round(result,3)
    return result

def Ellipse_area():
    radius_minor = float(input("Radius along minor axis  :  "))
    radius_major = float(input("Radius along major axis  :   "))
    result = (pi*(radius_major*radius_minor))
    result = round(result,3)
    return result

def right_angled_triangle_area():
    base = float(input("Base of the triangle    :    "))
    height = float(input("Height of the triangle   :    "))
    result = 0.5*(base*height)
    result = round(result,3)
    return result

def angled_triangle_area():
    a = float(input("Length of a side     :    "))
    b = float(input("Length of another side      :    "))
    c = float(input("Angle between them    :     "))
    result = ((0.5)*a*b)*(math.sin(c))
    result = round(result,3)
    return result

def  all_sided_triangle_area():
    a = float(input("Length of side A   :      "))
    b = float(input("Length of side B   :      "))
    c = float(input("Length of side C   :      "))
    s = (( a + b + c )/2)
    var = s*(s-a)*(s-b)*(s-c)
    result = math.sqrt(var)
    result = round(result,3)
    return result

def select_triangle_area_method():
    
    selection = 0
    #while selection != 9 :
    print()
    print("Which values are available for the given triangle?")
    print(" 1. A Right-Angled triangle with values of base and height")
    print(" 2. A Triangle given Length of two sides and the angle between them")
    print(" 3. A Triangle given Length of all its sides ONLY")
    #print(" 9. Exit")
    print()
    selection = int(input("Selection      :     "))
    if selection == 1:
        return right_angled_triangle_area()
    elif selection == 2:
        return angled_triangle_area()
    elif selection ==3:
        return all_sided_triangle_area()
    else:
        print("Invalid input. Please check and try again.")
    


    
def sphere_area():
    radius = float(input("Enter radius of the sphere     :     "))
    result  = (4*pi*(radius**2))
    result = round(result,3)
    return result

def cube_volume():
    S = float(input("Length of side of cube    :    "))
    result = S**3
    result = round(result,3)
    return result

def rect_prism_volume():
    length = float(input("Length of the Prism    :    "))
    width = float(input("Width of the Prism    :      "))
    height = float(input("Height of the Prism    :    "))
    result = (length * width * height)
    result = round(result,3)
    return result

def cylinder_volume():
    radius = float(input("Radius of the Cylinder       :     "))
    height = float(input("Height of the Cylinder      :     "))
    result = ((pi*(radius**2))*(height))
    result = round(result,3)
    return result

def cone_volume():
    r = float(input("radius of the cone's base     :    "))
    h = float(input("height of the cone     :     "))
    result = ((1/3)*(pi*(r ** 2) *h))
    result = round(result,3)
    return result

def sphere_volume():
    r =float(input("Radius of the sphere     :     "))
    result = ((4/3)*(pi*(r**3)))
    result = round(result,3)
    return result

def ellipsiod_volume():
    r1 = float(input("Radius 1    :     "))
    r2 = float(input("Radius 2    :     "))
    r3 = float(input("Radius 3    :     "))
    result = ((4/3)*pi*(r1*r2*r3))
    result = round(result,3)
    return result

def surface_area_shapes():
    print(" 1 ----- Cube")
    print(" 2 ----- Rectangular Prism")
    print(" 3 ----- Sphere")
    print(" 4 ----- Cylinder")

def cube_SA():
    S = float(input("Length of side     :      "))
    result = (6 * (S**2))
    result = round(result,3)
    return result

def sphere_SA():
    radius = float(input("Radius of Sphere:"))
    result = 4*pi*(radius**2)
    result = round(result,3)
    return result

def rect_prism_SA():
    length = float(input("Length of the Prism    :    "))
    width = float(input("Width of the Prism    :      "))
    height = float(input("Height of the Prism    :    "))
    result = ((2*length*width) + (2*length*height) + (2*width*height))
    result = round(result,3)
    return result

def cylinder_SA():
    radius = float(input("Radius of the Cylinder        :     "))
    height = float(input("height of the Cylinder        :       "))
    result =((2*pi*(radius**2)) + (2*pi*radius*height))
    result = round(result,3)
    return result

#Naming method was selected due to the nature of the program to avoid variable interference  

def  MORAH_CULATOR():
    
    #Salutataion
    print("               **Morah-Culator**               ")
    time.sleep(1.5)
    print("Good day!")
    print()
    time.sleep(1.5)
    print("----------This program calculates VOLUME , AREA, PERIMETER or SURFACE AREA of a Given shape.")
    print()
    time.sleep(1.5)
    #Space was intentional to ensuer that Attrention is paid Attention
    print("       **********ATTENTION!!!    All units must be in centimeters**********  ")

    print()
    print()
    
    print("To continue, please enter 'yes' on the keyboard\nOtherwise, enter anything else or nothing at all.")
    time.sleep(1.5)
    begin = input("Do you wish to continue ? \n")

    if begin == "yes":
        program_request = 0
        
      # Incorporating exit method as condiion for loopuing.   
    while program_request != 9:

        program_request_options()
        program_request = int(input("Choice:"))
        #Bunches of ifs and elifs that reflect the selected options
        if program_request == 1:

            print("Perimeter was selected.")
            time.sleep(1.5)
            
            continue_checking_perimeter = "y"
            #Menu management variable
            while continue_checking_perimeter == "y":
                print("Choose a shape whose perimeter you wish to calculate:")
                perimeter_shapes()

                choice = int(input("Choice :  "))
                if choice == 1:

                    print("Square was selected")
                    continue_square_peri = "y"
                    #Concurrent calculation management variable
                    while continue_square_peri == "y":

                        run_square_peri_def = square_perimeter()
                        print("The perimeter of the square is "+str(run_square_peri_def) +"cm")
                        time.sleep(4.5)
                        continue_square_peri = input("Would you like to calculate again?    ( y / n)")

                elif choice == 2:

                    print("Rectangle was selected")
                    continue_rect_peri = "y"
                    #Concurrent calculation management variable
                    while continue_rect_peri == "y":

                        run_rect_peri_def = rectangle_perimeter()
                        print("The perimeter of the rectangle is "+str(run_rect_peri_def)+"cm")
                        time.sleep(4.5)
                        continue_rect_peri = input("Calculate Again?    (y / n)")

                elif choice == 3:
                    print("Triangle was selected")
                    continue_tri_peri = "y"
                    #Concurrent calculation management variable
                    while continue_tri_peri == "y":

                        run_tri_peri_def = triangle_perimeter()
                        print("The perimeter of the triangle is "+ str(run_tri_peri_def) + "cm")
                        time.sleep(4.5)
                        continue_tri_peri = input("Calculate Again?      (y / n)")

                elif choice == 4:
                    print("Circle was selected")
                    continue_circle_peri = "y"
                    #Concurrent calculation management variable
                    while continue_circle_peri == "y":

                        run_circle_peri_def = circle_perimeter()
                        print("The perimeter of the circle is "+str(run_circle_peri_def) +"cm")
                        time.sleep(4.5)
                        continue_circle_peri = input("Calculate Again?        (y / n)")

                elif choice == 5:

                    print("Parallelogram was selected")
                    continue_para_peri = "y"
                    #Concurrent calculation management variable
                    while continue_para_peri == "y":

                        run_para_peri_def = parallelogram_perimeter()
                        print("The perimeter of the parallelogram is " + str(run_para_peri_def) + "cm")
                        time.sleep(4.5)
                        continue_para_peri = input("Calculate Again?      (y / n)")

                elif choice == 6:

                    print("Rhombus was selected")
                    continue_rhomb_peri = "y"
                    #Concurrent calculation management variable
                    while continue_rhomb_peri == "y":
                        run_rhomb_peri_def = rhombus_perimeter()
                        print("The perimeter of the rhombus is " + str(run_rhomb_peri_def) + "cm")
                        time.sleep(4.5)
                        continue_rhomb_peri = input("Calculate Again?      (y / n)")
                
                elif choice == 7:

                    print("Trapezoid was selected")
                    continue_trap_peri = "y"
                    #Concurrent calculation management variable
                    while continue_trap_peri == "y":
                        run_trap_peri_def = trapezoid_perimeter()
                        print("The perimeter of the trapezoid is " + str(run_trap_peri_def) + "cm")
                        time.sleep(4.5)
                        continue_trap_peri = input("Calculate Again?     (y / n)")
                continue_checking_perimeter = input("do you wish to continue calculating perimeter of shapes? \nEnter 'y' to continue. Otherwise enter anything else to exit.")
        
        elif program_request == 2:
            print("Area was selected")
            time.sleep(1.5)
            continue_checking_area = "y"
            while continue_checking_area == "y":
                print("Choose a shape whose area you wish to calculate")
                area_shapes()

                area_decision = int(input("Choice: "))
            
                if area_decision == 1:
                    print("Square was selected.")
                    continue_square_area = "y"
                    #Concurrent calculation management variable
                    while continue_square_area == "y":
                        run_square_area_def = square_area()
                        print("The area of the square is " + str(run_square_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_square_area = input("Calculate Again?     (y / n)")

                elif area_decision == 2:
                    print("Rectangle was selected.")
                    continue_rect_area = "y"
                    #Concurrent calculation management variable
                    while continue_rect_area == "y":
                        run_rect_area_def = rectangle_area()
                        print("The area of the rectangle is " + str(run_rect_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_rect_area = input("Calculate Again?       (y / n)")

                elif area_decision == 3:
                    print("Trapezoid was selected")
                    continue_trap_area = "y"
                    #Concurrent calculation management variable
                    while continue_trap_area ==  "y":
                        run_trap_area_def = trapezoid_area()
                        print("The area of the Trapeziod is " + str(run_trap_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_trap_area = input("Calculate Again?       (y / n)")

                elif area_decision == 4:
                    print("Parallelogram was selected")
                    continue_para_area = "y"
                    #Concurrent calculation management variable
                    while continue_para_area == "y":
                        run_para_area_def = parallelogram_area()
                        print("The area of the Parallelogram is " + str(run_para_area_def) +"cm^2")
                        time.sleep(4.5)
                        continue_para_area = input("Calculate Again?       (y / n)")

                elif area_decision == 5:
                    print("Circle was selected")
                    continue_circle_area = "y"
                    #Concurrent calculation management variable
                    while continue_circle_area == "y":
                        run_circle_area_def = circle_area()
                        print("The area of the Circle is " + str(run_circle_area_def) +"cm^2")
                        time.sleep(4.5)
                        continue_circle_area = input("Calculate Again?       (y / n)")

                elif area_decision == 6:
                    print("Ellipse was selected.")
                    continue_ellipse_area = "y"
                    #Concurrent calculation management variable

                    while continue_ellipse_area == "y":
                        run_ellipse_area_def = ellipse_area()
                        print("The area of the Ellipse is " + str(run_ellipse_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_circle_area = input("Calculate Again?       (y / n)")

                elif area_decision == 7:
                    print("Triangle was selected.")
                    continue_triangle_area = "y"
                    #Concurrent calculation management variable
                    while continue_triangle_area == "y":
                        run_triangle_area_def = select_triangle_area_method()
                        print("The area of the triangle is " + str(run_triangle_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_triangle_area = input("Calculate Again?       (y / n)")

                elif area_decision == 8:
                    print("Sphere was seelected.")
                    continue_sphere_area = "y"
                    #Concurrent calculation management variable
                    while continue_sphere_area == "y":
                        run_sphere_area_def = sphere_area()
                        print("The area of the sphere is " + str(run_sphere_area_def) + "cm^2")
                        time.sleep(4.5)
                        continue_sphere_area = input("Calculate Again?         (y / n)")
                continue_checking_area = input("Do you wish to continue checking Area of Shapes? \nEnter  'y'  to continue otherwise enter anything else to exit.")
        
        elif program_request == 3:
            print("Volume was selected.")
            time.sleep(1.5)

            continue_checking_volume = "y"

            while continue_checking_volume == "y":
                
                print("Choose a shape whose Volume you wish to calculate:")
                volume_shapes()

                volume_decision = int(input("Choice :  "))
                if volume_decision == 1:
                    print("Cube was selected.")
                    continue_cube_volume = "y"
                    #Concurrent calculation management variable
                    while continue_cube_volume == "y":
                        run_cube_volume_def = cube_volume()
                        print("The volume of the Cube is " +str(run_cube_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_cube_area = input("Calculate Again?      (y / n)")
                elif volume_decision == 2:
                    print("Rectangular Prism was selected.")
                    continue_rectprism_volume = "y"
                    #Concurrent calculation management variable
                    while continue_rectprism_volume == "y":
                        run_rectprism_volume_def = rect_prism_volume()
                        print("The volume of the Rectangular Prism is " +str(run_rectprism_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_rectprism_volume = input("Calculate Again?      (y / n)")

                elif volume_decision == 3:
                    print("Cylinder was selected.")
                    continue_cylinder_volume = "y"
                    #Concurrent calculation management variable
                    while continue_cylinder_volume == "y":
                        run_cylinder_volume_def = cylinder_volume()
                        print("The volume of the Cylinder is " +str(run_cylinder_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_cylinder_volume = input("Calculate Again?      (y / n)")

                elif volume_decision == 4:
                    print("Cone was selected.")
                    continue_cone_volume = "y"
                    #Concurrent calculation management variable
                    while continue_cone_volume == "y":
                        run_cone_volume_def = cone_volume()
                        print("The volume of the Cone is " +str(run_cone_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_cone_volume = input("Calculate Again?      (y / n)")

                elif volume_decision == 5:
                    print("Sphere was selected.")
                    continue_sphere_volume = "y"
                    #Concurrent calculation management variable
                    while continue_sphere_volume == "y":
                        run_sphere_volume_def = sphere_volume()
                        print("The volume of the Sphere is " +str(run_sphere_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_sphere_volume = input("Calculate Again?      (y / n)")

                elif volume_decision == 6:
                    print("Ellipsoid was selected.")
                    continue_ellipsoid_volume = "y"
                    #Concurrent calculation management variable
                    while continue_ellipsoid_volume == "y":
                        run_ellipsoid_volume_def = ellipsoid_volume()
                        print("The volume of the Ellipsoid is " +str(run_ellipsoid_volume_def)+"cm^3")
                        time.sleep(4.5)
                        continue_ellipsoid_volume = input("Calculate Again?      (y / n)")


                continue_checking_volume = input("Do you wish to continue calculating Volume of shapes?\nEnter 'y' to continue. Otherwise enter anything else to exit ")
            
        elif program_request == 4:
            print("Surface Area (SA) was selected.")
            time.sleep(1.5)

            continue_checking_SA = "y"

            while continue_checking_perimeter == "y":
                print("Choose a shape whose Surface Area you wish to calculate?")
                surface_area_shapes()

                SA_decision = int(input("Choice    :   "))
                if SA_decision == 1:

                    print("Cube was selected.")
                    continue_cube_SA = "y"
                    #Concurrent calculation management variable
                    while continue_cube_SA == "y":
                
                        run_cube_SA_def = cube_SA()
                        print("The Surface Area of the Cube is " + str(run_cube_SA_def) + "cm^2")
                        time.sleep(4.5)
                        continue_cube_SA = input("Calculate Again ?            (y / n)")

                elif SA_decision == 2:

                    print("Rectangular Prism was selected.")
                    continue_rect_prism_SA = "y"
                    #Concurrent calculation management variable
                    while continue_rect_prism_SA == "y":

                        run_rect_prism_SA_def = rect_prism_SA()
                        print("The Surface Area of the Rectangular Prism is " + str(run_rect_prism_SA_def) + "cm^2")
                        time.sleep(4.5)
                        continue_rect_prism_SA = input("Calculate Again ?            (y / n)")

                elif SA_decision == 3:

                    print("Sphere was selected.")
                    continue_sphere_SA = "y"
                    #Concurrent calculation management variable
                    while continue_sphere_SA == "y":

                        run_sphere_SA_def = sphere_SA()
                        print("The Surface Area of the Sphere is " + str(run_sphere_SA_def) + "cm^2")
                        time.sleep(4.5)
                        continue_Sphere_SA = input("Calculate Again ?            (y / n)")

                elif SA_decision == 4:

                    print("Cylinder was selected.")
                    continue_cylinder_SA = "y"
                    #Concurrent calculation management variable
                    while continue_cylinder_SA == "y":

                        run_cylijnder_SA_def = cylinder_SA()
                        print("The Surface Area of the Cylinder is " + str(run_cylinder_SA_def) + "cm^2")
                        time.sleep(4.5)
                        continue_cylinder_SA = input("Calculate Again ?            (y / n)")

                else:
                    print("Invalid Input. Please check and try again.")

            #Check to exit sub-menu (of some sort)
            continue_checking_SA = input("Do you wish to continue calculating Surface Area of shapes?\nEnter 'y' to continue. Otherwise enter anything else to exit ")

        else:
            print("Invalid Input. Please check and enter again.")
     #Gratitude                       
    print("Thank you for using this program!.")
    time.sleep(1)
    print("Goodbye!")
    #Workaround for immediate closure if using python_exe_window.
    #                              (*~*)                      (^_^)
    time.sleep(4)


# program.... incorporating defs from defs in def.

MORAH_CULATOR()           
                    
                                           
        
            
            
            
        
        






        
            
        
        
        
        
        
    
    
