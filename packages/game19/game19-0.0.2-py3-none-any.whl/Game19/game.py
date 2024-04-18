import operator
from functools import lru_cache

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.pow,
    '<' : operator.lt,
    '<=' : operator.le,
    '==' : operator.eq,
    '!=' : operator.ne,
    '>=' : operator.ge,
    '>' : operator.gt,
}

h = '><'

def move(array: tuple, moves: str):
    moves = moves.split()
    fin_array = list(list(array) for i in range(len(array) * len(moves)))
    for i in range(len(fin_array)):
        fin_array[i][i // len(moves)] = ops[moves[i % len(moves)][0]](fin_array[i][i // len(moves)], int(moves[i % len(moves)][1]))
    fin_array = tuple(set(tuple(tuple(i) for i in fin_array)))
    return fin_array

@lru_cache(None)
def game_all_sum(array: tuple, fin_value: str, fin_pos: str, moves: str, player = 1, step = 1):
    h1 = [i for i in h if i not in fin_value[0:2]][0]
    if ops[fin_value[0:2]](sum(array), int(fin_value[2:])) and str(step) in fin_pos:
        return True
    if (ops[h1](sum(array), int(fin_value[2:])) and str(step) == fin_pos[-1]) or (ops[fin_value[0:2]](sum(array), int(fin_value[2:])) and str(step) != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_all_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return all(game_all_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))

@lru_cache(None)
def game_any_sum(array: tuple, fin_value: str, fin_pos: str, moves: str, player = 1, step = 1):
    h1 = [i for i in h if i not in fin_value[0:2]][0]
    if ops[fin_value[0:2]](sum(array), int(fin_value[2:])) and str(step) in fin_pos:
        return True
    if (ops[h1](sum(array), int(fin_value[2:])) and str(step) == fin_pos[-1]) or (ops[fin_value[0:2]](sum(array), int(fin_value[2:])) and str(step) != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_any_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return all(game_any_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))

@lru_cache(None)
def game_any(array: tuple, fin_value: str, fin_pos: str, moves: str, player = 1, step = 1):
    h1 = [i for i in h if i not in fin_value[0:2]][0]
    if any(ops[fin_value[0:2]](i, int(fin_value[2:])) for i in array) and str(step) in fin_pos:
        return True
    if (all(ops[h1](i, int(fin_value[2:])) for i in array) and str(step) == fin_pos[-1]) or (any(ops[fin_value[0:2]](i, int(fin_value[2:])) for i in array) and str(step) != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_any(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return any(game_any(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))

@lru_cache(None)
def game_all(array: tuple, fin_value: str, fin_pos: str, moves: str, player = 1, step = 1):
    h1 = [i for i in h if i not in fin_value[0:2]][0]
    if any(ops[fin_value[0:2]](i, int(fin_value[2:])) for i in array) and str(step) in fin_pos:
        return True
    if (all(ops[h1](i, int(fin_value[2:])) for i in array) and str(step) == fin_pos[-1]) or (any(ops[fin_value[0:2]](i, int(fin_value[2:])) for i in array) and str(step) != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_all(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return all(game_all(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))


def game(type: str, array, fin_value: str, fin_pos, moves: str, player = 1, step = 1):
    array, fin_pos, player = tuple(array), str(fin_pos), int(player)
    if len(fin_pos) == 1:
        if type == 'all': return game_all(array, fin_value, fin_pos, moves, player, step)
        if type == 'any': return game_any(array, fin_value, fin_pos, moves, player, step)
        if type == 'all_sum': return game_all_sum(array, fin_value, fin_pos, moves, player, step)
        if type == 'any_sum': return game_any_sum(array, fin_value, fin_pos, moves, player, step)
    else:
        if type == 'all': return game_all(array, fin_value, fin_pos, moves, player, step) and not(game_all(array, fin_value, fin_pos[0], moves, player, step))
        if type == 'any': return game_any(array, fin_value, fin_pos, moves, player, step) and not(game_any(array, fin_value, fin_pos[0], moves, player, step))
        if type == 'all_sum': return game_all_sum(array, fin_value, fin_pos, moves, player, step) and not(game_all_sum(array, fin_value, fin_pos[0], moves, player, step))
        if type == 'any_sum': return game_any_sum(array, fin_value, fin_pos, moves, player, step) and not(game_any_sum(array, fin_value, fin_pos[0], moves, player, step))
