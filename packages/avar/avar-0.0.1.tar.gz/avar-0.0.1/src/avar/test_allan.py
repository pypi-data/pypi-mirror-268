import time
import numpy as np
import allan
import trm

# Constants
T = 0.01
t_dur = 200.0
J = 100
vc = np.array([0.5, 1.0, 7.85, 0.5, 0.1]) * 1e-9
taub = 0.5305

# Make time.
t = np.arange(0, t_dur, T)
K = len(t)

# Get mean Allan variance from Monte-Carlo noise.
M = allan.windows(K)
tau = M*T
va_real = np.zeros(len(M))
tic = time.perf_counter()
for j in range(J):
    n = allan.noise(vc, K, T, taub)
    va_real += allan.variance(n, M)/J
    trm.progress(j, J, tic)

# Get the ideal and fitted Allan variances.
va_ideal, _ = allan.ideal(tau, vc, taub)
va_fit, vc_fit = allan.fit(tau, va_real, taub)

# Show the results.
trm.table(np.array([vc, vc_fit]), left=["true", "fit"])
y = np.array([va_real, va_ideal, va_fit])
trm.plot(np.log10(tau), np.log10(y), rows=0.95)
