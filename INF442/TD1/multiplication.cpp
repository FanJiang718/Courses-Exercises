#include <iostream>

int** lireMatrice(int& n, int& m)
{
  std::cin >> n;
  std::cin >> m;
  
  int** matrice = 0;

  matrice = new int*[n];

  for (int i = 0; i < n; i++)
    {
      matrice[i] = new int[m];
      for (int j = 0; j < m; j++)
	std::cin >> matrice[i][j];
    }
  return matrice;
}

int main(int argc, char** argv)
{
  // lecture des deux matrices A et B

  int nA, mA;
  int** A = lireMatrice(nA, mA);

  int nB, mB;
  int** B = lireMatrice(nB, mB);

  // affichage de A x B

  for (int i = 0; i < nA; i++)
    {
      for (int j = 0; j < mB; j++)
	{
	  int s = 0;
	  for (int k = 0; k < mA; k++)
	    s += A[i][k] * B[k][j];

	  std::cout << s;
	  if (j < mB - 1)
	    std::cout << " ";
	}
      std::cout << std::endl;
    }
  return 0;
}
