from collections import defaultdict
parsed = open("input.txt",'r').read().splitlines()

dag = defaultdict(str)
roots = set()
memo = {}

# create DAG
for cmdRaw in parsed:
    splitCmd = cmdRaw.split(' -> ')
    dag[splitCmd[1]] = splitCmd[0]


def memoize(func):
    memo = {}
    def wrapper(*args, **kwargs):
        if tuple(args) not in memo:
            memo[tuple(args)] = func(*args, **kwargs)
        return memo[tuple(args)]
    return wrapper

@memoize
def dfs(cmd):
    cmdSplit = cmd.split(' ')
    resp = 0

    if len(cmdSplit) == 1:
        if cmdSplit[0].isnumeric():
            return int(cmdSplit[0])
        else:
            return dfs(dag[cmdSplit[0]])
    elif len(cmdSplit) == 2 and cmdSplit[0] == 'NOT':
        return ~dfs(dag[cmdSplit[1]])
    elif len(cmdSplit) == 2:
        raise Exception("NOT EXPECTED! " + str(cmdSPlit))
    elif len(cmdSplit) == 3:
        if cmdSplit[1] == 'RSHIFT':
            return dfs(dag[cmdSplit[0]]) >> int(cmdSplit[2])
        elif cmdSplit[1] == 'LSHIFT':
            return dfs(dag[cmdSplit[0]]) << int(cmdSplit[2])
        elif cmdSplit[1] == 'AND':

            if cmdSplit[2].isnumeric():
                return dfs(dag[cmdSplit[0]]) & int(cmdSplit[2])
            elif cmdSplit[0].isnumeric():
                return int(cmdSplit[0]) & dfs(dag[cmdSplit[2]])
            else:
                return dfs(dag[cmdSplit[0]]) & dfs(dag[cmdSplit[2]])
        elif cmdSplit[1] == 'OR':
            if cmdSplit[2].isnumeric():
                return dfs(dag[cmdSplit[0]]) | int(cmdSplit[2])
            elif cmdSplit[0].isnumeric():
                return int(cmdSplit[0]) | dfs(dag[cmdSplit[2]])
            else:
                return dfs(dag[cmdSplit[0]]) | dfs(dag[cmdSplit[2]])
        else:
            raise Exception("NOT EXPECTED 2! " + str(cmdSplit[1]))

print(dfs('a'))
