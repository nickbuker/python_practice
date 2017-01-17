from collections import deque

def combine(*args):
    result, active = [], True
    args_deque = [deque(arg) for arg in args]
    while active:
        for arg in args_deque:
            if len(arg) > 0:
                result.append(arg.popleft())
        actives = []
        for arg in args_deque:
            actives.append(len(arg) > 0)
        active = any(actives)
    return result
