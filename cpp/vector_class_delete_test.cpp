/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>

using namespace std;

class Person {
    public:
    Person(int age_self, int age_wife);
    
    private:
    int age_self;
    int age_wife;
};

Person::Person(int age_self, int age_wife){
    age_self = age_self;
    age_wife = age_wife;
}

Person* dummy_processing(Person* p){
    cout << "inside dummy_processing:" << endl;
    return p;
}

int main()
{
    cout<<"Hello World";
    
    Person* p_raja = new Person(30, 25);
    Person* p_ram = new Person(24, 19);
    Person* p_mohan = new Person(100, 80);
    Person* p_roy = new Person(50, 40);
    
    Person* p_kallan = dummy_processing(p_roy);
    
    vector<Person*> dbase;
    dbase.push_back(p_raja);
    dbase.push_back(p_ram);
    dbase.push_back(p_mohan);
    dbase.push_back(p_roy);
    
    dbase.push_back(p_kallan);
    
    cout << "\nno of entries: " << dbase.size() << endl;
    
    for (auto it=dbase.begin(); it!=dbase.end();){
        Person* p_man = *it;
        
        delete p_man;
        it = dbase.erase(it);
    }
    
    cout << "\nno of entries after delete: " << dbase.size() << endl;

    return 0;
}
