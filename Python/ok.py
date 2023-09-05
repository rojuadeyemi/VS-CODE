import pandas as pd
import numpy as np
from scipy.stats import f

def ancova(data, dependent, covar, fac):
	y = data[dependent]
	x = data[covar]

	d = data.groupby([fac]).sum()
	t = len(d[fac])
	N = data.shape[0]
	r = N/t
	xi = d[covar]
	yi = d[dependent]
	yt = sum(yi)
	xt = sum(xi)

	Cy = yt**2/N
	Cx = xt**2/N
	
	Syy = sum(y**2) - Cy
	Sxx = sum(x**2) - Cx
	Sxy = sum(y*x) - yt*xt/N
	
	Tyy = sum(yi**2)/r - yt**2/N
	Txx = sum(xi**2)/r - xt**2/N
	Txy = sum(xi*yi)/r - xt*yt/N
	
	Exx = Sxx - Txx
	Eyy = Syy - Tyy
	Exy = Sxy - Txy
	
	b = Exy**2/Exx
	Error = Eyy - b
	Total = Syy - Sxy**2/Sxx
	Treatment = Total - Error
	
	Sv = ["B", fac, "Error"]
	df = [1, t-1,t*(r-1)-1]
	ss = [b, Treatment, Error]
	ms = [ss[i]/df[i] for i in range(len(Sv))]
	fv = [ms[i]/ms[-1] for i in range(len(ms))]
	pvalue = [f.sf(fv[i], df[i], df[-1]) for i in range(len(fv))]
	fv[-1] = np.nan
	pvalue[-1] = np.nan
	ls = zip(Sv, df, ss, ms, fv, pvalue)
	result = pd.DataFrame(ls, columns=["Source", "DF", "SS", "MS", "F"]).reset_index(drop=True)
	return result

dt = pd.read_csv("data.csv")
print(ancova(data=dt, dependent="y", covar="x", fac= 'trt'))
	
	
	
	
	