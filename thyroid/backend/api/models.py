from django.db import models

class ThyroidTest(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    smoking = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    hx_smoking = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    hx_radiotherapy = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    thyroid_function = models.CharField(max_length=15, choices=[('Euthyroid', 'Euthyroid'), ('Hypothyroid', 'Hypothyroid'), ('Hyperthyroid', 'Hyperthyroid')])
    physical_exam = models.CharField(max_length=20, choices=[('Single', 'Single'), ('Multinodular', 'Multinodular')])
    adenopathy = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    pathology = models.CharField(max_length=15, choices=[('Micropapillary', 'Micropapillary'), ('Other', 'Other')])
    focality = models.CharField(max_length=20, choices=[('Uni-Focal', 'Uni-Focal'), ('Multi-Focal', 'Multi-Focal')])
    risk = models.CharField(max_length=15, choices=[('Low', 'Low'), ('Intermediate', 'Intermediate'), ('High', 'High')])
    t = models.CharField(max_length=10)
    n = models.CharField(max_length=10)
    m = models.CharField(max_length=10)
    stage = models.CharField(max_length=5)
    response = models.CharField(max_length=20, choices=[('Excellent', 'Excellent'), ('Indeterminate', 'Indeterminate')])

    def __str__(self):
        return f"{self.age} {self.gender}"
