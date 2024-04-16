# djazz!

A ready-to-use Django project tailored for practical, real-world applications, djazz comes with pre-configured essential
settings and industry best practices built-in, ensuring a streamlined development process right out of the box. Ideal
for developers looking to jumpstart their projects without the hassle of initial setup.

## Features

- **Django ^5.0.**: The latest version of Django, the web framework for perfectionists with deadlines.
- **PostgreSQL**: The world's most advanced open-source relational database.
- **Powered by Docker**: Dockerized development environment for easy setup and deployment.
- **Built-in User Authentication and Authorization**: Fully functional user authentication and authorization system
  included.
- **Custom User Model**: A custom user model is provided out of the box.
- **Built-in API**: A RESTful API (both django rest framework and django ninja) is included for easy integration with
  frontend frameworks.
- **Django Debug Toolbar**: For easy debugging and performance optimization.
- **And much more!**

## Quick Start

### Experience `djazz` in production ? 🚀

- **[Live Demo](#)** - Coming soon! 🚧
- **[Documentation](#)** - Coming soon! 🚧
- **[Download Latest Release](#)** - Coming soon! 🚧
- **[Report a Bug](https://github.com/azataiot/djazz/issues)** - Open an issue if you find a bug. 🐞
- **[Request a Feature](https://github.com/azataiot/djazz/issues)** - Open an issue if you want to request a feature. 🚀
- **[Contribute](https://github.com/azataiot/djazz/issues)** - Open a pull request if you want to contribute. 🎉

### Local Development

1. Star (⭐️) and Fork 🍴 the repository.
2. Clone the repository.
    ```bash
    git clone <your-github-username> djazz
    ```
3. Change the directory.
    ```bash
    cd djazz
    ```
4. Create a new virtual environment.
    ```bash
    python -m venv venv
    ```
5. Activate the virtual environment.
    ```bash
    source venv/bin/activate
    ```
6. Install the dependencies.
    ```bash
    pip install -r requirements.txt
    ```
7. Run the PostgreSQL and Redis services using Docker.
    ```bash
    docker-compose up -d
    ```
8. Apply the migrations.
    ```bash
    python manage.py migrate
    ```
9. Run the development server.
   ```bash
   python manage.py runserver
   ```
10. Open the browser and visit `http://localhost:8000/`.
11. You're all set! 🚀