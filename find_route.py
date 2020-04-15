import sys

class City:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = set()
        self.distance = 0
        self.h_distance = 0

class Solution:

    def __init__(self, map, heuristics):
        self.map = map
        self.heuristics = heuristics

    def find_route(self, start, dest):
        queue = []
        head = City(start)
        queue.append(head)
        expanded = 0
        generated = 0
        tail = None
        visited = set()
        maxNodes = 0
        while len(queue) > 0:
            maxNodes = max(maxNodes, len(queue))
            node = queue.pop(0)
            expanded += 1
            if node.name != dest:
                if node.name not in visited:
                    children = self.extract_children(node)
                    for child in children:
                        queue.append(child)
                    generated += len(children)
            else:
                tail = node
                break
            visited.add(node.name)
            if self.heuristics:
                queue.sort(key=lambda n: n.h_distance)
            else:
                queue.sort(key=lambda n: n.distance)
        print ("nodes expanded: "+str(expanded))
        print ("nodes generated: "+str(generated))
        print ("max nodes in memory: "+str(maxNodes))
        if tail:
            print ("distance: "+str(tail.distance)+" km")
        else:
            print("distance: infinity")
        print ("route:")
        if tail:
            temp = tail
            route = []
            while temp.parent:
                route.append([temp.parent.name, temp.name, temp.distance - temp.parent.distance])
                temp = temp.parent
            for i in range(len(route)-1, -1, -1):
                print (route[i][0]+" to "+route[i][1]+", "+str(route[i][2])+" km")
        else:
            print ("none")
        return

    def extract_children(self, parent_city):
        children = []
        for cities in self.map:
            if parent_city.name in cities:
                if cities[0] == parent_city.name:
                    new_city = City(cities[1])
                else:
                     new_city = City(cities[0])
                new_city.parent = parent_city
                new_city.distance = parent_city.distance + cities[2]
                if self.heuristics:
                    new_city.h_distance = parent_city.distance + cities[2] + self.heuristics[new_city.name]
                parent_city.child.add(new_city)
                children.append(new_city)
        return children


input_file_name = sys.argv[1]
opener = open(input_file_name)
lines = opener.readlines()
map = []
for line in lines:
    if line != "END OF INPUT":
        cities = line.split(" ")
        map.append([cities[0], cities[1], float(cities[2])])

if len(sys.argv) > 4:
    heuristic_file_name = sys.argv[4]  
else :
    heuristic_file_name = None
h_dict = None
if heuristic_file_name:
    h_opener = open(heuristic_file_name)
    h_lines = h_opener.readlines()
    h_dict = {}
    for line in h_lines:
        if line != "END OF INPUT":
            arr = line.split(" ")
            h_dict[arr[0]] = float(arr[1])

sol = Solution(map, h_dict)
sol.find_route(sys.argv[2], sys.argv[3])