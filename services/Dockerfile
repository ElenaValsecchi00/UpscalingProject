FROM python:3.11-slim
COPY /editor /app
WORKDIR /app
RUN apt update && apt install build-essential -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 wget -y
RUN pip install -r requirements.txt
RUN wget https://github.com/ElenaValsecchi00/UpscalingProject/raw/main/services/editor/pretrained/enhancer.pth -P ./pretrained/
RUN wget https://github.com/ElenaValsecchi00/UpscalingProject/raw/main/services/editor/pretrained/DAT_light_x4.pth -P ./pretrained/
EXPOSE 5100
CMD ["python", "up_app.py"]