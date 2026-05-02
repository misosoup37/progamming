score = 0
choice = "y"
while choice == "y":
    add = int(input("กรอกคะแนนที่ได้: "))
    score = score + add
    print("คะแนนรวม =", score)
    choice = input("เพิ่มคะแนนอีกไหม (y/n): ")