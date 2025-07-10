from django.db import models


class ListingStatus(models.TextChoices):
    AVAILABLE = "available", "Налично"
    ORDERED = "ordered", "Поръчано"
    COMPLETED = "completed", "Завършено"