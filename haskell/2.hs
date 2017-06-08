fibSeq = 1 : 1 : zipWith (+) fibSeq (tail fibSeq)
lessThan4Mil x = x < 4000000

main =
  print $ sum $ takeWhile lessThan4Mil [y | y <- fibSeq, even y]
