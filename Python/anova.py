import statsmodels.api as sm
from statsmodels.formula. api import ols
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np
import pingouin as pg

#Dummy Regression & One-way Anova

res = [10,14,12,16,16,18,20,22,22]

data = pd.DataFrame({"Treatment":np.repeat(["A", "B", "C"] ,repeats=3), "Response":res})

lm = ols('Response~Treatment', data=data)
res = lm.fit()
#print(res.summary())
#print(sm.stats.anova_lm(res, type=2))
#print(pairwise_tukeyhsd(groups=data["Treatment"],endog=data["Response"], alpha=0.05))

#Two way Anova
df = pd.DataFrame({"res":[212, 184,245,193,174,120,228,290,185,216,340,330],"block":np.tile([1,2,3],4),"trt":np.repeat(["A", "B", "C", "D"], 3)})
md = ols('res~C(trt)+C(block)', data=df).fit()
#print(md.summary())
#print(sm.stats.anova_lm(md, type=2))

#Two factors with replication
df2 = pd.DataFrame({"y":[6, 4,5,5,4,5,7,4,6,8,10,8,7,7,9,7,9,12,8,8,7,5,6,5,9,9,7,5,4,6,8,4,6,5,5,5,7,9,7,10],"machine":np.repeat(["A","B","C","D"], 10),"shift":np.tile(np.repeat([1,2],5),4)})

lm = ols("y~C(machine)*C(shift)", data=df2).fit()

#print(sm.stats.anova_lm(lm, type=2))

from statsmodels.graphics.factorplots import interaction_plot
#import atplotlib.pyplot as plt
#to obtain the interaction_plot
interaction_plot(df2["machine"], df2["shift"],df2["y"], colors=["red", "blue"],markers=["o", "D"], ms=10)
#plt.show()

#BIBD?
df1 = pd.DataFrame({"trt":list("ACDABCBCDABD"),"block":np.repeat([1,2,3,4],3),"response":[73,73,75,74,75,75,67,68,72,71,72,75]})


mod = ols("response~C(trt) +C(block)", data=df1).fit()
#print(mod.summary())
#print(sm.stats.anova_lm(mod, type=2))

#Latin Square Design
dat = pd.DataFrame({"trt":list("ACDBDBACBACDCDBA"), "col":np.tile([1,2,3,4],4),"rol":np.repeat([1,2,3,4],4), "response":[18, 21,25,11,22,12,15,19,15,20,23,24,22,21,10,17]})
model = ols("response~C(trt) + C(col) +C(rol)", data=dat).fit()

#print(sm.stats.anova_lm(model, type =2))

#Anocova (CRD)

dt = pd.read_csv("data.csv")

anc = pg.ancova(data=dt, dv="y", covar="x", between="trt")

print(anc)

#Nested Design 
y = [23.4,22.7,18.7,25.6,19.7,23.6,30.7,19.7,26.4,19.7,24.2,18.6,23.3,28.2,30.3,19.8,29.6,30.2,19.8,21.6,26.3,20.2,30.7,27.5]

new_dt = pd.DataFrame({"res":y, "A":np.repeat([1,2],12), "B":np.tile(np.repeat([1,2,3,4],3),2)})

md = ols("res~C(A)/C(B)", data=new_dt).fit()

#print(sm.stats.anova_lm(md, type=2))

z = [22.5,15.8,21.8,13.7,30.7,13.7,19.7,19.7,20.1,30.7,33.2,20.7,19.3,18.3]
A = [1,2,3,4,1,2,3,1,3,4,1,2,3,4]
dtt = pd.DataFrame(zip(z, A), columns=["y", "A"])