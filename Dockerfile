FROM python:3
RUN pip3 install django
COPY . .
RUN pip install --upgrade pip
RUN pip install openai
RUN python3 -m pip install Pillow
RUN python3 -m pip install python-dotenv
Run python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
