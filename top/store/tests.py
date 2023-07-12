from django.test import TestCase

# ТИПЫ ПОЛЕЙ БД
# BigIntegerField - большое числовое поле
# Виджет этого поля - TextInput

# BooleanField - поле истина\ложь
# виджет - CheckInput

# Charfield
# Виджет - TextInput
# обязательный аргумент : max_length

# TextField - Большое текстовое поле
# Виджет - Textarea

# DateField -поле даты

# 2 атрибута:
# auto_now = True -сохранение новой даты при любом сохранении модели
# то есть дата будет внесена при вызове Model.save()

# auto_now_add = True сохранение новой даты только при создании экземпляра
# виджет - Input type=date


# DataTameField - поле даты и времени
# Виджет - input type=datetime

# EmailField - поле почты
# проверяет валидность адреса почты через EmailValidator

# FileField - поле файла
# ImageField - поле изображения

# оба поля имеют необязательный аргумент - upload_to - директория загружаемых с сервера файлов

# ПОЛЯ ЧИСЕЛ
# IntegerField - 
# PositiveIntegerField
# SmallPositiveIntegerField

# ПОЛЯ СВЯЗИ
# ForeignKey (один-ко-многим)
# ManyToManyField(многие-ко-многим)
# OneToOneField(щдин-к-одному)

# class Meta
# db_table - для переименования таблицы модели
# verbose_name - для переименования модели
# verbose_name_plural - для переименования модели (мн.ч.)

#  <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
#         <div class="navbar-brand has-text-weight-bold has-text-white">
#           <a class="navbar-item" href="{% url 'store:home' %}">
#             <ion-icon name="flower-outline"></ion-icon>
#             YOUR GARDEN
#             <ion-icon name="flower-outline"></ion-icon>
#           </a>
#           <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
#             <span aria-hidden="true"></span>
#             <span aria-hidden="true"></span>
#             <span aria-hidden="true"></span>
#           </a>
#         </div>
#         <div id="navbarBasicExample" class="navbar-menu">
#           <div class="navbar-start">
#             <a href="{% url 'store:home' %}" class="navbar-item">
#                 <ion-icon name="home-outline"></ion-icon>
#             </a>
#             <div class="navbar-item has-dropdown is-hoverable">
#               <a class="navbar-link">
#                 Производители
#               </a>
#               <div class="navbar-dropdown">
#                 <a class="navbar-item">
#                     {% brands %}
#                 </a>
#               </div>
#             </div>
#           </div>
      
#           <div class="navbar-end">
#             {% if users.is_authenticated %}
#             <div class="navbar-item has-dropdown is-hoverable">
#                 <div class="navbar-link">
#                     {{ user }}
#                 </div>
#                 <div class="navbar-dropdown">
#                     <a class="navbar-item has-text-danger" 
#                      href="{% url 'users:sign_out' %}">
#                         Выйти
#                     </a>
#                 </div>
#             </div>
#             {% endif %}
#         </div>
#       </nav>