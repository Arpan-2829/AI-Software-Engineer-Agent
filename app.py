from graph.builder import graph

config = {
    "configurable": {
        "thread_id": "1"
    }
}

result = graph.invoke(
    {
        "task": "Create a Python function for binary search"
    },
    config=config
)
graph.invoke(
    {"task": "Add delete operation"},
    config=config
)

print("\n========== PLAN ==========\n")
print(result["plan"])

print("\n========== CODE ==========\n")
print(result["code"])

print("\n========== FIXED CODE ==========\n")
print(result["fixed_code"])

print("\n========== TESTS ==========\n")
print(result["tests"])

print("\n========== DOCUMENTATION ==========\n")
print(result["documentation"])