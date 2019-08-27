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

class Saying:
    def say(self):
        return '哈哈哈'

def template_variable(request):
    data = {
        'name':'老邢',
        'en_name':'laoxin',
        'age':18,
        'project':['python','PHP','c','c++','java'],
        'score':('python',100,'PHP',80),
        's':Saying()
    }
    temp = get_template('template_variable.html')
    result = temp.render(data)
    return HttpResponse(result)


def template_label(request):
    data = {
        'teacher':[
            {'name':'老邢','age':18},
            {'name':'老张','age':19},
            {'name':'老温','age':29},
            {'name':'老王','age':39},
            {'name':'老申','age':49},
        ]
    }
    temp = get_template('template_label.html')
    result = temp.render(data)
    return HttpResponse(result)