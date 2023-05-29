FROM python:3.11

WORKDIR /bewise

COPY requirements.txt .
RUN pip install --no-cache-dir -r /bewise/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]