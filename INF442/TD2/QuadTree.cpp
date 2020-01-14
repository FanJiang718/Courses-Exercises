#include "QuadTree.hpp"
#include <iostream>
using namespace std;

QuadTree::QuadTree(std::vector<Atom*>& v, Rectangle& r) {

	rectangle = r;

	if (v.size() == 0) {

		topLeft = 0;
		topRight = 0;
		bottomLeft = 0;
		bottomRight = 0;

		atom = 0;

	}
	else if (v.size() == 1) {

		topLeft = 0;
		topRight = 0;
		bottomLeft = 0;
		bottomRight = 0;

		atom = v[0];

	}
	else {

		atom = 0;
		Rectangle TL = Rectangle();
		TL = rectangle.topLeftRectangle();
    		Rectangle TR = Rectangle();
		TR = rectangle.topRightRectangle();
    		Rectangle BL = Rectangle();
		BL = rectangle.bottomLeftRectangle();
    		Rectangle BR = Rectangle();
		BR = rectangle.bottomRightRectangle();

		vector<Atom*> vTL;
		vector<Atom*> vTR;
		vector<Atom*> vBL;
		vector<Atom*> vBR;

		for(int i = 0; i < v.size(); ++i){
			if(TL.contains(v[i])){
				vTL.push_back(v[i]);
			}
			else if(TR.contains(v[i])){
				vTR.push_back(v[i]);
			}
			else if(BL.contains(v[i])){
				vBL.push_back(v[i]);
			}
			else if(BR.contains(v[i])){
				vBR.push_back(v[i]);
			}
		} 

		this->topLeft = new QuadTree(vTL, TL);
		this->topRight = new QuadTree(vTR, TR);
		this->bottomLeft = new QuadTree(vBL, BL);
		this->bottomRight = new QuadTree(vBR, BR);
	}
}

void QuadTree::print(unsigned int offset) const {

	if (topLeft) {

		for (unsigned int i = 0; i < offset; i++) std::cout << "\t";
		std::cout << "topLeft";
		std::cout << std::endl;
		topLeft->print(offset + 1);

		for (unsigned int i = 0; i < offset; i++) std::cout << "\t";
		std::cout << "topRight";
		std::cout << std::endl;
		topRight->print(offset + 1);

		for (unsigned int i = 0; i < offset; i++) std::cout << "\t";
		std::cout << "bottomLeft";
		std::cout << std::endl;
		bottomLeft->print(offset + 1);

		for (unsigned int i = 0; i < offset; i++) std::cout << "\t";
		std::cout << "bottomRight";
		std::cout << std::endl;
		bottomRight->print(offset + 1);

	}
	else if (atom) {

		for (unsigned int i = 0; i < offset; i++) std::cout << "\t";
		std::cout << "Atom = " << atom->x << " " << atom->y << std::endl;

	}

}

QuadTree::~QuadTree() {

	if (topLeft) delete topLeft;
	if (topRight) delete topRight;
	if (bottomLeft) delete bottomLeft;
	if (bottomRight) delete bottomRight;

}

void QuadTree::rangeSearch(std::vector<Atom*>& v, Rectangle& r) {

	if(this->atom != 0 && r.contains(atom)){
		v.push_back(this->atom);
	}

	if(this->topLeft != 0 && this->topLeft->rectangle.intersects(r)){
		topLeft->rangeSearch(v, r);
	}

	if(this->topRight != 0 && this->topRight->rectangle.intersects(r)){
		topRight->rangeSearch(v, r);
	}  

	if(this->bottomLeft != 0 && this->bottomLeft->rectangle.intersects(r)){
		bottomLeft->rangeSearch(v, r);
	}  

	if(this->bottomRight != 0 && this->bottomRight->rectangle.intersects(r)){
		bottomRight->rangeSearch(v, r);
	}
}
