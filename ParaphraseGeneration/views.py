'''
Created on 15-Feb-2018

@author: Vishnu
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .NLG import textgen

@permission_classes((permissions.AllowAny,))
class Para(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        paraphrase = textgen(question['messageText'])
        output = {}
        output['paraphrases'] = paraphrase
        return Response(output)
