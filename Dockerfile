FROM python:3

WORKDIR /app
COPY . /app
# Env vars
ENV bot_token ${bot_token}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "CatProjectBot.py" ]
