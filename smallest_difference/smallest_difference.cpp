#include <iostream>
#include <vector>
#include <bits/stdc++.h>
#include <cstdlib>

using namespace std;

void smallest_difference(vector<int>& arr1, vector<int>& arr2, vector<int>& out) {
   // Sort both the array
   sort(arr1.begin(), arr1.end());
   sort(arr2.begin(), arr2.end());

   // var to point to the array elements
   int idx1 = 0;
   int idx2 = 0;

   // Using the "out" array last element for holding the smallest diff value
   // initialize smallest difference with biggest value as a starter value
   out[2] = 99999;

   while (idx1 < arr1.size() && idx2 < arr2.size()) {
      // Difference b/w current array elements
      int diff = abs(arr1[idx1] - arr2[idx2]);

      if (diff == 0) {
         // if the difference is zero, then these are the pairs with 
         // smallest difference
         out[0] = arr1[idx1];
         out[1] = arr2[idx2];
         out[2] = diff;

         return;
      }

      // validating current diff with smallest_diff and updating the value
      if (diff < out[2]) {
         out[0] = arr1[idx1];
         out[1] = arr2[idx2];         
         out[2] = diff;
      }

      // Moving the array position pointers
      if (arr1[idx1] < arr2[idx2])
         idx1++;
      else 
         idx2++;
   }

   return;
}





/* Execution begins here */
int main() {
   // INPUT
   vector<int> arr1 = {-1, 5, 10, 20, 28, 3};
   vector<int> arr2 = {26, 134, 135, 15, 17};

   // OUTPUT [pair1, pair2, smallest_diff]
   vector<int> out(3);

   smallest_difference(arr1, arr2, out);

   cout << "PAIRS: " << out[0] << ", " << out[1] << endl;
   cout << "And their difference is " << out[2] << endl;

   return 0;
}
