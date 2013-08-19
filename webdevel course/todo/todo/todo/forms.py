from django import forms

#forms are a way to make html forms not in html using python/django
#now you wil make forms in this file, which will be imported through views into html

class TaskForm(forms.Form): #create a new class that is called Taskform that has the forms already created by django ; in the views document there has to be an import of the Taskforms
    add = forms.CharField(label="add task", max_length=10)#it's a place to but characters, the max_length doesn't let you put in more than 10 characters; the widget is within a box, if you know how to do widgets that how you can get placeholders
    email = forms.EmailField(label="E-mail")
    priority = forms.ChoiceField(label="priority", choices=(
        (1, "Urgent"),
        (2, "Important"),
        (3, "Not important"),
        ))
#has to be kept indented so as to belong to the class/form/function
    def clean_add(self):#to create a determined condition on the form 'add'
        add_value = self.cleaned_data['add'] #everything in the form is in the "data" section; accessing data in the value 'add' as gotten from the request
        if add_value == self.initial.get('add'):
            raise forms.ValidationError('Please type a real task')
        if add_value[0] in 'AEIOU': #checking if first letter is a vowel
            return add_value
        else:
            raise forms.ValidationError('You must use capitals for the first letter') #this will return an error mesage if the form is not completed correctly


#import ipdb; ipdb.set_trace() #tihs line will let the program be called up to the task_form valid part and then go to this section. on the terminal it will say where the program has stpped. this can be used within the form for example, so as to see what is going wrong in the code using the terminal
