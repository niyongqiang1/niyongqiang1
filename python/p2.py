import types
def f():
    pass

print(type(f) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x+1) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)