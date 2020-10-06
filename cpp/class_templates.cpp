//class templates
#include <iostream>
using namespace std;

template <class T>
class mypair {
public:
	T values[2];
	mypair(T first, T second) {
		values[0] = first;
		values[1] = second;
	}

	T getmax();
};

template <class T>
T mypair<T>::getmax() {
	return values[0] > values[1] ? values[0] : values[1];
}

int main() {
	mypair<int> my_int_object(10, 20);
	mypair<double> my_double_objects(21.1, 32.2);

	cout << "my_int_object first: " << my_int_object.values[0] << endl;
	cout << "my_double_objects second: " << my_double_objects.values[1] << endl;
	cout << "my_int_object max: " << my_int_object.getmax() << endl;
	cout << "my_double_objects max: " << my_double_objects.getmax() << endl;
} 