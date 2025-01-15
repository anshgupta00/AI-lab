import pprint
G = {
'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
'dharan' : {'itahari' : 20},
'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10},
'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40},
'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
'damak' : {'urlabari' : 6}
}
def DFS(G, start, goal):
  stack = list()
  prev = dict()
  visited = set()
# Push the starting state into the stack
  stack.append(start)
# Initialize the prev state of starting state to " "
  prev[start] = " "
# Repeat until stack is not empty
  while(stack):
    poppedState = stack.pop()
    visited.add(poppedState)
    if poppedState == goal:
        return True, prev
    for chimeki in G[poppedState]:
      if chimeki not in stack and chimeki not in visited:
          stack.append(chimeki)
          prev[chimeki] = poppedState
    return False, prev
def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
      path = previous[goal] + " -> "+ path
      goal = previous[goal]
    return path
start = 'biratnagar'
goal = 'damak'
goalFound, previous = DFS(G, start, goal)
if(goalFound):
  print(reconstruct_path(G, previous, goal))
else:
  print("NO SOLUTION!!")
  