
set name=%~n0
echo =%name%
wt -w 0 cmd /k "cd %cd% && call %cd%/%name%/Scripts/activate && code . && python manage.py runserver"
