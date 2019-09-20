class Board:
  def __init__(self):
    self.board = []

    for x in range(8):
      self.board.append([None] * 8)
      
  def in_row(self, row):
    return 'Q' in self.board[row]

  def in_col(self, col):
    search_col = []

    for i in range(8):
      search_col.append(self.board[i][col])

    return 'Q' in search_col

  def in_diag(self, x1, y1):
    for y, row in enumerate(self.board):
      for x, value in enumerate(row):
        if value == 'Q':
          if ((y-y1)==1*(x-x1) or (y-y1)==-1*(x-x1)):
            return True
          
    return False

  def set_square(self, x, y):
    self.board[y][x] = 'Q'

  def unset_square(self, x, y):
    self.board[y][x] = None

  def is_valid_queen(self, x, y):
    return not (self.in_row(y) or self.in_col(x) or self.in_diag(x,y))

  def draw_board(self):
    print('-' * 33)
    for i in self.board:
      for j in i:
        if j == None:
          char = ' '
        else:
          char = j
        print('| ' + char, end=' ')
      print('|')
      print('-' * 33)

def solve(b):
  piece_count = 0
  empty_spaces = []
  for y, row in enumerate(b.board):
    for x, value in enumerate(row):
      if value:
        piece_count += 1
      else:
        empty_spaces.append((x,y))
  
  if  piece_count == 8:
    return b

  for target in empty_spaces:
    if (b.is_valid_queen(target[0], target[1])):
      b.set_square(target[0], target[1])
      solution = solve(b)
      if solution:
        return solution
      else:
        b.unset_square(target[0], target[1])

  return False


  

