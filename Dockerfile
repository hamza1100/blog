FROM python:3
RUN pip3 install django
COPY . .
RUN python3 -m pip install Pillow
Run python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
