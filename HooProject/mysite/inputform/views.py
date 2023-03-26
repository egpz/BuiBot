from django.shortcuts import render
from .forms import InputForm
from . import chatgpt
 
# Create your views here.
def home_view(request):

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():

            input_code = form.cleaned_data['input_code']

            file = open("code.txt", "w")
            file.write(str(input_code))
            file.close()

            annotations = chatgpt.test("code.txt")
            annotations2 = []
            for annotation in annotations:
                annotations2.append(annotation.strip('\n'))
            annotations = '\n\n'.join(annotations2)
                
               #annotation = annotation.splitlines()
              #  annotations = '\n'.join(annotation)
            

            return render(request, 'home.html', {'input_code': input_code, 'annotations': annotations})

        
    else:
        form = InputForm()

    return render(request, "home.html", {"form": form })