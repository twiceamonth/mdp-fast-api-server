FROM python:3.12

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD alembic upgrade head &&\
#uvicorn 'src.app.main:app' --host 0.0.0.0 --port 8000 --reload --reload-include '*.py'
