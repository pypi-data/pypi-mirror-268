import numpy as np

from hipersim.turbgen.spectral_tensor import MannTurbulenceInput, OnetimeMannSpectralTensor, MannSpectralTensor
from numpy import newaxis as na
import os
from hipersim.turbgen.turb_utils import logbin_values, spectra, bin_values
import time


class MannTurbulenceField(MannTurbulenceInput):
    def __init__(self, uvw, alphaepsilon, L, Gamma, Nxyz, dxyz, seed=None, HighFreqComp=0,
                 double_xyz=(False, True, True), n_cpu=1, random_generator=None, generator='unknown'):
        MannTurbulenceInput.__init__(self, alphaepsilon, L, Gamma, Nxyz, dxyz,
                                     seed, HighFreqComp, double_xyz,
                                     n_cpu, random_generator, generator)
        self.uvw = uvw

    @staticmethod
    def from_netcdf(filename):
        import xarray as xr
        da = xr.load_dataarray(filename)
        return MannTurbulenceField(da.values,
                                   Nxyz=da.shape[1:],
                                   dxyz=[(v[1] - v[0]).item() for v in (da.x, da.y, da.z)],
                                   generator=da.attrs['Generator'],
                                   **{k: da.attrs[k] for k in da.attrs if k not in ['Generator', 'name']}
                                   )

    @staticmethod
    def from_hawc2(filenames, alphaepsilon, L, Gamma, Nxyz, dxyz, seed,
                   HighFreqComp, double_xyz=(False, True, True), generator='Unknown'):
        uvw = np.reshape([np.fromfile(f, np.dtype('<f'), -1) for f in filenames], (3,) + tuple(Nxyz))
        return MannTurbulenceField(uvw, alphaepsilon, L, Gamma, Nxyz, dxyz, seed,
                                   HighFreqComp, double_xyz, generator=generator)

    def to_xarray(self):
        """Return xarray dataarray with u,v,w along x,y,z,uvw axes with all input parameters as attributes:
        - x: In direction of U, i.e. first yz-plane hits wind turbine last
        - y: to the left, when looking in the direction of the wind
        - z: up
        """
        import xarray as xr

        return xr.DataArray(self.uvw, dims=('uvw', 'x', 'y', 'z'),
                            coords={'x': np.arange(self.Nx) * self.dx,
                                    'y': np.arange(self.Ny) * self.dy,
                                    'z': np.arange(self.Nz) * self.dz,
                                    'uvw': ['u', 'v', 'w']},
                            attrs={'alphaepsilon': self.alphaepsilon, 'L': self.L, 'Gamma': self.Gamma,
                                   'HighFreqComp': self.HighFreqComp,
                                   'Generator': 'Hipersim', 'seed': self.seed,
                                   'double_xyz': np.array(self.double_xyz, dtype=int),
                                   'name': self.name})

    def to_netcdf(self, folder='', filename=None):
        da = self.to_xarray()
        filename = os.path.join(folder, filename or self.name + ".nc")
        da.to_netcdf(filename)

    def to_hawc2(self, folder='', basename=None):
        basename = basename or self.name
        for turb, uvw in zip(self.uvw, 'uvw'):
            filename = os.path.join(folder, basename + f"{uvw}.turb")
            turb.astype('<f').tofile(filename)

    @staticmethod
    def generate(alphaepsilon=1, L=33.6, Gamma=3.9, Nxyz=(8192, 64, 64),
                 dxyz=(1, 1, 1), seed=1, HighFreqComp=0, double_xyz=(False, True, True),
                 n_cpu=1, verbose=0, random_generator=None, cache_spectral_tensor=False):
        """Generate a MannTurbulenceField

        Parameters
        ----------
        alphaepsilon : float, optional
            Mann model turbulence parameter $(\\alpha \\varepsilon)^{2/3}$ (Mann, 1994), default is 1.
        L : float, optional
            Mann model turbulence length scale parameter $L$ (Mann, 1994), default is 33.6
        Gamma : float, optional
            Mann model turbulence anisotropy parameter $\\Gamma$ (Mann, 1994), default is 3.9
        Nxyz: (int,int,int)
            Dimension of the turbulence box in x (longitudinal), y (transveral) and z (vertical) direction.
            Default is (8192,64,64)
        dxyz : (float, float, float), optional
            Spacing in meters between data points along the x,y,z coordinates. Default is (1,1,1)
        seed : int, optional
            Seed number for random generator. Default is 1
        HighFreqComp : bool, optional
            Defines whether high-frequency compensation is applied. There are three options
            0 or False (default): No high-frequency compensation applied
            1 or True: A fast high-Frequency compensation method is applied. This method differs from the method in Mann (1998)
            2: The high-Frequency compensation method from the C++ version is applied.
            The method corresponds to Eq. A.6 in Mann (1998) except that the convolution is only applied in the (k2,k3),
            i.e. -2<=n_l<=2, l=(2,3)
        double_xyz : (bool,bool,bool)
            Defines whether doubling is enabled along the x, y and z direction.
            When doubling is applied, a box with the double size is generated and the first half is returned. In this
            way periodicity is avoided.
            Default is False in the x direction and True in the y and z direction
        n_cpu : int or None, optional
            Number of CPUs to use for the turbulence generation. Default is 1 (no parallelization).
            If None, all available CPUs are used.
        verbose : bool
            If true, status messages and progress bars are printed
        random_generator : function or None, optional
            If None (default), the random generator depends on n_cpu:
                n_cpu=1: hipersim.turbgen.spectral_tensor.random_generator_seq
                n_cpu!=1: hipersim.turbgen.spectral_tensor.random_generator_par
            Alternatively a function, f(MannSpectralTensor) -> RandomNumbers, dim=(3, N1r, N2, N3), can be specified
        cache_spectral_tensor : boolean, optional
            If True, the spectral tensor is loaded from file if exists otherwise it is calculated and saved to file
            If False, the spectral tensor is always recalculated

        Returns
        -------
        MannTurbulenceField-object
        """
        return OnetimeMannSpectralTensor(alphaepsilon, L, Gamma, Nxyz, dxyz, HighFreqComp,
                                         double_xyz, n_cpu=n_cpu, verbose=verbose,
                                         cache_spectral_tensor=cache_spectral_tensor).generate(
                                             seed=seed, alphaepsilon=alphaepsilon, random_generator=random_generator)

    @property
    def spectral_vars(self):
        if hasattr(self, 'mannSpectralTensor'):
            return self.mannSpectralTensor.spectral_vars

    def scale(self, sigma_u, k_low, k_high):
        spectrum_u_std = np.sqrt(self.spectrum_variance(k_low, k_high))

        scale = sigma_u / spectrum_u_std
        self.uvw *= scale
        self.alphaepsilon *= scale**2  # scales the variance

    def scale_TI(self, ti, U, T=600, cutoff_frq=10):
        sigma_u = ti * U
        k_low, k_high = 2 * np.pi / (U * np.array([T, 1 / cutoff_frq]))
        self.scale(sigma_u, k_low, k_high)

    def spectra(self, log10_bin_size=.2, min_bin_count=2):
        from hipersim.turbgen.turb_utils import spectra
        k, S = spectra(self.uvw, self.Nx, self.dx, exclude_zero=True)
        if log10_bin_size:
            S = [logbin_values(k, s, log10_bin_size=log10_bin_size, min_bin_count=min_bin_count) for s in S]
            k = logbin_values(k, k, log10_bin_size=log10_bin_size, min_bin_count=min_bin_count)
        return k, S

    def coherence(self, dy, dz, component='u', bin_size=.01, min_bin_count=2):
        c1, c2 = (component + component)[:2]
        i, j = 'uvw'.index(c1), 'uvw'.index(c2)
        ui, uj = self.uvw[i], self.uvw[j]
        if dy:
            dyi = int(np.round(dy / self.dy))
            ui, uj = ui[:, :-dyi], uj[:, dyi:]
        if dz:
            dzi = int(np.round(dz / self.dz))
            ui, uj = ui[:, :, :-dzi], uj[:, :, dzi:]
        Nx, dx = self.Nx, self.dx

        # k, (SUPii, SUPij, SUPjj) = spectra([ui, None, uj], Nx, dx, exclude_zero=False, spectra=['uu', 'uw', 'ww'])
        # f = (dx / (2 * np.pi * Nx)) * (1 / (np.sqrt(2) * Nx * dx))
        # SUPii, SUPij, SUPjj = [SUP / f for SUP in [SUPii, SUPij, SUPjj]]
        # Coherence = np.real(SUPij) / (np.sqrt(SUPii) * np.sqrt(SUPjj))

        if c1 == c2:
            k, (SUPii, SUPij) = spectra([ui, None, uj], Nx, dx, exclude_zero=False, spectra=['uu', 'uw'])
            Coherence = np.real(SUPij) / SUPii
        else:
            k, (SUPii, SUPij, SUPjj) = spectra([ui, None, uj], Nx, dx, exclude_zero=False, spectra=['uu', 'uw', 'ww'])
            Coherence = np.real(SUPij * np.conj(SUPij) / (SUPii * SUPjj))
        if bin_size:
            Coherence = bin_values(k, Coherence, bin_size=bin_size, min_bin_count=min_bin_count)[0]
            k = bin_values(k, k, bin_size=bin_size, min_bin_count=min_bin_count)[0]
        return k, Coherence

    def __call__(self, x, y, z):
        x, y, z = [np.asarray(v) for v in [x, y, z]]
        assert x.shape == y.shape == z.shape
        shape = np.shape(x)
        x, y, z = [v.flatten() for v in [x, y, z]]
        ui = np.array([[0, 0, 0, 0, 1, 1, 1, 1],
                       [0, 0, 1, 1, 0, 0, 1, 1],
                       [0, 1, 0, 1, 0, 1, 0, 1]])
        V = np.moveaxis(self.uvw, 0, -1)

        def modf(x, N, double):
            if double:
                # modulo into the interval [-(N-1), (N-1)] and take abs to get xf on mirrored axis
                N1 = N - 1
                xf = N1 - np.abs(x % (2 * N1) - N1)
                x0, x1 = np.floor(xf), np.ceil(xf)

                # switch x0 and x1 where x is on mirrored part of axis that points opposite the axis direction
                m = N1 - np.abs(np.floor(x) % (2 * N1) - N1) > xf
                x0[m], x1[m] = x1[m], x0[m]
                xf = np.abs(xf - x0)
            else:
                xf = x % N
                x0 = np.floor(xf)
                x0 = np.where(x0 == N, 0, x0)  # if x is negative and version small, e.g. -1e14, x%N = N
                xf = xf - x0
                x1 = ((x0 + 1) % N)
                x1 = np.where(x1 == N, 0, x1)  # if x is negative and version small, e.g. -1e14, x%N = N
            return xf, [x0, x1]

        xyz_i = np.array([x, y, z]).T / self.dxyz
        (xif, yif, zif), xyz_i01 = zip(*[modf(xi, N, double)
                                         for xi, N, double in zip(xyz_i.T, self.Nxyz,
                                                                  [self.double_x, self.double_y, self.double_z])])

        indexes = [x_i01[i] for x_i01, i in zip(np.array(xyz_i01, dtype=int), ui)]

        v000, v001, v010, v011, v100, v101, v110, v111 = V[tuple(indexes)]
        v_00 = v000 + (v100 - v000) * xif[:, na]
        v_01 = v001 + (v101 - v001) * xif[:, na]
        v_10 = v010 + (v110 - v010) * xif[:, na]
        v_11 = v011 + (v111 - v011) * xif[:, na]
        v__0 = v_00 + (v_10 - v_00) * yif[:, na]
        v__1 = v_01 + (v_11 - v_01) * yif[:, na]

        v = (v__0 + (v__1 - v__0) * zif[:, na])
        return v.reshape(shape + (3,))

    def constrain(self, Constraints, method=2):
        '''
        ===============================================
        APPLY CONSTRAINTS
        ==============================================='''
        '''
        ====================================================================
         COMPUTE MANN TENSOR VALUES, THEN IFFT TO GET CORRELATIONS
        ===================================================================='''
        print('Computing Mann tensor / correlation arrays for constrained simulation:')

        from hipersim.turbgen.manntensor import manntensorcomponents
        tstart = time.time()
        N1, N1r, N2, N3 = self.N1, self.N1r, self.N2, self.N3
        R0uu = np.zeros((N1, N2, N3), dtype='cfloat')
        R0vv = np.zeros((N1, N2, N3), dtype='cfloat')
        R0ww = np.zeros((N1, N2, N3), dtype='cfloat')
        R0uw = np.zeros((N1, N2, N3), dtype='cfloat')
        Nx, Ny, Nz = self.Nxyz
        dx, dy, dz = self.dxyz
        '''
        The u-v, and v-w components are not considered because Rho_uv and Rho_vw
        are zero in the Mann turbulence model
        '''
        pi = np.pi
        k1sim = np.concatenate([np.arange(0, Nx), np.arange(-Nx, 0)]) * (pi / (Nx * dx))
        k2sim = np.concatenate([np.arange(0, Ny), np.arange(-Ny, 0)]) * (pi / (Ny * dy))
        k3sim = np.concatenate([np.arange(0, Nz), np.arange(-Nz, 0)]) * (pi / (Nz * dz))

        k2simgrid, k3simgrid = np.meshgrid(k2sim, k3sim)
        '''
        Only half of the wave numbers are considered, it is considered that
        the correlation will be symmetric about k1 = 0
        '''
        from numpy.testing import assert_array_equal as ae

        def phi(k1):
            Phi11ij, Phi22ij, Phi33ij, __, Phi13ij, __ = manntensorcomponents(
                k1 * np.ones(k2simgrid.shape), k2simgrid, k3simgrid, self.Gamma, self.L, self.alphaepsilon, 2)
            return Phi11ij.T, Phi22ij.T, Phi33ij.T, Phi13ij.T
        assert method in [1, 2]
        if method == 1:
            Phi = np.moveaxis([phi(k1sim[ik1]) for ik1 in np.arange(Nx)], 0, 1)
            R0 = np.fft.ifft2(Phi, axes=(2, 3))
            Ruu, Rvv, Rww, Ruw = np.real(np.fft.ifft(np.concatenate(
                [np.conj(R0), R0[:, ::-1]], axis=1), axis=1))[:, :Nx, :Ny, :Nz]
        elif method == 2:
            Phi = np.moveaxis([phi(k1sim[ik1]) for ik1 in np.arange(N1r)], 0, 1)
            Ruu, Rvv, Rww, Ruw = np.fft.irfftn(Phi, axes=(3, 2, 1))[:, :Nx, :Ny, :Nz]

        Ruw = Ruw / (np.sqrt(Ruu[0, 0, 0] * Rww[0, 0, 0]))
        Ruu = Ruu / Ruu[0, 0, 0]
        Rvv = Rvv / Rvv[0, 0, 0]
        Rww = Rww / Rww[0, 0, 0]

        del R0uu, R0vv, R0ww, R0uw  # Clear memory from unnecessary variables

        t1 = time.time()
        print('Correlation computations complete')
        print('Time elapsed is ' + str(t1 - tstart))

        '''
        ================================================================
         Compute distances, normalize wind fields and constraint fields
        ================================================================'''

        ConstraintValuesUNorm = Constraints[:, 3]
        ConstraintValuesVNorm = Constraints[:, 4]
        ConstraintValuesWNorm = Constraints[:, 5]
        Unorm, Vnorm, Wnorm = self.uvw

        '''
        ==========================================
         ASSEMBLE CONSTRAINT COVARIANCE MATRIX
        =========================================='''
        print('Populating covariance matrix for the constraints:')
        Clocx = np.rint(Constraints[:, 0] / dx)
        Clocy = np.rint(Constraints[:, 1] / dy)
        Clocz = np.rint(Constraints[:, 2] / dz)
        '''
        ---------------------------------
         Eliminate overlapping constraints
        ---------------------------------'''
        ClocA = np.concatenate([np.atleast_2d(Clocx), np.atleast_2d(Clocy), np.atleast_2d(Clocz)]).T
        __, ClocIndex = np.unique(ClocA, axis=0, return_index=True)
        Constraints = Constraints[ClocIndex, :]
        Clocx = Clocx[ClocIndex]
        Clocy = Clocy[ClocIndex]
        Clocz = Clocz[ClocIndex]
        ConstraintValuesUNorm = ConstraintValuesUNorm[ClocIndex]
        ConstraintValuesVNorm = ConstraintValuesVNorm[ClocIndex]
        ConstraintValuesWNorm = ConstraintValuesWNorm[ClocIndex]
        Nconstraints = Constraints.shape[0]

        '''
        ---------------------------------------------
         Eliminate constraints too close to each other
        ---------------------------------------------'''
        Xdist = np.dot(np.atleast_2d(Constraints[:, 0]).T, np.ones([1, Nconstraints])) - \
            np.dot(np.ones([Nconstraints, 1]), np.atleast_2d(Constraints[:, 0]))
        Ydist = np.dot(np.atleast_2d(Constraints[:, 1]).T, np.ones([1, Nconstraints])) - \
            np.dot(np.ones([Nconstraints, 1]), np.atleast_2d(Constraints[:, 1]))
        Zdist = np.dot(np.atleast_2d(Constraints[:, 2]).T, np.ones([1, Nconstraints])) - \
            np.dot(np.ones([Nconstraints, 1]), np.atleast_2d(Constraints[:, 2]))

        Rdist = np.sqrt(Xdist**2 + Ydist**2 + Zdist**2)
        Rlimit = max([self.L / 10, min([dx, dy, dz])])
        Rexceed = (Rdist > 0) & (Rdist < Rlimit)
        ValidDistIndex = np.full((Rdist.shape[0]), True, dtype='bool')
        for i in range(Nconstraints):
            if np.any(Rexceed[i, :i]):
                Rexceed[i, :] = 0
                Rexceed[:, i] = 0
                ValidDistIndex[i] = False
        Constraints = Constraints[ValidDistIndex, :]
        Clocx = Clocx[ValidDistIndex].astype('int')
        Clocy = Clocy[ValidDistIndex].astype('int')
        Clocz = Clocz[ValidDistIndex].astype('int')
        ConstraintValuesUNorm = ConstraintValuesUNorm[ValidDistIndex]
        ConstraintValuesVNorm = ConstraintValuesVNorm[ValidDistIndex]
        ConstraintValuesWNorm = ConstraintValuesWNorm[ValidDistIndex]
        Nconstraints = Constraints.shape[0]

        del Rdist, Rexceed, ValidDistIndex

        '''
        -----------------------------
         Assemble u-v-w-correlation matrix
        -----------------------------'''
        CorrCMannUVW = np.zeros((3 * Nconstraints, 3 * Nconstraints))

        for iC in range(Nconstraints):
            xloci = Clocx[iC]
            yloci = Clocy[iC]
            zloci = Clocz[iC]
            xlocCij = np.abs(xloci - Clocx).astype('int')
            ylocCij = np.abs(yloci - Clocy).astype('int')
            zlocCij = np.abs(zloci - Clocz).astype('int')

            CorrUUij = Ruu[xlocCij, ylocCij, zlocCij]
            CorrVVij = Rvv[xlocCij, ylocCij, zlocCij]
            CorrWWij = Rww[xlocCij, ylocCij, zlocCij]
            CorrUWij = Ruw[xlocCij, ylocCij, zlocCij]

            CorrCMannUVW[:Nconstraints, iC] = CorrUUij
            CorrCMannUVW[iC, :Nconstraints] = CorrUUij
            CorrCMannUVW[Nconstraints:2 * Nconstraints, Nconstraints + iC] = CorrVVij
            CorrCMannUVW[Nconstraints + iC, Nconstraints:2 * Nconstraints] = CorrVVij
            CorrCMannUVW[2 * Nconstraints:, 2 * Nconstraints + iC] = CorrWWij
            CorrCMannUVW[2 * Nconstraints + iC, 2 * Nconstraints:] = CorrWWij
            CorrCMannUVW[2 * Nconstraints:, iC] = CorrUWij
            CorrCMannUVW[iC, 2 * Nconstraints:] = CorrUWij

        t2 = time.time()
        print('Constraint-constraint covariance matrix has been assembled')
        print('Time elapsed is ' + str(t2 - t1))

        '''
        =========================================================
         APPLY CONSTRAINT EQUATIONS TO COMPUTE THE RESIDUAL FIELD
        =========================================================
         Using eq.(2) from Dimitrov & Natarajan (2016) to compute
         the residual field which is to be added to the unconstrained
         field in order to obtain the constrained result.

         Due to memory limitations, eq. (2) is evaluated in batches intended
         to avoid the need of fully assembling the first term in the equation,
         which is a matrix with size (Nx*Ny*Nz)x(Nconstraints).
         First, the product of the second and third term is evaluated,
         then it is multiplied piecewise to a subset of the rows of the
         first term.
        '''
        print('Applying constraints...')
        ConstraintValuesUVWNorm = np.concatenate([ConstraintValuesUNorm, ConstraintValuesVNorm, ConstraintValuesWNorm])
        UVWcontemporaneous = np.zeros((3 * Nconstraints))
        UVWcontemporaneous[:Nconstraints] = Unorm[Clocx, Clocy, Clocz]
        UVWcontemporaneous[Nconstraints:2 * Nconstraints] = Vnorm[Clocx, Clocy, Clocz]
        UVWcontemporaneous[2 * Nconstraints:] = Wnorm[Clocx, Clocy, Clocz]

        '''
         Computing the product of the second and third terms in eq.(2) in
         Dimitrov & Natarajan (2016)
        '''

        CConstUVW = np.linalg.solve(CorrCMannUVW, (ConstraintValuesUVWNorm - UVWcontemporaneous))
        # CConstUVW = np.dot(np.linalg.inv(CorrCMannUVW), ConstraintValuesUVWNorm - UVWcontemporaneous)

        CConstU = np.atleast_2d(CConstUVW[:Nconstraints]).T
        CConstV = np.atleast_2d(CConstUVW[Nconstraints:2 * Nconstraints]).T
        CConstW = np.atleast_2d(CConstUVW[2 * Nconstraints:]).T
        del CorrCMannUVW

        Ruu = Ruu.reshape(Nx * Ny * Nz)
        Rvv = Rvv.reshape(Nx * Ny * Nz)
        Rww = Rww.reshape(Nx * Ny * Nz)
        Ruw = Ruw.reshape(Nx * Ny * Nz)

        ygrid, xgrid, zgrid = np.meshgrid(np.arange(Ny), np.arange(Nx), np.arange(Nz))
        xvect = xgrid.reshape(Nx * Ny * Nz)
        yvect = ygrid.reshape(Nx * Ny * Nz)
        zvect = zgrid.reshape(Nx * Ny * Nz)

        del xgrid, ygrid, zgrid

        ures = np.zeros(Nx * Ny * Nz)
        vres = np.zeros(Nx * Ny * Nz)
        wres = np.zeros(Nx * Ny * Nz)

        dxic = (np.abs(np.arange(Nx)[na] - Clocx[:, na]) * (Ny * Nz))[:, :, na, na]
        dyic = (np.abs(np.arange(Ny)[na] - Clocy[:, na]) * Nz)[:, na, :, na]
        dzic = np.abs(np.arange(Nz)[na] - Clocz[:, na])[:, na, na, :]

        for dxi, dyi, dzi, constU, constV, constW in zip(dxic, dyic, dzic, CConstU, CConstV, CConstW):
            dlinear = (dxi + dyi + dzi).flatten()
            CorrUUi = Ruu[dlinear]
            CorrVVi = Rvv[dlinear]
            CorrWWi = Rww[dlinear]
            CorrUWi = Ruw[dlinear]
            ures += CorrUUi * constU + CorrUWi * constW
            vres += CorrVVi * constV
            wres += CorrUWi * constU + CorrWWi * constW

        Uconstrained = Unorm + np.reshape(ures, (Nx, Ny, Nz))
        Vconstrained = Vnorm + np.reshape(vres, (Nx, Ny, Nz))
        Wconstrained = Wnorm + np.reshape(wres, (Nx, Ny, Nz))

        tend = time.time()
        print('Constrained simulation complete')
        print('Total time elapsed is ' + str(tend - tstart))

        self.uvw = np.array([Uconstrained, Vconstrained, Wconstrained])
