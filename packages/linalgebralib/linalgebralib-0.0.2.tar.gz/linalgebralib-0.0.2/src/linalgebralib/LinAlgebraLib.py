import math

def _clean_number(n, precision=1e-6):
    if abs(n - round(n)) < precision:
        return int(round(n))
    else:
        return n

class rowVector():
    #Row vectors for matrix initialization or other uncommon applications.
    def __init__(self, contents=[], size=0):
        """Takes as argument a list of the vectors contents, or a desired size of which to initialize a zero vector."""
        if contents != []:
            self.contents = []
            for i in range(0, len(contents)):
                self.contents.append(contents[i])
            self.size = len(self.contents)
        else:
            self.contents = contents
            if size != 0:
                if (type(size) != type(1)) or (size < 0):
                    print("Vector size must be a positive integer.")
                    raise TypeError
                else:
                    for i in range(size):
                        self.contents.append(0)
                    self.size = size
    def __repr__(self):
        #Prints vectors contents.
        return f"{self.contents}"
    
    def __add__(self, u):
        #Method to add two vectors.
        if isinstance(u, Matrix):
            if (u.rows != 1) or (u.columns != len(self.contents)):
                raise TypeError("Can only add column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i]+u.contents[0][i])
                return rowVector(contents=tmp)
        elif isinstance(u, rowVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector addition must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i]+u.contents[i])
                return rowVector(contents=tmp)
        else:
            raise TypeError("Cannot add column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")
        
    def __sub__(self, u):
        #Method to subtract one vector from another.
        try:
            if len(self.contents) != len(u.contents):
                raise TypeError("Invalid pair of vectors. Vector subtraction must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(round(self.contents[i] - u.contents[i]))
                return rowVector(contents=tmp)
        except AttributeError:
            raise TypeError("Cannot subtract non-vectors from vectors!")
        
    def __mul__(self, u):
        #Method for scalar multiplication of row vectors, or multiplication of row vectors by column vectors or matrices of appropriate size.
        if (type(u) == int) or (type(u) == float):
            tmp = []
            for i in range(len(self.contents)):
                tmp.append(self.contents[i]*u)
            return rowVector(contents=tmp)
        elif (type(u) == Matrix) or (type(u) == columnVector):
            if type(u) == Matrix:
                if len(u.contents) == self.size:
                    result = 0
                    for i in range(len(u.contents)):
                        if len(u.contents[i]) != 1:
                            raise TypeError("Invalid dimensions for multiplication of row vector by matrix!")
                        result += self.contents[i]*u.contents[i][0]
                    return result
                else:
                    raise TypeError("Invalid dimensions for multiplication of row vector by matrix!")
            else:
                if u.size != self.size:
                    raise TypeError("Invalid dimensions for multiplication of row vector by column vector.")
                else:
                    result = 0
                    for i in range(self.size):
                        result += self.contents[i]*u.contents[i][0]
                    return result
        else:
            raise TypeError("Row vectors can only be multiplied by scalars, or column vectors of appropriate size.")
    def transpose(self):
        return columnVector(contents=self.contents)

class columnVector():
    #Column vectors for applications involving n*1 matricies.
    def __init__(self, contents=[], size=0):
        """Takes as argument a list of the vectors contents, or a desired size of which to initialize a zero vector."""
        if contents != []:
            self.contents = []
            for i in range(0, len(contents)):
                self.contents.append([contents[i]])
            self.size = len(self.contents)
        else:
            self.contents = contents
            if size != 0:
                try:
                    for i in range(size):
                        self.contents.append([0])
                except TypeError:
                    raise TypeError("Size must be a positive integer!")

    def __repr__(self):
        #Prints vectors contents.
        row_copy = rowVector([i[0] for i in self.contents])
        return f"{row_copy}**T"
    
    def __add__(self, u):
        #Method to add two vectors.
        if isinstance(u, Matrix):
            if (u.columns != 1) or (u.rows != len(self.contents)):
                raise TypeError("Can only add column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i][0]+u.contents[i][0])
                return columnVector(contents=tmp)
        elif isinstance(u, columnVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector addition must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i][0]+u.contents[i][0])
                return columnVector(contents=tmp)
        else:
            raise TypeError("Cannot add column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")

    def __sub__(self, u):
        #Method to subtract one vector from another.
        if isinstance(u, Matrix):
            if (u.columns != 1) or (u.rows != len(self.contents)):
                raise TypeError("Can only subtract column vectors with matricies of the same dimension!")
            else:
                tmp = []
                for i in range(self.contents):
                    tmp.append([self.contents[i][0]-u.contents[i][0]])
                return columnVector(contents=tmp)
        elif isinstance(u, columnVector):
            if len(self.contents) != len(u.contents):
                raise TypeError("Vector subtraction must use vectors of the same dimension!")
            else:
                tmp = []
                for i in range(len(self.contents)):
                    tmp.append(self.contents[i][0]-u.contents[i][0])
                return columnVector(contents=tmp)
        else:
            raise TypeError("Cannot subtract column vectors with non-vectors or row vectors (Aside from n*1 matricies of the same dimension).")
        
    def __mul__(self, u):
        #Method for scalar multiplication of column vectors, and multiplication by row vectors or matrices of appropriate sizes.
        if (type(u) == int) or (type(u) == float):
            tmp = []
            for i in range(len(self.contents)):
                tmp.append(self.contents[i][0]*u)
            return columnVector(contents=tmp)
        elif (type(u) == Matrix) or (type(u) == rowVector):
            if type(u) == Matrix:
                if (len(u.contents) == 1) and (len(u.contents[0]) == self.size):
                    result = 0
                    for i in range(len(u.contents[0])):
                        result += self.contents[i][0]*u.contents[0][i]
                    return result
                else:
                    raise TypeError("Invalid dimensions for multiplication of column vector by matrix.")
            else:
                if u.size != self.size:
                    raise TypeError("Invalid dimensions for multiplication of row vector by column vector.")
                else:
                    result = 0
                    for i in range(self.size):
                        result += self.contents[i][0]*u.contents[i]
                    return result
        else:
            raise TypeError("Vectors can only be multiplied by scalars.")
    def transpose(self):
        return rowVector(contents=[self.contents[i][0] for i in range(self.size)])

class Matrix():
    def __init__(self, content=[], size=(0,0)):
        """Create a matrix from a list of lists or row/column vectors, or initialize a zero matrix of a specified size passed as a tuple size=(m,n)."""
        if content != []:
            self.contents = []
            if type(content[0]) == rowVector:
                self.columns = len(content[0].contents)
                self.rows = len(content)
                for i in range(len(content)):
                    if len(content[i].contents) != self.columns:
                        raise TypeError("Rows of a matrix must be of equal length!")
                    elif not isinstance(content[i], rowVector):
                        raise TypeError("Matrix elements must be consistent in typing.")
                    else:
                        self.contents.append(content[i].contents)
            elif type(content[0]) == list:
                self.columns = len(content[0])
                self.rows = len(content)
                for i in range(len(content)):
                    if len(content[i]) != self.columns:
                        raise TypeError("Rows of a matrix must be of equal length!")
                    elif not isinstance(content[i], list):
                        raise TypeError("Matrix elements must be consistent in typing.")
                    else:
                        self.contents.append(content[i])
            elif type(content[0] == columnVector):
                self.columns = len(content)
                self.rows = len(content[0].contents)
                for i in range(self.columns):
                    if len(content[i].contents) != self.rows:
                        raise TypeError("Columns of a matrix must be of equal size!")
                    elif not isinstance(content[i], columnVector):
                        raise TypeError("Matrix elements must be consistent in typing.")
                for i in range(self.rows):
                    tmp = []
                    for j in range(self.columns):
                        tmp.append(content[j].contents[i][0])
                    self.contents.append(tmp)
            else:
                raise TypeError("Matricies can only have vector objects or lists as rows.")
        else:
            if (size[0] == 0 and size[1] != 0) or (size[1] == 0 and size[0] != 0):
                raise ValueError("Cannot have a matrix with rows and no columns, or columns and no rows.")
            self.contents = []
            self.rows = size[0]
            self.columns = size[1]
            for i in range(self.rows):
                self.contents.append(rowVector(size=self.columns).contents)

    def __repr__(self):
        #Respresents the matrix as rows on new lines.
        if self.contents == []:
            return "[]"
        result = []
        for row in self.contents:
            tmp = []
            for i in range(len(row)):
                new = round(float(row[i]), 5)
                try:
                    if new - float((str(new)[0])) == 0.0:
                        tmp.append(int(new))
                    else:
                        tmp.append(new)
                except ValueError:
                    #Handle case where float is a negative, and its first character is '-'
                    if new - float((str(new)[1])) == 0.0:
                        tmp.append(int(new))
                    else:
                        tmp.append(new)
            result.append(tmp)
        newline = "\n"
        return f'{newline.join(f"{row}" for row in result)}'
    
    def __add__(self, B):
        #Adds matricies and raises an exception if they are of different dimensions.
        try:
            if (self.rows != B.rows) or (self.columns != B.columns):
                raise ValueError("Cannot add matricies with different dimensions.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(self.columns):
                        tmp1.append(self.contents[i][j] + B.contents[i][j])
                    tmp.append(rowVector(contents=tmp1))
                return Matrix(content=tmp)
        except AttributeError:
            if isinstance(B, columnVector) or isinstance(B, rowVector):
                tmp = B + self
                return Matrix(content=tmp.contents)
            else:
                raise TypeError("Cannot add matricies with non matricies.")
        
    def __sub__(self, B):
        #Subtracts matricies and raises an exception if they are of different dimensions.
        try:
            if (self.rows != B.rows) or (self.columns != B.columns):
                raise ValueError("Cannot subtract matricies with different dimensions.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(self.columns):
                        tmp1.append(self.contents[i][j] - B.contents[i][j])
                    tmp.append(rowVector(contents=tmp1))
                return Matrix(content=tmp)
        except AttributeError:
            if isinstance(B, columnVector) or isinstance(B, rowVector):
                tmp = B - self
                return Matrix(content=[tmp.contents])
            else:
                raise TypeError("Cannot subtract matricies with non matricies.")

    def __mul__(self, B):
        #Defines matrix multiplication and scalar multiplication on matricies.
        if isinstance(B, int) or isinstance(B, float):
            tmp = []
            for i in range(self.rows):
                tmp1 = rowVector(self.contents[i])
                tmp.append(tmp1*B)
            return Matrix(content=tmp)
        elif isinstance(B, Matrix):
            if self.columns == B.rows:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(B.columns):
                        value = 0
                        for k in range(B.rows):
                            value += self.contents[i][k]*B.contents[k][j]
                        tmp1.append(value)
                    tmp.append(tmp1)
                return Matrix(content=tmp)
            else:
                raise ValueError("To multiply matrix A by matrix B, number of columns of A must equal number of rows of B.")
        elif isinstance(B,columnVector):
            if B.size != self.columns:
                raise ValueError("Invalid dimensions for matrix multiplication with a column vector.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = 0
                    for j in range(self.columns):
                        tmp1 += self.contents[i][j]*B.contents[j][0]
                    tmp.append([tmp1])
                return Matrix(content=tmp)._clean_matrix()
        elif isinstance(B, rowVector):
            if self.columns != 1:
                raise ValueError("Invalid dimensions for multiplication of a Matrix and a row vector.")
            else:
                tmp = []
                for i in range(self.rows):
                    tmp1 = []
                    for j in range(B.size):
                        tmp1.append(self.contents[i][0]*B.contents[j])
                    tmp.append(tmp1)
                return Matrix(content=tmp)._clean_matrix()
        else:
            raise TypeError("Can only multiply matrices by scalars and vectors of appropriate dimensions.")
        

    def row_swap(self,r1,r2):
        """Swap two rows of a matrix. If A is a matrix, A.row_swap(i,j) will swap rows i and j."""
        tmp = []
        if r1 == r2:
            raise Exception("Can't swap a row with itself.")
        if (r1 > self.rows) or (r2 > self.rows) or (r1 < 0) or (r2 < 0) or (type(r1) != int) or (type(r2) != int):
            raise Exception("Invalid input for rows.")
        tmp = self.contents[r1]
        self.contents[r1] = self.contents[r2]
        self.contents[r2] = tmp

    def row_scale(self, r, c):
        """Scales row r by a constant c. If A is a matrix A.row_scale(i,c) will scale the ith row of A by c."""
        if (type(c) != int) and (type(c) != float):
            raise TypeError("Row must be scaled by a scalar quantity.")
        elif (type(r) != int):
            raise TypeError("Row input must be an integer.")
        elif (r < 0) or (r > self.rows):
            raise TypeError("Specified row does not exist in the given matrix.")
        else:
            tmp = rowVector(contents=self.contents[r])*c
            self.contents[r] = tmp.contents
            
    def row_addition(self, r, rc, c=1):
        """Method for adding a scaled copy of one row of a matrix to another. If A is a matrix, A.row_addition(i,j,c) will add a copy of j scaled by constant c to row i. Default c is 1."""
        if r == rc:
            raise Exception("Adding a row to itself is just scaling. Use .row_scale() method instead.")
        elif (r > self.rows) or (rc > self.rows) or (r < 0) or (rc < 0) or (type(r) != int) or (type(rc) != int):
            raise Exception("Invalid input for one or both rows.")
        elif (type(c) != int) and (type(c) != float):
            raise TypeError("Row must be scaled by a scalar quantity.")
        else:
            v_to_add = rowVector(contents=self.contents[rc])*c
            tmp = rowVector(contents=self.contents[r])
            tmp = tmp + v_to_add
            self.contents[r] = tmp.contents
    
    def _clean_matrix(self):
        """Method meant to be used internally to clean up results of matrix algebra, returning a neater copy of the matrix object its called on."""
        copy = Matrix(content=self.contents)
        tmp = []
        for i in range(copy.rows):
            tmp1 = []
            for j in range(self.columns):
                tmp1.append(_clean_number(self.contents[i][j]))
            tmp.append(tmp1)
        return Matrix(content=tmp)

    def transpose(self):
        """Returns a copy of the transpose of the matrix."""
        transpose = []
        for j in range(self.columns):
            trow = []
            for i in range(self.rows):
                trow.append(self.contents[i][j])
            transpose.append(trow)
        return Matrix(content=transpose)

    def diagnol(self, det_value=1):
        """Returns a copy of the matrix, having used row operations to reduce it to a diagnol form without scaling for the purposes of computing the determinant."""
        copy = Matrix(content=self.contents)
        if copy.contents == [[0]] or copy.contents == [[1]]:
            return (copy, det_value)
        #1.Determine leftmost nonzero column.
        column = None
        for i in range(copy.columns):
            if copy.transpose().contents[i] == [0 for l in range(copy.rows)]:
                pass
            else:
                column = i
                break
        if column is None:
            return (copy, det_value)
        #2.Put a nonzero entry at the top of the column.
        for i in range(copy.rows):
            if copy.contents[i][column] != 0:
                if i == 0:
                    break
                else:
                    copy.row_swap(i,0)
                    det_value = det_value*-1
                    break
        #3.Use row operations to eliminate any nonzero entries below pivot.
        for i in range(1, copy.rows):
            if copy.contents[i][column] != 0:
                copy.row_addition(i,0,-copy.contents[i][column]/copy.contents[0][column])
        #4.Make a submatrix from the remainder of the matrix, and recursive call.
        submatrix = Matrix(content=[copy.contents[i][1:] for i in range(1, copy.rows)])
        submatrix_result = submatrix.diagnol()
        det_value *= submatrix_result[1]
        return (Matrix(content=[copy.contents[0]] + [[copy.contents[i+1][0]] + submatrix_result[0].contents[i] for i in range(submatrix.rows)])._clean_matrix(), det_value)
    
    def ref(self):
        """Returns a copy of the matrix, having used row operations to reduce it to row-echelon form."""
        copy = Matrix(content=self.contents)
        if copy.contents == [[0]] or copy.contents == [[1]]:
            return copy
        #1.Determine leftmost nonzero column.
        column = None
        for i in range(copy.columns):
            if copy.transpose().contents[i] == [0 for l in range(copy.rows)]:
                pass
            else:
                column = i
                break
        if column is None:
            return copy
        #2.Put a nonzero entry at the top of the column.
        for i in range(copy.rows):
            if copy.contents[i][column] != 0:
                if i == 0:
                    copy.row_scale(0, 1/copy.contents[0][column])
                    break
                else:
                    copy.row_swap(i,0)
                    copy.row_scale(0, 1/copy.contents[0][column])
                    break
        #3.Use row operations to eliminate any nonzero entries below pivot.
        for i in range(1, copy.rows):
            if copy.contents[i][column] != 0:
                copy.row_addition(i,0,-copy.contents[i][column])
        #4.Make a submatrix from the remainder of the matrix, and recursive call.
        submatrix = Matrix(content=[copy.contents[i][1:] for i in range(1, copy.rows)])
        return Matrix(content=[copy.contents[0]] + [[copy.contents[i+1][0]] + submatrix.ref().contents[i] for i in range(submatrix.rows)])._clean_matrix()
        
            
    def rref(self):
        """Returns a copy of the matrix in reduced row-echelon form."""
        copy = self.ref()
        for i in range(1, copy.rows):
            for j in range(copy.columns):
                if (copy.contents[i][j] != 0):
                    for k in range(i):
                        if copy.contents[k][j] != 0:
                            copy.row_addition(k,i,-copy.contents[k][j])
                    break
        return copy._clean_matrix()
                    
    def det(self):
        """Computes and returns the determinant of the matrix."""
        if self.rows == self.columns:
            copy = self.diagnol()
        else:
            raise ValueError("Only square matrices have determinants.")
        det = copy[1]
        for i in range(self.rows):
            det = det*copy[0].contents[i][i]
        if det == 0.0:
            return int(det)
        return round(det, 6)
    
    def row_space(self):
        """Returns a basis for the row space of a matrix as a set of row vectors."""
        copy = self.rref()
        basis = set()
        for row in copy.contents:
            if all(i == 0 for i in row):
                continue
            else:
                basis.add(tuple(row))
        return basis
    
    def column_space(self):
        """Returns a basis for the column space of a matrix as a set of column vectors."""
        copy = self.transpose()
        copy_reduced = copy.rref()
        basis = set()
        for i in range(copy.rows):
            if all(j == 0 for j in copy_reduced.contents[i]):
                continue
            else:
                basis.add(tuple(copy.contents[i]))
        return basis
    
    def null_space(self):
        """Returns a basis for the null space of a matrix as a set of column vectors."""
        copy = self.rref()
        if copy.contents == id_matrix(copy.rows).contents:
            return set()
        else:
            pivots = 0
            for i in range(self.rows):
                for j in range(self.columns):
                    if copy.contents[i][j] == 1:
                        pivots += 1
                        break
            basis_vector_count = copy.columns - pivots
            tmp = augment(copy.transpose(),id_matrix(copy.columns)).ref()
            basis = set()
            for i in range(basis_vector_count):
                tmp1 = []
                for j in range(copy.columns):
                    tmp1.append(tmp.contents[tmp.rows-i-1][copy.rows+j])
                basis.add(tuple(tmp1))
            return basis
    def inverse(self):
        """Returns a copy of the inverse of a matrix, provided that it is invertible."""
        copy = Matrix(content=self.contents)
        try:
            if copy.det() == 0:
                raise TypeError("Matrix is not invertible. Columns or rows must not be linearly independent.")
            else:
                equality = augment(copy,id_matrix(copy.rows)).rref()
                tmp = []
                for i in range(copy.rows):
                    tmp1 = []
                    for j in range(copy.columns):
                        tmp1.append(equality.contents[i][j+copy.columns])
                    tmp.append(tmp1)
                return Matrix(content=tmp)._clean_matrix()
        except ValueError:
            raise TypeError("Only square matrices can be invertible.")



def id_matrix(n):
    """Returns an identity matrix with dimension nxn. Usage: id_matrix(n)."""
    tmp = []
    for i in range(n):
        tmp1 = []
        for j in range(n):
            if i == j:
                tmp1.append(1)
            else:
                tmp1.append(0)
        tmp.append(tmp1)
    return Matrix(content=tmp)

def augment(A,B):
    """augment(A,B) will return the augmented matrix of A and B."""
    if (type(A) != Matrix) or (type(B) != Matrix):
        raise ValueError("Can only augment matrices.")
    elif A.rows != B.rows:
        raise ValueError("Matrices must have equal numbers of rows in order to augment.")
    else:
        tmp = []
        for i in range(A.rows):
            tmp1 = []
            for j in range(A.columns):
                tmp1.append(A.contents[i][j])
            for k in range(B.columns):
                tmp1.append(B.contents[i][k])
            tmp.append(tmp1)
        return Matrix(content=tmp)
        
def dot(A,B):
    """Takes two vectors (both row vectors or both column vectors) and outputs their dot product."""
    if (isinstance(A,rowVector) and isinstance(B,rowVector)) or (isinstance(A,columnVector) and isinstance(B,columnVector)):
        return A*B.transpose()
    else:
        raise TypeError("Invalid input: Must be two vectors of the same type.")
    
def magnitude(A):
    """Returns the magnitude of a vector."""
    if type(A) == rowVector or type(A) == columnVector:
        return (dot(A,A))**(0.5)
    else:
        raise TypeError("Invalid input: Can only compute the magnitude of vectors.")
    
def angle(A,B, degrees=False):
    """Returns the angle between two vectors in the same vector space. Default output is in radians."""
    if (isinstance(A,rowVector) and isinstance(B,rowVector)) or (isinstance(A,columnVector) and isinstance(B,columnVector)):
        if A.size == B.size:
            result = math.acos(dot(A,B)/(magnitude(A)*magnitude(B)))
            if degrees:
                return result * (180/math.pi)
            else:
                return result
        else:
            raise TypeError("Vectors must be of the same dimension.")
    else:
        raise TypeError("Invalid input: Must be two vectors of the same type in the same vector space.")
    
