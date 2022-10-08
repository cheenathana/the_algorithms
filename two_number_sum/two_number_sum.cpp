#include <iostream>
#include <vector>
#include <map>

using namespace std;

void two_number_sum_using_map(vector<int>& arr, int targetsum, vector<int>& out) {
   map<int, bool> tmp;

   for (auto i: arr) {
      int val = targetsum - i;

      if (tmp.find(val) != tmp.end()) {
         out.push_back(val);
         out.push_back(i);
      }
      else
         tmp.insert(pair<int, bool>(i, true));
   }
}


void two_number_sum(vector<int>& arr, int targetsum, vector<int>& out) {
   int lptr = 0;
   int rptr = arr.size() - 1;

   while (1) {
      if (arr[lptr] + arr[rptr] == targetsum) {
         out.push_back(arr[lptr]);
         out.push_back(arr[rptr]);
         break;
      }

      if (arr[lptr] + arr[rptr] > targetsum)
         rptr -= 1;
      else
         lptr += 1;
   }
}


/* Execution begins here */
int main() {
   vector<int> out1;
   vector<int> out2;
   vector<int> arr = {3, 5, -1, 8, 11, 1, -1};
   int targetsum = 10;

   two_number_sum_using_map(arr, targetsum, out1);
   two_number_sum(arr, targetsum, out2);

   cout << "APPROCH 1: The values constitute target sum is " << out1[0] << " and " << out1[1] << endl;
   cout << "APPROCH 2: The values constitute target sum is " << out2[0] << " and " << out1[1] << endl;

   return 0;
}
