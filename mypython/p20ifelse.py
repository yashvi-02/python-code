"7) maths ss eng , total , 0-50 c 50-100 b >100 a"
maths = int(input("enter maths marks: "))
ss = int(input("enter ss marks: "))
english = int(input("enter english marks: "))
total = maths+ss+english
print("Total marks: ", total)
if total>50 and total<=100:
    print("Grade C")
elif total>50 and total<100:
    print("Grade B")
elif total>100:
    print("Grade A") 
