# -*- coding: utf-8 -*-
#


from django.db import models


class TestModel(models.Model):
    int_value = models.PositiveIntegerField('value', default=0)
    string_value = models.CharField('string value', max_length=255)

    def __str__(self):
        return str(self.value)


