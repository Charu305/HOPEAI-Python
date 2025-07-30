list= ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
class Multifunction:
    def Subfields():
        print("Sub-fields in AI are:")
        for i in list:
            print (i)
    def OddEven():
        num = int(input("Enter a number:"))
        if ((num%2)==0):
            print(num,"is Even number")
            message= (num,"is Even number")
        else:
            print(num,"is Odd number")
            message= (num,"is Odd number")
        return message
    def Elegible():
        Gender = input("Your Gender")
        Age = int(input("Your Age"))
        if (Gender == "Male" and Age>=21):
            print ("Eligible")
            agemessage = ("Eligible")
        elif (Gender == "Male" and Age<21):
            print ("Not Eligible")
            agemessage = ("Not Eligible")
        elif (Gender == "Female" and Age>=18):
            print ("Eligible")
            agemessage = ("Eligible")
        else :
            print ("Not Eligible")
            agemessage = ("Not Eligible")
        return agemessage
    def percentage():
        Sub1 = int(input("Subject1="))
        Sub2 = int(input("Subject2="))
        Sub3 = int(input("Subject3="))
        Sub4 = int(input("Subject4="))
        Sub5 = int(input("Subject5="))
        Total =(Sub1+Sub2+Sub3+Sub4+Sub5)
        print ("Total :",Total)
        submessage=("Total :",Total)
        Percentage = Total/5
        print ("Percentage :",Percentage)
        submessage=("Percentage :",Percentage)
        return submessage