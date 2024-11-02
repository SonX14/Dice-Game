import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class DiceGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DiceGame")
        self.setGeometry(100,100,300,300)

        self.layout = QVBoxLayout()
        
        self.dice_label_1 = QLabel("Dice: 0", self)
        self.dice_label_1.setAlignment(Qt.AlignCenter)
        
        self.dice_label_2 = QLabel("Dice: 0", self) 
        self.dice_label_2.setAlignment(Qt.AlignCenter)

        self.roll_button = QPushButton("Roll Dice", self)
        self.roll_button.clicked.connect(self.roll_dice)

        self.status_label = QLabel("Click 'Roll Dice' to start!", self)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.dice_label_1)
        self.layout.addWidget(self.dice_label_2)
        self.layout.addWidget(self.roll_button)
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def roll_dice(self):
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)

        self.dice_label_1.setText(f"Dice 1: {dice_1}")
        self.dice_label_2.setText(f"Dice 2: {dice_2}")

        total_score = dice_1 + dice_2
        self.status_label.setText(f"Total Score: {total_score}")




def start_dice_game():
    app = QApplication(sys.argv)
    window = DiceGame()
    window.show()
    sys.exit(app.exec_())

# Start the game
if __name__ == "__main__":
    start_dice_game()