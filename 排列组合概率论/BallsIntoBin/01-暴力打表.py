from balls2bin import bruteforce, exact, dp

for i in range(1, 10):
    p = bruteforce.solve(i, i)
    x = exact.standard2(i, i)
    y = dp.solve(i, i)
    print(f"{i}=>{p} {x} {y}")
