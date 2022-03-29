from collections import deque

graph = {}
graph["alice"] = ["bob", "viktor", "vlad"]
graph["bob"] = []
graph["viktor"] = ["vlad"]
graph["vlad"] = ["bob"]

def MangoGraph(name):
    
    seq = deque()
    seq += graph[name]
    searched = []
    while seq:
        person = seq.popleft()
        if not person in searched:
            if person[-1] == 'viktor':
                print(f"find mango seller: {name[-1], name}")
            else:
                seq += graph[person]
                searched.append(person)
    return False

print(MangoGraph("alice"))