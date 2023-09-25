"""Input management"""
import pygame
import numpy as np


class Input(object):
    """Manages the users commands"""
    def __init__(self) -> None:
        """User terminated?"""
        self.quit = False
        # lists to store key states
        # down, up: discrete event; lasts for one iteration
        # pressed: continuous event, between down and up events
        self.key_down_list = []
        self.key_pressed_list = []
        self.key_up_list = []
        self.mouse_move_x = 0
        self.mouse_move_y = 0
        self.mouseDown = False
        self.line_start = [0, 0, 0]
        self.line_end = [0, 0, 0]
        self.afterLaunch = False
        self.aim = True
        self.mousemotion = False
    
    # functions to check key states
    def is_key_down(self, keyCode):
        """Check is key is pressed"""
        return keyCode in self.key_down_list
    def is_key_pressed(self, keyCode):
        """Check if key is pressed"""
        return keyCode in self.key_pressed_list
    def is_key_up(self, keyCode):
        """Check if key was released"""
        return keyCode in self.key_up_list
    
    def get_mouse_move_x(self):
        return self.mouse_move_x
    def get_mouse_move_y(self):
        return self.mouse_move_y

    def update(self):
        """Manage user input events"""
        # Reset discrete key states
        self.key_down_list = []
        self.key_up_list = []
        # Iterate to detect changes since last check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            # Check for key-down and key-up events;
            # get name of key from event and append to or remove from corresponding lists
            if event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == "escape": self.quit = True
                self.key_down_list.append(key_name)
                self.key_pressed_list.append(key_name)
            if event.type == pygame.KEYUP:
                key_name = pygame.key.name(event.key)
                self.key_pressed_list.remove(key_name)
                self.key_up_list.append(key_name)

            # get line start input
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouseDown = True
                line_start = pygame.mouse.get_pos()
                self.line_start = [line_start[0], line_start[1], 0]
                
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.afterLaunch = True
                self.mouseDown = False
                line_end = pygame.mouse.get_pos()
                self.line_end = [line_end[0], line_end[1], 0]

            if self.aim and event.type == pygame.MOUSEMOTION:
                self.mouse_move_x = event.rel[1]
                self.mouse_move_y = event.rel[0]
                
            if event.type == pygame.MOUSEMOTION:
                self.mousemotion = True
            else: self.mousemotion = False

                
                    




