from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import (
    PersonalInfo, Skill, Project, Experience, 
    Education, Certification, Contact, BlogPost
)
from .forms import ContactForm

def home(request):
    """Home page view with all portfolio information"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_projects = Project.objects.exclude(featured=True)[:6]
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'featured_projects': featured_projects,
        'recent_projects': recent_projects,
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    """About page view"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certifications = Certification.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    """Projects listing page"""
    projects_list = Project.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        projects_list = projects_list.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(technologies__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(projects_list, 9)
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    context = {
        'projects': projects_page,
        'search_query': search_query,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, project_id):
    """Individual project detail page"""
    project = get_object_or_404(Project, id=project_id)
    
    # Get related projects (same technologies)
    related_projects = Project.objects.filter(
        technologies__in=project.technologies.all()
    ).exclude(id=project.id).distinct()[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    """Contact page with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('portfolio:contact')  # Changed from 'contact' to 'portfolio:contact'
    else:
        form = ContactForm()
    
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    context = {
        'form': form,
        'personal_info': personal_info,
    }
    return render(request, 'portfolio/contact.html', context)

def blog(request):
    """Blog listing page"""
    posts = BlogPost.objects.filter(published=True)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts_page = paginator.get_page(page_number)
    
    context = {
        'posts': posts_page,
        'search_query': search_query,
    }
    return render(request, 'portfolio/blog.html', context)

def blog_detail(request, slug):
    """Individual blog post detail page"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    
    # Get related posts
    related_posts = BlogPost.objects.filter(published=True).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'portfolio/blog_detail.html', context)

def skills(request):
    """Skills page with detailed skill information"""
    skills = Skill.objects.all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skill_categories:
            skill_categories[category] = []
        skill_categories[category].append(skill)
    
    context = {
        'skill_categories': skill_categories,
    }
    return render(request, 'portfolio/skills.html', context)
