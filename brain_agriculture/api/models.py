from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class State(BaseModel):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=2)

class City(BaseModel):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.state.acronym}"

class Produtor(BaseModel):
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=255)
    farm_name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    farm_total_area = models.FloatField()
    arable_total_area = models.FloatField()
    vegetation_total_area = models.FloatField()
    
    class Meta:
        db_table = "produtor"

class PlantedCrops(BaseModel):
    name = models.CharField(max_length=255)
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE, related_name="planted_crops")
