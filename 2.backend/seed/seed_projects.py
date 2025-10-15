from app import create_app, db
from app.models.project import Project
from datetime import datetime

# Create app context
app = create_app()

with app.app_context():
    # Clear existing projects (optional)
    db.session.query(Project).delete()

    # Define seed data
    projects = [
        Project(
            title="Website Redesign",
            description="A complete revamp of the client website with modern UI/UX principles.",
            budget=5000.00,
            status="open",
            client_id=2,
            freelancer_id=7
        ),
        Project(
            title="Mobile App Development",
            description="Develop a cross-platform mobile application for online shopping.",
            budget=12000.00,
            status="in_progress",
            client_id=2,
            freelancer_id=5
        ),
        Project(
            title="Logo and Brand Design",
            description="Create a new logo and visual identity for a startup company.",
            budget=1500.00,
            status="completed",
            client_id=2,
            freelancer_id=6
        ),
        Project(
            title="E-commerce Platform Backend",
            description="Build a secure backend API for an e-commerce platform.",
            budget=8000.00,
            status="open",
            client_id=3,
            freelancer_id=1
        ),
        Project(
            title="SEO Optimization",
            description="Improve website ranking and search engine performance.",
            budget=2000.00,
            status="in_progress",
            client_id=3,
            freelancer_id=5
        ),
        Project(
            title="Portfolio Website",
            description="Develop a personal portfolio site for a creative professional.",
            budget=2500.00,
            status="completed",
            client_id=3,
            freelancer_id=6
        ),
        Project(
            title="Data Analytics Dashboard",
            description="Build a dashboard to visualize company sales and user metrics.",
            budget=7000.00,
            status="open",
            client_id=2,
            freelancer_id=7
        ),
        Project(
            title="Cloud Migration Project",
            description="Migrate on-premise systems to AWS cloud infrastructure.",
            budget=15000.00,
            status="in_progress",
            client_id=3,
            freelancer_id=1
        ),
    ]

    # Add to DB
    db.session.add_all(projects)
    db.session.commit()

    print("✅ Seeded 8 projects successfully!")
