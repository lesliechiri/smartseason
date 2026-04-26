BACKEND SETUP
cd backend
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env # Add your SECRET_KEY, DB creds
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

FRONTEND SETUP
cd frontend
npm install
cp .env.example .env
npm run dev

USING DOCKER
docker compose up --build