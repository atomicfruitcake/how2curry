add5 n = [n + 5]

add10 n = [n + 10]

main = do
    print $ [20] >>= add5 >>= add10
