line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter a position (e.g. A1, B2, C3): ")
letter = position[0].lower()
number = int(position[1]) - 1

abc=["a", "b", "c"]
letter_index= abc.index(letter)
map[number][letter_index]=' X'

print(f"{line1}\n{line2}\n{line3}")