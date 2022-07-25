# needed modules
import numpy as np
from scipy.stats import norm

# Black-Scholes Call Formula
def Black_scholes(call_or_put, s, k, r, t, vol):
    """
    Parameters:
        - call_or_put (str): ['call' or 'put']
        - s (float): spot price for underlying
        - k (float): strike price of contract
        - r (float): risk-free interest rate
        - t (float): time to maturity (in years)
        - vol (float): volatility of underlying
    """

    # initialising a normal distribution
    N = norm.cdf

    # for call 
    if call_or_put == 'call':
        """ for estimating value of call options """
        d1 = (np.log(s/k) + (r+ vol**2/2)*t) / (vol*np.sqrt(t))
        d2 = d1 - vol * np.sqrt(t)
        return s * N(d1) - (k * np.exp(-r*t) * N(d2))
    
    # for put
    if call_or_put == 'put':
        """ for estimating value of put options """
        d1 = (np.log(s/k) + (r+ vol**2/2)*t) / (vol*np.sqrt(t))
        d2 = d1 - vol * np.sqrt(t)
        return (k * np.exp(-r*t) * N(-d2)) - s*N(-d1)
