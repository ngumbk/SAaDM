import numpy as np
import re


# returns the list of nodes and their relation
def task(csv_string):
    result = []

    # making adjacency list out of edge list
    graph_start_nodes = re.findall(r'\d+,', csv_string)
    for i in range(len(graph_start_nodes)):
        graph_start_nodes[i] = int(graph_start_nodes[i][:-1])
    graph = {i: [] for i in range(1, max(graph_start_nodes) + 1)}

    csv_string = csv_string.split('\n')
    if csv_string[-1] == '':
        del csv_string[-1]

    for i in csv_string:
        nodes = i.split(',')
        graph[int(nodes[0])].append(nodes[1])

    # main task
    r1, r2, r3, r4, r5 = [], [], [], [], []

    

    return result


def main():
    with open('data.csv') as file:
        csv_string = file.read()
        result = task(csv_string)
        print(result)


if __name__ == '__main__':
    main()
