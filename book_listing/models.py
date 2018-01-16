from django.db import models
from django.contrib.auth.models import User
import pandas as pd
import csv
from django.urls import reverse


class Book_List(models.Model):
    uploaded_by = models.ForeignKey(User, default=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    book_image = models.FileField(null=True, blank=True)
    author = models.CharField(max_length=250)
    SEMESTER = (('1', 'Semester 1'),
                ('2', 'Semester 2'),
                ('3', 'Semester 3'),
                ('4', 'Semester 4'),
                ('5', 'Semester 5'),
                ('6', 'Semester 6'),
                ('7', 'Semester 7'),
                ('8', 'Semester 8'), )
    semester = models.CharField(max_length=1000, choices=SEMESTER, default="Semester 1")

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
    subject = models.CharField(max_length=1000, choices=SUBJECTS, default="Maths 1")

    PUBLICATION = (('Techmax', 'Techmax'), ('Technical', 'Technical'), ('Reference Book', 'Reference Book'),
                   ('Easy Solution', 'Easy Solution'))
    publication = models.CharField(max_length=30, choices=PUBLICATION, default="Techmax")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_listing:search")
