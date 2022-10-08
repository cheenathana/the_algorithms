#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

void three_number_sum(vector<int>& arr, int targetsum, vector< vector<int>>& out) {
   // Sort the array
   sort(arr.begin(), arr.end());

   for (int i = 0; i < arr.size() -2; i++) {
      // Initialize right & left pointer with positional values
      int lptr = i + 1;
      int rptr = arr.size() - 1;

      // Loop to move the left & right pointers
      while (lptr < rptr) {
         int current_sum = arr[i] + arr[lptr] + arr[rptr];

         // CHECK 01
         if (current_sum == targetsum) {
            // Adding the current value in to output vector
            vector<int> tmp = {arr[i], arr[lptr], arr[rptr]};
            out.push_back(tmp);

            // Moving both the pointers
            lptr++;
            rptr--;
         }

         // CHECK 02
         if (current_sum < targetsum)
            lptr++;

         // CHECK 03
         if (current_sum > targetsum)
            rptr--;
      }
   }
}





// EXECUTION BEGINS HERE
int main() {
   // INPUTS
   vector<int> arr = {12, 3, 1, 2, -6, 5, -8, 6};
   int targetsum = 0;

   // OUTPUTS [[-8, 2, 6], [-8, 3,5], [-6, 1, 5]]
   vector< vector<int>> out;

   three_number_sum(arr, targetsum, out);

   // Printing output
   cout << "Triplets adds to target sum "<< targetsum << " are: " << endl;
   for (const auto i: out) {
      for (const auto j: i) {
         cout << j << " ";
      }
      cout << endl;
   }
}
