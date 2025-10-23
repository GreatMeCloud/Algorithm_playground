'''
Not finished

Automatic Robot Avoidance and Movement
Description: On a l×w grid, x robots randomly move up, down, left, and right. This algorithm ensures that each robot makes one move at a time and does not get stuck.
'''

import pygame
import sys
import time

def main():
    values = get_values()

def get_values():
    print("Please enter the length of the grid:", end = "")
    l = int(input())
    print("Please enter the width of the grid:", end = "")
    w = int(input())
    while True:
        print(f"Please enter the number of robots (0 < number ≦ {l*w}):", end = "")
        n = int(input())
        if 0 < n <= l * w:
            break
        print("Out of range\n")
    return l, w, n

def display():
    pygame.init()

main()
