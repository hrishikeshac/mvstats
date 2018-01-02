# -*- coding: utf-8 -*-

"""Main module."""
import xarray as xr
import numpy as np

def cov(x, y, lagx=0, lagy=0):
    """
    Computes covariance between x and y along time dimension, accounting for given lags (if any)
    Input: Two single- or multi-dimensional xrarray DataArray objects (x and y) which have 'time' as the first dimension.
        Lag values (lagx for input data x, and lagy for input data y) can also be prescribed. Default lag values are zero.
    Output: An xarray DataArray object showing covariance between x and y along the 'time' dimension.
        If lag values are provided, the returned object will show lagged covariance.
    """
    #1. Add lag information if any, and shift the data accordingly
    if lagx!=0:
        #If x lags y by 1, x must be shifted 1 step backwards.
        #But as the 'zero-th' value is nonexistant, xr assigns it as invalid (nan). Hence it needs to be dropped
        x   = x.shift(time = -lagx).dropna(dim='time', how = 'all')

    if lagy!=0:
        y   = y.shift(time = -lagy).dropna(dim='time', how = 'all')

    #2. Ensure that the data are properly alinged to each other.
    x,y = xr.align(x,y)

    #3. Compute data length, mean and standard deviation along time dimension for further use:
    n     = x.time.shape[0]
    xmean = x.mean(dim='time')
    ymean = y.mean(dim='time')
    xstd  = x.std(dim='time')
    ystd  = y.std(dim='time')

    #4. Compute covariance along time dimension
    cov   =  np.sum((x - xmean)*(y - ymean), axis=0)/(n)

    return cov

def cor(x, y, lagx=0, lagy=0):
    """
    Computes Pearson Correlation coefficient between x and y along time dimension, accounting for given lags (if any)
    Input: Two single- or multi-dimensional xrarray DataArray objects (x and y) which have 'time' as the first dimension
        Lag values (lagx for input data x, and lagy for input data y) can also be prescribed. Default lag values are zero.
    Output: An xarray DataArray object showing Pearson Correlation coefficient between x and y along the 'time' dimension
        If lag values are provided, the returned object will show lagged correlation.
    """
    #1. Add lag information if any, and shift the data accordingly
    if lagx!=0:
        #If x lags y by 1, x must be shifted 1 step backwards.
        #But as the 'zero-th' value is nonexistant, xr assigns it as invalid (nan). Hence it needs to be dropped
        x   = x.shift(time = -lagx).dropna(dim='time', how = 'all')

    if lagy!=0:
        y   = y.shift(time = -lagy).dropna(dim='time', how = 'all')

    #2. Ensure that the data are properly alinged to each other.
    x,y = xr.align(x,y)

    #3. Compute data length, mean and standard deviation along time dimension for further use:
    n     = x.time.shape[0]
    xmean = x.mean(dim='time')
    ymean = y.mean(dim='time')
    xstd  = x.std(dim='time')
    ystd  = y.std(dim='time')

    #4. Compute covariance along time dimension
    cov   =  np.sum((x - xmean)*(y - ymean), axis=0)/(n)

    #5. Compute correlation along time dimension
    cor   = cov/(xstd*ystd)

    return cor

def reg(x, y, lagx=0, lagy=0):
    """
    Computes simple linear regression slope and intercept for y with respect to x, accounting for given lags (if any)
    Input: Two single- or multi-dimensional xrarray DataArray objects (x and y) which have 'time' as the first dimension.
        Lag values (lagx for input data x, and lagy for input data y) can also be prescribed. Default lag values are zero.
    Output: Two xarray DataArray objects showing estimated regression slope and intercept values for y with respect to x along the 'time' dimension.
        If lag values are provided, the returned object will show lagged regression.
    """
    #1. Add lag information if any, and shift the data accordingly
    if lagx!=0:
        #If x lags y by 1, x must be shifted 1 step backwards.
        #But as the 'zero-th' value is nonexistant, xr assigns it as invalid (nan). Hence it needs to be dropped
        x   = x.shift(time = -lagx).dropna(dim='time', how = 'all')

    if lagy!=0:
        y   = y.shift(time = -lagy).dropna(dim='time', how = 'all')

    #2. Ensure that the data are properly alinged to each other.
    x,y = xr.align(x,y)

    #3. Compute data length, mean and standard deviation along time dimension for further use:
    n     = x.time.shape[0]
    xmean = x.mean(dim='time')
    ymean = y.mean(dim='time')
    xstd  = x.std(dim='time')
    ystd  = y.std(dim='time')

    #4. Compute covariance along time dimension
    cov   =  np.sum((x - xmean)*(y - ymean), axis=0)/(n)

    #5. Compute regression slope and intercept:
    slope     = cov/(xstd**2)
    intercept = ymean - xmean*slope

    return slope, intercept

def linregress_ND(x, y, lagx=0, lagy=0):
    """
    Multidimensional equivalent of scipy.stats.linregress()
    Input: Two single- or multi-dimensional xrarray DataArray objects (x and y) which have 'time' as the first dimension.
        Lag values (lagx for input data x, and lagy for input data y) can also be prescribed. Default lag values are zero.
    Output: Xarray DataArray objects showing Covariance, correlation, regression slope and intercept, p-value, and standard error on regression (short: cov,cor,slope,intercept,pval,stderr)
    for y with respect to x along time dimension, accounting for given lags (if any)
    """
    #1. Add lag information if any, and shift the data accordingly
    if lagx!=0:
        #If x lags y by 1, x must be shifted 1 step backwards.
        #But as the 'zero-th' value is nonexistant, xr assigns it as invalid (nan). Hence it needs to be dropped
        x   = x.shift(time = -lagx).dropna(dim='time', how = 'all')

    if lagy!=0:
        y   = y.shift(time = -lagy).dropna(dim='time', how = 'all')

    #2. Ensure that the data are properly alinged to each other.
    x,y = xr.align(x,y)

    #3. Compute data length, mean and standard deviation along time axis for further use:
    n     = x.time.shape[0]
    xmean = x.mean(dim='time')
    ymean = y.mean(dim='time')
    xstd  = x.std(dim='time')
    ystd  = y.std(dim='time')

    #4. Compute covariance along time axis
    cov   =  np.sum((x - xmean)*(y - ymean), axis=0)/(n)

    #5. Compute correlation along time axis
    cor   = cov/(xstd*ystd)

    #6. Compute regression slope and intercept:
    slope     = cov/(xstd**2)
    intercept = ymean - xmean*slope

    #7. Compute P-value and standard error
    #Compute t-statistics
    tstats = cor*np.sqrt(n-2)/np.sqrt(1-cor**2)
    stderr = slope/tstats

    from scipy.stats import t
    pval   = t.sf(np.abs(tstats), n-2)*2
    pval   = xr.DataArray(pval, dims=cor.dims, coords=cor.coords)

    return cov,cor,slope,intercept,pval,stderr

def detrend_ND_xr(y, rolling_mean_window = 0):
    """
    Use the reg() to detrend the data
    Input: An xarray DataArray object
        If seasonlity is not removed from the input array, a moving average filter can be applied by prescribing a value to rolling_mean_window
        (e.g. for monthly data, rolling_mean_window = 12 will remove seasonality). Default: rolling_mean_window = 0
    Output: Detrended input array. If a rolling_mean_window value is prescribed, the output data will have trimmed ends
    detrended data = y - (slope*x + intercept) + y.mean()
    """
    #1 Apply boxcar filter to remove seasonality
    y_deseason = y.rolling(time= rolling_mean_window, center=True).mean()#.dropna(dim='time', how = 'all')

    #2. Create index array 'x' for y
    x = xr.DataArray(np.arange(y.shape[0]), dims = ['time'], coords=[y.time])

    #3. Compute regression for deseaonsed y with respect to x
    slope, intercept = reg(x,y_deseason)

    #4 Compute trend for y
    y_trend = (slope*x + intercept)

    #5. Subtract the estimated trend from y
    det = y - y_trend + y.mean()

    return det
