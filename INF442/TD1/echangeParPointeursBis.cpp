#include <iostream>

void swap(int* a, int* b)
{
  *a=*a xor *b;
  *b=*b xor *a;
  *a=*a xor *b;
}

int main(int argc, char **argv)
{
  int a = 0;
  int b = 0;
	
  std::cin >> a;
  std::cin >> b;
	
  swap(&a,&b);
	
  std::cout << a << " " << b << std::endl;
  
  return 0;
}
