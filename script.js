// Mobile Navigation
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}));

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar background on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// Active navigation link highlighting
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === current) {
            link.classList.add('active');
        }
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Add animation classes and observe elements
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = document.querySelectorAll('.skill-category, .project-card, .highlight-item, .stat-item, .contact-item');
    animateElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
});

// Projects Data and Management
let projects = [
    {
        id: 1,
        title: "Real-time Data Pipeline with Apache Kafka",
        description: "Built a scalable real-time data pipeline processing 1M+ events per hour using Apache Kafka, Spark Streaming, and Elasticsearch. Implemented data validation, transformation, and storage with 99.9% uptime.",
        technologies: ["Apache Kafka", "Spark Streaming", "Elasticsearch", "Python", "Docker"],
        category: "data-engineering",
        link: "https://example.com/project1",
        github: "https://github.com/vandna-thakur/kafka-pipeline"
    },
    {
        id: 2,
        title: "Customer Churn Prediction Model",
        description: "Developed a machine learning model to predict customer churn with 87% accuracy using ensemble methods. Implemented feature engineering, model selection, and deployed using AWS SageMaker.",
        technologies: ["Python", "Scikit-learn", "AWS SageMaker", "Pandas", "XGBoost"],
        category: "machine-learning",
        link: "https://example.com/project2",
        github: "https://github.com/vandna-thakur/churn-prediction"
    },
    {
        id: 3,
        title: "E-commerce Analytics Dashboard",
        description: "Created an interactive analytics dashboard for e-commerce data using Tableau and Python. Provides real-time insights into sales trends, customer behavior, and inventory management.",
        technologies: ["Tableau", "Python", "SQL", "PostgreSQL", "AWS"],
        category: "analytics",
        link: "https://example.com/project3",
        github: "https://github.com/vandna-thakur/ecommerce-dashboard"
    },
    {
        id: 4,
        title: "Distributed Data Warehouse on AWS",
        description: "Architected and implemented a cloud-based data warehouse using AWS Redshift, S3, and Glue. Optimized queries for 10TB+ data with automated ETL pipelines and data quality monitoring.",
        technologies: ["AWS Redshift", "AWS S3", "AWS Glue", "Python", "SQL"],
        category: "data-engineering",
        link: "https://example.com/project4",
        github: "https://github.com/vandna-thakur/aws-datawarehouse"
    },
    {
        id: 5,
        title: "Social Media Sentiment Analysis",
        description: "Built a sentiment analysis system for social media data using NLP techniques and deep learning. Processes 50K+ posts daily with real-time sentiment scoring and trend analysis.",
        technologies: ["Python", "NLTK", "TensorFlow", "MongoDB", "Apache Airflow"],
        category: "machine-learning",
        link: "https://example.com/project5",
        github: "https://github.com/vandna-thakur/sentiment-analysis"
    },
    {
        id: 6,
        title: "Supply Chain Optimization Analytics",
        description: "Developed analytics solution for supply chain optimization using advanced statistical methods. Reduced inventory costs by 15% through demand forecasting and route optimization algorithms.",
        technologies: ["R", "Python", "Tableau", "PostgreSQL", "Apache Spark"],
        category: "analytics",
        link: "https://example.com/project6",
        github: "https://github.com/vandna-thakur/supply-chain-analytics"
    }
];

// Project filtering
const filterButtons = document.querySelectorAll('.filter-btn');
const projectsGrid = document.getElementById('projects-grid');

function renderProjects(projectsToRender = projects) {
    projectsGrid.innerHTML = '';
    
    projectsToRender.forEach(project => {
        const projectCard = createProjectCard(project);
        projectsGrid.appendChild(projectCard);
    });

    // Re-observe new elements for animations
    const newCards = projectsGrid.querySelectorAll('.project-card');
    newCards.forEach(card => {
        card.classList.add('fade-in');
        observer.observe(card);
    });
}

function createProjectCard(project) {
    const card = document.createElement('div');
    card.className = 'project-card';
    card.dataset.category = project.category;
    
    const technologiesTags = project.technologies.map(tech => 
        `<span class="tech-tag">${tech}</span>`
    ).join('');
    
    const projectLinks = `
        <div class="project-links">
            ${project.link ? `<a href="${project.link}" target="_blank" rel="noopener" class="project-link primary">
                <i class="fas fa-external-link-alt"></i> Live Demo
            </a>` : ''}
            ${project.github ? `<a href="${project.github}" target="_blank" rel="noopener" class="project-link secondary">
                <i class="fab fa-github"></i> GitHub
            </a>` : ''}
        </div>
    `;
    
    card.innerHTML = `
        <h3>${project.title}</h3>
        <p>${project.description}</p>
        <div class="project-technologies">
            ${technologiesTags}
        </div>
        ${projectLinks}
    `;
    
    return card;
}

// Filter functionality
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        // Filter projects
        const filter = button.dataset.filter;
        const filteredProjects = filter === 'all' 
            ? projects 
            : projects.filter(project => project.category === filter);
        
        // Render filtered projects with animation
        projectsGrid.style.opacity = '0';
        setTimeout(() => {
            renderProjects(filteredProjects);
            projectsGrid.style.opacity = '1';
        }, 200);
    });
});

// Add new project functionality
const projectForm = document.getElementById('project-form');

projectForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const formData = new FormData(projectForm);
    const newProject = {
        id: Date.now(), // Simple ID generation
        title: document.getElementById('project-title').value,
        description: document.getElementById('project-description').value,
        technologies: document.getElementById('project-technologies').value
            .split(',').map(tech => tech.trim()).filter(tech => tech),
        category: document.getElementById('project-category').value,
        link: document.getElementById('project-link').value || null,
        github: document.getElementById('project-github').value || null
    };
    
    // Add to projects array
    projects.unshift(newProject); // Add to beginning
    
    // Re-render projects
    renderProjects();
    
    // Reset form
    projectForm.reset();
    
    // Show success message
    showNotification('Project added successfully!', 'success');
    
    // Scroll to projects section
    document.getElementById('projects').scrollIntoView({ behavior: 'smooth' });
});

// Contact form handling
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Get form data
    const formData = new FormData(contactForm);
    const contactData = {
        name: formData.get('name'),
        email: formData.get('email'),
        subject: formData.get('subject'),
        message: formData.get('message')
    };
    
    // Simulate form submission (in real implementation, you would send this to a server)
    console.log('Contact form submitted:', contactData);
    
    // Show success message
    showNotification('Message sent successfully! I\'ll get back to you soon.', 'success');
    
    // Reset form
    contactForm.reset();
});

// Notification system
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        </div>
    `;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : '#3b82f6'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        transform: translateX(400px);
        transition: transform 0.3s ease;
        max-width: 400px;
    `;
    
    const content = notification.querySelector('.notification-content');
    content.style.cssText = `
        display: flex;
        align-items: center;
        gap: 0.5rem;
    `;
    
    const closeBtn = notification.querySelector('.notification-close');
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        margin-left: auto;
        padding: 0;
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        removeNotification(notification);
    }, 5000);
    
    // Close button functionality
    closeBtn.addEventListener('click', () => {
        removeNotification(notification);
    });
}

function removeNotification(notification) {
    notification.style.transform = 'translateX(400px)';
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 300);
}

// Typing animation for hero subtitle
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing animation when page loads
document.addEventListener('DOMContentLoaded', () => {
    const heroSubtitle = document.querySelector('.hero-subtitle');
    if (heroSubtitle) {
        setTimeout(() => {
            typeWriter(heroSubtitle, 'Big Data Professional', 150);
        }, 1000);
    }
    
    // Initialize projects display
    renderProjects();
});

// Parallax effect for hero section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    
    if (hero) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translateY(${rate}px)`;
    }
});

// Smooth reveal animations for stats
function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-item h3');
    
    statNumbers.forEach(stat => {
        const finalNumber = parseInt(stat.textContent);
        let currentNumber = 0;
        const increment = finalNumber / 50;
        const timer = setInterval(() => {
            currentNumber += increment;
            if (currentNumber >= finalNumber) {
                stat.textContent = finalNumber + (stat.textContent.includes('+') ? '+' : '');
                clearInterval(timer);
            } else {
                stat.textContent = Math.floor(currentNumber) + (stat.textContent.includes('+') ? '+' : '');
            }
        }, 50);
    });
}

// Trigger stats animation when about section is visible
const aboutSection = document.querySelector('.about');
if (aboutSection) {
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateStats();
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    statsObserver.observe(aboutSection);
}

// Add loading animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// Add CSS for loading animation
const loadingStyles = `
    body:not(.loaded) {
        overflow: hidden;
    }
    
    body:not(.loaded)::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    body:not(.loaded)::after {
        content: 'Loading...';
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        z-index: 10001;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
`;

// Add the loading styles to the page
const styleSheet = document.createElement('style');
styleSheet.textContent = loadingStyles;
document.head.appendChild(styleSheet);
