#include "Molecule.h"
#include <iostream>
#include <cstdlib>
#include <limits>
#include "mpi.h"

unsigned long monteCarlo(unsigned long e, std::vector<Boule> mol,
		double BB[3][2]) {
	// TODO: complete this function, exactly as in Ex. 3
	
	unsigned long ePrime = 0;
	for(unsigned long i = 0; i< e; i++){
                double pt[3];
                randomPoint(pt, BB);
                for(std::vector<Boule>::iterator it = mol.begin(); it!= mol.end(); it++){
                        if(it->contains(pt)){
                                ePrime++;
                                break;
                        }
                }
        }
	
	return ePrime;
}

int main(int argc, char **argv) {
	const int root = 0;

	int numtasks, taskid;
	MPI_Status status;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &taskid);
	MPI_Comm_size(MPI_COMM_WORLD, &numtasks);

	if (argc != 3) {
		if (taskid == root) {
			std::cerr << "Usage : " << argv[0]
				<< " e moleculefile (where e = # Monte Carlo trials)"
				<< std::endl;
		} else {
			// print nothing, fail quietly
		}
		MPI_Finalize();
		return 1;
	}

	const unsigned long e = atol(argv[1]);
	if (e <= 0) {
		if (taskid == root) {
			std::cerr << "Argument must be an integer > 0" << std::endl;
		} else {
			// print nothing, fail quietly
		}
		MPI_Finalize();
		return 1;
	}

	// In the spirit of reproducibility, explicit initialisation of seed
	srand(taskid);

	unsigned long elocal = 0;  // the number of samples for this process

	// TODO: the root decides how may samples will be handled by each of the
	// processors, and MPI_Scatters its decision
	unsigned long  e_per_task[numtasks];
	unsigned long counts = 0;
	for(int i=0; i< numtasks-1; i++){
		e_per_task[i] = e/numtasks;
		counts += e_per_task[i];	
	}
	e_per_task[numtasks-1] = e - counts;
	MPI_Scatter(&e_per_task,1,MPI_UNSIGNED_LONG,&elocal,1,MPI_UNSIGNED_LONG,root,MPI_COMM_WORLD);	

	// Load molecule.
	std::vector<Boule> molecule = readMolecule(argv[2]);
	// Bounding box.
	double BB[3][2];
	boundingBox(BB, molecule);

	unsigned long ePrime;
	unsigned long ePrimelocal = monteCarlo(elocal, molecule, BB);

	// TODO: Compute the global ePrime using MPI_Reduce.
	MPI_Reduce(&ePrimelocal,&ePrime,1,MPI_UNSIGNED_LONG,MPI_SUM,root,MPI_COMM_WORLD);
	if (taskid == root) {
		// The root computes and prints the final result.
		double vBB = 1.0;
		for (unsigned int i = 0; i < 3; i++) {
			vBB *= (BB[i][1] - BB[i][0]);
		}
		double vol = vBB * (double(ePrime) / double(e));
		// Set maximal precision when printing doubles.
		std::cout.precision(std::numeric_limits<double>::digits10 + 1);
		std::cout << "volume : " << vol << std::endl;
	} else {
		// nothing left to be done.
	}

	MPI_Finalize();
	return 0;
}
