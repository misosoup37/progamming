def calculateyear(age):
    year=2569-int(age);
    return year;
    
#questions and reply

a = input ("กรุณาใส่ชื่อของคุณ")
print ("สวัสดีคุณ " + a )
b = input ("คุณอายุเท่าไร?")
print ("โอ้ คุณอายุ "+b+" แล้วหรอเนี่ย")
#calcute year of birth
y=calculateyear(b)
print ("งั้นคุณคงเกิดปีพุทธศักราช "+str(y)+"")