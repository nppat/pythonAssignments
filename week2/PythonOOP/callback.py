def invoker(callback):
    # invoke the input pass the argument 2
    print callback(3)
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)
invoker(lambda z: 7 * z)