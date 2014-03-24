## File: Mondrian.py
## Description: Colorful tree, drawing art recursively.
##              This program draws a colorful tree and a star circle recusively
##              Features: (1)interactive: prompt user to inpput the length of tree,
##              which defines the order of recursion. (2) Starting with a random RGB
##              color set and then change the color gradually.
##              Total time consumed: 3 hours
## Author: Xiaoqin LI
## Date Created: 03/04/2014
## Date Last Modified:03/07/2014

import turtle
import tkinter 
import random

#draw a tree recursively
def drawTree (ttl, length, RGB):
  # Changing color gradually in each recursion case. Reset any components
  # of RGB to zero if they reach 255.
  if RGB[0] == 255:
      if RGB[2] == 255:
          RGB[2] = 0
      if RGB[1] != 255:
          RGB[1] += 1
      else:
          RGB[0] = 0
  elif RGB[1] == 255:
      if RGB[2] != 255:
          RGB[2] += 1
      else:
          RGB[1] = 0      
  elif RGB[2] == 255:
      if RGB[0] != 255:
          RGB[0] += 1
      else:
          RGB[2] = 0
    
  ttl.pencolor (RGB)
  # branches have different length and angle, which increases diversity.
  if length > 5:
    ttl.forward (length/4)
    ttl.left (30)
    drawTree (ttl, (length/3)*2, RGB)
    ttl.right(30)
    ttl.backward (length/4)

    ttl.forward (length/2)
    ttl.right (25)
    drawTree (ttl, length/2, RGB)
    ttl.left(25)
    ttl.backward (length/2)

    ttl.forward (5/6*length)
    ttl.right (25)
    drawTree (ttl, length/2, RGB)
    ttl.left(25)
    ttl.backward (5/6*length)

#draw a star circle recursively
def drawstar(ttl,length, angle,RGB,num):

    if RGB[0] == 255:
       RGB[1] += 3
    elif RGB[1] == 255:
       RGB[2] += 3  
    elif RGB[2] == 255:
       RGB[0] += 3
    num -= 1
    if num < 0:
        return
    else:
        ttl.pencolor (RGB)
        ttl.penup()
        ttl.forward(length) 
        ttl.left(angle)
        ttl.pendown()
        for j in range(5):
            ttl.forward(10)
            ttl.right(144)
            ttl.forward(10)
            ttl.left(72)
        drawstar(ttl,length, angle,RGB,num)
            
def main():
  # prompt the user to enter a branch length

  print("Colorful Tree")
  print()
  
  length = int (input ('Enter branch length(suggested:300-400): '))

  # put label on top of page
  turtle.title ('Colorful Tree')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create Turtle object
  ttl = turtle.Turtle()
  
  # assign a background color to the turtle object
  turtle.bgcolor('black')
  # color mode: RGB
  turtle.colormode(255)

  ttl.speed(10)
  # Write some text on the canvas.
  ttl.penup()
  ttl.goto( 0, -345 )
  ttl.pendown()
  ttl.pencolor ([253,227,0])
  ttl.write('Colorful Tree', False, align = "center", font = ("Arial", 14, "italic"))
  ttl.penup()
  ttl.goto( 0, -365 )
  ttl.pendown()
  ttl.write('CS313E',False,align = "center", font = ("Times", 14,"italic"))
  ttl.penup()

  ttl.goto(-10, -300)
  # Randomly generate starting point of RGB color set
  RGB_index = random.randint(0,2)
  RGB_list = [0,0,0]
  RGB_list[RGB_index] = 255

  # draw five angle stars in a circle.
  star_rotation = 5
  star_num = 360/star_rotation
  drawstar(ttl,length/15,star_rotation,RGB_list,star_num)


  RGB_index = random.randint(0,2)
  RGB_list = [0,0,0]
  RGB_list[RGB_index] = 255
  # draw the colorful tree
  ttl.penup()
  ttl.goto (0, -300)
  ttl.pendown()
  ttl.left (90)
  ttl.pendown()
  drawTree (ttl, length, RGB_list)
  ttl.penup()
  
  ttl.hideturtle()

  #save the final plot as an .eps file
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file = "Mondrian.eps")

  # persist drawing
  turtle.done()

main()

