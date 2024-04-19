import os
import subprocess

def setupDjango(name):
    subprocess.call(["python", "-m", "venv", "create"])
    if os.name == "nt":
        activate_script = os.path.join("create", "Scripts", "activate")
    else:
        activate_script = os.path.join("create", "bin", "activate")

    subprocess.call([activate_script])

    # install Django
    subprocess.call(["pip", "install", "django"])

    # make Django project
    projact_name = name
    subprocess.call(["django-admin", "startproject", project_name])

def makeDirTree(project_name, app_name):
    subprocess.call(['python', os.path.join(project_name, "manage.py"), "startapp", app_name])

    # create templates dir
    templates_dir = os.path.join(project_name, app_name, "templates", app_name)
    os.makedirs(templates_dir)

    # create index.html
    index_html_path = os.path.join(templates_dir, "index.html")
    with open(index_html_path, "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang='en'>\n")
        f.write("<head>\n")
        f.write("    <meta charset='UTF-8'>\n")
        f.write("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        f.write("    <title>{}</title>\n".format(app_name.capitalize()))
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("    <h1>Welcome to {}!</h1>\n".format(app_name.capitalize()))
        f.write("</body>\n")
        f.write("</html>\n")

    # create base file
    with open(os.path.join(project_name, app_name, "views.py"), w) as f:
        f.write("from django.shortcuts import render\n\n")
        f.write("def index(request):\n")
        f.write("   return render(request, '{}/index.html')\n".format(app_name))
    
    urls_file = os.path.join(project_name, app_name, "urls.py")
    with open(urls_file, "w") as f:
        f.write("from django.urls import path\n\n")
        f.write("from . import views\n\n")
        f.write("urlpatterns = [\n")
        f.write("   path('', view.index, name='index'),\n")
        f.write("]\n")
    