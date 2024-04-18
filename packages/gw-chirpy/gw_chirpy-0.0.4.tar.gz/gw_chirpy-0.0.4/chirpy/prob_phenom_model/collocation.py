import numpy as np

import sympy
# sympy.init_printing()
x_sym = sympy.symbols('x_sym')

class CollocationModel(object):
    def __init__(self, collocation_points, rhs, ansatz, sub_dict=None):
        """
        collocation_points: dictionary with integer keys representing the order
            of derivative and the values are a list of numbers that are the
            values of the x-coordinate to evaluate the rhs at.
            {0:[], 1:[], ...}
            [[d0], [d1], [d2], ...]
            d0 == points to evaluate RHS at zeroth derivative
            d1 == points to evaluate RHS at 1st derivative
            d2 == points to evaluate RHS at 2nd derivative ...etc
            The sum total of elments of the flattened list is the
            number of equations and equivalently the number of
            coefficients to fix by comparing with data.
            Data is provided as the right hand side (RHS).
        rhs: right hand side (rhs)
            provided in the same format as collocation_points
        ansatz: sympy stuff
            this must be a linear-in-coefficients ansatz so that
            it can be expressed in a matrix form
        sub_dict: this is a dictionary mapping sympy symbol name to a constant
            this is needed because after we (potentially) differentiate the ansatz
            term we need to evaluate the expression so we need a value for these constants
        """
        self.collocation_points = collocation_points
        self.rhs = rhs
        self.sub_dict = sub_dict
        
        # flatten collocation points
        # collocation_points = []
        # [collocation_points.extend(r) for r in self.collocation_points]
        # self.collocation_points_1d = np.array(collocation_points, dtype=np.float64)
        # self.collocation_points_1d = np.concatenate(self.collocation_points)
        self.collocation_points_1d = np.concatenate([v for k, v in self.collocation_points.items()])
        
        # flatten right hand side
        # rhs = []
        # [rhs.extend(r) for r in self.rhs]
        # self.rhs_1d = np.array(rhs, dtype=np.float64)
        # self.rhs_1d = np.concatenate(self.rhs)
        self.rhs_1d = np.concatenate([v for k, v in self.rhs.items()])
        
        assert len(self.collocation_points_1d) == len(self.rhs_1d), "number of collocation points and rhs are not the same"
        
        # set degrees of freedom
        self.dof = len(self.collocation_points_1d)
        
        self.ansatz = ansatz.copy()
        
        assert self.dof == len(self.ansatz.args), f"ansatz doesn't contain correct number of degrees of freedom. dof = {self.dof}. Ansatz has {len(self.ansatz.args)}"
        
        # create some human readable names for the collocation points
        # for example if collocation_points = {0:[1,2,3], 1:[2,3]}
        # then tags = ["d0_c1","d0_c2","d0_c3", "d1_c1", "d1_c2"]
        self.tags = []
        for d in self.collocation_points.keys():
            for c in range(len(self.collocation_points[d])):
                self.tags.append(f"d{d}_c{c}")
        
        
        self.lambdify_ansatz(sympy_args=(x_sym))
        self.create_information_matrix()
        self.fit()
        
    def lambdify_ansatz(self, sympy_args):
        """
        sympy_args: these are the sympy symbols that that lambda function will
            be a function of
        """
        # terms_fn: list of sympy.lambdify functions
        # each element of the list corresponds to each term in the ansatz
        ansatz = self.ansatz.copy()
        if self.sub_dict is not None:
            ansatz = ansatz.subs(self.sub_dict)
        # self.terms_fn = [sympy.lambdify(sympy_args, term, "numpy") for term in self.ansatz.args]
        self.terms_fn = [sympy.lambdify(sympy_args, term, "numpy") for term in ansatz.args]
        
    def create_information_matrix(self):
        """
        evaluate the ansatz at the collocation_points
        
        extra_sub_dict: this is a dictionary mapping sympy symbol name to a constant
            this is needed because after we (potentially) differentiate the ansatz
            term we need to evaluate the expression so we need a value for these constants
        """
        # compute information matrix

        # need to compute derivatives term by term
        # that way we can be sure that we arrive at the correct number of
        # elements in each row
        # and then we can correctly handle when a derivative is zero.
        row = []
        # loop over groups of collocation points which corresponds to different derivative orders
        # for d in range(len(self.collocation_points)):
        for d in self.collocation_points.keys():
            # loop over each collocation point for each derivative
            for c in self.collocation_points[d]:
                # take derivative of each term in the ansatz
                terms = [sympy.diff(term, x_sym, d) for term in self.ansatz.args]
                # evaluate terms at given collocation point
                sub_dict = {'x_sym':c}
                # evaluate terms at given constants (if any)
                if self.sub_dict is not None:
                    sub_dict.update(self.sub_dict)
                row.append([term.subs(sub_dict) for term in terms])
            ########
            # delete this block after refactoring
            # for c in self.collocation_points[d]:
            #     # initial substituations
            #     ansatz_args = [term.subs(self.sub_dict) for term in self.ansatz.args]
            #     # take derivative of each term in the ansatz
            #     # terms = [sympy.diff(term, x_sym, d) for term in self.ansatz.args]
            #     terms = [sympy.diff(term, x_sym, d) for term in ansatz_args]
            #     # evaluate terms at given collocation point
            #     sub_dict = {'x_sym':c}
            #     # evaluate terms at given constants (if any)
            #     # if self.sub_dict is not None:
            #     #     sub_dict.update(self.sub_dict)
            #     row.append([term.subs(sub_dict) for term in terms])
            #     print(row)
            ########
        information_matrix = np.array(row, dtype=np.float64)
        self.information_matrix = information_matrix
        
    def fit(self, information_matrix=None, rhs=None):
        if information_matrix is None:
            information_matrix = self.information_matrix
        if rhs is None:
            rhs = self.rhs_1d
        self.coeffs = np.linalg.solve(information_matrix, rhs)
        
    def get_basis(self, x, dtype=object):
        """
        dtype: used to be object because in sympy when we have a constant
        term such as x_sym**0 this gets simplified to just '1'.
        This doesn't get broadcast when you pass an array but
        seems to work with dtype=object
        """
        basis = np.array([t(x) for t in self.terms_fn], dtype=dtype)
        return basis
        
    def predict(self, x, residual=None, dtype=np.float64):
        """
        TODO: remove residual part - deal with this outside
        """
        # turn basis into a property that only gets
        # recalculated when the `x`s change.
        basis = self.get_basis(x)

        if residual is None:
            return np.dot(self.coeffs, basis).astype(dtype)
        else:
            return (np.dot(self.coeffs, basis) + residual).astype(dtype)