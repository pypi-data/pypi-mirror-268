import csv

from django.db import models, transaction


class PLZdb(models.Model):
    """Model to optionally store city/postcodes in the database."""
    name = models.CharField(max_length=50)
    plz = models.CharField(max_length=4)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['plz']),
        ]

    def __str__(self):
        return f"{self.plz} {self.name}"

    @classmethod
    def import_from_csv(cls, csv_path):
        """
        The CSV file is supposed to contain the city in the first col, and the
        postcode in the second.
        """
        with transaction.atomic():
            PLZdb.objects.all().delete()
            with open(csv_path) as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    PLZdb.objects.create(name=row[0], plz=row[1])
