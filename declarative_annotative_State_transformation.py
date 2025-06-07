# learning today ... here instead of updating the state in particular node , we will update it in the class only 
#we will need annotation
# frist imoport annotated from typing
# Annotated(type, how to update it in future using operator. function or use your custom function
# )


from typing import TypedDict, List, Annotated
from langgraph.graph import StateGraph, END
import operator

class simpleState(TypedDict):
    count:int
    sum :Annotated[int, operator.add]
    seq:Annotated[List[int], operator.concat]

def increment(state:simpleState)->simpleState:
    new_count=state["count"]+1
    # next_count=
    return{
        "count":new_count,
        "sum": new_count,
        "seq":[new_count]
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
    "count":0,
    "sum":0,
    "seq":[]
}

result =app.invoke(state)
print(result)


# till this it was basic struxtire of the state 
# now we will see complex structure
