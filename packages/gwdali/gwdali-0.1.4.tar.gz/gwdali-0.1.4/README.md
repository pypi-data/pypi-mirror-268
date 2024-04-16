# **GWDALI Software**

Software developed to perform parameter estimations of gravitational waves from compact objects coalescence (CBC) via Gaussian and Beyond-Gaussian approximation of GW likelihood. The Gaussian approximation is related to Fisher Matrix, from which it is direct to compute the covariance matrix by inverting the Fisher Matrix **[1]**. GWDALI also deals with the not-so-infrequent cases of Fisher Matrix with zero-determinant. The Beyond-Gaussian approach uses the Derivative Approximation for LIkelihoods (DALI) algorithm proposed in **[2]** and applied to gravitational waves in **[3]**, whose model parameter uncertainties are estimated via Monte Carlo sampling but less costly than using the GW likelihood with no approximation.


## Installation

To install the software run the command below:

```
$ pip install gwdali
```

## Documentation

Available in [https://gwdali.readthedocs.io/en/latest/](https://gwdali.readthedocs.io/en/latest/)
    
## Usage [example]
    import numpy as np
    #-------------------
    import GWDALI as gw
    #-------------------
    from tqdm import trange
    from astropy.cosmology import FlatLambdaCDM
    cosmo = FlatLambdaCDM(70,0.3)

    rad = np.pi/180 ; deg = 1./rad
    #--------------------------------------------
    # Detector, position and orientation
    #--------------------------------------------
    FreeParams = ['DL','iota','psi','phi_coal']

    # Cosmic Explorer:
    det0 = {"name":"CE","lon":-119,"lat":46,"rot":45,"shape":90}
    # Einstein Telescope:
    det1 = {"name":"ET","lon":10,"lat":43,"rot":0,"shape":60}
    det2 = {"name":"ET","lon":10,"lat":43,"rot":120,"shape":60}
    det3 = {"name":"ET","lon":10,"lat":43,"rot":-120,"shape":60}

    #------------------------------------------------------
    # Setting Injections (Single detection)
    #------------------------------------------------------
    z = 0.1 # Redshift

    params = {}
    params['m1']  = 1.3*(1+z) # mass of the first object [solar mass]
    params['m2']  = 1.5*(1+z) # mass of the second object [solar mass]
    params['z']   = z
    params['RA']       = np.random.uniform(-180,180)
    params['Dec']      = (np.pi/2-np.arccos(np.random.uniform(-1,1)))*deg
    params['DL']       = cosmo.luminosity_distance(z).value/1.e3 # Gpc
    params['iota']     = np.random.uniform(0,np.pi)          # Inclination angle (rad)
    params['psi']      = np.random.uniform(-np.pi,np.pi) # Polarization angle (rad)
    params['t_coal']   = 0  # Coalescence time
    params['phi_coal'] = 0  # Coalescence phase
    # Spins:
    params['sx1'] = 0
    params['sy1'] = 0
    params['sz1'] = 0
    params['sx2'] = 0
    params['sy2'] = 0
    params['sz2'] = 0

    #----------------------------------------------------------------------
    # "approximant" options:
    #               [Leading_Order, TaylorF2_py, ...] or any lal approximant
    #----------------------------------------------------------------------
    # "dali_method" options:
    #               [Fisher, Fisher_Sampling, Doublet, Triplet, Standard]
    #----------------------------------------------------------------------
    res = gw.GWDALI(Detection_Dict = params, 
                    FreeParams = FreeParams, 
                    detectors = [det0,det1,det2,det3], # Einstein Telescope + Cosmic Explorer, 
                    approximant = 'TaylorF2_py',
                    fmin  = 1., 
                    fmax  = 1.e4, 
                    fsize = 3000, 
                    dali_method    = 'Doublet',
                    sampler_method = 'nestle', # Same as Bilby sampling method
                    npoints      = 300, # points for "nested sampling" or steps/walkers for "MCMC"
                    rcond        = 1.e-4,
                    new_priors   = None, # If you want to change the standard priors
                    save_samples = False, 
                    save_cov     = False, 
                    save_fisher  = False,
                    plot_corner  = False,
                    hide_info    = False,
                    step_size    = 1.e-6, # dx := max( step_size , step_size*abs(x) )
                    diff_order   = 2, # Numerical Derivative (Finite Difference) precision O(2) or O(4)
                    run_sampler  = True, # If you want to run MCMC.
                    index        = 1)

    Samples = res['Samples']
    Fisher  = res['Fisher']
    CovFish = res['CovFisher']
    Cov     = res['Covariance']
    Rec     = res['Recovery']
    Err     = res['Error']
    SNR     = res['SNR']
    Tensors = res['Tensors']

## References

[1] L. S. Finn and D. F. Chernoff, “Observing binary inspiral in gravitational radiation: One interferometer,” Phys. Rev. D, vol. 47, pp. 2198–2219, 1993.

[2] E. Sellentin, M. Quartin, and L. Amendola, “Breaking the spell of gaussianity: forecasting with higher order fisher matrices,” Monthly Notices of the Royal Astronomical Society, vol. 441, no. 2, pp. 1831–1840, 2014.

[3] Z. Wang, C. Liu, J. Zhao, and L. Shao, “Extending the fisher information matrix in gravitational-wave data analysis,” arXiv preprint arXiv:2203.02670, 2022.

## Authors

- **Josiel Mendonça Soares de Souza** (developer)
- **Riccardo Sturani** (collaborator)

## License

MIT License