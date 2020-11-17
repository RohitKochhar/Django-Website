from django.db import models

class Project(models.Model):
    # Constants ----------------------------------------------------------------

    # Fields -------------------------------------------------------------------
    s_Title                 = models.CharField(max_length=100)
    s_Description           = models.TextField()
    s_ImageFile             = models.CharField(max_length=20, default = 'stock1.png')
    s_LinkGitHub            = models.CharField(max_length=100, default = "None")

    def __str__(self):
        return f"{self.s_Title}"

class TechnologyUsed(models.Model):
    # Constants ----------------------------------------------------------------
    MATLAB  = 'MATLAB'
    CPP     = 'C++'
    PY      = 'Python'
    DJ      = 'Django'
    SL      = 'Simulink'
    DOCKER  = 'Docker'
    TechnologyChoices = [
                (MATLAB, "MATLAB"),
                (CPP, "C++"),
                (PY, "Python"),
                (DJ, "Django"),
                (SL, "Simulink"),
                (DOCKER, "Docker"),
                ("None", "None"),
    ]

    # Fields -------------------------------------------------------------------
    s_Name          = models.CharField(max_length=50, choices = TechnologyChoices, default = "None")
    i_Value         = models.IntegerField(default=0)
    o_Project       = models.ManyToManyField('Project', related_name='technologies')
    def __str__(self):
        return f"{self.s_Name}"