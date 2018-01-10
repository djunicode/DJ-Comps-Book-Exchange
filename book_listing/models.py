from django.db import models
from django.urls import reverse
from django.utils import timezone
import pandas as pd
import csv


class Book_List(models.Model):
    doc = open(r'Subjects.csv', 'r')
    df = pd.read_csv('Subjects.csv')
    reader = csv.reader(doc)
    total_rows = len(list(reader))
    SUBJECTS = []
    for i in range(1, 9):
        sem = 'Semester ' + str(i)
        subject = df[sem]
        for row in range(0, total_rows - 1):
            sub = ()
            if type(subject[row]) is float:
                break
            a, b = subject[row].split('#')
            sub = (a, b)
            SUBJECTS.append(sub)
    SEMESTER = (
        ("SEM 1", "SEM 1"),
        ("SEM 2", "SEM 2"),
        ("SEM 3", "SEM 3"),
        ("SEM 4", "SEM 4"),
        ("SEM 5", "SEM 5"),
        ("SEM 6", "SEM 6"),
        ("SEM 7", "SEM 7"),
        ("SEM 8", "SEM 8")
    )

    PUBLICATIONS = (
        ('Techmax', 'Techmax'),
        ('Technical', 'Technical'),
        ('Reference Book', 'Reference Book'),
        ('Easy Solution', 'Easy Solution')
    )
    user = models.ForeignKey('auth.User', null=True)
    title = models.CharField(max_length=50)
    sem = models.CharField(
        max_length=200,
        choices=SEMESTER,
        default="SEM 1"
    )
    subject = models.CharField(max_length=1000, choices=SUBJECTS, default="Maths 1")
    description = models.TextField(max_length=500)
    book_image = models.FileField(null=True, blank=True)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=20, choices=PUBLICATIONS, default="Tech-Max")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:search')

    class Meta():
        ordering = ["-date_created"]
