FROM python:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN wget https://github.com/ZHKKKe/Harmonizer/raw/master/pretrained/enhancer.pth -P ./pretrained/
EXPOSE 5000
CMD ["python", "up_app.py"]