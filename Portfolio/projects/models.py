from django.db import models

# Create your models here.

class Project(models.Model):
    # Constants ----------------------------------------------------------------
    MATLAB  = 'matlab'
    CPP     = 'cpp'
    PY      = 'py'
    DJ      = 'dj'
    SL      = 'sl'
    TechnologyChoices = [
                (MATLAB, "MATLAB"),
                (CPP, "C++"),
                (PY, "Python"),
                (DJ, "Django"),
                (SL, "SimuLink"),

    ]
    # Fields -------------------------------------------------------------------
    s_Title                 = models.CharField(max_length=100)
    s_Description           = models.TextField()
    s_PrimaryTechnology     = models.CharField(max_length=20, choices = TechnologyChoices, default = "None")
    s_SecondaryTechnology   = models.CharField(max_length=20, choices = TechnologyChoices, default = "None")
    s_TertiaryTechnology    = models.CharField(max_length=20, choices = TechnologyChoices, default = "None")
    s_ImageFile             = models.CharField(max_length=20, default = 'stock1.png')


    def __str__(self):
        return f"{self.s_Title}"
