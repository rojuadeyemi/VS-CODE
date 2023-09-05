# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 20:45:09 2021

@author: Aderoju Adeyemi
"""
import matplotlib.pyplot as plt

n = [50, 100, 200, 500, 1000]
nominal = [0.05]*5
first = [[0.041,0.054,0.049,0.057,0.049],[0.034,0.050,0.041,0.053,0.049]]
second = [[0.132,0.136,0.120,0.157,0.149],[0.062,0.056,0.031,0.068,0.040]]
third = [[0.323,0.318,0.333,0.328,0.319],[0.073,0.064,0.058,0.063,0.046]]

fig = plt.figure(figsize=(12,6))
fig.suptitle("Type I Error At various sample size")

ax1 =plt.subplot(221)
ax1.plot(n, first[0],label="Poisson", c='red')
ax1.plot(n, first[1],label="Negative Binomial",c='blue')
ax1.plot(n, nominal,label="Nominal level",c='black')
ax1.set_ylabel("Type I Error")
ax1.set_title(r"$ \alpha $ = 0.0")
ax1.set_ylim([0,1.0])
ax1.legend(loc='best')

ax2 =plt.subplot(223)
ax2.plot(n, second[0],label="Poisson", c='red')
ax2.plot(n, second[1],label="Negative Binomial",c='blue')
ax2.plot(n, nominal,label="Nominal level",c='black')
ax2.set_xlabel("Sample size")
ax2.set_ylabel("Type I Error")
ax2.set_title(r"$ \alpha $ = 0.5")
ax2.set_ylim([0,1.0])
ax2.legend(loc='upper right', frameon='False')

ax3 =plt.subplot(122)
ax3.plot(n, third[0],label="Poisson", c='red')
ax3.plot(n, third[1],label="Negative Binomial",c='blue')
ax3.plot(n, nominal,label="Nominal level",c='black')
ax3.set_xlabel("Sample size")
ax3.set_ylabel("Type I Error")
ax3.set_ylim([0,1.0])
ax3.set_title(r"$ \alpha $ = 2.0")
ax3.legend(loc='upper right', frameon='False')