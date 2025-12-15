FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

# 1. 安装 Python 包
# 2. 执行 unidic 下载命令 (这会下载约 800MB+ 的数据)
# 注意：这一步取决于你的网络速度，可能会比较慢
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m unidic download

COPY main.py .

EXPOSE 23333

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "23333"]