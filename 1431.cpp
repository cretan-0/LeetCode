#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        bool result[n];
        int res[n];
        for(int i = 0; i<n; i++) {
            res[i] = candies[i] + extraCandies;
            if(res[i] > res[i-1])
                result[i] = true;
            else
                result[i] = false;
        result[0] = true;
        cout << result[i] << endl;
        }
    }
};

int main()
{
    Solution solution;
    vector<int> v ={12,1,12}; //{4,2,1,1,2}; error on test case 2
    solution.kidsWithCandies(v, 1);
    return 0;
}