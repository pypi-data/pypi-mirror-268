import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import os
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import phenom
import copy

# gpr fitting
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import WhiteKernel, RBF, ConstantKernel, RationalQuadratic, Matern, DotProduct

from chirpy.prob_phenom_model import pn, collocation

def load_nr_data(
    catalogue_dir="/Users/sebastian.khan/personal/data/non_spinning_catalogue_dec_2022", 
    names_to_drop=['RIT-BBH-0957-n084'],
    test_set_query='(q>1 and q<2) or (q>2 and q<=4) or (q>=7 and q<10) or (q>=14 and q<16) or (q>=32 and q<33)'
):
    
    df = pd.read_csv(os.path.join(catalogue_dir, 'metadata.csv'))
    times = np.load(os.path.join(catalogue_dir, 'times.npy'))
    strains = np.load(os.path.join(catalogue_dir, 'strains.npy'))
    
    if names_to_drop != None:
        idxs_to_keep = df[~df['name'].isin(names_to_drop)].index
        strains = strains[idxs_to_keep]
        df = df.iloc[idxs_to_keep].copy().reset_index(drop=True)

    amps=np.array([np.abs(strain) for strain in strains])
    phases=np.array([np.unwrap(np.angle(strain)) for strain in strains])
    freqs=np.array([IUS(times, phase).derivative()(times) for phase in phases])
    # freqs is the angular frequency
    
    
    # compute start frequency of NR data at 100 Msun
    nr_start_freq = phenom.MftoHz(freqs[:,0]/(2*np.pi), 100)
    df['start_freq_100Msun'] = nr_start_freq
    
    df_test = df.query(test_set_query)
    df_train = df[~df.isin(df_test)].dropna()
    df['set'] = None
    df.loc[df.index.isin(df_train.index), 'set']="train"
    df.loc[df.index.isin(df_test.index), 'set']="test"
    
    qs_with_dup = df['q'].value_counts()[df['q'].value_counts() > 1].index
    df['has_dup'] = df['q'].isin(qs_with_dup)

    # create a simple tag e.g. for plot titles
    df['tag'] = df.apply(lambda x: "q" + str(x['q']) + "_" + x['name'], axis=1)
    
    train_idxs = df.query('set == "train"').index
    test_idxs = df.query('set == "test"').index

    
    
    output = {
        'df':df,
        'times':times,
        'strains':strains,
        'amps':amps,
        'phases':phases,
        'freqs':freqs,
        'train_idxs':train_idxs,
        'test_idxs':test_idxs,
    }
    
    return output


class Waveform(object):
    """
    a class to store waveform data/meta-data
    """
    def __init__(self, strain, times, amp, phase, freq, q, meta_data=None):
        self.strain = strain
        self.times = times
        self.amp = amp
        self.phase = phase
        # freq == angular frequency
        self.freq = freq
        self.q = q
        self.eta = phenom.eta_from_q(self.q)
        self.fin_spin = phenom.remnant.FinalSpin0815(self.eta, 0, 0)
        self.fring = phenom.remnant.fring(self.eta, 0, 0, self.fin_spin)
        self.fdamp = phenom.remnant.fdamp(self.eta, 0, 0, self.fin_spin)
        self.meta_data = meta_data
        
        
# we can apply an affine transformation
# to the PN inspiral portion
# of the waveform in order to
# get the data in the appropriate
# form for the PN-like ansatz

def transformation_affine_foward(x, a=1, b=0):
    """
    return y=a*x + b
    """
    return a*x + b

def transformation_affine_reverse(y, a=1, b=0):
    """
    return x=(y-b)/a
    """
    return (y-b)/a

        
def get_taylort3_inspiral_omega_affine_params(t, tc, eta, M):
    """
    get inspiral angular GW frequency TaylorT3 Newtonian term
    and TaylorT3 approximation
    
    returns: Newtonaian Term and Full TaylorT3 approximation
    """
    omega_N = pn.TaylorT3_Omega_GW_Newt(t, tc, eta, M)
    omega_pn = pn.TaylorT3_Omega_GW(t, tc, eta, M)
    return omega_N, omega_pn
        
    
def get_taylort3_inspiral_amp_affine_params(omega_22, eta, M):
    """
    get inspiral amplitude TaylorT3 Newtonian term
    and TaylorT3 approximation
    
    returns: Newtonaian Term and Full TaylorT3 approximation
    """
    x = pn.x_from_omega_22(omega_22, M=M)
    amp_N = pn.Hhat22_pre_factor(x, eta)
    amp_pn = pn.Hhat22_x(x, eta)
    amp_pn = np.abs(amp_pn)
    return amp_N, amp_pn
        

def prepare_fit_data(waveform, t_start, t_end, target, dt=None):
    """
    waveform: instance of waveform
    t_start, t_end: float. start and end times that the returned data will cover
    target: str. name of target attribute to model e.g. 'amp', 'phase', 'freq'
    """
    eta = waveform.eta
    times = waveform.times
    mask = (times >= t_start) & (times <= t_end)

    t = times[mask]
    y = waveform.__getattribute__(target)
    y = y[mask]

    if dt != None:
        # interpolate with new spacing
        t_new = np.arange(t[0], t[-1], dt)
        y = IUS(t, y)(t_new)
        t = t_new
        
    return t, y

        
class WaveformCollocationFitter(object):
    """
    a class to manage fitting with the collocation method
    """
    def __init__(self,
                 x,
                 y,
                 collocation_points,
                 ansatz,
                 sub_dict={}, # empty dict by default
                ):
        """
        
        sub_dict: substitution dictionary for sympy ansatz
        """
        self.x = x
        self.y = y
        self.collocation_points = collocation_points
        self.ansatz = ansatz.copy()
        self.sub_dict = sub_dict.copy()
        # self.rhs_override = rhs_override
        

        # interpolate target so we can evaluate
        # it and it's derivative at any x value
        self.iy = IUS(self.x, self.y)
        
        # evaluate interpolant at corresponding derivative order
        # and location
        self.rhs = {}
        for k in self.collocation_points.keys():
            v = map(self.iy.derivative(k), self.collocation_points[k])
            v = np.array(list(v))
            self.rhs[k] = v
            
        # override rhs
        # can use this to enforce rhs values
        # if self.rhs_override is not None:
        #     for k in self.rhs_override.keys():
        #         for i, v in self.rhs_override[k]:
        #             self.rhs[k][i] = v
        
            
        self.cm = collocation.CollocationModel(
            collocation_points=self.collocation_points,
            rhs=self.rhs,
            ansatz=self.ansatz,
            sub_dict=self.sub_dict,
        )
        
        
        
def get_nrows(ncols, nsamples):
    """
    https://engineeringfordatascience.com/posts/matplotlib_subplots/
    """
    nrows = nsamples // ncols + (nsamples % ncols > 0)    
    return nrows

        
def plot_grid(xs, ys, ncols, figsize=(30, 30), titles=None, label=None, suptitle=None):
    """
    xs: array for x axis
    ys: array with shape (a,b,c)
        a: number of lines to plot (this will equal len(label))
        b: number of samples (plots) to plot
        c: number of time samples (this will be equal to len(xs))
    """
    assert len(ys) == len(label), "len(ys) == len(label) condition not met"
    assert len(xs) == len(ys[0][0]), "len(xs) == len(ys[0][0]) condition not met i.e. number of time samples not correct"
    nsamples = len(ys[0])
    nrows = get_nrows(ncols, nsamples)
    
    plt.figure(figsize=(30, 30))
    plt.subplots_adjust(hspace=0.8, wspace=0.2)
    if suptitle != None:
        plt.suptitle(suptitle, fontsize=22, y=0.91)
    
    for i in range(nsamples):
        ax = plt.subplot(nrows, ncols, i + 1)
        for j in range(ys.shape[0]):
            ax.plot(xs, ys[j][i], label=label[j])
        if label != None:
            ax.legend()
        if titles != None:
            ax.set_title(titles[i])

    plt.show()
        
        
def compute_alphas(xs, ys):
    """
    xs: pd.Series of mass-ratios
    ys: pd.DataFrame of collocation rhs values.
    
    sets the self.alphas attribute
    use this when you have multiple observations i.e. multiple mass-ratio x simulations
    for each collocation point we compute the standard deviation over observations
    and use this as a proxy for the uncertainty in that data point.
    for data points where we only have one observation we assume that their uncertainty
    is given by the median value of the distribution of standard deviations
    """
    
    alphas = {}
    for col in ys.columns:
        df = pd.DataFrame({'x':xs, 'y':ys[col]})
        # group by mass-ratio and compute standard deviation
        df2 = df.groupby(by='x').std()
        df2=df2.rename(columns={'y':'alpha'})
        # remove nans (these are the cases were only one simulation exists)
        # and compute the median value of the distribution of stds
        median_std = np.median(df2['alpha'].values[~np.isnan(df2['alpha'].values)])
        # print(median_std)
        # impute nans with median value
        # join back onto original dataframe so that we have a value of alpha
        # for every data point
        df3=pd.merge(df, df2.fillna(median_std), left_on='x', right_index=True).sort_index()
        alphas[col] = df3['alpha'].values

    return alphas


# def gpr_fit(x:np.ndarray, y:np.ndarray, GaussianProcessRegressor_kwargs, log_abs_transform=True):
def gpr_fit(x:np.ndarray, y:np.ndarray, GaussianProcessRegressor_kwargs):
    """
    use_estimate_alpha: if this is true then will use an estimate for alpha based on the data
    """
    # if log_abs_transform:
        # y = np.log(np.abs(y))
    gpr = GaussianProcessRegressor(**GaussianProcessRegressor_kwargs).fit(x[:,np.newaxis], y)
    
    return gpr


def transform_collocation_t_to_x(collocation_points, q, gpm_omega_inspiral):
    """
    given a dictionary of collocation points as a function of time
    we transform to the PN variable x(t) = (omega_22(t)/2)**(2/3)
    
    this requires the mass-ratio and the model for omega_22 (gpm_omega_inspiral)
    """
    collocation_points_out = copy.deepcopy(collocation_points)
    for d in collocation_points_out.keys():
        for i, v in enumerate(collocation_points_out[d]):
            om = gpm_omega_inspiral.predict(t=v, q=q)[0,0]
            x = pn.x_from_omega_22(om)
            collocation_points_out[d][i] = np.around(x, 8)
    return collocation_points_out

##
# custom model specific classes/functions
##

def get_fdamp_from_q(q):
    """
    estimate ringdown damping frequency from mass-ratio `q`.
    """
    eta = phenom.eta_from_q(q)
    fin_spin = phenom.remnant.FinalSpin0815(eta, 0, 0)
    fdamp = phenom.remnant.fdamp(eta, 0, 0, fin_spin)
    return fdamp

def get_fring_from_q(q):
    """
    estimate ringdown frequency from mass-ratio `q`.
    """
    eta = phenom.eta_from_q(q)
    fin_spin = phenom.remnant.FinalSpin0815(eta, 0, 0)
    fring = phenom.remnant.fring(eta, 0, 0, fin_spin)
    return fring
