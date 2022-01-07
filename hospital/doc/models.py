from django.db import models

# Create your models here.


class sp(models.Model):
    code = models.CharField(max_length=3)
    cpecializations = models.CharField(max_length=64)

    def __str__(self):
        return f"Лікар-{self.cpecializations}"


class doctor(models.Model):
    last_name = models.CharField(max_length=34)
    name = models.CharField(max_length=34)
    father = models.CharField(max_length=50)
    spec = models.ForeignKey(sp, on_delete=models.CASCADE)
    models.CharField(max_length=50)

    def __str__(self):
        return f"{self.spec} {self.last_name} {self.name} {self.father}"


class diseases(models.Model):
    disease = models.CharField(max_length=100)
    ICD_10 = models.CharField(max_length=5)
    specialty = models.ForeignKey(sp, on_delete=models.CASCADE)
    models.CharField(max_length=50)

    def __str__(self):
        return f"{self.disease}"
