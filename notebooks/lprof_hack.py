import builtins

try:
    profile = builtins.profile
except AttributeError:
    def profile(func): 
        return func
