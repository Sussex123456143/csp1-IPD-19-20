
##### Each team's file must define four tokens:# team_name: a string# strategy_name: a string# strategy_description: a string# move: A function that returns 'c' or 'b'####
team_name = 'Rest Stop @ 1580'
strategy_name = 'Robin Hood'
strategy_description = 'Betrays people with higher scores, colludes with the less fourtunate' 
def move(my_history, their_history, my_score, their_score): 
  """Checks their score and my score, and outputs c if they are lower then us and b if they are higher""" 
  if my_score < their_score: 
    return "b" 
  else: return "c"
