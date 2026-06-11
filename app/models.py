

from django.db import models
from django.utils import timezone
b_time = models.DateTimeField(default=timezone.now)


class Departments(models.Model):
    d_name= models.CharField(max_length=100)
    d_disc= models.TextField()
    
    def __str__(self):
        return self.d_name

class Members(models.Model):
    m_name= models.CharField(max_length=100)
    m_field= models.TextField()
    m_department= models.ForeignKey(Departments, on_delete=models.CASCADE)
    m_image= models.ImageField(upload_to='members/')

    def __str__(self):
        return 'Dr. ' + self.m_name + ' (' + self.m_department.d_name + ')'

class Booking(models.Model):
    p_name= models.CharField(max_length=100)
    p_phone= models.CharField(max_length=20)
    p_email= models.EmailField()
    pd_name= models.ForeignKey(Members, on_delete=models.CASCADE)
    b_date= models.DateField()
    b_time= models.TimeField(null=True, blank=True)
    on_b=models.DateField(auto_now_add=True)
    on_t=models.TimeField(auto_now_add=True ,null=True, blank=True)
    
    
    def __str__(self):
        return 'Dr. ' + self.p_name + ' -(' + self.pd_name.m_department.d_name + ')'
        
    
        

        


        
# Create your models here.
