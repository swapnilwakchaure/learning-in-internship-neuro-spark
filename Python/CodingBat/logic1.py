# 1. When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigar, is_weekend):
    if is_weekend and cigar >= 40:
        print(True)
    elif (cigar >= 40 and cigar <= 60):
        print(True)
    else:
        print(False)

cigar_party(30, False) # → False
cigar_party(50, False) # → True
cigar_party(70, True) #→ True


# 2. You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
    pass

date_fashion(5, 10) # → 2
date_fashion(5, 2) # → 0
date_fashion(5, 5) # → 1

