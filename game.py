import PySimpleGUI as sg
import json

# Theme for GUI
sg.theme("DarkBlue14")

def load_questions(level_file):
  with open(level_file, 'r') as file:
    data = json.load(file)
  return data.get("questions", [])

# Layout for level selection screen
level_layout = [
  [sg.Text("Choose a level to play:")],
  [sg.Button("Level 1"), sg.Button("Level 2"), sg.Button("Level 3")],
  [sg.Button("Exit")]
]

# Window for level selection
level_window = sg.Window("Beyond the Surface", level_layout)

selected_level = None

while True:
  event, _ = level_window.read()
  if event in (sg.WINDOW_CLOSED, "Exit"):
    break 
  if event in ("Level 1", "Level 2", "Level 3"):
    selected_level = f"{event.lower().replace(' ', '')}.json"
    break

level_window.close()

level_window.close()

#Load questions based on the selected level
questions = load_questions(selected_level)

#Question Layout
question_layout = [
  [sg.Text("Question:", font=("Helvetica", 16), key="-QUESTION-")],
  [sg.Button("Next"), sg.Button("Exit")]
]

# Window for prompting questions
question_window = sg.Window("Beyond the Surface", question_layout, finalize=True)

question_index = 0

if questions:
  question_window["-QUESTION-"].update(questions[question_index])

while True:
  event, _ = question_window.read()
  if event in (sg.WINDOW_CLOSED, "Exit"):
    break
  if event == "Next":
    question_index += 1
    if question_index < len(questions):
      question_window["-QUESTION-"].update(questions[question_index])
    else:
      sg.popup("You have completed the level!")
      break
  
question_window.close()
