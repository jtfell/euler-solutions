sumOfSquares top = sum [1..top] ^ 2 - sum [x^2 | x <- [1..top]]

main = print $ sumOfSquares 100
