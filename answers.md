# CMPS 2200 Recitation 09

## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `recitation-09.md` here for easier grading.



- **2) (2 pts)** What is the worst-case work of your algorithm, assuming $G$ has $k$ connected components?

With $k$ connected components and $n$ total vertices, the densest graph (and one requiring the most work) has one complete component of $n - k - 1$ vertices and $k - 1$ isolated vertices

The amount of edges on this graph is $E = \frac{(n-k-1)(n-k)}{2} = (n-k+1)^{2}$

- **4) (2 pts)** What is the work of your full algorithm in the previous answer?
