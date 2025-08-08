
## Learning Docker

This is a simple web app that lets users submit their **name and age**, and stores it in a **PostgreSQL** database — all running inside Docker containers.

I love to learn by implementing stuff. Just a basic introduction, designed for **Docker beginners** to learn how to:

* Dockerize a Python Flask app
* Run a database in a container
* Use **Docker Compose** to manage multi-container apps
* Persist data using **volumes**
* Connect services with **internal Docker networking**

---

## 📂 Project Structure

```
.
├── app.py               # Flask app
├── templates/form.html  # HTML form
├── Dockerfile           # Flask app container build
├── docker-compose.yml   # App + DB services
├── .env                 # Environment variables
└── requirements.txt     # Python dependencies
```

---

## Getting Started

1. **Clone the repo**

```bash
git clone <your-repo-url>
cd <your-project>
```

2. **Create a `.env` file**

```env
DB_HOST=db
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
```

3. **Run the app**

```bash
docker compose up --build
```

4. Open your browser: [http://localhost:3001](http://localhost:3001)

---

## 📌 Key Docker Features Used

* **Docker Compose**: Define multi-container setup
* **Volumes**: Persist Postgres data
* **`.env` file**: Manage secrets/configs
* **Internal networking**: App talks to DB using service name `db`

