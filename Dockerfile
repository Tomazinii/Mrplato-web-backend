FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
WORKDIR /code/tools/src
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]