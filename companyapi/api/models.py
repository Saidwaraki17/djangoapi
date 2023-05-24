from django.db import models

# Create your models here.

# create company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    location =  models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            choices=(('IT','IT'),
                                     ('NON-IT','NON-IT'),
                    ('MOBILE Phone','Mobile Phones')))
    
    added_date = models.DateTimeField(auto_now=True)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ", "+ self.location


# Employee Model

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=20,choices=(('Manager','manager'),
                                        ('Developer','Softare Developer'),
                                        ('Management Lead','Management Lead')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



#companies/{companyId}/employees
