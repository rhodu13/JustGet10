# Just Get 10

Welcome to **Just Get 10**, an addictive puzzle game developed in Python using the Pygame library! 
This game challenges your strategic thinking and planning skills in a delightful and engaging way.

## About the Game

**Just Get 10** is a popular puzzle game that is easy to learn but hard to master. The goal is simple: combine numbers on a grid to create the number 10. With each move, identical numbers merge and increase in value, offering endless opportunities for creating new strategies and high scores. 

### Features

- **Intuitive Gameplay:** Simple controls and straightforward mechanics make it easy to pick up and play.
- **Challenging Puzzles:** Increasing difficulty levels ensure that the game remains challenging and engaging.
- **Clean and Elegant Design:** Enjoy a visually pleasing interface that enhances your gaming experience.
- **High Scores:** Compete with yourself and others to achieve the highest score possible.
- **Sound Effects and Music:** Immerse yourself in the game with enjoyable sound effects and background music.

## Screenshots

![JustGet10](screenshot.png)

## Installation

Follow these steps to set up and play **Just Get 10** on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rhodu13/JustGet10
   ```
2. **Navigate to the project directory:**
   ```bash
   cd JustGet10
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the game:**
   ```bash
   python src/justGetTenGUI.py
   ```

## How to Play

1. Choose your difficulty
2. Click on adjacent tiles with the same number to merge them.
3. The merged tiles will increment by one.
4. Plan your moves carefully to avoid filling up the grid.
5. Aim to create a tile with the number 10.

## Contributing

We welcome contributions from the community! Feel free to fork the repository and submit pull requests. Whether it’s bug fixes, feature enhancements, or new ideas, your input is valuable.

## TODO Features

1. **High Score System**
   - [ ] Implement a system to track and display high scores.
   - [ ] Save high scores locally or online for persistent tracking.

2. **Sound Effects and Music**
   - [ ] Add sound effects for tile merging and other game actions.
   - [x] Add sound effects for winning or losing game.
   - [ ] Include background music.

3. **Fullscreen Mode**
   - [ ] Enable fullscreen mode for an immersive gaming experience.
   - [ ] Add a toggle option to switch between windowed and fullscreen modes.

4. **Hover Effect**
   - [ ] Implement hover effects for interactive elements like buttons.
   - [ ] Add visual feedback when hovering over tiles to indicate possible merges.

5. **Advanced Menu for Settings**
   - [ ] Develop a comprehensive settings menu to change various game parameters.
   - [ ] Include options to adjust sound, music, display settings, and gameplay preferences.
   - [ ] Add speaker to mute (can be in footer or gameboard).

6. **Adaptive Layout**
   - [ ] Ensure the game layout adapts to different board sizes.

7. **Timer Feature**
   - [ ] Add a timer to track the duration of each game session.
   - [ ] Display the timer prominently during gameplay.

8. **Score and Timer Recording**
   - [ ] Implement a feature to record scores along with the timer and player pseudonyms.
   - [ ] Save and display this data on a leaderboard or within the game.

9. **User Profile and Pseudonym**
   - [ ] Allow players to create profiles with pseudonyms.
   - [ ] Display the player's pseudonym in the game and on leaderboards.

## Implementation Steps

### High Score System
- [ ] Create a local or online database to store high scores.
- [ ] Update the game logic to check and update high scores after each game session.

### Sound Effects and Music
- [ ] Source or create sound files for game actions and background music.
- [ ] Use Pygame's mixer module to integrate sound effects and music control.

### Fullscreen Mode
- [ ] Use Pygame's display module to add fullscreen functionality.
- [ ] Provide an option in the settings menu to toggle fullscreen mode.

### Hover Effect
- [ ] Use Pygame's event handling to detect mouse hover over tiles and buttons.
- [ ] Change the vi


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Connect with Us

For any questions, suggestions, or feedback, please open an issue on GitHub or contact us at [rhodu13@gmail.com].

## Credits

Game produced and developped by Negro Haze and rhodu13.

Support by bheubheu