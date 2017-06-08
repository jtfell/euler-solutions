lcmSeq = foldr1 lcm

main =
  print $ lcmSeq [1..20]
