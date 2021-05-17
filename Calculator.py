#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:59:05 2020

@author: Suryaansh
"""
import tkinter as tk

#Functions Defined Here:
def add2():
    lbl['text']=lbl['text']+'+'

def sub2():
    lbl['text']=lbl['text']+'-'

def mul2():
    lbl['text']=lbl['text']+'*'

def div2():
    lbl['text']=lbl['text']+'/'

def mod2():
    lbl['text']=lbl['text']+'%'
    
def one2():
    lbl['text']=lbl['text']+'1'
    
def two2():
    lbl['text']=lbl['text']+'2'
    
def three2():
    lbl['text']=lbl['text']+'3'
    
def four2():
    lbl['text']=lbl['text']+'4'
    
def five2():
    lbl['text']=lbl['text']+'5'
    
def six2():
    lbl['text']=lbl['text']+'6'
    
def seven2():
    lbl['text']=lbl['text']+'7'
    
def eight2():
    lbl['text']=lbl['text']+'8'
    
def nine2():
    lbl['text']=lbl['text']+'9'
    
def zero2():
    lbl['text']=lbl['text']+'0'
    
def clr2():
    lbl['text']=lbl['text'][:-1]
    
def aclr2():
    lbl['text']=''
    
def point2():
    lbl['text']+='.'
    
def eq2():
    try:
        val=lbl['text']
        lbl['text']=str(eval(val))
    except:
        lbl['text']='Error! Please Try Again.'

#WINDOW CODE STARTING HERE:
window=tk.Tk()
window.geometry("600x500")

window.title("Calculator")
window.resizable()

lbl_frame=tk.Frame(master=window)

lbl=tk.Label(master=lbl_frame,bg='black',fg='white',font=('CourierNew 40'),text='')
lbl_frame.rowconfigure(0,weight=1, minsize=50)

lbl_frame.columnconfigure(0,weight=1, minsize=50)

lbl.grid(row=0, column=0, sticky='nsew')
lbl_frame.grid(row=0,column=0,sticky='nsew')

btn_frame=tk.Frame(master=window)


'''
Work to be done:
    after getting final label string see if i need to define new functipon to solve that 
    or does eval() function work
    also for the final = function need to use try and except to display error msg
    
'''

one=tk.Button(master=btn_frame, text='1', command=one2,font=('CourierNew 24'))
two=tk.Button(master=btn_frame, text='2', command=two2,font=('CourierNew 24'))
three=tk.Button(master=btn_frame, text='3', command=three2,font=('CourierNew 24'))
four=tk.Button(master=btn_frame, text='4', command=four2,font=('CourierNew 24'))
five=tk.Button(master=btn_frame, text='5', command=five2,font=('CourierNew 24'))
six=tk.Button(master=btn_frame, text='6', command=six2,font=('CourierNew 24'))
seven=tk.Button(master=btn_frame, text='7', command=seven2,font=('CourierNew 24'))
eight=tk.Button(master=btn_frame, text='8', command=eight2,font=('CourierNew 24'))
nine=tk.Button(master=btn_frame, text='9', command=nine2,font=('CourierNew 24'))
zero=tk.Button(master=btn_frame, text='0', command=zero2,font=('CourierNew 24'))


one.grid(row=0,column=0, sticky='nsew')
two.grid(row=0,column=1, sticky='nsew')
three.grid(row=0,column=2, sticky='nsew')
four.grid(row=1,column=0, sticky='nsew')
five.grid(row=1,column=1, sticky='nsew')
six.grid(row=1,column=2, sticky='nsew')
seven.grid(row=2,column=0, sticky='nsew')
eight.grid(row=2,column=1, sticky='nsew')
nine.grid(row=2,column=2, sticky='nsew')
zero.grid(row=3,column=0, columnspan=3, sticky='nsew')

add=tk.Button(master=btn_frame, text='+', command=add2,font=('CourierNew 24'))
sub=tk.Button(master=btn_frame, text='-', command=sub2,font=('CourierNew 24'))
mul=tk.Button(master=btn_frame, text='*', command=mul2,font=('CourierNew 24'))
div=tk.Button(master=btn_frame, text='/', command=div2,font=('CourierNew 24'))
mod=tk.Button(master=btn_frame, text='mod', command=mod2,font=('CourierNew 24'))
eq=tk.Button(master=btn_frame, text='=', command=eq2,font=('CourierNew 24'))
clr=tk.Button(master=btn_frame, text='C', command=clr2,font=('CourierNew 24'))
aclr=tk.Button(master=btn_frame, text='AC', command=aclr2,font=('CourierNew 24'))
point=tk.Button(master=btn_frame, text='.',font=('CourierNew 24'))

add.grid(row=0,rowspan=3,column=3, sticky='nsew')
sub.grid(row=0,column=4, sticky='nsew')
mul.grid(row=1,column=4, sticky='nsew')
div.grid(row=2,column=4, sticky='nsew')
mod.grid(row=2, column=5, sticky='nsew')
eq.grid(row=3,column=3, columnspan=3,rowspan=2, sticky='nsew')
clr.grid(row=0, column=5, sticky='nsew')
aclr.grid(row=1, column=5, sticky='nsew')



btn_frame.rowconfigure([0,1,2,3],weight=1, minsize=50)

btn_frame.columnconfigure([0,1,2,3,4,5],weight=1, minsize=50)


btn_frame.grid(row=1, column=0,sticky='nsew')

window.rowconfigure([0,1],weight=1, minsize=50)

window.columnconfigure(0,weight=1, minsize=50)

window.mainloop()


