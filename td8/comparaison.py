from time import perf_counter_ns

def operation1(prec: int) -> int:
    t0 = perf_counter_ns()
    l = []
    for i in range(prec):
        l = l + [i]
    t1 = perf_counter_ns()
    return t1 - t0
def operation2(prec: int) -> int:
    t0 = perf_counter_ns()
    l = []
    for i in range(prec):
        l += [i]
    t1 = perf_counter_ns()
    return t1 - t0
def operation3(prec: int) -> int:
    t0 = perf_counter_ns()
    l = []
    for i in range(prec):
        l.append(i)
    t1 = perf_counter_ns()
    return t1 - t0
def operation4(prec: int) -> int:
    t0 = perf_counter_ns()
    l = []
    append = l.append
    for i in range(prec):
        append(i)
    t1 = perf_counter_ns()
    return t1 - t0
def operation5(prec: int) -> int:
    t0 = perf_counter_ns()
    l = [*range(prec)]
    t1 = perf_counter_ns()
    return t1 - t0

precision = 10000

print(operation1(precision))
print(operation2(precision))
print(operation3(precision))
print(operation4(precision))
print(operation5(precision))

