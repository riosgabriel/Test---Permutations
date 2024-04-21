def combos(word):
   def combos_inner(word, perm):
       if perm:
           arr.append(perm)

       if not word:
           return
       else:
           for idx, _ in enumerate(word):
               combos_inner(word[:idx] + word[idx + 1:], perm + word[idx])

   arr = []
   combos_inner(word, "")
   return arr


if __name__ == "__main__":
   word = "abc"

   # using `sorted` function to the result remains the same as the instructions
   for p in sorted(combos(word), key=len):
       print(p)

