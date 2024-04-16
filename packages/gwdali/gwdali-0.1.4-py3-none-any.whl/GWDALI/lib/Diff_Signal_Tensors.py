import numpy as np
import GWDALI.lib.Waveforms as wf
import GWDALI.lib.Angles_lib as geo
import GWDALI.lib.Dictionaries as gwdict
from scipy.interpolate import interp1d
from scipy.integrate import trapezoid
from scipy.optimize import root

rad = np.pi/180
deg = 1./rad

c = 299792458. # m/s
R_earth = 6371.e3 # meters

PSD, labels_tex = gwdict.Load_Dictionaries()

#----------------------------------------------
# m1(m2,Mc) or m2(m1,Mc)
def func_mMc(x,args):
	m, Mc = args
	return x**3 - (Mc**5/m**3)*x - Mc**5/m**2
def m_Mc(m,Mc,x0):
	res = root(func_mMc,x0,args=[m,Mc])
	return float(res.x[0])
#----------------------------------------------
# m1(eta,Mc) and m2(eta,Mc)
def eta_Mc(eta,Mc):
	m1 = 0.5*(Mc/eta**(3./5)) * (1 + np.sqrt(1-4*eta))
	m2 = 0.5*(Mc/eta**(3./5)) * (1 - np.sqrt(1-4*eta))
	return m1, m2
#----------------------------------------------
def q_Mc(q,Mc):
	m1 = ((1+q)/q**3)**(1./5)*Mc
	m2 = (q**2*(1+q))**(1./5)*Mc
	return m1, m2
#----------------------------------------------
def eta_m2(eta,m2): # return m1
	return 0.5*(m2/eta)*( (1-2*eta) + np.sqrt(1-4*eta))
def eta_m1(eta,m1): # return m2
	return 0.5*(m1/eta)*( (1-2*eta) - np.sqrt(1-4*eta))
#----------------------------------------------
def get_iota(prms):
	if("cos_iota" in prms.keys() ):
		iota = np.arccos(prms['cos_iota']) # rad
	elif("iota" in prms.keys() ):
		iota = prms['iota'] # rad
	else:
		print(">> Parameter 'iota' not found!")
		print(">> Received Parameters:", list(prms.keys()))
		quit()
	return iota

def get_dL(prms):
	if("ln_dL" in prms.keys()):
		dL = np.exp( prms['ln_dL'] ) * 1.e3
	elif("inv_dL" in prms.keys()):
		dL = 1.e3/prms['inv_dL']
	elif("DL" in prms.keys()):
		dL = prms["DL"] * 1.e3
	else:
		print(">> Parameter 'DL' not found!")
		print(">> Received Parameters:", list(prms.keys()))
		quit()
	return dL

def get_spins(prms):
	if(all([x in prms.keys() for x in ['sx1','sy1','sz1','sx2','sy2','sz2'] ])):
		sx1 = prms['sx1']
		sy1 = prms['sy1']
		sz1 = prms['sz1']
		sx2 = prms['sx2']
		sy2 = prms['sy2']
		sz2 = prms['sz2']
	elif( all( [x in prms.keys() for x in ['S1','theta_1','phi_1','S2','theta_2','phi_2']] ) ):
		sx1 = prms['S1']*np.sin( prms['theta_1'] )*np.cos( prms['phi_1'] )
		sy1 = prms['S1']*np.sin( prms['theta_1'] )*np.sin( prms['phi_1'] )
		sz1 = prms['S1']*np.cos( prms['theta_1'] )
		sx2 = prms['S2']*np.sin( prms['theta_2'] )*np.cos( prms['phi_2'] )
		sy2 = prms['S2']*np.sin( prms['theta_2'] )*np.sin( prms['phi_2'] )
		sz2 = prms['S2']*np.cos( prms['theta_2'] )
	else:
		print(">> Invalid or Incomplete Spin Inputs!")
		print(">> GWDALI works with:")
		print("\t ['S1','theta_1','phi_1','S2','theta_2','phi_2'] , or")
		print("\t ['sx1','sy1','sz1','sx2','sy2','sz2']")
		quit()
	return [sx1, sy1, sz1], [sx2, sy2, sz2]

def get_mass(prms):
	keys = list(prms.keys())
	Mass = {}	
	for key in keys:
		if( key in ['m1','m2','q','eta','Mc'] ):
			Mass[key] = prms[key]
	
	keys = Mass.keys()
	if(all(x in ['m1','m2'] for x in keys) ):
		return Mass['m1'], Mass['m2']
	elif(all(x in ['eta','Mc'] for x in keys) ):
		eta, Mc = Mass['eta'], Mass['Mc']
		return eta_Mc(eta,Mc)
	elif(all(x in ['eta','m1'] for x in keys) ):
		m1, eta = Mass['m1'], Mass['eta']
		m2 = eta_m1(eta,m1)
		return m1, m2
	elif(all(x in ['eta','m2'] for x in keys) ):
		m2, eta = Mass['m2'], Mass['eta']
		m1 = eta_m2(eta,m2)
		return m1, m2
	elif( all(x in ['m1','q'] for x in keys) ):
		m1, q = Mass['m1'], Mass['q']
		m2 = m1*q
		return m1, m2
	elif( all(x in ['m2','q'] for x in keys) ):
		m2, q = Mass['m2'], Mass['q']
		m1 = m2/q
		return m1, m2
	elif( all(x in ['q','Mc'] for x in keys) ):
		q, Mc = Mass['q'], Mass['Mc']
		return q_Mc(q,Mc)
	elif( all(x in ['m1','Mc'] for x in keys) ):
		m1, Mc = Mass['m1'], Mass['Mc']
		m2 = m_Mc(m1,Mc,m1)
		return m1, m2
	elif( all(x in ['m2','Mc'] for x in keys) ):
		m2, Mc = Mass['m2'], Mass['Mc']
		m1 = m_Mc(m2,Mc,m2)
		return m1, m2
	if(all(x in ['q','eta'] for x in keys) ):
		print("---"*10)
		print("Error! It is not possible to recover (m1,m2) from (q,Mc)")
		print("---"*10) ; quit()
	else:
		print("---"*10)
		print("Error! We need at least 2 mass parameters!")
		print("Parameters allowed: (m1, m2, q, eta, Mc)")
		print("---"*10) ; quit()

#------------------------------------------------

def Pattern_Func(alpha,beta,psi,Omega):
	u = np.cos(beta) ; Coeff = np.sin(Omega)
	fp = 0.5*(1.+u**2)*np.cos(2.*alpha)*Coeff
	fx = -u*np.sin(2.*alpha)*Coeff
	
	Fp =  fp*np.cos(2.*psi) + fx*np.sin(2.*psi)
	Fx = -fp*np.sin(2.*psi) + fx*np.cos(2.*psi)

	return Fp, Fx

#-------------------------------------------------

def ScalarProduct(freq,Sn,A,B):
	return 4*np.real( trapezoid( A*np.conj(B)/Sn, freq) )

def GW_Polarizations(params, freq, approx):
	keys = list(params.keys())
	
	m1, m2   = get_mass(params)
	iota 	 = get_iota(params) # rad
	DL       = get_dL(params)   # Mpc
	psi      = params['psi']    # rad

	s1, s2 = get_spins(params)

	hp, hx, freq0 = wf.Waveforms(m1,m2,iota,DL,s1,s2,freq, approx=approx)

	return hp, hx, freq0

# det: abreviation of detector
def Signal(params,dets,approx):
	alpha    = params['RA']*rad       # rad
	beta     = (90-params['Dec'])*rad # rad
	psi      = params['psi']          # rad
	t_coal   = params['t_coal']       # sec
	phi_coal = params['phi_coal']     # rad
	iota = get_iota(params) # rad

	det_a, det_b = dets
	tau_a    = geo.get_TimeDelay(det_a,params) # sec (time-delay between det_a and geocenter)
	tau_b    = geo.get_TimeDelay(det_b,params) # sec (time-delay between det_b and geocenter)
	tau_ab = (tau_a - tau_b) # time_delay (between det_a and det_b)

	name  = det_b['name']
	freq  = det_b['freq'].copy()
	lon   = det_b['lon'] # deg
	lat   = det_b['lat'] # deg
	rot   = det_b['rot'] # deg

	alpha_obs, beta_obs, psi_obs = geo.ObsAngles(alpha,beta,iota,psi,lon,lat,rot)
	Fp, Fx = Pattern_Func(alpha_obs,beta_obs,psi_obs,det_b['shape']*rad)
	hp, hx, freq0 = GW_Polarizations(params, freq, approx)

	# t_coal := t_(0,a)
	# tau_ab := tau_a - tau_b = t_(0,a) - t_(0,b)
	# t_(0,b) = t_(0,a) - tau_ab
	Phase = 2*np.pi*freq0*(t_coal-tau_ab) - phi_coal
	H = (Fp*hp + Fx*hx)*np.exp(1.j*Phase)
	
	gw_signal = interp1d(freq0,H,bounds_error=False,fill_value='extrapolate')
	H = gw_signal(freq)

	return H

#-------------------------------------------------

# eps (standard) = 1.e-6
def split_prms(params,x,eps, diff_order):
	p = params[x]
	dx = np.max([eps,eps*p])
	P0 = params.copy() ; P0[x] = p - dx	
	P1 = params.copy() ; P1[x] = p - dx/2
	P2 = params.copy() ; P2[x] = p + dx/2
	P3 = params.copy() ; P3[x] = p + dx
	if(diff_order == 2): return [P1,P2], dx
	elif(diff_order==4): return [P0,P1,P2,P3], dx
	else:
		print("\n\t Invalid diff_order! Allowed values: [2,4] ")
		quit()

def Diff1(x, params, dets, approx, eps, diff_order):
	Ps, dx = split_prms(params,x,eps, diff_order)
	Y = [Signal(P, dets, approx) for P in Ps]
	if(diff_order == 2): return (Y[1]-Y[0])/dx
	elif(diff_order==4): return 4*(Y[2]-Y[1])/(3*dx) - (Y[3]-Y[0])/(6*dx)

def Diff2(xi, xj, params, dets, approx, eps, diff_order):
	Ps, dx = split_prms(params,xi,eps, diff_order)
	Y = [Diff1(xj, P, dets, approx, eps, diff_order) for P in Ps]
	if(diff_order == 2): return (Y[1]-Y[0])/dx
	elif(diff_order==4): return 4*(Y[2]-Y[1])/(3*dx) - (Y[3]-Y[0])/(6*dx)

def Diff3(xi, xj, xk, params, dets, approx, eps, diff_order):
	Ps, dx = split_prms(params,xi,eps, diff_order)
	Y = [Diff2(xj,xk, P, dets, approx, eps, diff_order) for P in Ps]
	if(diff_order == 2): return (Y[1]-Y[0])/dx
	elif(diff_order==4): return 4*(Y[2]-Y[1])/(3*dx) - (Y[3]-Y[0])/(6*dx)

#-------------------------------------------------#-------------------------------------------------
#-------------------------------------------------#-------------------------------------------------

def Fisher_ij(xi,xj, params, dets, approx, eps, diff_order): # [1,1]
	det = dets[1]
	Dxi = Diff1(xi, params, dets, approx, eps, diff_order)
	Dxj = Diff1(xj, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], Dxi, Dxj )

#-------------------------------------------------#-------------------------------------------------
# (arXiv:2203.02670)

def Doublet12(xi,xj,xk, params, dets, approx, eps, diff_order): # [1,2]
	det = dets[1]
	D_i  = Diff1(xi, params, dets, approx, eps, diff_order)
	D_jk = Diff2(xj,xk, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], D_i, D_jk)

def Doublet22(xi,xj,xk,xl, params, dets, approx, eps, diff_order): # [2,2]
	det = dets[1]
	D_ij = Diff2(xi,xj, params, dets, approx, eps, diff_order)
	D_kl = Diff2(xk,xl, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], D_ij, D_kl)

#-------------------------------------------------#-------------------------------------------------

def Triplet13(xi,xj,xk,xl, params, dets, approx, eps, diff_order): # [1,3]
	det = dets[1]
	D_i   = Diff1(xi, params, dets, approx, eps, diff_order)
	D_jkl = Diff3(xj,xk,xl, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], D_i, D_jkl)

def Triplet23(xi,xj,xk,xl,xm, params, dets, approx, eps, diff_order): # [2,3]
	det = dets[1]
	D_ij  = Diff2(xi,xj, params, dets, approx, eps, diff_order)
	D_klm = Diff3(xk,xl,xm, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], D_ij, D_klm)

def Triplet33(xi,xj,xk,xl,xm,xn, params, dets, approx, eps, diff_order): # [3,3]
	det = dets[1]
	D_ijk = Diff3(xi,xj,xk, params, dets, approx, eps, diff_order)
	D_lmn = Diff3(xl,xm,xn, params, dets, approx, eps, diff_order)
	return ScalarProduct(det['freq'], det['Sn'], D_ijk, D_lmn)

#-------------------------------------------------#-------------------------------------------------
