from django.db import models

# Create your models here.
class Districts(models.Model):
    name=models.CharField(max_length=100, blank=True,null=True)
    def __str__(self):
        return self.name
ac_choices=(("1","current account"),("2","savings account"),("3","join account"))

b_choices=[('Kannur',(('1','Thaliparambu'),('2','Payyannur'),)),('Kozhikode',(('1','Vadakara'),('2','Perambra'),)),('Malappuram',(('1','Tirur'),('2','Edappal'),)),('Palakkad',(('1','Ottapalam'),('2','Pattambi'),)),('Thrissur',(('3','Cheruthuruthi'),('4','Kunnamkulam'),))]
class PersonalDetails(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    district=models.ForeignKey(Districts,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.CharField(max_length=50,choices=b_choices)
    account_type=models.CharField(max_length=50,choices=ac_choices)
    materials_provided=models.BooleanField("Debit Card",default=False)
    materials_provided2 = models.BooleanField("Cheque Book", default=False)
    materials_provided3 = models.BooleanField("Credit Card", default=False)



    def __str__(self):
        return self.name