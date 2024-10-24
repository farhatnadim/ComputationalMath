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
The column spaces and row space for both A and U  have dimension = 2.   
The rref of the Matrix A  has two pivot columns that means the rank of the marix is 2 and the column space dimension is 2
The rref of the Matrix A Transpose has two pivot columns that means the ranks of the matrix is 2 and the row space dimension is 
We expect the same for U since U 

The column space of A and U are the same , not the row spaces 

#### Sympy Solution 
```python  
import sympy as sp 

A = sp.Matrix([[1, 1,0], [1, 3, 1], [3, 1, -1]])
U = sp.Matrix([[1,1,0],[0,2,1],[0,0,0]])
print("A Reduced Row Echelon form",A.rref())
tr_A = A.T
print("Transposed Reduced Row echelon form ",tr_A.rref())
print("U Reduced Row Echelon form",U.rref())
tr_U = U.T
print(tr_U)
print(tr_A)
# True
```