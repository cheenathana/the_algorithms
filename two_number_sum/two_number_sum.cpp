#include <iostream>
#include <vector>
#include <map>
#include <bits/stdc++.h>

using namespace std;

/* APPROACH I */
void two_number_sum_using_map(vector<int>& arr, int targetsum, vector<int>& out) {
   // Empty hashtable to hold the arr elements
   map<int, bool> tmp;

   for (auto i: arr) {
      int val = targetsum - i;

      if (tmp.find(val) != tmp.end()) {
         out.push_back(val);
         out.push_back(i);
      }
      else
         // If the value never contributes to target sum, then add it to hashtable
         tmp.insert(pair<int, bool>(i, true));
   }
}


/* APPROACH II */
void two_number_sum(vector<int>& arr, int targetsum, vector<int>& out) {
   // sort the array in ascending order
   sort(arr.begin(), arr.end());

   int lptr = 0;
   int rptr = arr.size() - 1;

   while (1) {
      int current_sum = arr[lptr] + arr[rptr];

      if (current_sum == targetsum) {
         out.push_back(arr[lptr]);
         out.push_back(arr[rptr]);
         break;
      }

      // Moving the pointer based on comparing current_sum and targetsum
      if (current_sum > targetsum)
         rptr -= 1;
      else
         lptr += 1;
   }
}



/* Execution begins here */
int main() {
   vector<int> out1;
   vector<int> out2;
   vector<int> arr = {3, 5, 300, 8, 11, 1, -1};
   int targetsum = 10;

   two_number_sum_using_map(arr, targetsum, out1);
   two_number_sum(arr, targetsum, out2);

   cout << "APPROCH 1: The values constitute target sum is " << out1[0] << " and " << out1[1] << endl;
   cout << "APPROCH 2: The values constitute target sum is " << out2[0] << " and " << out1[1] << endl;

   return 0;
}
