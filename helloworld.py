# -*- coding: utf-8 -*-

class HelloWorld:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("Hello," + self.name)

a = HelloWorld(' World!')
a.greet()

#クラスの概念を簡単に理解するためのコード 
