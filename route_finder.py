import networkx as nx
import sys

DG = nx.DiGraph()


def add(args):
    """

    :param args: 4 parameters
    [origin, destination, mileage, duration]
    """

    if len(args) != 4:
        sys.stderr.write('MALFORMED ADD ' + ','.join(args) + '\n')
        return

    for node in args[0:2]:
        if node not in DG.nodes():
            node = node.strip()
            DG.add_node(DG.add_node(node))

    DG.add_edge(args[0], args[1], mileage=float(args[2]), duration=float(args[3]))

    sys.stdout.write("EDGE " + ' '.join(args) + '\n')


def query(args):
    """

    :param cmd:
    :param args: [origin, destination]
    :return:
    """
    if len(args) != 2:
        sys.stderr.write('MALFORMED QUERY ' + ', '.join(args) + '\n')
        return

    try:
        _paths = nx.all_simple_paths(DG, args[0], args[1])
    except nx.NodeNotFound:
        sys.stderr.write('MALFORMED QUERY ' + ', '.join(args) + '\n')
        return

    paths = []
    for path in _paths:
        paths.append(path)

    if paths is not None and len(paths) == 0:
        sys.stderr.write('MALFORMED QUERY ' + ', '.join(args) + '\n')
        return

    sys.stdout.write('QUERY ' + ','.join(args) + '\n')
    for path in list(paths):

        cost = 0
        pairs = []
        for index, item in enumerate(path):
            if index + 1 < len(path):
                pairs.append([item, path[index + 1]])
        for pair in pairs:
            data = DG[pair[0]][pair[1]]
            cost += data['mileage'] * 15 + data['duration'] * 30

        sys.stdout.write('\tPATH ' + str(round(cost, 2)) + ' ' + ', '.join(path) + '\n')






def handler(args):
    temp = str(args).strip('\n').split(' ', 1)
    cmd = temp[0]
    arguments = [x for x in temp[1].split(',') if len(x) > 0]
    _ = {
        "ADD": add,
        "QUERY": query
    }
    if cmd not in _.keys():
        sys.stdout.write('MALFORMED ' + args + '\n')
    else:
        _[cmd](arguments)

