import Data.List (find)
import Data.Bits (shiftL, shiftR)

triangleNums = scanl (+) 0 [1..]

factors n = [x | x <- [1.. n `div` 2], n `mod` x == 0]

main = 
  print $ find (\ xs -> length xs > 500) $ map factors triangleNums
