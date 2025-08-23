from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from portfolio.models import (
    PersonalInfo, Skill, Project, Experience, 
    Education, Certification, Contact, BlogPost
)

class Command(BaseCommand):
    help = 'Populate the database with sample data for Jamuna Yadav portfolio'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data for Jamuna Yadav portfolio...')
        
        # Create Personal Info
        personal_info, created = PersonalInfo.objects.get_or_create(
            name="Jamuna Yadav",
            defaults={
                'title': "Senior Data Engineer",
                'email': "jamuna.yadav@example.com",
                'phone': "+1 (555) 123-4567",
                'location': "San Francisco, CA",
                'linkedin': "https://linkedin.com/in/jamunayadav",
                'github': "https://github.com/jamunayadav",
                'website': "https://jamunayadav.dev",
                'about_me': """I am a passionate and experienced Data Engineer with over 5 years of expertise in building scalable data solutions. My journey in data engineering began with a fascination for transforming raw data into actionable insights that drive business decisions.

Throughout my career, I have successfully designed and implemented data pipelines, ETL processes, and data warehousing solutions for various industries including e-commerce, healthcare, and fintech. I specialize in cloud-based data architectures, real-time data processing, and machine learning pipeline development.

My technical expertise includes Python, SQL, Apache Spark, Apache Kafka, AWS, and various data warehousing technologies. I am committed to staying current with the latest technologies and best practices in the rapidly evolving data landscape.

When I'm not building data solutions, I enjoy contributing to open-source projects, writing technical blogs, and mentoring aspiring data engineers.""",
                'summary': "Passionate Data Engineer with expertise in building scalable data pipelines, ETL processes, and data warehousing solutions. Transforming raw data into actionable insights that drive business decisions."
            }
        )
        
        if created:
            self.stdout.write(f'Created Personal Info for {personal_info.name}')
        
        # Create Skills
        skills_data = [
            # Programming Languages
            {'name': 'Python', 'category': 'programming', 'proficiency': 95, 'icon': 'fab fa-python'},
            {'name': 'SQL', 'category': 'programming', 'proficiency': 90, 'icon': 'fas fa-database'},
            {'name': 'Scala', 'category': 'programming', 'proficiency': 85, 'icon': 'fas fa-code'},
            {'name': 'Java', 'category': 'programming', 'proficiency': 80, 'icon': 'fab fa-java'},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 90, 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-leaf'},
            {'name': 'Redis', 'category': 'database', 'proficiency': 80, 'icon': 'fas fa-memory'},
            {'name': 'Snowflake', 'category': 'database', 'proficiency': 88, 'icon': 'fas fa-snowflake'},
            
            # Cloud Platforms
            {'name': 'AWS', 'category': 'cloud', 'proficiency': 92, 'icon': 'fab fa-aws'},
            {'name': 'Azure', 'category': 'cloud', 'proficiency': 85, 'icon': 'fab fa-microsoft'},
            {'name': 'GCP', 'category': 'cloud', 'proficiency': 80, 'icon': 'fab fa-google'},
            
            # Tools & Technologies
            {'name': 'Apache Spark', 'category': 'tools', 'proficiency': 90, 'icon': 'fas fa-fire'},
            {'name': 'Apache Kafka', 'category': 'tools', 'proficiency': 85, 'icon': 'fas fa-stream'},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 88, 'icon': 'fab fa-docker'},
            {'name': 'Kubernetes', 'category': 'tools', 'proficiency': 82, 'icon': 'fas fa-cube'},
            {'name': 'Airflow', 'category': 'tools', 'proficiency': 90, 'icon': 'fas fa-wind'},
            
            # Soft Skills
            {'name': 'Problem Solving', 'category': 'soft', 'proficiency': 95, 'icon': 'fas fa-lightbulb'},
            {'name': 'Communication', 'category': 'soft', 'proficiency': 90, 'icon': 'fas fa-comments'},
            {'name': 'Leadership', 'category': 'soft', 'proficiency': 85, 'icon': 'fas fa-users'},
            {'name': 'Project Management', 'category': 'soft', 'proficiency': 88, 'icon': 'fas fa-tasks'},
        ]
        
        skills = []
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            skills.append(skill)
            if created:
                self.stdout.write(f'Created skill: {skill.name}')
        
        # Create Projects
        projects_data = [
            {
                'title': 'Real-time ETL Pipeline for E-commerce',
                'short_description': 'Built a real-time data pipeline processing 1M+ events daily for an e-commerce platform.',
                'description': """Designed and implemented a real-time ETL pipeline that processes over 1 million events daily for a major e-commerce platform. The solution uses Apache Kafka for event streaming, Apache Spark for data processing, and Snowflake for data warehousing.

Key achievements:
- Reduced data processing time by 60%
- Improved data quality with automated validation
- Implemented real-time monitoring and alerting
- Achieved 99.9% uptime over 12 months""",
                'featured': True,
                'github_url': 'https://github.com/jamunayadav/ecommerce-etl',
                'live_url': 'https://demo.jamunayadav.dev/ecommerce-etl',
                'technologies': ['Python', 'Apache Kafka', 'Apache Spark', 'Snowflake', 'Docker']
            },
            {
                'title': 'Healthcare Data Analytics Platform',
                'short_description': 'Developed a comprehensive analytics platform for healthcare data with HIPAA compliance.',
                'description': """Built a comprehensive healthcare data analytics platform that processes patient data while maintaining HIPAA compliance. The platform includes data ingestion, transformation, and visualization components.

Features:
- HIPAA-compliant data processing
- Real-time patient monitoring dashboards
- Predictive analytics for patient outcomes
- Automated reporting system
- Integration with multiple EHR systems""",
                'featured': True,
                'github_url': 'https://github.com/jamunayadav/healthcare-analytics',
                'technologies': ['Python', 'PostgreSQL', 'Apache Airflow', 'AWS', 'Tableau']
            },
            {
                'title': 'Machine Learning Pipeline for Fraud Detection',
                'short_description': 'Created an ML pipeline for real-time fraud detection in financial transactions.',
                'description': """Developed a machine learning pipeline for real-time fraud detection in financial transactions. The system processes millions of transactions daily and provides real-time risk scoring.

Technical highlights:
- Real-time feature engineering
- Model training and deployment automation
- A/B testing framework for model validation
- Real-time scoring API
- Comprehensive monitoring and alerting""",
                'featured': True,
                'github_url': 'https://github.com/jamunayadav/fraud-detection-ml',
                'technologies': ['Python', 'Apache Spark', 'MLflow', 'Kubernetes', 'Redis']
            },
            {
                'title': 'Data Lake Architecture for IoT',
                'short_description': 'Designed and implemented a scalable data lake for IoT sensor data processing.',
                'description': """Architected and implemented a scalable data lake solution for processing IoT sensor data from multiple sources. The system handles data ingestion, storage, and analytics for millions of sensors.

Architecture components:
- Multi-zone data lake (raw, processed, curated)
- Real-time data ingestion with Apache Kafka
- Batch processing with Apache Spark
- Data governance and cataloging
- Self-service analytics platform""",
                'github_url': 'https://github.com/jamunayadav/iot-data-lake',
                'technologies': ['Python', 'Apache Kafka', 'Apache Spark', 'AWS S3', 'Apache Hive']
            },
            {
                'title': 'Customer 360 Data Platform',
                'short_description': 'Built a unified customer data platform integrating data from 20+ sources.',
                'description': """Developed a Customer 360 data platform that integrates customer data from over 20 different sources including CRM, marketing automation, website analytics, and social media.

Key features:
- Real-time customer profile updates
- Cross-channel attribution modeling
- Customer segmentation and scoring
- Personalized recommendation engine
- GDPR compliance and data governance""",
                'github_url': 'https://github.com/jamunayadav/customer360',
                'technologies': ['Python', 'PostgreSQL', 'Apache Airflow', 'Redis', 'Elasticsearch']
            },
            {
                'title': 'Supply Chain Optimization Analytics',
                'short_description': 'Created analytics solutions for supply chain optimization and demand forecasting.',
                'description': """Built comprehensive analytics solutions for supply chain optimization including demand forecasting, inventory optimization, and route optimization.

Analytics capabilities:
- Time series forecasting models
- Inventory optimization algorithms
- Route optimization for logistics
- Real-time supply chain monitoring
- Predictive maintenance for equipment""",
                'github_url': 'https://github.com/jamunayadav/supply-chain-analytics',
                'technologies': ['Python', 'Apache Spark', 'PostgreSQL', 'Docker', 'Kubernetes']
            }
        ]
        
        for project_data in projects_data:
            technologies = project_data.pop('technologies')
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            
            # Add technologies
            for tech_name in technologies:
                try:
                    tech = Skill.objects.get(name=tech_name)
                    project.technologies.add(tech)
                except Skill.DoesNotExist:
                    pass
            
            if created:
                self.stdout.write(f'Created project: {project.title}')
        
        # Create Experience
        experience_data = [
            {
                'company': 'TechCorp Solutions',
                'position': 'Senior Data Engineer',
                'location': 'San Francisco, CA',
                'start_date': date(2022, 1, 1),
                'current': True,
                'description': """Lead data engineering initiatives for a fast-growing tech company, managing a team of 5 data engineers. Responsible for architecting and implementing scalable data solutions that process over 10TB of data daily.

Key responsibilities:
- Design and implement data architecture for new products
- Lead data engineering team and mentor junior engineers
- Optimize data pipelines for performance and cost
- Collaborate with data science team on ML model deployment
- Establish data governance and quality standards""",
                'achievements': """- Reduced data processing costs by 40% through optimization
- Improved data pipeline reliability to 99.9% uptime
- Successfully migrated legacy systems to cloud infrastructure
- Mentored 3 junior engineers to senior level
- Implemented data quality framework reducing errors by 60%""",
                'technologies_used': ['Python', 'Apache Spark', 'AWS', 'Snowflake', 'Apache Airflow']
            },
            {
                'company': 'DataFlow Inc.',
                'position': 'Data Engineer',
                'location': 'Seattle, WA',
                'start_date': date(2020, 3, 1),
                'end_date': date(2021, 12, 31),
                'description': """Built and maintained data pipelines for a SaaS analytics platform serving 1000+ customers. Worked on real-time data processing, ETL development, and data warehouse optimization.

Key projects:
- Real-time event processing pipeline
- Customer analytics dashboard development
- Data warehouse migration to cloud
- API development for data access
- Performance optimization of existing pipelines""",
                'achievements': """- Built real-time pipeline processing 5M events/hour
- Reduced query response time by 70%
- Successfully migrated data warehouse with zero downtime
- Developed 10+ data APIs used by 50+ teams
- Implemented automated testing reducing bugs by 50%""",
                'technologies_used': ['Python', 'PostgreSQL', 'Apache Kafka', 'Docker', 'Kubernetes']
            },
            {
                'company': 'AnalyticsPro',
                'position': 'Junior Data Engineer',
                'location': 'Austin, TX',
                'start_date': date(2019, 6, 1),
                'end_date': date(2020, 2, 28),
                'description': """Started career as a junior data engineer working on data pipeline development and maintenance. Learned best practices in data engineering and gained hands-on experience with various technologies.

Responsibilities:
- Develop and maintain ETL pipelines
- Data quality monitoring and reporting
- Database administration and optimization
- Support data analysts and scientists
- Documentation and knowledge sharing""",
                'achievements': """- Built 15+ ETL pipelines for different business units
- Improved data quality score from 85% to 95%
- Reduced pipeline failures by 80%
- Created comprehensive documentation for team
- Received 'Rising Star' award for outstanding performance""",
                'technologies_used': ['Python', 'SQL', 'PostgreSQL', 'Apache Airflow', 'Git']
            }
        ]
        
        for exp_data in experience_data:
            technologies = exp_data.pop('technologies_used')
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                start_date=exp_data['start_date'],
                defaults=exp_data
            )
            
            # Add technologies
            for tech_name in technologies:
                try:
                    tech = Skill.objects.get(name=tech_name)
                    experience.technologies_used.add(tech)
                except Skill.DoesNotExist:
                    pass
            
            if created:
                self.stdout.write(f'Created experience: {experience.position} at {experience.company}')
        
        # Create Education
        education_data = [
            {
                'institution': 'Stanford University',
                'degree': 'Master of Science',
                'field_of_study': 'Computer Science',
                'start_date': date(2017, 9, 1),
                'end_date': date(2019, 6, 1),
                'gpa': 3.8,
                'description': 'Specialized in Data Science and Machine Learning. Completed thesis on "Scalable Data Processing for Real-time Analytics".'
            },
            {
                'institution': 'University of California, Berkeley',
                'degree': 'Bachelor of Science',
                'field_of_study': 'Computer Science',
                'start_date': date(2013, 9, 1),
                'end_date': date(2017, 6, 1),
                'gpa': 3.7,
                'description': 'Graduated with honors. Minor in Mathematics. Active member of the Data Science Club and ACM chapter.'
            }
        ]
        
        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                field_of_study=edu_data['field_of_study'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created education: {education.degree} in {education.field_of_study} from {education.institution}')
        
        # Create Certifications
        certifications_data = [
            {
                'name': 'AWS Certified Solutions Architect - Professional',
                'issuing_organization': 'Amazon Web Services',
                'issue_date': date(2023, 3, 15),
                'credential_id': 'AWS-SAA-PRO-123456',
                'credential_url': 'https://aws.amazon.com/verification'
            },
            {
                'name': 'Google Cloud Professional Data Engineer',
                'issuing_organization': 'Google Cloud',
                'issue_date': date(2022, 11, 20),
                'credential_id': 'GCP-DE-789012',
                'credential_url': 'https://cloud.google.com/certification'
            },
            {
                'name': 'Databricks Certified Associate Developer',
                'issuing_organization': 'Databricks',
                'issue_date': date(2022, 8, 10),
                'credential_id': 'DB-ADEV-345678',
                'credential_url': 'https://databricks.com/certification'
            },
            {
                'name': 'Apache Spark Developer Certification',
                'issuing_organization': 'Databricks',
                'issue_date': date(2021, 12, 5),
                'credential_id': 'SPARK-DEV-901234',
                'credential_url': 'https://databricks.com/certification'
            },
            {
                'name': 'Snowflake SnowPro Core Certification',
                'issuing_organization': 'Snowflake',
                'issue_date': date(2021, 6, 20),
                'credential_id': 'SNOW-CORE-567890',
                'credential_url': 'https://snowflake.com/certification'
            }
        ]
        
        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuing_organization=cert_data['issuing_organization'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'Created certification: {certification.name}')
        
        # Create Blog Posts
        blog_posts_data = [
            {
                'title': 'Building Scalable Data Pipelines with Apache Airflow',
                'slug': 'building-scalable-data-pipelines-with-apache-airflow',
                'content': """# Building Scalable Data Pipelines with Apache Airflow

Apache Airflow has become the de facto standard for orchestrating data pipelines in the modern data stack. In this post, I'll share my experience building scalable data pipelines using Airflow and best practices I've learned along the way.

## Why Apache Airflow?

Apache Airflow provides a powerful platform for programmatically authoring, scheduling, and monitoring workflows. Its key advantages include:

- **DAG-based workflow management**: Define complex dependencies between tasks
- **Rich UI**: Monitor and debug pipelines through an intuitive web interface
- **Extensibility**: Custom operators and plugins for specific use cases
- **Scalability**: Horizontal scaling for high-volume workloads

## Best Practices for Scalable Pipelines

### 1. Task Design
- Keep tasks atomic and focused on a single responsibility
- Use appropriate task timeouts and retry policies
- Implement proper error handling and logging

### 2. Resource Management
- Configure appropriate pool sizes for resource-intensive tasks
- Use XCom for small data sharing between tasks
- Implement proper cleanup procedures

### 3. Monitoring and Alerting
- Set up comprehensive monitoring for pipeline health
- Configure alerts for failures and performance issues
- Implement SLA monitoring for critical pipelines

## Example Implementation

Here's a simple example of a data pipeline that processes daily sales data:

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_sales_processing',
    default_args=default_args,
    description='Process daily sales data',
    schedule_interval='0 2 * * *',
    catchup=False
)

def extract_sales_data():
    # Extract data from source systems
    pass

def transform_sales_data():
    # Transform and clean data
    pass

def load_sales_data():
    # Load data into data warehouse
    pass

extract_task = PythonOperator(
    task_id='extract_sales_data',
    python_callable=extract_sales_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_sales_data',
    python_callable=transform_sales_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_sales_data',
    python_callable=load_sales_data,
    dag=dag
)

extract_task >> transform_task >> load_task
```

## Conclusion

Apache Airflow provides a robust foundation for building scalable data pipelines. By following best practices and leveraging its rich ecosystem, you can create reliable and maintainable data workflows that scale with your business needs.

Remember to always monitor your pipelines, implement proper error handling, and continuously optimize for performance and cost efficiency.""",
                'excerpt': 'Learn how to build scalable data pipelines using Apache Airflow with best practices and real-world examples.',
                'published': True
            },
            {
                'title': 'Real-time Data Processing with Apache Kafka and Spark Streaming',
                'slug': 'real-time-data-processing-with-kafka-spark-streaming',
                'content': """# Real-time Data Processing with Apache Kafka and Spark Streaming

Real-time data processing has become essential for modern applications that require immediate insights and actions. In this post, I'll explore how to build real-time data processing systems using Apache Kafka and Spark Streaming.

## Architecture Overview

The typical architecture for real-time data processing includes:

1. **Data Sources**: Applications, IoT devices, logs, etc.
2. **Message Queue**: Apache Kafka for reliable message streaming
3. **Processing Engine**: Spark Streaming for real-time analytics
4. **Storage**: Real-time databases and data lakes
5. **Serving Layer**: APIs and dashboards for real-time insights

## Apache Kafka Setup

Kafka provides a distributed, fault-tolerant streaming platform. Here's how to set up a basic Kafka cluster:

```python
from kafka import KafkaProducer, KafkaConsumer
import json

# Producer setup
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send messages
def send_event(event_data):
    producer.send('user-events', event_data)
    producer.flush()

# Consumer setup
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='spark-streaming-group'
)
```

## Spark Streaming Integration

Spark Streaming provides a high-level API for processing real-time data streams:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RealTimeProcessing") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user-events") \
    .load()

# Parse JSON data
parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Apply transformations
processed_df = parsed_df \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(window("timestamp", "5 minutes"), "user_id") \
    .agg(
        count("*").alias("event_count"),
        sum("amount").alias("total_amount")
    )

# Write to output
query = processed_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
```

## Best Practices

### 1. Fault Tolerance
- Configure proper replication factors in Kafka
- Implement checkpointing in Spark Streaming
- Use idempotent operations where possible

### 2. Performance Optimization
- Tune Kafka partition numbers based on throughput
- Configure appropriate Spark executor resources
- Use structured streaming for better performance

### 3. Monitoring
- Monitor Kafka lag and throughput
- Track Spark Streaming processing times
- Set up alerts for failures and performance issues

## Real-world Example

Here's a complete example of a real-time recommendation system:

```python
# Event producer
def produce_user_events():
    events = [
        {"user_id": 1, "product_id": 100, "action": "view", "timestamp": "2023-01-01T10:00:00Z"},
        {"user_id": 1, "product_id": 101, "action": "purchase", "timestamp": "2023-01-01T10:05:00Z"},
        {"user_id": 2, "product_id": 100, "action": "view", "timestamp": "2023-01-01T10:10:00Z"}
    ]
    
    for event in events:
        send_event(event)

# Real-time processing
def process_user_behavior():
    # Read user events
    events_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "user-events") \
        .load()
    
    # Process events
    user_behavior = events_df \
        .withWatermark("timestamp", "1 hour") \
        .groupBy("user_id", window("timestamp", "30 minutes")) \
        .agg(
            count("*").alias("total_events"),
            sum(when(col("action") == "purchase", 1).otherwise(0)).alias("purchases")
        )
    
    # Generate recommendations
    recommendations = user_behavior \
        .filter(col("purchases") > 0) \
        .select("user_id", "recommendations")
    
    # Write to recommendation service
    query = recommendations \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()
    
    return query
```

## Conclusion

Real-time data processing with Kafka and Spark Streaming enables businesses to make immediate decisions based on current data. By following best practices and implementing proper monitoring, you can build robust real-time systems that scale with your needs.

The key is to start simple and gradually add complexity as your requirements grow.""",
                'excerpt': 'Explore how to build real-time data processing systems using Apache Kafka and Spark Streaming with practical examples.',
                'published': True
            }
        ]
        
        for post_data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {post.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data for Jamuna Yadav portfolio!')
        )
        self.stdout.write('You can now access the admin panel at /admin/')
        self.stdout.write('Default admin credentials: admin / admin (you should change this)')

