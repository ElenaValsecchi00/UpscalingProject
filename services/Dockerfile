FROM python:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN wget https://github.com/ElenaValsecchi00/UpscalingProject/raw/master/services/editor/pretrained/enhancer.pth -P ./pretrained/
RUN wget https://github.com/ElenaValsecchi00/UpscalingProject/raw/master/services/editor/pretrained/DAT_x4.pth -P ./pretrained/
EXPOSE 5000
CMD ["python", "up_app.py"]