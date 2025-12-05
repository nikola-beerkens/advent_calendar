def count_adjacent(graph):
    # Convert each row to a list of characters for mutability
    new_graph = [list(row) for row in graph]
    forklift = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            count = 0
            if graph[i][j] == '.' or graph[i][j] == 'x':
                continue
            if i > 0 and graph[i-1][j] == '@':
                count += 1
            if i < len(graph)-1 and graph[i+1][j] == '@':
                count += 1
            if j > 0 and graph[i][j-1] == '@':
                count += 1
            if i> 0 and j > 0 and graph[i-1][j-1] == '@':
                count += 1
            if i> 0 and j < len(graph[i])-1 and graph[i-1][j+1] == '@':
                count += 1
            if i < len(graph)-1 and j > 0 and graph[i+1][j-1] == '@':
                count += 1
            if i < len(graph)-1 and j < len(graph[i])-1 and graph[i+1][j+1] == '@':
                count += 1
            if j < len(graph[i])-1 and graph[i][j+1] == '@':
                count += 1
            if count < 4:
                if new_graph[i][j] == '@':
                    new_graph[i][j] = 'x'
                    forklift += 1
    # Convert each row back to a string
    return [''.join(row) for row in new_graph], forklift

if __name__ == "__main__":
    f = open("input4.txt", "r")
    graph =[]
    for line in f:
        input_data = line.strip()
        graph.append(input_data)
    f.close()
    sum =0
    new_graph,forklift = count_adjacent(graph)
    print(forklift)
    sum += forklift
    while forklift > 0:
        new_graph,forklift = count_adjacent(new_graph)
        sum += forklift
        print(forklift)
    print("Total forklifts moved:", sum)