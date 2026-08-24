# Adaptive Filipino Story Reading App

**Name:** Jiane Rackyle Sarting
**Section:** CS4D
**Date:** August 24, 2026

## What is this?

This is a simple Python program. It gives you a short Filipino story to
read. After you read it, it asks you two questions. Based on your
score and how fast you read, the program changes what happens next.
That's why we call it "adaptive" because it changes based on you.

- **Beginner ("Magkaibigan Kami"):** Two kids stay best friends even
  though their moms don't get along. Lesson: don't let other people's
  problems ruin your own friendships.
- **Intermediate ("Ang Malaking Pangarap"):** A boy cries at night
  because his family is poor, but he still goes to school every day
  because his dream is bigger than his problems.
- **Advanced ("Ang Pangarap ni Miko"):** A boy is raised by his lola
  after his parents split up. He uses that pain to study hard and
  build a better future, instead of repeating his parents' mistakes.

## How to Run It

1. Make sure Python is installed on your computer.
2. Get the `app.py` file from this repository.
3. Open a terminal (command window) in the folder where you saved it.
4. Type this and press Enter:
   ```
   python app.py
   ```
5. Read the story. Press Enter when you're done.
6. Type how many seconds it took you to read (just guess a number).
7. Answer the two questions about the story.

## The Two Rules

**Rule 1: If your score is below 70% → the next story will be easier.**
After you answer the questions, the program checks your score. If your
score is below 70%, the next story will be easier. If your score is 70%
or higher, the next story will be harder.

**Rule 2: If you read slower than average → "Reading Support Mode" turns on.**
The program checks how many words per minute (WPM) you read. If you
read slower than the average speed for that story, it turns on
"Reading Support Mode." This means the next story would use easier
words and give you a "read aloud" option.

## Why These Rules Are Helpful

These two rules make the app change based on each person, instead of
giving everyone the exact same story every time:

- If someone doesn't understand the story well, they get an easier
  one next time, so they don't feel too frustrated.
- If someone reads slowly, the app gives them extra help (easier
  words, read-aloud), so they don't feel left behind.

This way, every user gets a story and a reading speed that matches
their own level.

## Files in This Project

- `app.py` — the main program
- `README.md` — this file
