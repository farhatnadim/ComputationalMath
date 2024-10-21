Problems with * have numerical/sympy solutions in the python file in the same directory.



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
The column spaces and row space both have dimension = 2 because they are made from a minimum number of 2 independents vectors. 
The column space of U is different than the column space of A;
 if you notice there we cannot write the the first column of A with any combination of the columns of U ( third element is zero )
The row spaces are the same though because they can be written as a linear combination of each others