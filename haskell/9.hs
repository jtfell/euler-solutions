-- a + b + c == 1000
-- a ^ 2 + b ^ 2 == c ^ 2
-- => c = sqrt (a ^ 2 + b ^ 2)

main =
  print $ head [ a * b * c | a <- [1..1000], b <- [a..500], let c = sqrt (a^2 + b^2), a + b +c == 1000]
