# fronse('<h1 style="color:red;">hello world my name is %s i am %s years old</h1>'%(name, age))m django.http import HttpResponse
#
# def index(request,name,age):
#     return HttpResponse('<h1 style="color:red;">hello world my name is {} i am {} years old</h1>'.format(name,age))
#
# def index1(request,name,age):
#     return HttpResponse('<h1 style="color:red;">hello world my name is %s i am %d years old</h1>'%(name,age))
#
# def introduce(request,name,age):
#     return HttpRespo



from django.http import HttpResponse
from django.template.loader import get_template

def index(request):
    template = get_template("index.html")
    result = template.render({'name':'laoxing'})
    return HttpResponse(result)

def page_list(request,page):
    page = int(page)
    template = get_template('page_list.html')
    result = template.render({'page':page})
    return HttpResponse(result)