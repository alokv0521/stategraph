from typing import TypedDict
from langgraph.graph import StateGraph, END

class simpleState(TypedDict):
    count:int

def increment(state:simpleState)->simpleState:
    return {
        "count":state["count"]+1
    }

def should_count(state):
    counter=state["count"]
    if counter>=5 : return "stop"
    return "continue"

graph=StateGraph(simpleState)
graph.set_entry_point("increment")

graph.add_node("increment", increment)
graph.add_conditional_edges("increment", should_count, { "stop":END, "continue":"increment"}) 
  
    # so here in the above example we can see that , we can pass another argument that where it should go if the conditional edge returns something 

app=graph.compile()

state={
    "count":0
}

result =app.invoke(state)
print(result)


# till this it was basic struxtire of the state 
# now we will see complex structure
