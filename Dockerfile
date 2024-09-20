# syntax=docker/dockerfile:1

FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install streamlit pandas numpy
CMD ["streamlit", "run", "Hello.py", "--server.port=8501", "--server.address=0.0.0.0"]
EXPOSE 8501