from django.shortcuts import render
from testApp import forms
import os
import tempfile
import subprocess
# Create your views here.
def student_view(request):
    form=forms.studentForm()
    if request.method=='POST':
        form=forms.studentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            imag=form.cleaned_data['Image']

            t='images/'+str(imag)
            #print(t)
            print("form data inserted into the database")
            stpr=ocr(t)
            print(stpr)
            return render(request,'testApp/text.html',{'text':stpr})
    return render(request,'testApp/register.html',{'form':form})


def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents
