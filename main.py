
def lenkuparbaude(len1, len2, len3):
  rezultats = False
  if len1 + len2 + len3 == 180:
    rezultats = True
  return rezultats

len1 = int(input('Ievadiet 1 lenki:'))
len2 = int(input('Ievadiet 2 lenki:'))
len3 = int(input('Ievadiet 3 lenki:'))
rezultats = lenkuparbaude(len1, len2, len3)
if rezultats:
   print('Trijsturis eksiste')
else:
   print('Trijsturis neeksiste')