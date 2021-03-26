# 基于镜像基础
FROM python:3.8

# 设置代码文件夹工作目录 /app
WORKDIR /app

# 复制当前代码文件到容器中 /app
ADD . /app


RUN pip install -r requirements.txt

# Run server.py when the container launches
CMD ["python", "server.py"]