/*It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. 
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example :
if q = [1, 2, 3, 5, 4, 6, 7, 8]
If person 5 bribes person 4, the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8 . Only 1 bribe is required. Print 1.

if q = [4, 1, 2, 3]
Person 4 has to bribe 3 people to get to the current position. Print too chaotic


Sample Input

STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]


Sample Output

3
Too chaotic
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
     * Complete the 'minimumBribes' function below.
     *
     * The function accepts INTEGER_ARRAY q as parameter.
     */

    public static void minimumBribes(List<Integer> q) {
    // Write your code here
    int swap = 0;
    int flag = 0;
    for(int i=0; i<q.size(); i++){
        if(q.get(i) - i - 1>2){
            flag = 1;
        }
    }
    if(flag==1){
        System.out.println("Too chaotic");
    }
    else{
            for(int i = 1;i < q.size(); i++) {
                int j = i;
                while(j > 0 && q.get(j) < q.get(j-1)) {
                    int temp = q.get(j);
                    q.set(j, q.get(j-1));
                    q.set(j-1, temp);
                    j--;
                    swap += 1;
                }
            }
            System.out.println(swap);       
        }
        
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Integer.parseInt(bufferedReader.readLine().trim());

            String[] qTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

            List<Integer> q = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qTemp[i]);
                q.add(qItem);
            }

            Result.minimumBribes(q);
        }

        bufferedReader.close();
    }
}

// I was able to solve the question with relative ease. The only issue faced was time complexity. 
// Hence, avoid using Bubble or Selection sort and go for insertion/quick sort.
