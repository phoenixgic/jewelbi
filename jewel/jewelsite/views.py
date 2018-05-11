# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django import forms
import uuid
import ConnJewelType.cnnTestCalc as cnnTestCalc

# Create your views here.
def index(request):
    return render_to_response("upload.html", {})

def upload(request):
    result = 'unknown'
    if request.method == "POST":
        file = request.FILES['imgupload']
        result = handle_uploaded_file(file)

        #We may get result from here
    return HttpResponse(result)


def handle_uploaded_file(f):
    filename = '/root'+ uuid.uuid1().__str__() + '.jpg'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return cnnTestCalc.getImageResult(filename)