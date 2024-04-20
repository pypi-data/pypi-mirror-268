class IMIC_Calculate:
    # Tìm Max giữa 2 số
    def find_max(self,a,b):
        if a > b:
            return a
        return b

    # Xác định năm nhuận
    def leap_year(self,a):
        return True if ((a%4==0 and a%100!=0) or (a%400==0)) else False

    # Xác định kiểu tam giác
    def check_triangle(self,a,b,c):
        if int(a)==int(b) and int(b)==int(c):
            return 'Equilateral triangle'
        elif(int(a)==int(b) or int(a)==int(c) or int(b)==int(c)):
            return 'Isosceles triangle'
        else:
            return 'Scalene triangl'

    # Xác định loại xếp hạng
    def check_grade(self,a,b,c,d,e):
        per = (a+b+c+d+e)/5.0
        if per>=90:
            return f'Grade A - Percentage >= {per}%'
        elif per>=80:
            return f'Grade B - Percentage >= {per}%'
        elif per>=70:
            return f'Grade C - Percentage >= {per}%'
        elif per>=60:
            return f'Grade D - Percentage >= {per}%'
        elif per>=40:
            return f'Grade E - Percentage >= {per}%'
        return f'Grade F - Percentage >= {per}%'  
    
class Personal_BMI:
    def __init__(self, age, weight, height, gender):
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.bmi = 0        

    def calculate_bmi(self):
        if self.gender.upper() == 'male'.upper():
            self.bmi = self.weight/(self.height/100 * self.height/100)*0.98
        else:
            self.bmi = self.weight/(self.height/100 * self.height/100)*0.94
        return self.bmi
    
    def conclusions(self):
        if self.bmi < 18.5:
            return 'Your weight is too low'
        elif self.bmi < 24.9:
            return 'Your weight is too normal'
        elif self.bmi < 29.9:
            return 'Your have an overweight'
        elif self.bmi < 34.9:
            return '1st level overweight'
        elif self.bmi < 39.9:
            return '2nd level overweight'
        else:
            return '3rd level overweight'