#include "Molecule.h"
#include <iostream>
#include <cstdlib>
#include <limits>

unsigned long monteCarlo(unsigned long e, std::vector<Boule> mol,
                         double BB[3][2]) {
  // TODO: complete this function
  unsigned long ePrime = 0;
  for (unsigned int i = 0; i < e; ++i) {
    double pt[3];
    randomPoint(pt, BB);
    for (std::vector<Boule>::iterator b = mol.begin(), END = mol.end();
         b != END; ++b) {
      if (b->contains(pt)) {
        ePrime += 1;
        break;
      }
    }
  }
  return ePrime;
}

int main(int argc, char **argv) {
  if (argc != 3) {
    std::cerr << "Usage : " << argv[0]
              << " e moleculefile (where e = # Monte Carlo trials)"
              << std::endl;
    return 1;
  }

  const long e = atol(argv[1]);
  if (e <= 0) {
    std::cerr << "Argument must be an integer > 0" << std::endl;
    return 1;
  }

  // In the spirit of reproducibility, explicit initialisation of seed
  srand(0);

  // Load molecule.
  std::vector<Boule> molecule = readMolecule(argv[2]);
  // Bounding box.
  double BB[3][2];
  boundingBox(BB, molecule);

  // Compute volume.
  unsigned long ePrime = monteCarlo(e, molecule, BB);
  double vBB = 1.0;
  for (unsigned int i = 0; i < 3; i++) {
    vBB *= (BB[i][1] - BB[i][0]);
  }
  double vol = vBB * (double(ePrime) / double(e));

  // Set maximal precision when printing doubles.
  std::cout.precision(std::numeric_limits<double>::digits10);
  std::cout << "volume : " << vol << std::endl;

  return 0;
}
