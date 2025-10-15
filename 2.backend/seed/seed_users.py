from wsgi import app  # adjust if your Flask instance is in another file
from app import db
from app.models.user import User

def seed_users():
    with app.app_context():
        print("🌱 Seeding users...")

        # Clear any existing users (optional)
        User.query.delete()

        # Create users
        users = [
            User(
                username="freelancer_jane",
                email="jane.freelancer@example.com",
                role="freelancer",
                bio="Skilled web developer with experience in Flask and React.",
                skills=["Flask", "React", "PostgreSQL"],
                rating=4.8
            ),
            User(
                username="client_anna",
                email="anna.client@example.com",
                role="client",
                bio="Small business owner looking for freelance developers.",
                skills=[],
                rating=None
            ),
            User(
                username="client_mike",
                email="mike.client@example.com",
                role="client",
                bio="Startup founder seeking backend developers for MVP.",
                skills=[],
                rating=None
            ),
            User(
                username="admin_rovenel",
                email="admin@example.com",
                role="admin",
                bio="Platform administrator.",
                skills=[],
                rating=None
            )
        ]

        # Set passwords
        users[0].password = "password123"
        users[1].password = "password123"
        users[2].password = "password123"
        users[3].password = "adminpass"

        # Add to session and commit
        db.session.bulk_save_objects(users)
        db.session.commit()

        print("✅ Users seeded successfully!")

if __name__ == "__main__":
    seed_users()
