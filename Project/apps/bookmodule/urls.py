from . import views
from django.urls import path , include

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('viewbook/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/text/formatting', views.format, name="books.format"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/links', views.link, name= "books.link"),
    path('html5/tables', views.tables, name= "books.tables"),
    path('search/', views.search, name= "books.search"),
    path('simple/query/', views.simple_query, name= "books.simple_query"),
    path('complex/query/', views.lookup_query, name= "books.lookup_query"),
    path('lab8/task1/', views.task1, name= "books.task1"),
    path('lab8/task2/', views.task2, name= "books.task2"),
    path('lab8/task3/', views.task3, name= "books.task3"),
    path('lab8/task4/', views.task4, name= "books.task4"),
    path('lab8/task5/', views.task5, name= "books.task5"),
    path('lab8/task6/', views.task6, name= "books.task6"),
    path('lab9_part1/listbooks', views.listbooks, name= "books.listbooks"),
    path('lab9_part1/addbook', views.addbook, name= "books.addbook"),
    path('lab9_part1/editbook/<bID>', views.editbook, name= "books.editbook"),
    path('lab9_part1/deleteBook/<bID>', views.deleteBook, name= "books.deleteBook"),
    path('lab9_part2/addBookByForm', views.addBookByForm, name= "books.addBookByForm"),
    path('lab9_part2/editBookByForm/<bID>', views.editBookByForm, name= "books.editBookByForm"),
    path('lab10/addStudent', views.addStudent, name= "students.addStudent"),
    path('lab10/listStudent', views.listStudent, name= "students.listStudent"),
    path('lab10/deleteStudent<bID>', views.deleteStudent, name= "students.deleteStudent"),
    path('lab10/editStudent<bID>', views.editStudent, name= "students.editStudent"),
    
    path('lab10/addStudentM', views.addStudent2, name= "students.addStudent2"),
    path('lab10/listStudentM', views.listStudent2, name= "students.listStudent2"),
    path('lab10/deleteStudentM/<bID>', views.deleteStudent2, name= "students.deleteStudent2"),
    path('lab10/editStudentM/<bID>', views.editStudent2, name= "students.editStudent2"),
    path('lab10/addBookWithCover', views.addBookWithCover, name= "books.addBookWithCover"),

    
]
