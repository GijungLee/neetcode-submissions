class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        # cols = dict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        # print(board[0])
        # print(board[0][1])
        # print(board[0][1] in board[0])
        # if board[0][1] not in cols[1]:
        # # cols[1].update(dict(1=board[0][1]))
        #     cols[1].add(board[0][1])
        # print(cols)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in squares[(r // 3, c // 3)]):
                #    print(rows)
                #    print(cols)
                #    print(squares)
                #    print(r,c)
                #    print(board[r][c])
                   return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
                # print(squares)
        return True