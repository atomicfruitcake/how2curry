add7 n = [n + 7]

double n = [n * 2]

main = do
    print $ [4] >>= add7 >>= double

    print $ [4] >>= double >>= add5
