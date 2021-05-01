#include <iostream>
#include <string>
using namespace std;

class student {
private:
    string name;
    int ShomareDaneshjooi;
    int moadel;
public:
    void increment() {
      moadel++;
    }
    void rename(){

    }
    void set(string nameo, int s) {
      student.nameo = s;
    }
    int print() {
      return student.nameo;
    }
};

int main(){
  student student;
  student.increment();
  cout << student.moadel;
}
