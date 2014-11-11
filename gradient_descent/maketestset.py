#!/usr/bin/python
import random as rd

class dataset:
    "A class which can create random dataset"
    def makedata(self,num):
        f = open('./testset','w')
        for i in range(1,num+1):
            f.write(str(rd.random()*10)+' '+str(rd.random()*10)+'\n')
        f.close()
