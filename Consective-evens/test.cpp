#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums){
    int count=0;
    int max=0;
    for(int i=0;i<nums.size();i++){
        count=(nums[i]>0) ? ++count:count*nums[i];
        max=(max<count) ? count:max;
    }
    return max;
}
int main()
{
    std::ifstream file("input.txt");
    std::string line;
    getline(file, line);
    getline(file, line);
    stringstream stream(line);
    int n, N = 0, l, r,cmd;
    std::vector<int> A,a;
    while(stream >> n){
        A.push_back(n);
        N++;
    }
    int i, sum =0;
    for (i = 0; i < N; i++){ 
        A[i] = abs((A[i]+1)%2);
    }
    getline(file, line);
    while (std::getline(file, line))
    {
        stringstream stream(line);
        stream >> n;
        cmd = n;
        stream >> n;
        l = n;
        stream >> n;
        r = n;
        if (cmd==1){
           a = std::vector<int>(A.begin() + l, A.begin() + r +1);
            cout << findMaxConsecutiveOnes(a) << endl;
        }else{
            A[l] = abs((r + 1) % 2);
        }
    }
}
