# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to Safaricom Enchanted African Gala
        
         """)

msgs = [‘From the bench, you radiate fairness and integrity. Keep lighting up the legal world! 
You rule with wisdom and grace, keep bringing justice to light!’,

‘With each argument, keep igniting the flame of righteousness. Shine on, champion of the law!’,

‘In the realm of justice, you are a beacon of hope and a beacon of light. Together, Let's shine bright, legal luminaries!’, 

‘With each verdict, you paint the world with hues of fairness and hues of truth. Let your shine illuminate the path to righteousness!’, 

‘In the courtroom, our words are like rays of sunlight piercing through darkness. Let's shine on, custodians of justice!’,

‘From the halls of justice, you unleash waves of brilliance and waves of integrity. Together, we'll illuminate the path to a brighter future!’,
 ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name + " " + msg)
