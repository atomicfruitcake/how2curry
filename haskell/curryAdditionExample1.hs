add5 n = [n + 5]

main = do
    print $ [3] >>= add5
