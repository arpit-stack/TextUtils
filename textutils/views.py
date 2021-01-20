#I have made this file - Arpit
from django.http import HttpResponse
from django.shortcuts import render

# Code for video 6
# def index(request):
#     return HttpResponse('''<h1>Arpit Pandey</h1> <a href="https://www.youtube.com/"> Code with harry</a>''')

# def about(request):
#     return HttpResponse("started python now and will work on it")

#code for video 7

def index(request):
    return render(request, 'index.html');
    # return HttpResponse('Home')

def ex1(request):
    return HttpResponse(''' <a href="https://www.youtube.com/">sikada</a>''')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    remove_punc = request.POST.get('removepunc', 'off')
    full_caps = request.POST.get('fullcaps', 'off')
    new_line_remover = request.POST.get('newlineremover', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    character_counter = request.POST.get('charcterCounter', 'off')
    if remove_punc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
    	    if char not in punctuations:
    		    analyzed = analyzed + char
        params = { 'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if full_caps == "on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = { 'purpose': 'Capitalize Letter', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if new_line_remover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
              analyzed = analyzed + char
        params = { 'purpose': 'Remove Next line', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extra_space_remover == 'on':
        analyzed = ""
        for index, text in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1 ] == " "):
              analyzed = analyzed + text
        params = { 'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if character_counter == 'on':
        string_lenght = len(djtext)
        params = { 'purpose': 'The number of character count is', 'analyzed_text': string_lenght}
        djtext = string_lenght
        # return render(request, 'analyze.html', params)
    if(remove_punc != "on" and full_caps != "on" and new_line_remover != "on" and extra_space_remover != 'on' and character_counter != 'on'):
        return HttpResponse('Here punctuations is of so we will get the error here')
    # else:
    # 	return HttpResponse('Here punctuations is of so we will get the error here')
    return render(request, 'analyze.html', params)

# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     return HttpResponse('''<a href="/">Back</a>removepunc''')

# def capFirst(request):
#     return HttpResponse('''<a href="/">Back</a>capitalize First''')

# def newLineRemove(request):
#     return HttpResponse('''<a href="/">Back</a>newLineRemove''')

# def spaceRemover(request):
#     return HttpResponse('''<a href="/">Back</a>spaceRemover''')

# def charCount(request):
#     return HttpResponse('''<a href="/">Back</a>charCount''')
