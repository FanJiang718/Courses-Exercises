#include <iostream>
using namespace std;

class Complex {

public:

	Complex();
	Complex(double a, double b);
	double module();
	~Complex();


	double a;
	double b;

};

ostream& operator<<(ostream& s, const Complex& c);

