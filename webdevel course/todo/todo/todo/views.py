import anydbm #database that will be in the hard disk, that will collect the information in sessions of the site, keeps more than the request.session

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe

from todo.forms import TaskForm #the import has to be hte import of the form TaskForm

#def tasks_views(request):
#    add = request.GET.get('add', 'There is nothing to do. Yeeep!')
#    delete = request.GET.get('delete', 'There is nothing to do. Yeeep!')
#    return render_to_response('tasks.html', {
#        'add': add,
#    })

#requestcontext is a must for forms

#db = anydbm.open('todo.db', 'c')#used instead of request.session and saves more information rather than what is just one session

def tasks_view(request):
#    request.session.clear()
    tasks_number = request.session.get('tasks_number', 0) #we are using a counter to store every new task in; also add new variable to mean the task_number counter
#    task_text = request.POST.get('add') now that the task_form has come in this is not needed
    initials = {
        'add': "Type your task" #instead of the form being in blank, now things are introduced, but if you press add, this text will be added as if it's a chore on todo list ; to make sure this doesn't happen go to forms and fix clean.self function. Here the initial is a variable of the dictionary that is the initial form, since it's outside of the main body of program, this is outside and not bound by so many restrictions
    }
    task_form = TaskForm(initial=initials)
    if request.POST:
        task_form = TaskForm(request.POST, initial=initials) #if a POST comes in make a form out of the TaskForm file
        if task_form.is_valid(): #if the form is valid, give the data, but the clean_data
            data = task_form.cleaned_data
            priority = data['priority']
            task_text = data['add']
            if task_text and task_text not in request.session.values():#if value already in dictionary doesn't show. This line is checking if value is in request session
#                while tasks_number in request.session:
                tasks_number += 1
                request.session[tasks_number] = task_text #in the dictionary request.session will be added the key tasks_number and the value will be task_text
                tasks_number += 1
                request.session['tasks_number'] = tasks_number
                return redirect("tasks") #after adding correctly a task, it asks the browser to redirect to a page, here it could be the page without the form filled up; the "tasks" refers to the name given to the url, now it is easier to call the url; can be any url. Remember that import is necessary 
    task_to_delete = request.GET.get('del') #the information on Post should be the text going into the form, the task to delete is the phrases so it should stay in GET
    if task_to_delete and int(task_to_delete) in request.session:
        request.session[int(task_to_delete)] = mark_safe('<s>'+request.session[int(task_to_delete)]+'</s>')
    return render_to_response('tasks.html', RequestContext(request, {
        'tasks_number': tasks_number,
        'tasks': request.session,
        'task_form': task_form
    }))

#in place of doing del you have to mark it as erased


#everytme length is run in a dictionary len(d) then you will know how many keys are in there
#keys that are going to be used in the request.session dictionary will be numbers and the value will be the tasks
#request.session.get('tasks_number', 0) -> the tasks_number is actually and integer and that is why the next point is 0, so if there are no tasks return 0, but if there are then put in a numerical key


#using format
#    request.session[int(task_to_delete)] = mark_safe('<s>{0}</s>'.format(request.session[int(task_to_delete)])
    #format -> the {} denote the format to replace after the format in {} in html
