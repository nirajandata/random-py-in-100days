class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mat_l=len(matrix)
        final_mat=[]
        test=[]
        for i in range(mat_l):
            for j in range(mat_l):
                test.append(matrix[j][i])
            test=test[::-1]
            final_mat.append(test) 
            test=[]
        print(final_mat)
       
