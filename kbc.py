question_list=[
              "1.when is national womans day?",
              "2.where was Mahatma Gandhi born",
              "3.name the river bank on which Taj Mahal is situated?",
              "4.lower house of the parliament of india?",
              "5.what is the national bird  of india?"]
options_list=[
      ["9 aug.","15aug.","5 sep.","16 nov."],
      ["cuttack","allahabad","porbandar","gujrat"],
      ["ganga ","yamuna","godavari","sarswati"],
      ["lok sabha","rajya sabha","vidhan sabha","none"],
      ["crow","sapprow","pig","peacock"]]
solution_list=[1,3,2,1,4]

lifeline=[["(1) 9 aug","(2)15 aug"],
        ["(3)porbandar","(4)gujrat"],
        ["(1)ganga","(2)yamuna"],
        ["(1)lok sabha","(2)rajya sabha"],
        ["(3)pig","(4)peacock"]]

print(         "welcome to KBC"     )
print(         "your game is start now"      )
i=0
money=0
c=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        #print(d)
        j=j+1
    if c<2:
        a=input('do you want use lifeline :')
        if a=="yes":
            c=c+1
            print("5050",lifeline[i])   
        else:
            print("choose your answer")
    b=int(input("choose correct answer:")) 
    if b==solution_list[i]:
        money=money+5000
        print("your ansere is correct")
        print("congratualation")
        print("your win Rs./",money)
    else:
        print("your answer is wrong")
        #print("sare paise bhul jao")  
        break 
    i=i+1 







