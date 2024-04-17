import numpy as np
from dataclasses import dataclass
from elphem.lattice.empty import EmptyLattice

@dataclass
class FreeElectron:
    """Represents a free electron model on a given crystal lattice.
    
    Attributes:
        lattice (EmptyLattice): The lattice on which the free electron model is applied.
        n_band (int): Number of energy bands considered.
        n_electron (int): Number of electrons per unit cell.
    """
    lattice: EmptyLattice
    n_band: int
    n_electron: int
    
    def __post_init__(self):
        """Validate and initialize the FreeElectron model."""
        if not isinstance(self.lattice, EmptyLattice):
            raise TypeError("The type of first variable must be EmptyLattice.")
        if self.n_electron <= 0:
            raise ValueError("Second variable (number of electrons per unit cell) should be a positive value.")
        
        self.electron_density = self.n_electron / self.lattice.volume["primitive"]
        self.g = self.get_reciprocal_vector()

    def fermi_energy(self) -> float:
        """Calculate the Fermi energy of the electron system.

        Returns:
            float: The Fermi energy.
        """
        return 0.5 * (3 * np.pi ** 2 * self.electron_density) ** (2/3)

    def eigenenergy(self, k: np.ndarray) -> np.ndarray:
        """Calculate the electron eigenenergies at wave vector k.

        Args:
            k (np.ndarray): A numpy array representing vectors in reciprocal space.

        Returns:
            np.ndarray: The electron eigenenergies at each wave vector.
        """
        return 0.5 * np.linalg.norm(k, axis=-1) ** 2 - self.fermi_energy()
    
    def grid(self, n_k: np.ndarray) -> tuple:
        """Generate a (G, k)-grid for electron states calculation.

        Args:
            n_k (np.ndarray): A numpy array specifying the density of k-grid points in each direction of reciprocal space.

        Returns:
            tuple: A tuple containing G-meshgrid and k-meshgrid for electron state calculations.
        """
        basis = self.lattice.basis["reciprocal"]
        
        k_x = np.linspace(-0.5, 0.5, n_k[0])
        k_y = np.linspace(-0.5, 0.5, n_k[1])
        k_z = np.linspace(-0.5, 0.5, n_k[2])
        k = np.array(np.meshgrid(k_x, k_y, k_z, indexing='ij')).T.reshape(-1, 3) @ basis

        k_grid = np.tile(k, (self.n_band, 1, 1))
        g_grid = np.repeat(self.g[:, np.newaxis, :], len(k), axis=1)

        return g_grid, k_grid
    
    def get_band_structure(self, k_names: list[np.ndarray], n_split: int) -> tuple:
        """Calculate the electronic band structures along the specified path in reciprocal space.

        Args:
            k_names (list[np.ndarray]): A list of special points names defining the path.
            n_split (int): Number of points between each special point to compute the band structure.

        Returns:
            tuple: A tuple containing x-coordinates for plotting, eigenenergy values, and x-coordinates of special points.
        """
        x, k, special_x = self.lattice.reciprocal_cell.path(k_names, n_split)
        
        eigenenergy = np.array([self.eigenenergy(k + g_i) for g_i in self.g])
        
        return x, eigenenergy, special_x
    
    def get_reciprocal_vector(self) -> np.ndarray:
        """Generate the reciprocal lattice vectors used to define the Brillouin zone boundaries.

        Returns:
            np.ndarray: An array of reciprocal lattice vectors.
        """
        basis = self.lattice.basis["reciprocal"]

        n_cut = np.ceil(np.cbrt(self.n_band))

        n_1d = np.arange(-n_cut, n_cut + 1)
        n_3d = np.array(np.meshgrid(n_1d, n_1d, n_1d)).T.reshape(-1, 3)
        
        g = n_3d @ basis
        g_norm = np.linalg.norm(g, axis=-1).round(decimals=5)
        g_norm_unique = np.unique(g_norm)

        g_list = []

        for g_ref in g_norm_unique:
            count = 0
            for g_compare in g_norm:
                if g_compare == g_ref:
                    g_list.append(g[count])
                count += 1

        return np.array(g_list[0:self.n_band])