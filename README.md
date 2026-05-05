This code is from HackerRank Python IfElse.
Following is the link for the same: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true.

TASK:
Given an integer, n, perform the following conditional actions:
- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird

SOLUTION:
1. What the problem is testing from us?
- Breaking a problem into cases.
- Ordering conditions correctly

2. Break the problems.
- Case 1 = check the odd numbers. Which means 1,3,5,7... are all odds
- Case 2 = now that only even numbers remain (2,4,6,8...), go for the conditions. 2-5 not weird, 6-20 weird, 20+ weird.

3. Visual understanding of the task is below.
            n
            |
     ----------------
     |              |
   Odd            Even
   |               |
 Weird     ---------------------
            |        |        |
          2-5      6-20     >20
           |         |        |
     Not Weird    Weird   Not Weird

4. Cleaner way to think this:
- When should I print "Weird"?
  Odd numbers, Even numbers between 6–20.
  Else remaining will be "Not Weird".
