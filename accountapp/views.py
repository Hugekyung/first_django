from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save() # db에 저장한다

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world}) # request를 받아서 내용을 base.html파일에서 가져온다.
        # return HttpResponse('안녕하세요') # 해당 모듈이 없을 때, alt+enter를 누르면 해당 모듈이 어떤 라이브러리에 있는지 자동으로 찾아준다.
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!'})