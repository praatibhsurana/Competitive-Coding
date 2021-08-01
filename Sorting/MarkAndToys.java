/*
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 
Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.

Sample Input

7 50
1 12 5 111 200 1000 10

Sample Output

4

Explanation

He can buy only  toys at most. These toys have the following prices: 1, 5, 10, 12.

*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class Result {

    /*
     * Complete the 'maximumToys' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY prices
     *  2. INTEGER k
     */

    public static int maximumToys(List<Integer> prices, int k) {
    // Write your code here
    int max = 0;
    int sum = 0;
    
    Collections.sort(prices); 
    for(int i=0; i<prices.size(); i++){
        if (prices.get(i)<=k && sum<=k){
            sum += prices.get(i);
            max++;
            if(sum>k){
                max--;
            }
        }
    }
    return max;
    
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int k = Integer.parseInt(firstMultipleInput[1]);

        String[] pricesTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> prices = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int pricesItem = Integer.parseInt(pricesTemp[i]);
            prices.add(pricesItem);
        }

        int result = Result.maximumToys(prices, k);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

// Very straightforward as is visible from the code. I just sorted the list using the inbuilt collections function. 
// The summation part to calculate max toys could further be optimised but the compiler ran all test cases so I did not bother to change the code.
