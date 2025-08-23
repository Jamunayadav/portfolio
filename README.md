# Jamuna Yadav - Data Engineer Portfolio

A professional, full-stack portfolio website built with Django and Python, showcasing the skills, projects, and experience of Jamuna Yadav, a Senior Data Engineer.

## 🌟 Features

### Core Features
- **Responsive Design**: Modern, mobile-first design using Bootstrap 5
- **Professional Layout**: Clean and professional appearance suitable for a data engineer
- **Dynamic Content**: All content is managed through Django admin panel
- **SEO Optimized**: Proper meta tags, structured data, and clean URLs

### Portfolio Sections
- **Home Page**: Hero section with introduction, featured projects, and skills overview
- **About Page**: Detailed personal information, experience timeline, education, and certifications
- **Projects**: Showcase of data engineering projects with search and filtering
- **Skills**: Comprehensive skills display organized by categories with proficiency levels
- **Blog**: Technical articles and insights about data engineering
- **Contact**: Contact form with validation and social media links

### Technical Features
- **Admin Panel**: Full-featured Django admin for content management
- **Image Management**: Support for profile pictures, project images, and blog post images
- **Search Functionality**: Search projects and blog posts
- **Pagination**: Efficient pagination for projects and blog posts
- **Form Validation**: Client-side and server-side form validation
- **Social Sharing**: Share projects and blog posts on social media
- **Responsive Navigation**: Mobile-friendly navigation with smooth scrolling

## 🛠️ Technology Stack

### Backend
- **Django 5.0.6**: Web framework
- **Python 3.12**: Programming language
- **SQLite**: Database (can be easily changed to PostgreSQL/MySQL for production)

### Frontend
- **Bootstrap 5**: CSS framework for responsive design
- **FontAwesome 6**: Icons
- **Google Fonts**: Typography (Inter font family)
- **Custom CSS**: Modern styling with CSS variables and animations
- **Vanilla JavaScript**: Interactive features and animations

### Additional Packages
- **django-crispy-forms**: Form styling
- **crispy-bootstrap5**: Bootstrap 5 integration for forms
- **Pillow**: Image processing

## 📁 Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── README.md
├── portfolio_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                  # Main app
│   ├── __init__.py
│   ├── admin.py               # Admin interface configuration
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── urls.py                # URL patterns
│   ├── forms.py               # Form definitions
│   └── management/            # Custom management commands
│       └── commands/
│           └── populate_sample_data.py
├── templates/                 # HTML templates
│   ├── base.html
│   └── portfolio/
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── project_detail.html
│       ├── skills.html
│       ├── contact.html
│       ├── blog.html
│       └── blog_detail.html
├── static/                    # Static files
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── media/                     # User-uploaded files
    ├── profile/
    ├── projects/
    ├── certifications/
    └── blog/
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd portfolio
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 7: Populate Sample Data (Optional)
```bash
python manage.py populate_sample_data
```

### Step 8: Run Development Server
```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

## 📊 Database Models

### PersonalInfo
- Basic personal information (name, title, email, phone, location)
- Social media links (LinkedIn, GitHub, website)
- Profile picture
- About me and summary text

### Skill
- Skill name and category (Programming, Database, Cloud, Tools, Soft Skills)
- Proficiency level (1-100)
- Icon class for FontAwesome
- Order for display

### Project
- Project title, description, and short description
- Project image
- GitHub and live demo URLs
- Technologies used (many-to-many with Skill)
- Featured flag and order

### Experience
- Company, position, location
- Start and end dates
- Current position flag
- Description and achievements
- Technologies used

### Education
- Institution, degree, field of study
- Start and end dates
- GPA and description

### Certification
- Certification name and issuing organization
- Issue and expiry dates
- Credential ID and verification URL
- Certification image

### BlogPost
- Title, content, and excerpt
- Slug for SEO-friendly URLs
- Published flag
- Blog post image

### Contact
- Contact form submissions
- Name, email, subject, message
- Read/unread status

## 🎨 Customization

### Colors and Styling
The website uses CSS variables for easy customization. Edit `static/css/style.css`:

```css
:root {
    --primary-color: #0d6efd;
    --secondary-color: #6c757d;
    --success-color: #198754;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --light-color: #f8f9fa;
    --dark-color: #212529;
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Content Management
All content is managed through the Django admin panel at `/admin/`:

1. **Personal Information**: Update your basic info, about me, and social links
2. **Skills**: Add your technical skills with proficiency levels
3. **Projects**: Showcase your data engineering projects
4. **Experience**: Add your work experience with detailed descriptions
5. **Education**: Include your educational background
6. **Certifications**: Add professional certifications
7. **Blog Posts**: Write and publish technical articles

### Adding New Skills
1. Go to Admin Panel → Skills
2. Click "Add Skill"
3. Fill in:
   - Name: Skill name (e.g., "Apache Spark")
   - Category: Choose from dropdown
   - Proficiency: 1-100
   - Icon: FontAwesome class (e.g., "fas fa-fire")
   - Order: Display order

### Adding New Projects
1. Go to Admin Panel → Projects
2. Click "Add Project"
3. Fill in:
   - Title: Project name
   - Description: Detailed project description
   - Short Description: Brief overview
   - Technologies: Select from existing skills
   - GitHub URL: Link to code repository
   - Live URL: Link to live demo (if available)
   - Featured: Check if it's a featured project

## 🔧 Configuration

### Settings
Key settings in `portfolio_project/settings.py`:

```python
# Static and Media Files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```

### Production Deployment
For production deployment:

1. **Change Database**: Replace SQLite with PostgreSQL or MySQL
2. **Set Environment Variables**: Configure SECRET_KEY, DEBUG, ALLOWED_HOSTS
3. **Static Files**: Run `python manage.py collectstatic`
4. **Media Files**: Configure media file serving
5. **Security**: Set DEBUG=False and configure HTTPS

## 📱 Responsive Design

The website is fully responsive and optimized for:
- **Desktop**: Full-featured experience with sidebar navigation
- **Tablet**: Optimized layout with collapsible navigation
- **Mobile**: Mobile-first design with touch-friendly interactions

## 🎯 SEO Features

- Clean, semantic HTML structure
- Meta tags for social sharing
- SEO-friendly URLs with slugs
- Structured data for search engines
- Fast loading times with optimized assets

## 🔒 Security Features

- CSRF protection on all forms
- SQL injection protection through Django ORM
- XSS protection through template escaping
- Secure file upload handling
- Admin panel security

## 📈 Performance

- Optimized database queries
- Efficient pagination
- Compressed static files
- Lazy loading for images
- Minimal JavaScript footprint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support or questions:
- Email: jamuna.yadav@example.com
- LinkedIn: [Jamuna Yadav](https://linkedin.com/in/jamunayadav)
- GitHub: [jamunayadav](https://github.com/jamunayadav)

## 🚀 Future Enhancements

- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Advanced search filters
- [ ] Newsletter subscription
- [ ] Portfolio analytics
- [ ] API endpoints for external integrations
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

**Built with ❤️ by Jamuna Yadav**

*Senior Data Engineer | Python Developer | Data Architecture Specialist*

