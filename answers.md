# CMPS 2200 Recitation 09

## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-09.md` here for easier grading.



- **2) (2 pts)** What is the worst-case work of your algorithm, assuming $G$ has $k$ connected components?

With $k$ connected components and $n$ total vertices, the densest graph (and one requiring the most work) has one complete component of $n - k - 1$ vertices and $k - 1$ isolated vertices

The amount of edges on this graph is $E = \frac{(n-k-1)(n-k)}{2} = (n-k+1)^{2}$

The loop checks every vertex, giving $O(n)$

prim_helper goes through each vertex's adjacency list; undirected edges appear in two lists. So there are at most $n-k+1$ operations done in prim_helper, costing $log(n-k+1)$ 

So, the total worst-case cost is $W(n,k) = O(n + (n-k+1)log(n-k+1))$


- **4) (2 pts)** What is the work of your full algorithm in the previous answer?

Building the edges loops through $n$ points twice; $O(n^{2})$

The worst case for the prim calculation is $k=1$, where the work is $O(n^{2}logn)$

Returning tree cost $O(1)$

Total work is $W(n) = O(n^{2} + n^{2}logn + 1) = O(n^{2}logn)$
