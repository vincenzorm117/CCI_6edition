


#include <iostream>


using namespace std;

template <class T>class SmartPointer {

    T* ptr;
public:
    SmartPointer(T* ptr = NULL) ptr(ptr) {

    }



    SmartPointer<T> & operator=(SmartPointer<T> &sptr) {
        
    }

    ~SmartPointer() {

    }

    T getValue() {

    }
private:
    int count = 0;

    void remove() {

    }
}

int main() {

}