import calendar
import urllib2
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, render_to_response #used to render a template and convert it to response ; use instead of httpresponse
from django.template import RequestContext
from django.utils.safestring import mark_safe

def hello_view(request, name, year):
    message = u'{name} is {years} old'.format(name=name, 
                                              years=(2013 - int(year)))
    response = HttpResponse(message)
    return response

def sum_view(request,x,y):
    """URL and view to sum two values"""
    res = int(x) + int(y)
    return HttpResponse(res)

def grade_view(request,n):
    """View to give a grade"""
    n = int(n)
    if 50 <= n < 60:
        grade = 'd'
    elif 60 <= n < 70:
        grade = 'c'
    elif 70 <= n < 80:
        grade = 'b'
    elif 80 <= n <= 100:
        grade = 'a'
    else:
        grade = 'fail'
    return HttpResponse(grade)

def sort_view(request, l):
    """View to sort a list of values seperated by comma"""
    real_list = l.split(',')
    num_list = []
    for item in real_list:
        item = int(item)
        num_list += [item]
    num_list.sort()
    res = ''
    for item in num_list:
        res += ''.format()
    return HttpResponse(num_list)

def sort_view(request,l):
    num_list = [int(i) for i in l.split (',')]
    num_list.sort()
    #or map can be used than comprehension list below, map
        #str_list = map(str, num_list)
    str_list = [str(i) for i in num_list] # for every item return it in teh new way here it would be return the item in a string
    return HttResponse(",".join(str_list))

def map(func, l): ## this is what map does
    res = []
    for item in l:
        res.append(func(item))
    return res

def sort_view(request, l):
    num_list = [int(i) for i in l.split(',')]
    #add one to all numbers on the list
    #added_list = [i + 1 for i in num_list] or added to the top one being num_list = [int(i) + 1 for i in l.split(',')]
    num_list.sort()
    str_list = [str(i) for i in num_list]
    return HttpResponse(",".join(str_list))

def now_view(request):
    """View to return current time"""
    now = datetime.now()
    return HttpResponse(now)

def code_view(request):
    """View to return the current source code of the file in which the view is defined"""
    f = open('/home/webdevel/projects/day6/projects/hello/views.py', 'r')
        ## or python can do a path for itself which is f = open (__file__, 'r')
    res = f.read()
    res = res.replace('\n', '<br>')
    res = res.replace(' ', '&nbsp;')
    res = res.replace('def', '<b style="color: red;">def</b>') 
    #to bold and make red all words def with html inside django
    return HttpResponse(res)

def code_view(request):
    """View to retur the current source code of the file in which the view is defined"""
    color = request.GET['color']
    f = open(__file__, 'r')
    res = f.read()
    res = res.replace('\n', '<br>')
    res = res.replace(' ', '&nbsp;')
    res = res.replace('def', '<b style="color: {c};">def</b>'.format(c=color))
        #here you can use the c to assign what it is here it would be c=color, however if you use numbers, it automatically goes in order
            #so now the color can be manipulated in the url so the url would be 127.0.0.1:8000/code/?color=green
    return render_to_response('code.html', {'code': res})

def code_view(request):
    """View to retur the current source code of the file in which the view is defined"""
    color = request.GET.get('color')
    rcolor = request.GET.get('rcolor')
    print color
    f=open(__file__, 'r')
    res = f.read()
    res = res.replace('\n', '</br>')
    res = res.replace(' ', '&nbsp;')
    res = res.replace('def', '<b style="color: {c};">def</b>'.format(c=color))
    res = res.replace('return', '<b style="color: {c};">return</b>'.format(c=rcolor))
    return render_to_response('code.html', {
        'code': mark_safe(res),
        'color': color,
        'rcolor': rcolor, ## make sure that when one is added that there is also a request.GET.get that matches with the new key and value
    })

#1. New URL and view to sum two values 
#2. URL and view to give a grade 
#3. URL and view to sort a list of values seperated by comma
#4. URl and view to return current date and time. HINT take a look at datetime module in python
#5. URL and view to return the current source code of the file in which the view is defined HINT open 

def hosts_view(request):
    comment = request.GET.get('comment', 'black')
    h = open('/etc/hosts', 'r')
    res = h.read()
    res = res.replace('\n', '</br>')
    res = res.replace(' ', '&nbsp;')
    res = res.replace('127.0.0.1', '<b style="color: blue;">127.0.0.1</b>')
    res = res.replace('127.0.1.1', '<b style="color: blue;">127.0.1.1</b>')
    if comment == 'true':
        res = res.replace('#', '<b style="color: magenta;">#</b>')
    return render_to_response('url.html', {
        'code': mark_safe(res),
        'comment': comment,
    })

def temperature_view(request, n): #here the function is taking two objects, the request and the variable n
    n = int(n)  #the n variable will always be turned into an integer
    temperature = n
    units = request.GET.get('to', 'Celsius') #units is what determines the behaviour of the function
    if units == 'Fahrenheit':
        temperature = (n * 9)/5 + 32
    return render_to_response('temperature.html', { #this part is used to present the information on the browser
        'temperature' : temperature,
        'units' : units,
    })

def current_percentage(request, x, y): #this function is not necessary to have hmtl template therefore you can just put the httpresponse at the bottom instead of the render and .GET
    p = (float(x)/100) * int(y)
    message = x + '% of ' + ' is ' + str(p)
    return HttpResponse(message)

def dna_view(request, d):#take the list and convert it into a dictionary,
    #use a four loup see how many time each key appears 
    dna_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0} #the value is 0 because the dictionary is not written, therefore the loop will begin to fill in the numbers as per the amount the keys come up in a list
        #here it is an empty dictionary, it was created so that every time the dictioanry is iterated the base that increases will be stored in the value portion of hte dictionary for every key
    for base in d:      #the base at every step of the loop is A, T, C, G
        dna_dict[base] += 1     #everytime that the base comes up it will be increased by 1
    messsage = u'A: {A}, T: {T}, C: {C}, G: {G}'.format(
        A= dna_dict['A'], # a more compact way of doing the .format
        T= dna_dict['T'], #.format(**dna_dict)
        C= dna_dict['C'], # also does it with list, but with *
        G= dna_dict['G'] 
    )
    return render_to_response('dna.html', {
    'dna': message
    }) #the dna_view is the name of the box in the template which will print the message in the browser


#def gutenberg_view(request, ebook_id):
#    url = 'http://www.gutenberg.org/cache/epub/{0}/pg{0}.txt'.format(ebook_id) #this is formatted so that it can be manipulated late, but still has to do with the real url
#    ebook = urllib2.urlopen(url) # this is the part that opens the url, like the open and read of the file used in previous excecise
#    text = ebook.readlines()
# #takes a list that each element is a line of the document taken
#    title: ''
#    author: ''
#    for line in text:
#        if line.startswith('Title: '): #the .startswith takes iterates/finds the Title:
#            split_line = line.split(': ') # a partir of hte two points starts the title, which varies depending on the book chosen, ex.['Title', 'Alice']; it returns a list of two values, the Title and the titulo
#            title = split_line[-1] #the [] is talking about the position of the string
#        elif line.startswith('Author: '):
#            split_line = line.split(': ')
#            author = split_line[-1]
#    number_chars = int(request.GET.get('chars', 0)) #what hte tuple means is that if 'chars' is not asked for in url then return 0 (nothing)
#    text = '\n'.join(text_lines): #because we want a query to call the amount of numbers determined by the query, the ebook.read will have to read all of the book; the problem is that readlines after the loop is done, the ebook is empty, therefore the .join will ask the text that we made to read over again 
#    if 'CONTENTS.' in text: #this way if contents is not part of a book then it will leave it
#        content_position = text.index('CONTENTS.') + len('CONTENTS.') #.index allows to go from the beginning of that the text that is determined in the string, here would be 'content'
## we don't want the actual word "contents", in order to do that, you have to add the len of hte word contents. so that the word won't show up
#        first_chars = text[content_position:content_position + number_chars] #the first_chars will the key for the template
##used to ask the function to give the range of 'number' from the text, but this is wrong, instead the +# means that it would be the position plus the number of characters indicated afterwards
##before it was +500, but we changed it to number_chars which is previously determined as a request
#    else:
#        first_chars = '' #this, in addition to the title and author with empty '' at the top are used to avoid the error when the author or title are not even in the text from project gutenberg
#    return render_to_response('gutenberg.html', {
#        'title': title,
#        'author': author,
#        'first_chars': first_chars,
#    })

def date_view(request,y,m,d):
    y = int(y)
    d = int(d)
    m = int(m)
    comment = request.GET.get('comment')
    if not comment:
        menglish = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        m = menglish[m-1]
        message = '{m} {d}, {y}'.format(m=m, d=d, y=y)
    else:
        mspanish = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        m = mspanish[m-1]
        message = '{d} de {m} de {y}'.format(d=d,m=m,y=y)
    return render_to_response('date.html', {
        'message': message,
    })


def averagegrades_view(request,username):
    grades = {
    'ndutta': {'Name': 'Nandita', 'exams': [80, 90, 56]},
    'versae': {'Name': 'Javier', 'exams': [70, 98, 67]},
    'jsuarez': {'Name': 'Juan Luis', 'exams': [57, 89, 62]},
    'ncaldas': {'Name': 'Natalia', 'exams': [48, 82, 36]},
    'ajimene': {'Name': 'Antonio', 'exams': [36, 90, 74]},
    'mafana': {'Name': 'Mohammed', 'exams': [80, 90, 29]},
    'dbrown': {'Name': 'David', 'exams': [71, 95, 0]},
    }
    average_list = {}
    person_dict = grades[username]#a new dictionary was made with the usernames
    person_name = person_dict['Name']
    person_grade = person_dict['exams']
    average_person_grade = sum(person_grade)/len(person_grade) #the sum is a function in python to add all that is within a list, here it was made under person_grade, all of this is then divided by 3
    if 'final' in request.GET: 
        needed_points = (80 - 3*average_person_grade/4) * 4 
    else:
        needed_points = None #saying that the needed points is nothing
    return render_to_response('averagegrades_view.html', {
    'Name' : person_name,
    'average' : average_person_grade,
    'needed_points' : needed_points
    })

def guess_view(request):
    guess = request.GET.get('guess')
    if 'x' in request.session: #if x is in the dictionary that we are storing stuff (request.session)...
        random_number2 = request.session['x'] #...then the number will stay the same. Here the random number will be the value of x. the only time the session will be over is when the browser is closed
    else:
        random_number2 = int(
    random_number2 = int(random.uniform(1,100)) #if the url has no get pattern in query going to generate a number, but everytime go to url a new number will be generated ; there is a way to store information between different requests, which is request.session (it's actually a dictionary)
    #basically it's supposed to act as if everytime you enter a guess the random number selected will not change when page refreshed, but if no guess is selected and page is refreshed the numbers will change
    #for this to be done the random number must be held in the dictionary request.session because that is the dictionary that holds the random number and doesn't lose it when refreshing page
    request.session['x'] = random_number2 #request.session stays the same during a whoel time of being on session of internet
#the logic of this problem is that if there is no number enter one, if there is a number leave it for the next sessions.
#        the rest of this is part of david's code:
#        message = u"Guess a number between 1 and 100"
#        random_number = int(random.uniform(1,100))
#        request.session['random'] = random_number
#    else:
#        guess = int(guess)
#        if guess == request.session['random']
#            message = u'Awesome Dude! The number was {0}. \
#                Try a new number!'.format(request.session['random'])
#            random_number = int(random.uniform(1,100))
#            request.session['random'] = random_number
#        elif guess > request.session['random']:
#            message = u'{0} too high. Try again!'.format(guess)
#        else:
#            message = u'{0} too low. Try again!'.format(guess)
#    return render_to_response('guess.html', {
#        'message': message,
#    })

# username = 'versae'
# password = '123'
def login_view(request):
    username = request.POST.get('username') #if you send this type of information by .GET you will see it in the URL and whoever can manipulate it. the POST will make what comes in url invisible
    password = request.POST.get('password') 
    if request.session.get('loggedin'):#must serve as a first step because it's asking if loggedin (the key of hte dictionary request.session) is the same as logged (the password) then dejalo
        if 'logout' in request.GET: #if the logout request, which is sent from GET. log the username out. This is a request that you make in the url 
            request.session['loggedin'] = False
            logged = False
        else: 
            logged = request.session['loggedin']#the next part would be to add a logged out option, it would be an if statement that is request.session['loggedin'] = False
            username = request.session['username']
    else:
        if username == 'versae' and password == '123':
            logged = True 
            request.session['loggedin'] = logged
            request.session['username'] = username
            #the username needs to be put into the dictionary of logged because if it is not the username will not appear after the first refresh of the page, therefor the username needs to be added into the same dictionary of logged which is actually the dictionary of session. The next step is making sure that it prints on hte screen therefore it needs to be placed in the first if
        else:
            logged = False #logged is a variable that determines whether a person is logged in or not, must be sent to the view (html) page
    return render_to_response('login.html', RequestContext(request, {
    'username': username,
    'logged': logged,
    }))
    #django has this by defaul called @login_required 




def html_view(request):
    return render_to_response ('html.html', {})

