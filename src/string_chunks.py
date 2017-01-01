def string_chunk(string, *args):
    if len(args) == 0 or args[0] <= 0 or type(args[0]) != int:
        return []
    return [string[x:x+args[0]] for x in xrange(0,len(string), args[0])]
