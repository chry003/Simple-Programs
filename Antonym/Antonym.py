antonyms = {
            "Right": "Left",
            "Up": "Down",
            "Far": "Near",
            "Dumb": "Smart"
        }


print("[Antonyms]")
print(*antonyms.keys(), sep="\n")
opt = input("Enter: ")

if opt not in antonyms.keys():
    print("Sorry we can't find antonym of", opt)
else:
    print("Antonym of", opt, "is", antonyms[opt])
