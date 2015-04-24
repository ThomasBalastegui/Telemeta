# -*- coding: utf-8 -*-
from telemeta.models import *
from haystack.forms import *
from haystack.query import SearchQuerySet

class HaySearchFormItem(SearchForm):

    def search(self):
        sqs=SearchQuerySet().load_all()

        if not self.is_valid():
            return sqs

        if self.cleaned_data['q']:
            sqs=sqs.models(MediaItem).filter(content__contains=self.cleaned_data['q'])

        return sqs

class HaySearchFormCollection(SearchForm):

    def search(self):
        sqs=SearchQuerySet().load_all()

        if not self.is_valid():
            return sqs

        if self.cleaned_data['q']:
            sqs=sqs.models(MediaCollection).filter(content__contains=self.cleaned_data['q'])

        return sqs


class HayAdvanceSearchForm(ModelSearchForm):

    title = forms.CharField(required=False)

    def search(self):
        sqs=SearchQuerySet().load_all()

        if not self.is_valid():
            return sqs

        if self.cleaned_data['q']:
            sqs=sqs.filter(content__contains=self.cleaned_data['q'])

        return sqs
