class Solution(object):
    def tictactoe(self, moves):
        """
        when is it called a player wins 
        either same elements in a col , row or diagonal
        how do we know the elements are in the same row ?
            the first elements in the moves are the same
        how do we know the elements are in the same col ? 
            the second elements are the same
        how do we know the elements are in the same diagonal ?
            the difference between the first element and the next move first element and the
            the difference between the second elements of contagious element is 1
         """
        #  pseudocode
        # create two pointers to track the moves of a and b
        # create a helper function that returns boolean by checking the 3 conditions
        # if 3 of them fails break out of the loop and return 'Draw"
       

        def hasWon(moves):
            row_count = [0] * 3
            col_count = [0] * 3
            diag = 0
            anti_diag = 0

            for x, y in moves:
                row_count[x] += 1
                col_count[y] += 1
                if x == y:
                    diag += 1
                if x + y == 2:
                    anti_diag += 1

            return 3 in row_count or 3 in col_count or diag == 3 or anti_diag == 3

        moves_A = []
        moves_B = []

        for i, move in enumerate(moves):
            if i % 2 == 0:
                moves_A.append(move)
            else:
                moves_B.append(move)
        if hasWon(moves_A):
            return 'A'
        elif hasWon(moves_B):
            return 'B'
        elif len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'

       


                
        