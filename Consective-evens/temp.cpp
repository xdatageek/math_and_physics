#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using std::string;
using std::stringstream;
using std::cout;
using std::endl;

int main(int argc,char** argv) {

    string num="-24 2 90 24 50 76 2 0 3";

    stringstream stream(num);

    int n;
    std::vector<int> values;
    while(stream >> n){
        cout << n << endl;
        values.push_back(n);
    }

    return 0;
}