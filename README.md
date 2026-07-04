# 🚀 Mohsin Ali — Developer Portfolio

A modern, animated personal portfolio website built with **Django**. Features a sleek dark theme with gradient accents, smooth transitions, 
and a fully responsive layout — designed to showcase skills, projects, and contact information in a clean and professional way.


---


## 📌 About the Project

This is a single-page portfolio website built using the **Django** web framework. It's designed for developers who want a fast,
lightweight, and visually appealing portfolio without relying on heavy front-end frameworks. All content — name, role, skills, and 
projects — is rendered dynamically through Django's templating engine, making it easy to update without touching the HTML structure.

---

## ✨ Features

- 🎨 **Modern dark theme** with blue, cyan, and violet gradient accents
- 🌀 **Smooth animations** — rotating gradient avatar ring, glowing pulse indicator, floating background glows, and hover transitions
- 📱 **Fully responsive** — looks great on desktop, tablet, and mobile
- ⚡ **Dynamic content** — skills and projects are rendered from a Python context (no hardcoded HTML)
- 🧩 **Clean project structure** — easy to extend with new sections, pages, or a database-backed model
- 🔤 **Custom typography** — Sora & Space Grotesk fonts for a modern, technical feel
- 📧 **Direct contact link** — one-click email via `mailto:`

---

## 🛠 Tech Stack

| Layer      | Technology                          |
|------------|--------------------------------------|
| Backend    | Python, Django                      |
| Frontend   | HTML5, CSS3 (custom, no framework)  |
| Fonts      | Google Fonts — Sora, Space Grotesk  |
| Templating | Django Template Language (DTL)      |

---

## 📁 Project Structure

```
prettysite/
├── manage.py                      # Django management script
├── prettysite/                    # Project configuration
│   ├── __init__.py
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
└── core/                          # Main application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py                   # Portfolio content & logic
    ├── urls.py                    # App-level URL routing
    ├── migrations/
    ├── templates/
    │   └── core/
    │       └── index.html         # Main portfolio page
    └── static/
        └── core/
            └── css/
                └── style.css      # All styling & animations
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- pip (comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/mohsin-portfolio.git
   cd mohsin-portfolio/prettysite
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # Activate it
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

### Running the Server

```bash
python manage.py migrate
python manage.py runserver
```

Then open your browser and visit:

```
http://127.0.0.1:8000/
```

> ⚠️ **Note:** Make sure you `cd` into the folder that directly contains `manage.py` before running the command above.

---

## 🎨 Customization

All personal content lives in **`core/views.py`** — update the `context` dictionary to change:

```python
context = {
    "name": "Your Name",
    "role": "Your Role / Title",
    "tagline": "A short line about you.",
    "skills": [...],      # Add/edit skill cards
    "projects": [...],    # Add/edit project cards
    "contact_email": "you@example.com",
}
```

To change the color theme, edit the CSS variables at the top of **`core/static/core/css/style.css`**:

```css
:root {
    --bg: #0a0e17;
    --blue: #3b82f6;
    --cyan: #22d3ee;
    --violet: #7c6cf6;
    /* ... */
}
```

---

## 🖼 Screenshots

> Add screenshots of your live site here once deployed.

```
![Homepage](screenshots/homepage.png)
![Projects Section](screenshots/projects.png)
```

---

## 🗺 Roadmap

- [ ] Add a working contact form (Django forms + email backend)
- [ ] Add a blog section
- [ ] Connect projects to a database model with an admin-editable interface
- [ ] Deploy to production (Render / Railway / PythonAnywhere)
- [ ] Add dark/light theme toggle

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it for your own portfolio.

---

## Authar

**Mohsin Ali**


---

<p align="center">Made with ❤️ using Django</p>
