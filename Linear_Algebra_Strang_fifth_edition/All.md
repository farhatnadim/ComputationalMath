Problems with * have numerical/sympy solutions



### 12 
#### Problem   
The vector $\vec{b}$ is in the subspace spanned by the columns of A when "    " has a solution . The vector $\vec{c}$ is in the row space of A when  "    " has a solution.
#### Solution 
The vector $\vec{b}$ is in the subspace spanned by the columns of A when the equation $A\vec{x} = \vec{b}$ has a solution. The vector $\vec{c}$ is in the row space of A when the equation $A^T\vec{y} = \vec{c}$ has a solution.
#### Problem 
True or False : if the zero vector is in the row space , the rows are dependent .
#### Solution
False : The zero vector is always in the row space of any matrix.

### 13 * 
#### Problem
Find the dimensions of these 4 spaces . Which two of the spaces are the same ? (a) The column space of A (b) The column space of U (c) The row space of A (d) The row space of U.  
$A = \begin{bmatrix} 1 & 1 & 0  \\ 1 & 3 & 1 \\ 3 & 1 & -1   \end{bmatrix}$ and $U = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 2  & 1 \\ 0 & 0 & 0\end{bmatrix}$
#### Solution
The column spaces and row space for both A and U  have dimension = 2  . for the column space of the Matrix A, the first vector is a combination of the first two . 
$\vec{c_1} = \vec{c_2} - 2*\vec{c_3}$.  and $\vec{c_2} ,\vec{c_3}$ are independent.   
THe columns space  
The column space of U is different than the column space of A;
 if you notice there we cannot write the the first column of A with any combination of the columns of U ( third element is zero )
The row spaces are the same though because they can be written as a linear combination of each others
#### Sympy Solution 
```python  
import sympy as sp 

A = sp.Matrix([[1, 1,0], [1, 3, 1], [3, 1, -1]])
U = sp.Matrix([[1,1,0],[0,2,1],[0,0,0]])

A[1,:] = A[1,:] - A[0,:]
A[2,:] = A[2,:] - 3 * A[0,:]
A[2,:] = A[2,:] + A[1,:]
print(A)
```