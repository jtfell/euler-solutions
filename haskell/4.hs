isPalindrome :: Integer -> Bool
isPalindrome num = reverse (show num) == show num

palidromes = [ x * y | x <- [999,998..100], y <- [999,998..100], isPalindrome (x * y)]

main =
  print $ maximum palidromes
