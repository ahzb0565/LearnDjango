from django.db import models

# Create your models here.


class ExecutionPlan(models.Model):
    #ECS7_Multimedia_Camera_GMIN-L001320
    platform =  models.CharField(max_length = 200)
    build_img =  models.CharField(max_length = 100)
    domain =  models.CharField(max_length = 50)

    def __str__(self):
        return "%s_%s_%s"%(self.domain, self.platform, self.build_img)

class TestCase(models.Model):
    # case, result, comments
    plan =  models.ForeignKey(ExecutionPlan)
    case_name = models.CharField(max_length = 300)
    result = models.CharField(max_length = 30)
    comments = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.case_name

