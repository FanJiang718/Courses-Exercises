#include "Complex.hpp"
#include <math.h>
using namespace std;


Complex::Complex() {
	a = 0.0;
	b = 0.0;
}


Complex::Complex(double _a, double _b){
	this->a = _a;
	(*this).b = _b;
}


double Complex::module(){
	double _a = this->a;
	double _b = (*this).b;
	return pow( ( pow(_a, 2) + pow(_b, 2) ), 0.5 );
}


Complex::~Complex() {}



ostream& operator<<(ostream& s, const Complex& c){
        s << c.a;
        if (c.b > 0){
                s << "+" << c.b << "*i";
        }
        else{
                if (c.b < 0){
                        s << c.b << "*i";
                }
        }
        return s;
}

