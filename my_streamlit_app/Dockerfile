FROM python:3.9

# Créer dossier de l'application
WORKDIR /app

# Copier fichiers
COPY app.py /app/
COPY configurations.py /app/
COPY requirements.txt /app/

# Installer dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer port Streamlit
EXPOSE 8080

# Lancer Streamlit (port Cloud Run compatible)
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
