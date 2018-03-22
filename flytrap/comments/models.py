#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Created by flytrap
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(User, null=True, related_name="comments", on_delete=False)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=False)
    object_id = models.IntegerField()
    content_object = GenericForeignKey()

    comment = models.TextField()

    submit_date = models.DateTimeField(default=datetime.now)
    ip_address = models.GenericIPAddressField(null=True)
    public = models.BooleanField(default=True)

    reply = models.ForeignKey('self', null=True, blank=True, on_delete=True, related_name='reply_comment')
    is_valid = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'comments'
        verbose_name_plural = verbose_name
        ordering = ['-submit_date']

    def data(self):
        return {
            "pk": self.pk,
            "comment": self.comment,
            "author": self.author.username,
            "name": self.name,
            "email": self.email,
            "website": self.website,
            "submit_date": str(self.submit_date)
        }

    def __str__(self):
        return "pk=%d" % self.pk

    def delete_obj(self):
        self.is_valid = False
        self.save()
