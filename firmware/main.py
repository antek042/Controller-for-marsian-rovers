import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9)
keyboard.row_pins = (board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],
]

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.D0, board.D1),
    (board.D2, board.D3),
)

encoder_handler.map = [
    ((KC.RIGHT, KC.LEFT), (KC.UP, KC.DOWN)),
]

if __name__ == "__main__":
    keyboard.go()