# 🔁 LangGraph StateGraph Examples: Manual vs Annotated Merging

This repository demonstrates two variations of implementing a loop-based state machine using [LangGraph](https://github.com/langchain-ai/langgraph):

1. ✅ **Manual State Update** (Basic)
2. ✨ **Annotated Auto-Merge** (Advanced)

---

## 📦 What is LangGraph?

LangGraph is a library from LangChain for building **stateful, graph-based workflows**, especially useful in AI pipelines, memory-based agents, and event-driven applications.

---

## 🧠 Concept Demonstrated

Both examples increment a counter from 0 to 5, and at each step:
- Update a `sum` value
- Append the current count to a sequence (`seq`)
- Stop when the counter reaches 5

---

## 📁 File Structure

```bash
📂 stategraph-langgraph-demo/
│
├── annotated_merge.py   # Uses Annotated[] to auto-merge fields
├── manual_merge.py      # Explicitly updates 'sum' and 'seq' in each node
├── basic_state.py       # file defining basic structure of stateGraph
├── README.md            # This file
