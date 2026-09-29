class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        gridValid = {}

        for row in range(len(board)):

            rowValid = {}
            colValid = {}

            for col in range(len(board[0])):
                value = board[row][col]

                if value != ".":
                    rowValid[value] = rowValid.get(value,0)+1

                    if rowValid[value]>1:
                        return False
                value  = board[col][row]

                if value !=".":
                    colValid[value] = colValid.get(value,0)+1

                    if colValid[value]>1:
                        return False
        
        for box in range(9):
            boxValid = {}
            startRow = (box // 3) * 3
            startCol = (box%3) * 3

            for row in range(startRow, startRow+3):
                for col in range(startCol, startCol+3):
                    value = board[row][col]
                    if value != ".":
                        boxValid[value] = boxValid.get(value,0)+1

                        if boxValid[value]>1:
                            return False
        return True


                
                

        
        
        

        

        
