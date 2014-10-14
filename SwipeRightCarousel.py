#!/usr/bin/kivy

import kivy
kivy.require('1.8.0')

from glob import glob
from os.path import join, dirname
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory

class MyClass(App):

    def build(self):   
      
        root = self.root
        
        # get any files into images directory
        curdir = dirname(__file__)
     
        carousel = Carousel(direction='right', loop='True')
        #replace file_name with the directory where your pictures are located
        for filename in glob(join(curdir, 'file_name', '*')):
            image = Factory.AsyncImage(source=filename, allow_stretch=True)
            carousel.add_widget(image)
        return carousel
   
if __name__ == '__main__':
    MyClass().run()
