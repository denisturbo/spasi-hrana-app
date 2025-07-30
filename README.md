# SpasiHrana

SpasiHrana is a platform with the goal of eliminating the food waste.
## Live Demo [NOT YET]
## CHECK OUT HERE.. 
# First Steps
**1. Clone the repo**
```bash
git clone https://github.com/denisturbo/spasi-hrana-app.git
cd spasi-hrana-app
```
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install everything needed.
```bash
pip install -r requirements.txt
```
## Setup
- Since we are using ``environs`` Copy the template from ``.env.example`` for all of the secrets and paste them into ``.env`` with your settings.
- [Optional] ``.envrc`` if you are using  [https://direnv.net](https://direnv.net)
```python
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver
```
Before creating the users, we actually need to create 2 Groups - Customer & Business. Quite simple.
1. Go to Django Administration
2. Navigate to Authentication and Authorization -Groups
3. Create 2 Groups - Business & Customer. - Permissions All with ``customauth | businessuser`` for Business and All with ``customauth | cuustomeruser`` for Customer


- Optional for Deployment
 **Collect static**
```python
python manage.py collectstatic
```
## Tailwind Setup
We are using [django-tailwind](https://django-tailwind.readthedocs.io/) to integrate TailwindCSS into Django.
1. **Install Node.js** (required for building Tailwind assets):  
   [https://nodejs.org](https://nodejs.org) 
2. **Install Tailwind Dependencies**
```python
python manage.py tailwind install
```
3. **Run Tailwind in Development Mode**  
```python
python manage.py tailwind start
```
4. **Build for Production**
```python
python manage.py tailwind build
```
# Tech Stack
- [Django](https://github.com/django/django) - Back-end
- [PostgreSQL](https://www.postgresql.org/) - DB
- [TailwindCSS](https://tailwindcss.com/) - CSS Framework
- [HTMX](https://htmx.org/) - Lightweight JS Library
- [AlpineJS](https://alpinejs.dev/) - Lightweight JS Framework


# SoftUni Bonus Requirements

## ⭐ Bonuses – Up to **15%**

- ✅ At least **10 Unit & Integration Tests**
- **Asynchronous Views**
- **Django REST Capabilities**
- ✅ **Extended Django User Model**
- **Project Deployment**

