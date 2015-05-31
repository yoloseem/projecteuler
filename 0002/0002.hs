fib :: Integer -> Integer
fib 0 = 1
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

main = print (sum (filter (\x -> x `mod` 2 == 0) (takeWhile (<4000000) (map fib [1..]))))
