def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


print("MDC(48, 18) =", mdc(48, 18))
print("MDC(100, 75) =", mdc(100, 75))
print("MDC(17, 5) =", mdc(17, 5))
