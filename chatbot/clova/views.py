from django.shortcuts import render
from clova.send import ChatbotMessageSender

def chatbot(request):

    if request.method == "POST":
        text = request.POST['text']
        res = ChatbotMessageSender().req_message_send(text)
        print(res.status_code)
        if(res.status_code == 200):
            print(res.text)
            res_data ={}
            res_data['text'] = res.text
            return render(request, "chatbot.html",res_data)
    else:
        return render(request, "chatbot.html")
