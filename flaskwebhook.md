Deploying a Flask Application on Heroku
📋 Description
This project deploys a Flask application to Heroku, making it accessible via a public URL.

🚀 How to Deploy
1. Install the Heroku CLI
Download and install the Heroku CLI.

2. Log in to Heroku
In your terminal:

bash
Copiar
Editar
heroku login
3. Prepare your project
Make sure your project includes:

requirements.txt: Lists all dependencies (e.g., Flask, Gunicorn).

Procfile: Tells Heroku how to start your app.

Example content for Procfile:

makefile
Copiar
Editar
web: gunicorn app:app
4. Initialize Git (if not already initialized)
bash
Copiar
Editar
git init
git add .
git commit -m "Initial commit"
5. Create a Heroku app
bash
Copiar
Editar
heroku create your-app-name
Heroku will generate a URL like https://your-app-name.herokuapp.com.

6. Deploy your app
bash
Copiar
Editar
git push heroku master
7. Access your app in the browser
After deployment, open:

arduino
Copiar
Editar
https://your-app-name.herokuapp.com
8. View app logs (optional)
bash
Copiar
Editar
heroku logs --tail
Use this command to troubleshoot any errors if necessary.

📦 Example requirements.txt
nginx
Copiar
Editar
Flask
gunicorn
🛠️ Notes
Apps on the free plan may sleep after 30 minutes of inactivity.