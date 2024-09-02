# Flash Cards Language Learning App
This is a Python-based Flash Cards Language Learning App designed to help users learn French. The app displays flashcards with words in French and their English translations, allowing users to practice and test their language skills interactively.

## Features
- Interactive Flashcards: Learn new words by flipping between French and English flashcards.
- Progress Tracking: Successfully learned words are removed from the learning deck, and your progress is saved automatically.
- Customizable Timing: Cards automatically flip to reveal translations after a short delay.

## How to Use
- Start the App: Launch the app by running main.py.
- View Flashcards: The app will display a French word on a flashcard. Try to recall the English translation.
- Flip the Card: After a few seconds, the card will automatically flip to reveal the English translation.

## Mark as Known or Unknown:
- Click the Right Button (✓) if you correctly identified the word. The word will be removed from the learning deck.
- Click the Wrong Button (✗) if you didn’t know the word. The word will remain in the deck for future practice.

## Project Structure
- main.py: The main script that initializes and runs the application.
- snake.py, food.py, scoreboard.py: Not used in this project, listed incorrectly in the earlier template.
- data/: Contains CSV files with French words and their English translations.
- french_words.csv: The initial dataset of words.
- To_learn.csv: The dataset that tracks words the user needs to continue learning.
- images/: Contains images used for the flashcards and buttons.

## Future Improvements
- Additional Languages: Add support for more languages, such as Spanish, German, etc.
- Custom Decks: Allow users to create and upload their custom decks of words.
- Improved UI: Enhance the user interface with animations and better graphics.
