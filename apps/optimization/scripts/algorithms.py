
import numpy as np

class CGA:
    def __init__(self, n_p, bounds, func, bin_len = 65, dec = 48):
        self.func = func
        self.__n_p = n_p
        self.initialization(n_p, bounds, bin_len, dec)
        self.bin_len = bin_len
        self.dec = dec
        self.best_x = None
        self.best_fx = None
        self.worst_x = None
        self.worst_fx = None

    def float2bin(self,float_, length = 65, dec = 48):
        if float_ >= 0:
            sign = '0'
        else:
            sign = '1'
        int_ = int(float_)
        frac_ = abs(float_ - int_)
        bin_ = ''

        for i in range(dec):

            if frac_ >= 1/(2 ** (i + 1)):
                bin_ += '1'
                frac_ -= 1/(2 ** (i + 1))
            else:
                bin_ += '0'

        bin_int = bin(int_).split('b')[ - 1]
        if len(bin_int) < length - dec - 1:
            bin_int = '0' * (length - dec - 1 - len(bin_int)) + bin_int
        return sign + bin_int + bin_

    def bin2float(self, bin_, length = 65, dec = 48):

        if isinstance(bin_, int):
            bin_ = str(bin_)
        if len(bin_) < length:
            bin_ = '0' * (length - len(bin_)) + bin_
        if bin_[0] == '1':
            sign = - 1
        else:
            sign = 1
        int_ = bin_[1:length - dec]
        frac_ = bin_[-dec:]
        float_0 = np.array([int(int_[-i]) * 2  ** (i - 1) for i in range(1,
                                                        len(int_) + 1)]).sum()

        float_1 = np.array([int(frac_[i - 1])/(2  ** i) for i in range(1,
                                                        len(frac_) + 1)]).sum()

        return sign * (float_0 + float_1)

    def initialization(self, n_p, bounds = ( - 65536.0, 65536.0), bin_len=65,
                       dec=48):
        self.x = np.random.uniform(bounds[0], bounds[1], n_p)

        self.x_bin = np.array([self.float2bin(i, bin_len, dec) for i in self.x])

        self.fx = np.array([self.func(x) for x in self.x])
        self.fxs = []
        self.fxs_ = []

    def selection(self):
        to_change = self.fm <= np.array(self.fx)
        self.x[to_change] = self.m[to_change][:]
        self.fx[to_change] = self.fm[to_change][:]
        self.x_bin[to_change] = self.m_bin[to_change]

    def mutation(self, r=0.5):
        v_bin = np.array([[j for j in i] for i in self.v_bin])
        mutation_point = np.random.rand(v_bin.shape[0],v_bin.shape[1])<=r

        m_bin = v_bin.copy()
        m_bin[np.logical_and(mutation_point, v_bin=='1')] = '0'
        m_bin[np.logical_and(mutation_point, v_bin=='0')] = '1'

        self.m_bin = np.array([''.join(i) for i in m_bin])
        self.m = np.array([self.bin2float(i, self.bin_len, self.dec) for i in \
                           self.m_bin])
        self.fm = np.array([self.func(x) for x in self.m])

    def crossover(self):
        self.rank =  np.argsort(self.fx)
        prob = (len(self.rank) - self.rank)/sum(self.rank + 1)
        cross_point  = np.random.randint(0,self.bin_len,size=len(self.x))
        self.v_bin = [self.x_bin[i][cross_point[i]:] + \
                      np.random.choice(self.x_bin,size=1, \
                      p=prob)[0][:cross_point[i]]  for i in range(self.__n_p)]

    def run(self, n_g= 100, diff_ = 3.552713678800501e-15, verbose=False):
        g = 0
        while True:
            self.crossover()
            self.mutation()
            self.selection()
            i_min = np.argmin(self.fx)
            i_max = np.argmax(self.fx)
            self.fxs.append(self.fx[i_min])
            self.fxs_.append(self.fx[i_max])

            g +=1
            if g>=n_g:
                if verbose:
                    print('Max number of iteration reached.')
                break
            if abs(self.fx[i_max] - self.fx[i_min]) <= diff_:
                if verbose:
                    print('Precision reached.')
                break

        self.best_x = self.x[i_min]
        self.best_fx = self.fx[i_min]
        self.worst_x = self.x[i_max]
        self.worst_fx = self.fx[i_max]
        if verbose:
            print('Best x:', self.best_x, '\t - >\tBest fx', self.best_fx)
            print('Worst x:', self.worst_x, '\t - >\tWorst fx', self.worst_fx)

class DE:
    def __init__(self, func, bounds, np_ = 4, cr = 0.9, f = 0.8):
        self.func = func
        self.__np = np_
        self.__cr = cr
        self.__f = f
        self.low = bounds[0]
        self.up = bounds[1]
        self.initialization()

    def initialization(self):
        self.x = np.array([self.low + (self.up - self.low) *\
                np.random.uniform(size=len(self.up)) for i in range(self.__np)])
        self.fx = np.array([self.func(x) for x in self.x])
        self.fxs = []
        self.fxs_ = []

    def selection(self):
        to_change = self.fu <= self.fx
        self.x[to_change] = self.u[to_change][:]
        self.fx[to_change] = self.fu[to_change][:]

    def mutation(self):
        abc = np.random.randint(self.__np, size=(self.__np, 3))

        v = [self.x[abc[i,:][0]] + self.__f * (self.x[abc[i,:][1]] - \
                            self.x[abc[i,:][2]]) for i in range(len(self.x))]

        v = [[i[j] if i[j] > self.low[j] else self.low[j] for j in \
                                                    range(len(i))] for i in v]

        self.v = np.array([[i[j] if i[j]<self.up[j] else self.up[j] for j in \
                                                    range(len(i))] for i in v])

    def crossover(self):
        r = np.random.uniform(size=self.x.shape)<self.__cr
        self.u = self.x.copy()
        self.u[r] = self.v[r]
        self.fu = np.array([self.func(x) for x in self.u])

    def run(self, n_g= 100, diff_ = 3.552713678800501e-15, verbose = False):
        g = 0
        while True:
            self.mutation()
            self.crossover()
            self.selection()

            i_min = np.argmin(self.fx)
            i_max = np.argmax(self.fx)
            self.fxs.append(self.fx[i_min])
            self.fxs_.append(self.fx[i_max])

            g +=1
            if g>=n_g:
                if verbose:
                    print('Max number of iteration reached.')
                break

        if verbose:
            print('Best x:', self.x[i_min], '\t - >\tBest fx', self.fx[i_min])
            print('Worst x:', self.x[i_max], '\t - >\tWorst fx', self.fx[i_max])

