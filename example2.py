##### Each team's file must define four tokens:# team_name: a string# strategy_name: a string# strategy_description: a string# move: A function that returns 'c' or 'b'####
team_name = 'Rest Stop @ 1580'
strategy_name = 'Angry Pig'
strategy_description = 'Betray them unless they have only colluded in the past' 
def move(my_history, their_history, my_score, their_score): 
  '''Has a variable that is true. If it is ever set to false by a b in their history, we will betray them unconditionally. ''' 
  trust = True
  for check in their_history: 
    if check != "c": 
      trust = "False" 
  if trust == False: 
    return "b" 
  else: 
    return "c"
