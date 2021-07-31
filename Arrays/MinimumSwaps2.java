/*You are given an unordered array consisting of consecutive integers belonging to [1, 2, 3, ..., n] without any duplicates. 
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

Example: arr = [7, 1, 3, 2, 4, ,5, 6]

Solution:
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]

Hence, it took 5 swaps to sort the array.
*/
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the minimumSwaps function below.
    static int minimumSwaps(int[] arr) {
        
        int swap = 0;
        
        for (int i = 0; i < arr.length; i++){
            // Checking if number at corresponding index is wrong 
            if(arr[i] != i + 1){
                // Start searching for actual element
                for (int j = i + 1; j < arr.length; j++){
                    // If element is found, perform a swap and break from the loop
                    if(arr[j] == i + 1){
                        arr[j] = arr[i];
                        arr[i] = i + 1;
                        swap++;
                        break;
                    }
                }
            }
        }
        return swap;
    }    

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int res = minimumSwaps(arr);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

// I had to think a little bit to solve this problem. Initially, I tried using sorting techniques but then realised that the numbers are supposed to be
// in order with their particular index so I could discard that approach. Then I looked at how I can swap digits successfully. One approach could be to use 
// a Dictionary datatype but that felt a little cumbersome. Another way was to carry out a search for the element if there was a mismatch between element and index and swap.
// I tried this and also looked at a blog. This method worked and was able to execute under the alloted time, hence I decided to go with this solution.
