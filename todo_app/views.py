from django.shortcuts import render
# from django.db.models.functions import Now
import datetime

from todo_app.models import ToDoEntry

# Create your views here.
def index(request):
    """Hier ist die App-Logik und Steuerung der Daten untergebracht. Diese 
    werden mit Hilfe des context-Dictionaries an das index-Template uebergeben.
    Info:  
     -> die Todos werden hier persistent gespeichert (Tabelle ToDoEntry)
    ---
    Ohne persistente Speicherung könnte man mit einem Dictionary arbeiten, 
    wobei der ToDo-Text als key dienen könnte.
    Dann müsste allerdings als request.POST['completed_todo'] der Text und 
    nicht die id uebergeben werden (in index.html Zeile 44 ändern: 
    value="{{item.id}}" => value="{{item.text}}")
    """
    if request.method == 'POST':
        # nur wenn new_todo nicht leer ist
        if 'new_todo' in request.POST and request.POST['new_todo']:
            todo = ToDoEntry(
                text = request.POST['new_todo'], 
                completion_date = None
            )
            todo.save()
        if 'completed_todo' in request.POST:
            ToDoEntry.objects.filter(id=request.POST['completed_todo']).update(
                completion_date=datetime.datetime.now())
    else:
        # mit leeren Listen starten
        ToDoEntry.objects.all().delete()
        # oder todo_entries = {} fuer eine nicht-persistente Lsg
            
    context = {}
    context['open_todos'] = ToDoEntry.objects.all().filter(completion_date=None)
    context['completed_todos']= ToDoEntry.objects.exclude(completion_date=None) 

    return render(request,'todo_app/index.html', context)