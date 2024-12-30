import json

def introduction():
  print("Welcome to Beyond The Surface!")
  print("There are 3 levels to the game and in each levels the questions get deeper.")

def get_level():
  while True:
      try:
          level = int(input("What level do you want to start on? (1, 2, or 3)"))

          if 1<= level <= 3:
              return level
          else:
              print("Pick a level only from the ranges 1-3.")

      except ValueError:
        print("Invalid Input. Pick a level only from the ranges 1-3.")


def load_questions(level):
    filename = f"level{level}.json"

    try: 
      with open(filename, "r") as file:
        questions_info = json.load(file)
        questions = [entry["question"] for entry in questions_info]
      return questions
    except FileNotFoundError:
      print(f" {filename} is not found.")
      return []

def display_questions(questions):
  for question in questions:
      print(question)
      input("Click Enter to continue...")

def replay():
  try:
    user_input = input("Do you want to play again? (Yes/No)").lower()

    if user_input == "yes":
      return True
    elif user_input == "no":
      return False
    else:
      raise ValueError("Invalid Input, try again")

  except ValueError:
    return replay()