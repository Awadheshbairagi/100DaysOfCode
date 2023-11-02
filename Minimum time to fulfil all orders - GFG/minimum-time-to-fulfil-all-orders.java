//{ Driver Code Starts
import java.io.*;
import java.util.*;


class IntArray
{
    public static int[] input(BufferedReader br, int n) throws IOException
    {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);
        
        return a;
    }
    
    public static void print(int[] a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
    
    public static void print(ArrayList<Integer> a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int n; 
            n = Integer.parseInt(br.readLine());
            
            
            int l; 
            l = Integer.parseInt(br.readLine());
            
            
            int[] arr = IntArray.input(br, l);
            
            Solution obj = new Solution();
            int res = obj.findMinTime(n, l, arr);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends


class Solution {
    public static int findMinTime(int n, int l, int[] arr) {
        int s = 0, e = 10000007;
        int mid, ans = -1;

        // Loop to implement binary search
        while (s <= e) {
            mid = (s + e) / 2;
            if (isPossible(n, arr, l, mid)) {
                ans = mid;
                e = mid - 1;
            } else {
                s = mid + 1;
            }
        }
        return ans;
    }

    public static boolean isPossible(int p, int[] cook, int n, int mid) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int c = 0;
            int time = mid;
            int perpratas = cook[i];
            while (time > 0) {
                time = time - perpratas;
                if (time >= 0) {
                    c += 1;
                    perpratas += cook[i];
                }
            }
            cnt += c;
            if (cnt >= p)
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        int N = 10, L = 4;
        int[] rank = new int[]{1, 2, 3, 4};

        // Function call
        System.out.println(findMinTime(N, L, rank));
    }
}

