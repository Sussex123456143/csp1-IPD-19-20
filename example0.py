
    ##### Each team's file must define four tokens:# team_name: a string# strategy_name: a string# strategy_description: a string# move: A function that returns 'c' or 'b'####
team_name = 'Rest Stop @ I580'
strategy_name = 'Collude Unless '
strategy_description = 'Always collude unless faced with a person who betrays more then they.' 
def move(my_history, their_history, my_score, their_score): 
  """Make my move based on the history with this player. observes the opponents history. If they collude more then they betray, I collude. Otherwise, I betray Returns 'c' or 'b' for collude or betray.""" 
  trust =0 
  distrust=0 
  for hist in their_history: 
    if hist == "c": trust += 1 
    if hist == "b": distrust += 1 
  if trust > distrust: return "c" 
  else: return "b" 