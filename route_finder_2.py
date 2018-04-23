import networkx as nx
import igraph

DG = nx.DiGraph()


def add(cmd, args):
    """

    :param args: 4 parameters
    [origin, destination, mileage, duration]
    """

    if len(args) != 4:
        print('MALFORMED ' + cmd + ' ' + ', '.join(args) + '\n')
        return

    for node in args[0:2]:
        if node not in DG.nodes():
            node = node.strip()
            DG.add_node(DG.add_node(node))
            # print(node)

    DG.add_edge(args[0], args[1], mileage=float(args[2]), duration=float(args[3]))

    print("EDGE " + ' '.join(args) + '\n')


def query(cmd, args):
    """

    :param cmd:
    :param args: [origin, destination]
    :return:
    """
    if len(args) != 2:
        print('MALFORMED ' + cmd + ' ' + ', '.join(args) + '\n')
        return

    try:
        _paths = nx.all_simple_paths(DG, args[0], args[1])
    except nx.NodeNotFound:
        print('MALFORMED ' + cmd + ' ' + ', '.join(args) + '\n')
        return

    paths = []
    for path in _paths:
        paths.append(path)

    if paths is not None and len(paths) == 0:
        print('MALFORMED ' + cmd + ' ' + ', '.join(args) + '\n')
        return

    print('QUERY ' + ','.join(args) + '\n')
    for path in list(paths):

        cost = 0
        pairs = []
        for index, item in enumerate(path):
            if index + 1 < len(path):
                pairs.append([item, path[index + 1]])
        for pair in pairs:
            data = DG.get_edge_data(pair[0], path[1])
            cost += data['mileage'] * 15 + data['duration'] * 30

        print('PATH ' + str(round(cost, 2)) + ' ' + ', '.join(path) + '\n')




output_file = open('output.txt', 'w')
error_file = open('error.txt', 'w')


def handler(args):
    temp = str(args).strip('\n').split(' ', 1)
    cmd = temp[0]
    arguments = [x for x in temp[1].split(',') if len(x) > 0]
    _ = {
        "ADD": add,
        "QUERY": query
    }
    if cmd not in _.keys():
        print('MALFORMED ' + args + '\n')
        # print('MALFORMED ' + args + '\n')
    else:
        _[cmd](cmd, arguments)


print('=======================')
with open('input.txt', 'r') as file:


    for line in file:
        print(line)
        handler(line)

print('=======================')
output_file.close()
error_file.close()