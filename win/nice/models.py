from django.db import models


class ObservationType(models.TextChoices):
    # Define your ObservationType choices here
    CHOICE1 = "CHOICE1", "Choice 1"
    CHOICE2 = "CHOICE2", "Choice 2"
    # Add more choices as needed


class ObservationLevel(models.TextChoices):
    DEFAULT = "DEFAULT", "Default"
    ERROR = "ERROR", "Error"


class Observation(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    parent_observation_id = models.TextField(null=True)
    type = models.CharField(max_length=50, choices=ObservationType.choices)
    trace_id = models.TextField(null=True)
    metadata = models.JSONField(null=True)
    model = models.TextField(null=True)
    modelParameters = models.JSONField(null=True)
    input = models.JSONField(null=True)
    output = models.JSONField(null=True)
    level = models.CharField(
        max_length=50,
        choices=ObservationLevel.choices,
        default=ObservationLevel.DEFAULT,
    )
    status_message = models.TextField(null=True)
    completion_start_time = models.DateTimeField(null=True)
    completion_tokens = models.IntegerField(default=0)
    prompt_tokens = models.IntegerField(default=0)
    total_tokens = models.IntegerField(default=0)
    version = models.TextField(null=True)
    project_id = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    unit = models.TextField(null=True)
    prompt_id = models.TextField(null=True)
    input_cost = models.DecimalField(max_digits=65, decimal_places=30, null=True)
    output_cost = models.DecimalField(max_digits=65, decimal_places=30, null=True)
    total_cost = models.DecimalField(max_digits=65, decimal_places=30, null=True)
    internal_model = models.TextField(null=True)

    class Meta:
        db_table = "observations"
        managed = False
