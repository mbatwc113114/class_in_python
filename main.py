class person:
  def __init__(self, age, name, height, weight):
    self.age = age 
    self.name = name
    self.height = height
    self.weight = weight
  
  def greet(self, end):
    #greeting
    message = "good morning {} how are you. {}".format(self.name, end)
    return message
  
  def bmi(self):
    #height in meter
    bmi = (self.weight)/((self.height/100)**2)
    bmi = round(bmi,2)
    if bmi < 18.5:
      bmi = "{} underweight".format(bmi)
    elif bmi >= 18.5 and bmi < 25 :
      bmi = "{} healthy".format(bmi)
    elif bmi >= 25 and bmi <= 30:
      bmi = "{} overweight".format(bmi)
    else:
      bmi = "{} obesity".format(bmi)
    return bmi


  def agedif(self, other):
    # return age diffrence 
    dif =0
    if self.age > other.age:
      dif = self.age-other.age
    else:
      dif = other.age-self.age
    dif = "{} years".format(dif)
    return dif
     
if __name__== "__main__":
  aman = person(17, "aman", 167, 61)
  print(aman.greet("how is day"))
  print("your bmi is {}".format(aman.bmi()))

  suman = person(12, "suman", 156, 47)
  print(suman.agedif(aman))
