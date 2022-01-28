#include <iostream>

using namespace std;
int main(int argc, char* argv[]){
  for(string s; getline(cin, s); ){
    cout << s << endl;
  }
  return 0;
}
