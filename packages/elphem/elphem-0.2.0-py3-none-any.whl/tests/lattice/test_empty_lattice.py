from unittest import TestCase
import numpy as np

from elphem.lattice.empty import EmptyLattice

class TestUnit(TestCase):
    def test_vector(self):
        lattice = EmptyLattice('fcc', 5.0)
        basis_primitive = lattice.basis["primitive"]
        basis_reciprocal = lattice.basis["reciprocal"]

        for b in [basis_primitive, basis_reciprocal]:
            self.assertEqual(b.shape, (3,3))
    
    def test_volume(self):
        lattice = EmptyLattice('sc', 4.65)
        volume = lattice.volume["primitive"]
        self.assertTrue(abs(volume - np.prod(lattice.constants.length)) < 1e-10)