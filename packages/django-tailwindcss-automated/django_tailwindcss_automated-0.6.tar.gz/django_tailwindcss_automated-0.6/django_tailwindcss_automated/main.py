import os
import shutil
from pathlib import Path
import webbrowser
import threading

def create_django_project(project_name):
    os.system(f"django-admin startproject {project_name}")
    os.chdir(project_name)

def install_django_compressor():
    os.system("python -m pip install django-compressor")

def configure_django_settings(project_name):
    settings_path = os.path.join(os.getcwd(), project_name, "settings.py")
    with open(settings_path, "w") as f:
        f.write(
            f"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-2ye&_9@aev(f(8r&f$$e!o(*ycqi02b+-&r&utixj7a6(iyzws"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "compressor",
    "{project_name}",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{project_name}.urls"

TEMPLATES = [
    {{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {{
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        }},
    }},
]

WSGI_APPLICATION = "{project_name}.wsgi.application"

DATABASES = {{
    "default": {{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }},
}}

AUTH_PASSWORD_VALIDATORS = [
    {{
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    }},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Compressor settings
COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = True
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)
"""
        )

def create_static_folders():
    os.makedirs("static/src", exist_ok=True)
    with open("static/src/input.css", "w") as f:
        f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")

def create_views_and_templates(project_name):
    os.makedirs(f"{project_name}/templates", exist_ok=True)
    with open(f"{project_name}/templates/_base.html", "w") as f:
        f.write(
            """
<!-- templates/_base.html -->

{% load compress %}
{% load static %}

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automated Setup</title>

    {% compress css %}
    <link rel="stylesheet" href="{% static 'src/output.css' %}">
    {% endcompress %}  

    <link rel="stylesheet" type='text/css' href="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css" />
</head>

<body class="bg-neutral-950">
    <div class="container mx-auto mt-4" id="content">
        {% block content %}
        
        {% endblock content %}
    </div>
</body>

</html>
"""
        )

    with open(f"{project_name}/views.py", "w") as f:
        f.write(
            """
from django.shortcuts import render


def index(request):
    return render(request, "index.html")
"""
        )

    with open(f"{project_name}/urls.py", "w") as f:
        f.write(
            f"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
]    
"""
        )

    with open(os.path.join(project_name, "templates", "index.html"), "w") as f:
        f.write(
            """
{% extends "_base.html" %}
{% block content %}
{% load static %}

{% comment %} You can remove this code :) happy coding!! {% endcomment %}
<div class="flex items-center justify-center h-screen overflow-hidden">
  <div class="flex flex-col items-center">
      <div class="flex flex-row justify-center items-center mx-auto">
          <p class="text-center text-7xl lg:text-7xl mx-4">
              <i class="devicon-django-plain colored"></i>
          </p> 
          <p class="text-center text-7xl lg:text-7xl mx-4">
              <i class="devicon-tailwindcss-original colored"></i>
          </p>
      </div>
      <h1 class="mt-6 mb-6 text-white tracking-tight text-center text-3xl lg:text-5xl font-bold font-heading max-w-7xl mx-auto">
          Automated Django Setup with TailwindCSS
      </h1>
      <p class="text-white text-xl text-center max-w-xl mx-auto">by:
          <span class="text-teal-400 font-medium hover:underline">
              <a href="https://github.com/mwwlean">@mwwlean</a>
          </span>  
      </p>
  </div>
</div>

{% endblock content %}
"""
        )


def tailwind_setup(project_name):
    os.system("npm init -y")  
    os.system("npm install")  
    os.system("npm install -D tailwindcss")  

    tailwind_config_content = f"""
/* Modified tailwind.config.js content */
module.exports = {{
  content: ["./{project_name}/**/*.html"], /* Use project name here */
  theme: {{
    extend: {{
    }},
  }},
  plugins: [],
}};
"""
    with open("tailwind.config.js", "w") as f:
        f.write(tailwind_config_content)

    # Run Tailwind CSS in watch mode
    os.system(
        f"npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch"
    )


def main():
    global project_name
    project_name = input("Enter your project name: ")

    create_django_project(project_name)
    install_django_compressor()
    configure_django_settings(project_name)
    create_static_folders()
    create_views_and_templates(project_name)

    os.chdir(project_name)
    os.chdir("..")
    tailwind_setup(project_name)
    print(f"Django project '{project_name}' with Tailwind CSS has been created  ")

    

if __name__ == "__main__":
    main()
    