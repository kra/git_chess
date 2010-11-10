# requires http://www.willmcgugan.com/blog/tech/2006/6/18/chesspy/
import chess

file_pgn = file("foo.pgn")

while True:
    game = chess.Game()
    if not game.import_pgn(file_pgn):
        break
    print game.board.fen()
