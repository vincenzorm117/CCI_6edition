


#include<iostream>

using namespace std;
  
class Animal {
public: 
    virtual void print () { 
        cout<< "print Animal class" <<endl; 
    } 
    void show () { 
        cout<< "show Animal class" <<endl; 
    } 
}; 
  
class Dog:public Animal {
public: 
    void print () {
        cout<< "print Dog class" <<endl;
    }
  
    void show () {
        cout<< "show Dog class" <<endl;
    }
}; 

void runAnimal(Animal *creature) {    
    //virtual function, binded at runtime 
    creature->print();  
      
    // Non-virtual function, binded at compile time 
    creature->show();  
}


void runDog(Dog *creature) {    
    //virtual function, binded at runtime 
    creature->print();  
      
    // Non-virtual function, binded at compile time 
    creature->show();  
}
  
  
int main() {
    Dog dog;
    runAnimal(&dog);
    runDog(&dog);
} 