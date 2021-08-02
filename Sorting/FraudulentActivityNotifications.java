/*
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, 
they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least 
that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the 
client will receive a notification over all n days.

Example
expenditure = [10, 20, 30, 40, 50]
d=3

On the first three days, they just collect spending data. At day 4, trailing expenditures are [10, 20, 30]. 
The median is 20 and the day's expenditure is 40. Because 40 >= 2*20, there will be a notice. 
The next day, trailing expenditures are [20, 30, 40] and the expenditures are 50. This is less than 2*30 so no notice will be sent. Over the period, there was one notice sent.
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
     * Complete the 'activityNotifications' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY expenditure
     *  2. INTEGER d
     */

    public static int activityNotifications(List<Integer> expenditure, int d) {
    // Write your code here
    
     int[] count = new int[201];
        int result = 0;
        for(int i = 0; i < d; i++){
            count[expenditure.get(i)]++;
        }
        for(int i = d; i < expenditure.size(); i++){
            int median = getMedian(count, d);
            if(median <= expenditure.get(i)){
                result++;
            }
            count[expenditure.get(i-d)]--;
            count[expenditure.get(i)]++;
        }
        return result;
    }
    
    public static int getMedian(int[] count, int d){
        int sum = 0;
        for(int i = 0; i < count.length; i++){
            sum += count[i];
            if((2*sum) == d){
                return (2*i+1);
            }else if((2*sum) > d){
                return (i*2);
            }
        }
        return 1;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int d = Integer.parseInt(firstMultipleInput[1]);

        String[] expenditureTemp = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        List<Integer> expenditure = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int expenditureItem = Integer.parseInt(expenditureTemp[i]);
            expenditure.add(expenditureItem);
        }

        int result = Result.activityNotifications(expenditure, d);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

// Although getting a solution is easy, the optimisation for this problem was extremely difficult. Sorting only even d elements is extremely time consuming.
// Also consider the case of median in the even case. Lot's of resources pointed to using count sort to solve this problem. The solution given in the code above
// does just that. 
