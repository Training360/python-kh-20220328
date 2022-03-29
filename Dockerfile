FROM python
WORKDIR app
COPY hello.py requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT python hello.py

