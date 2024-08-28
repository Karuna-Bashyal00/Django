from django.db import models

class TODO(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Employee(models.Model):

    ''' DEPARTMENT CHOICES '''
    FRONTEND_DEPART = 'FD'
    BACKEND_DEPART = 'BD'
    DATABASE_DEPART = 'DD'
    OTHERS = 'O'
    
    DEPARMENT_CHOICES = [
        (FRONTEND_DEPART, 'FRONTEND'),
        (BACKEND_DEPART, 'BACKEND'),
        (DATABASE_DEPART, 'DATABASE'),
    ]

    ''' GENDER CHOICES '''
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    ]

    ''' SHIFT CHOICES '''
    MORNING = 'M'
    DAY = 'D'
    EVENING = 'E'

    SHIFT_CHOICES = [
        (MORNING, 'MORNING'),
        (DAY, 'DAY'),
        (EVENING, 'EVENING'),
    ]

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=20)
    salary = models.IntegerField()
    department = models.CharField(max_length=10, choices=DEPARMENT_CHOICES)
    working_hrs = models.DateTimeField(auto_now_add=True)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name
    

