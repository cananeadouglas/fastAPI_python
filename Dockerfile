FROM ubuntu
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app"]