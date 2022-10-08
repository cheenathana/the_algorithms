#include <stdlib.h>
#include <stdio.h>

int compare_val(const void* x, const void* y) {
   // Makeing the pointer to int pointer
   int element1 = *((int*)x);
   int element2 = *((int*)y);

   if (element1 > element2)
      return 1;
   
   if (element1 < element2)
      return -1;

   return 0;
}



void two_number_sum(int arr[], int size, int targetsum, int out[]) {
   int lptr = 0;
   int rptr = size - 1;

   while (1) {
      // Condition one
      if (arr[lptr] + arr[rptr] == targetsum) {
         out[0] = arr[lptr];
         out[1] = arr[rptr];
         break;
      }

      // Condition two and three
      if (arr[lptr] + arr[rptr] > targetsum)
         rptr -= 1;
      else 
         lptr += 1;
   }
}


/* EXECUTION BEGINS HERE */
int main() {
   int out[2];
   int arr[] = {3, 5, 44, 8, 11, 1, -1};
   int targetsum = 10;

   // Sort the array
   qsort(arr, sizeof(arr)/sizeof(arr[0]), sizeof(arr[0]), compare_val);

   two_number_sum(arr, sizeof(arr)/sizeof(arr[0]), targetsum, out);

   printf("Value are %d and %d which constitute %d\n", out[0], out[1], targetsum);

   return 0;
}
