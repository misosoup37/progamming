choice = "y"
while choice == "y":
    num1 = int(input("กรอกตัวเลขที่หนึ่ง; "))
    num2 = int(input("กรอกตัวเลขที่สอง: "))
    total = num1 + num2
    print("ผลบวก =", total)
    choice = input("ต้องการให้บวกต่อไปหรือไม่ (y/n): ")