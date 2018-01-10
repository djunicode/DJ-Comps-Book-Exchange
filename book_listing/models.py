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
    SEMESTER = (('1', 'Semester 1'),
                ('2', 'Semester 2'),
                ('3', 'Semester 3'),
                ('4', 'Semester 4'),
                ('5', 'Semester 5'),
                ('6', 'Semester 6'),
                ('7', 'Semester 7'),
                ('8', 'Semester 8'), )

    PUBLICATION = (
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
        default="Semester 1"
    )
    subject = models.CharField(max_length=1000, choices=SUBJECTS, default="Maths 1")
    description = models.TextField(max_length=500)
    book_image = models.FileField(null=True, blank=True)
    author = models.CharField(max_length=50)
    publication = models.CharField(max_length=20, choices=PUBLICATION, default="Tech-Max")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:search')

    class Meta():
        ordering = ["-date_created"]
