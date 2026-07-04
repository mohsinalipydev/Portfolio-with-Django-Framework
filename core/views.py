from django.shortcuts import render


def home(request):
    context = {
        "name": "Mohsin Ali",
        "role": "Full-Stack Developer & UI Designer",
        "tagline": "I build fast, modern and reliable digital experiences that people love to use.",
        "skills": [
            {"title": "Web Development", "desc": "Building fast, responsive and scalable websites using modern frameworks like Django, React and Node.js.", "icon": "💻"},
            {"title": "UI/UX Design", "desc": "Designing clean, user-friendly interfaces that balance aesthetics with usability.", "icon": "🎯"},
            {"title": "Backend Engineering", "desc": "Creating robust APIs, databases and server-side logic that power real applications.", "icon": "⚙️"},
            {"title": "Problem Solving", "desc": "Turning complex requirements into simple, efficient and maintainable solutions.", "icon": "🚀"},
        ],
        "projects": [
            {"title": "E-Commerce Platform", "desc": "A full-featured online store with cart, payments and admin dashboard.", "emoji": "🛒"},
            {"title": "Task Manager App", "desc": "A productivity app to organize tasks, deadlines and team collaboration.", "emoji": "📋"},
            {"title": "Portfolio CMS", "desc": "A lightweight content management system for personal portfolios and blogs.", "emoji": "🗂️"},
        ],
        "contact_email": "mohiali1144@gmail.com",
    }
    return render(request, "core/index.html", context)
