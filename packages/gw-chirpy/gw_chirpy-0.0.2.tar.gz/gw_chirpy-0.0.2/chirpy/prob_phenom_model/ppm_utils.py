"""
Generative Probabilistic Phenomenological Model (GPM)
Or Probabilistic Phenomenological Model (PPM)
"""

import cloudpickle
import phenom
import numpy as np
import copy
from scipy.interpolate import InterpolatedUnivariateSpline as IUS
import lal
import pycbc.types

from chirpy.prob_phenom_model import pn, collocation, workflow_utils



import sympy
# x_sym: generic name I use for independent variables for sympy
x_sym = sympy.symbols('x_sym')


class GPM_Omega_Inspiral(object):
    def __init__(self, model_components_filename):
        self.model_components_filename = model_components_filename

        data = self.load_model_components(self.model_components_filename)
        self.tc = data["tc"]
        self.M = data["M"]
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]
        self.signs_dict = data["signs_dict"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        tc = self.tc
        M = self.M
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps
        signs_dict = self.signs_dict

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        omega_N, omega_pn = workflow_utils.get_taylort3_inspiral_omega_affine_params(t, tc, eta, M)
        
        theta = pn.TaylorT3_theta(x_sym, tc, eta, M)
        pn_sub_dict = {'x_sym': np.array(theta)}
        ansatz = base_ansatz.subs(pn_sub_dict)
        
        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(t)
            yhat = workflow_utils.transformation_affine_foward(yhat, omega_N, omega_pn)
            yhats.append(yhat)
        
        return np.array(yhats)
    
    
class GPM_Amp_Inspiral(object):
    def __init__(self, model_components_filename, gpm_omega_inspiral):
        self.model_components_filename = model_components_filename
        self.gpm_omega_inspiral = gpm_omega_inspiral

        data = self.load_model_components(self.model_components_filename)
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        tc = self.gpm_omega_inspiral.tc
        M = self.gpm_omega_inspiral.M
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        omega_22 = self.gpm_omega_inspiral.predict(t, q, n_samples=-1)[0]
        x_pn = pn.x_from_omega_22(omega_22, M=M)
        amp_N, amp_pn = workflow_utils.get_taylort3_inspiral_amp_affine_params(omega_22, eta, M)

        ansatz = base_ansatz.copy()
        
        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    # v = np.exp(v)
                    # v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    # v = np.exp(v)
                    # v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        collocation_points_x = workflow_utils.transform_collocation_t_to_x(
            collocation_points=collocation_points,
            q=q,
            gpm_omega_inspiral=self.gpm_omega_inspiral
        )
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points_x,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(x_pn)
            yhat = workflow_utils.transformation_affine_foward(yhat, amp_N, amp_pn)
            yhats.append(yhat)
        
        return np.array(yhats)
    
    
class GPM_Omega_Merger(object):
    def __init__(self, model_components_filename):
        self.model_components_filename = model_components_filename

        data = self.load_model_components(self.model_components_filename)
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]
        self.signs_dict = data["signs_dict"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps
        signs_dict = self.signs_dict

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        ang_fdamp = workflow_utils.get_fdamp_from_q(q)*2*np.pi

        sub_dict = {'a_sym':ang_fdamp}
        ansatz = base_ansatz.subs(sub_dict)

        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(t)
            yhat = workflow_utils.transformation_affine_foward(yhat)
            yhats.append(yhat)
        
        return np.array(yhats)
    
class GPM_Amp_Merger(object):
    def __init__(self, model_components_filename):
        self.model_components_filename = model_components_filename

        data = self.load_model_components(self.model_components_filename)
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]
        self.signs_dict = data["signs_dict"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps
        signs_dict = self.signs_dict

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        ang_fdamp = workflow_utils.get_fdamp_from_q(q)*2*np.pi

        sub_dict = {'a_sym':ang_fdamp}
        ansatz = base_ansatz.subs(sub_dict)

        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(t)
            yhat = workflow_utils.transformation_affine_foward(yhat, eta)
            yhats.append(yhat)
        
        return np.array(yhats)
    
    
class GPM_Omega_Ringdown(object):
    def __init__(self, model_components_filename):
        self.model_components_filename = model_components_filename

        data = self.load_model_components(self.model_components_filename)
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]
        self.signs_dict = data["signs_dict"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps
        signs_dict = self.signs_dict

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        ang_fdamp = workflow_utils.get_fdamp_from_q(q)*2*np.pi

        sub_dict = {'a_sym':ang_fdamp}
        ansatz = base_ansatz.subs(sub_dict)

        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(t)
            yhat = workflow_utils.transformation_affine_foward(yhat)
            yhats.append(yhat)
        
        return np.array(yhats)
    

class GPM_Amp_Ringdown(object):
    def __init__(self, model_components_filename):
        self.model_components_filename = model_components_filename

        data = self.load_model_components(self.model_components_filename)
        self.collocation_points = data["collocation_points"]
        self.base_ansatz = data["base_ansatz"]
        self.gps = data["gps"]
        self.signs_dict = data["signs_dict"]


    def load_model_components(self, model_components_filename):
        with open(model_components_filename, 'rb') as f:
            data = cloudpickle.load(f)
        return data


    def predict(self, t, q, n_samples=-1, random_state=None):
        """
        if n_samples = -1 then generate the mean otherwise draw a n_samples
        """
        collocation_points = self.collocation_points
        base_ansatz = self.base_ansatz
        gps = self.gps
        signs_dict = self.signs_dict

        if random_state == None:
            random_state = np.random.randint(0, 1000000)
        if n_samples == -1:
            mode = "mean"
            n_samples = 1
        else:
            mode = "sample"
        
        t = np.atleast_1d(t)
        eta = phenom.eta_from_q(q)
        log_q = np.log(q)
        
        ang_fdamp = workflow_utils.get_fdamp_from_q(q)*2*np.pi

        sub_dict = {'a_sym':ang_fdamp}
        ansatz = base_ansatz.subs(sub_dict)

        # number of derivatives
        num_d_points = len(collocation_points.keys())
        # number of collocations points for each derivative
        num_c_points = [len(collocation_points[d]) for d in collocation_points.keys()]
        
        rhs = {}
        ## if mean then use the 'predict' method from the GP
        if mode == "mean":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].predict([[log_q]])
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(np.array([v]))
        ## if sample then use the 'sample_y' method from the GP
        elif mode == "sample":
            for d in range(num_d_points):
                rhs[d] = []
                for c in range(num_c_points[d]):
                    tag = f"d{d}_c{c}"
                    v = gps[tag].sample_y([[log_q]], n_samples, random_state=random_state)
                    v = np.exp(v)
                    v = signs_dict[tag].values * v
                    rhs[d].append(v.T)
        else:
            raise ValueError(f"mode = {mode} unknown")

        # store a copy
        rhs_ = copy.deepcopy(rhs)
        
        yhats = []
        for n in range(n_samples):
            
            # have to extract the rhs for each sample
            for d in rhs_.keys():
                for i in range(len(rhs_[d])):
                    rhs[d][i] = rhs_[d][i][n,0]
                    
                    
            # for 1st derivative to be zero at peak
            rhs[1][0] = 0.

                    
            cm = collocation.CollocationModel(
                collocation_points=collocation_points,
                rhs=rhs,
                ansatz=ansatz,
                sub_dict=None,
            )
            yhat = cm.predict(t)
            yhat = workflow_utils.transformation_affine_foward(yhat, eta)
            yhats.append(yhat)
        
        return np.array(yhats)
    

    
def rd_ansatz_log(t, a, b):
    return np.log(a) - t*b

def connect_rd(t0, y0, fdamp):
    """
    y0 == y(t0)
    this is just fixing the constant offset between the phenom model from peak amplitude
    to about t0=30M.
    We assume the slope is given by the approximately known damping frequency
    We assume exponential decay so it's linear in log-space
    """
    b = fdamp*2*np.pi
    log_a = np.log(y0) + b * t0
    return np.exp(log_a), b

def td_amp_scale(mtot, distance):
    """
    mtot in solar masses
    distance in m
    M*G/c^2 * M_sun / dist
    """
    return mtot * lal.MRSUN_SI / distance

class PPM(object):
    def __init__(self,
                 inspiral_freq_model_components_filename,
                 merger_freq_model_components_filename,
                 ringdown_freq_model_components_filename,
                 inspiral_amp_model_components_filename,
                 merger_amp_model_components_filename,
                 ringdown_amp_model_components_filename,
                ):
        self.inspiral_freq_model_components_filename = inspiral_freq_model_components_filename
        self.merger_freq_model_components_filename = merger_freq_model_components_filename
        self.ringdown_freq_model_components_filename = ringdown_freq_model_components_filename
        self.inspiral_amp_model_components_filename = inspiral_amp_model_components_filename
        self.merger_amp_model_components_filename = merger_amp_model_components_filename
        self.ringdown_amp_model_components_filename = ringdown_amp_model_components_filename
        
        self.gpm_omega_inspiral = GPM_Omega_Inspiral(model_components_filename=self.inspiral_freq_model_components_filename)
        self.gpm_omega_merger = GPM_Omega_Merger(model_components_filename=self.merger_freq_model_components_filename)
        self.gpm_omega_ringdown = GPM_Omega_Ringdown(model_components_filename=self.ringdown_freq_model_components_filename)
        
        self.gpm_amp_inspiral = GPM_Amp_Inspiral(model_components_filename=self.inspiral_amp_model_components_filename, gpm_omega_inspiral=self.gpm_omega_inspiral)
        self.gpm_amp_merger = GPM_Amp_Merger(model_components_filename=self.merger_amp_model_components_filename)
        self.gpm_amp_ringdown = GPM_Amp_Ringdown(model_components_filename=self.ringdown_amp_model_components_filename)
        
        # self.freq_t0 = -300
        self.freq_t0 = -100
        self.freq_t1 = 0
        
        # self.amp_t0 = -300
        self.amp_t0 = -100
        self.amp_t1 = 0
        self.amp_t2 = 30
        

    def generate_frequency(self, t, q, n_samples=-1, random_state=None):
        """
        n_samples is only used when you specify that you want to sample the model and the output shape is going to be (n_samples, n_time)
        if you want to compute the mean model (i.e. use the mean from the GP) then n_samples should be left at 1 and the output will be (1, n_time)
        """
        
        mask = t < self.freq_t0
        inspiral_times = t[mask]
        
        mask = (t >= self.freq_t0) & (t < self.freq_t1)
        merger_times = t[mask]

        mask = t >= self.freq_t1
        ringdown_times = t[mask]

        y_ins = self.gpm_omega_inspiral.predict(inspiral_times, q, n_samples=n_samples, random_state=random_state)
        y_merger = self.gpm_omega_merger.predict(merger_times, q, n_samples=n_samples, random_state=random_state)
        y_ringdown = self.gpm_omega_ringdown.predict(ringdown_times, q, n_samples=n_samples, random_state=random_state)
        
        return np.concatenate((y_ins, y_merger, y_ringdown), axis=1)
    
    def generate_amplitude(self, t, q, n_samples=-1, random_state=None):
        
        mask = t < self.amp_t0
        inspiral_times = t[mask]
        
        mask = (t >= self.amp_t0) & (t < self.amp_t1)
        merger_times = t[mask]

        mask = (t >= self.amp_t1) & (t < self.amp_t2)
        ringdown_times = t[mask]

        mask = t >= self.amp_t2
        late_ringdown_times = t[mask]

        y_ins = self.gpm_amp_inspiral.predict(inspiral_times, q, n_samples=n_samples, random_state=random_state)
        y_merger = self.gpm_amp_merger.predict(merger_times, q, n_samples=n_samples, random_state=random_state)
        y_ringdown = self.gpm_amp_ringdown.predict(ringdown_times, q, n_samples=n_samples, random_state=random_state)
        
        # compute all late ringdowns
        # note that the `b`'s only depend on mass-ratio
        # so we only have one of them and not n_samples of them

        # this is the value of the final point
        # which we use to connect the exponential ringdown
        y0 = self.gpm_amp_ringdown.predict(self.amp_t2, q, n_samples=n_samples, random_state=random_state)
        # y0 = y0[np.newaxis, :]
        
        fdamp = workflow_utils.get_fdamp_from_q(q)

        a, b = connect_rd(t0=self.amp_t2, y0=y0, fdamp=fdamp)

        y_late_ringdown = np.exp(rd_ansatz_log(late_ringdown_times, a, b))
        
        return np.concatenate((y_ins, y_merger, y_ringdown, y_late_ringdown), axis=1)

    
    def generate_phase(self, t, q, n_samples=-1, random_state=None):
        """
        n_samples: if -1 then will use the mean, otherwise generates samples
        """
        
        freqs = self.generate_frequency(t, q, n_samples, random_state)
        ifreqs = [IUS(t, f) for f in freqs]
        phis = np.array([ifreq.antiderivative()(t) for ifreq in ifreqs])
        return phis
        

    def generate_h22(self, t, q, n_samples=-1, random_state=None):
        """
        n_samples: if -1 then will use the mean, otherwise generates samples
        """
        
        amps = self.generate_amplitude(t, q, n_samples, random_state)
        phis = self.generate_phase(t, q, n_samples, random_state)
        
        # check sign
        h22s = amps * np.exp(1.j * phis)
        
        return h22s

        
        
  
    def generate_pycbc_hp_hc(self, times, q, M, delta_t, distance=1e6 * lal.PC_SI, n_samples=-1, random_state=None, theta=0, phi=0):
        """
        n_samples: if -1 then will use the mean, otherwise generates samples
        
        q: mass-ratio >= 1
        times: times in units of M
        M: in units of Msun
        delta_t: output delta_t in seconds
        distance: in metres
        """
        dt_M = times[1] - times[0]
        times_s = phenom.MtoS(times, M)
        
        epoch = phenom.MtoS(times[0], M)
        
        h22 = self.generate_h22(times, q, n_samples, random_state)
        
        h22 *= td_amp_scale(M, distance)
        h22 *= lal.SpinWeightedSphericalHarmonic(theta, phi, -2, 2, 2)
        
        hp = h22.real
        hc = h22.imag

        t0 = phenom.MtoS(times[0], M)
        t1 = phenom.MtoS(times[-1], M)
        new_times = np.arange(t0, t1, delta_t)
        
        hp = [IUS(times_s, hp_)(new_times) for hp_ in hp]
        hc = [IUS(times_s, hc_)(new_times) for hc_ in hc]
        hp = [pycbc.types.TimeSeries(hp_, delta_t=delta_t, epoch=epoch) for hp_ in hp]
        hc = [pycbc.types.TimeSeries(hc_, delta_t=delta_t, epoch=epoch) for hc_ in hc]
        
        return hp, hc

        
