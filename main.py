"""
goal of this project

- create a project to visualize algorithms such as
bubble sort, insertion sort, quicksort and merge sort

- the numbers will be like rectangles and the value of each number
represents the height

- each rectangle will have a unique color, the goal is to have a good design
and the visualization should be clear

outcomes of this project:

- better understanding of sorting algorithms
- better standing of using turtle module in python
- a good project to include in the resume

"""

from random import *
from Rectangle import *

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.colormode(255)
my_screen.setup(850, 700)
y = -(700/2)
n = 80


def selection_sort(list_rectangles, size):  # selection sort O(N^2)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if list_rectangles[j].rectangle.height < list_rectangles[min_index].rectangle.height:
                min_index = j
        if i != min_index:
            temp = list_rectangles[min_index]
            list_rectangles[min_index] = list_rectangles[i]
            list_rectangles[i] = temp
            xcor_current = list_rectangles[i].rectangle.xcor()
            xcor_successor = list_rectangles[min_index].rectangle.xcor()
            list_rectangles[i].rectangle.goto(xcor_successor, y)
            list_rectangles[min_index].rectangle.goto(xcor_current, y)


def bubble_sort(list_rectangles, size):  # bubble sort O(N^2)
    for i in range(size):
        for j in range(size-1):
            if list_rectangles[j].rectangle.height > list_rectangles[j+1].rectangle.height:
                temp = list_rectangles[j+1]
                list_rectangles[j+1] = list_rectangles[j]
                list_rectangles[j] = temp
                xcor_current = list_rectangles[j].rectangle.xcor()
                xcor_successor = list_rectangles[j+1].rectangle.xcor()
                list_rectangles[j].rectangle.goto(xcor_successor, y)
                list_rectangles[j+1].rectangle.goto(xcor_current, y)


def insertion_sort(list_rectangles, size):  # insertion sort O(N^2)
    for i in range(1, size):
        temp = list_rectangles[i]
        j = i-1
        while j >= 0 and temp.rectangle.height < list_rectangles[j].rectangle.height:
            temp = list_rectangles[j+1]
            list_rectangles[j + 1] = list_rectangles[j]
            list_rectangles[j] = temp
            xcor_current = list_rectangles[j].rectangle.xcor()
            xcor_successor = list_rectangles[j + 1].rectangle.xcor()
            list_rectangles[j+1].rectangle.goto(xcor_current, y)
            list_rectangles[j].rectangle.goto(xcor_successor, y)
            j -= 1


def insertion_sort_desc(list_rectangles, size):  # insertion sort O(N^2)
    for i in range(1, size):
        temp = list_rectangles[i]
        j = i-1
        while j >= 0 and temp.rectangle.height > list_rectangles[j].rectangle.height:
            temp = list_rectangles[j+1]
            list_rectangles[j + 1] = list_rectangles[j]
            list_rectangles[j] = temp
            xcor_current = list_rectangles[j].rectangle.xcor()
            xcor_successor = list_rectangles[j + 1].rectangle.xcor()
            list_rectangles[j+1].rectangle.goto(xcor_current, y)
            list_rectangles[j].rectangle.goto(xcor_successor, y)
            j -= 1


def selection_sort_desc(list_rectangles, size):  # selection sort O(N^2)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if list_rectangles[j].rectangle.height > list_rectangles[min_index].rectangle.height:
                min_index = j
        if i != min_index:
            temp = list_rectangles[min_index]
            list_rectangles[min_index] = list_rectangles[i]
            list_rectangles[i] = temp
            xcor_current = list_rectangles[i].rectangle.xcor()
            xcor_successor = list_rectangles[min_index].rectangle.xcor()
            list_rectangles[i].rectangle.goto(xcor_successor, y)
            list_rectangles[min_index].rectangle.goto(xcor_current, y)


def bubble_sort_desc(list_rectangles, size):  # bubble sort O(N^2)
    for i in range(size):
        for j in range(size-1):
            if list_rectangles[j].rectangle.height < list_rectangles[j+1].rectangle.height:
                temp = list_rectangles[j+1]
                list_rectangles[j+1] = list_rectangles[j]
                list_rectangles[j] = temp
                xcor_current = list_rectangles[j].rectangle.xcor()
                xcor_successor = list_rectangles[j+1].rectangle.xcor()
                list_rectangles[j].rectangle.goto(xcor_successor, y)
                list_rectangles[j+1].rectangle.goto(xcor_current, y)


def rectangles_setup(list_numbers):  # this changes the list numbers to actual rectangles
    x = 10
    size = len(list_numbers)
    list_rectangles = []
    for i in range(size):
        tracer(100)
        rectangle_object = Rectangle(list_numbers[i])
        rectangle_object.rectangle.speed(1000)
        rectangle_object.rectangle.goto((-395 + (x * i)), y)
        list_rectangles.append(rectangle_object)
    tracer(1)
    return list_rectangles


def list_setup(size):  # this function creates a list of random numbers, and returns the list
    list_numbers = []
    for i in range(size):
        list_numbers.append(randint(5, 120))
    # shuffle(list_numbers)
    return list_numbers


list_nums = list_setup(n)
list_rectangles = rectangles_setup(list_nums)


def bubble_asc():
    bubble_sort(list_rectangles, n)


def selection_asc():
    selection_sort(list_rectangles, n)


def insertion_asc():
    insertion_sort(list_rectangles, n)


def bubble_desc():
    bubble_sort_desc(list_rectangles, n)


def selection_desc():
    selection_sort_desc(list_rectangles, n)


def insertion_desc():
    insertion_sort_desc(list_rectangles, n)


onkey(selection_asc, "1")
onkey(bubble_asc, "2")
onkey(insertion_asc, "3")
onkey(selection_desc, "4")
onkey(bubble_desc, "5")
onkey(insertion_desc, "6")

my_screen.listen()

my_screen.exitonclick()
