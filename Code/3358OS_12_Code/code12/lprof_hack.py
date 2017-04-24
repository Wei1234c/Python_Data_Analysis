import __builtin__

try:
    profile = __builtin__.profile
except AttributeError:
    def profile(func): 
        return func
