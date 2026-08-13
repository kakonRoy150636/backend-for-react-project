from database.session import SessionLocal
from models.user import Admin
from services.auth_service import get_password_hash

def create_admin():
    db = SessionLocal()
    admin_email = "kakonroy150636@gmail.com"
    admin_pass = "kakonroy150636"
    
    # চেক করা যে এডমিন আগে থেকে আছে কিনা
    existing = db.query(Admin).filter(Admin.email == admin_email).first()
    if existing:
        print("Admin already exists!")
        return

    # নতুন এডমিন তৈরি
    new_admin = Admin(
        email=admin_email,
        hashed_password=get_password_hash(admin_pass),
        role="admin"
    )
    db.add(new_admin)
    db.commit()
    print("Admin created successfully! Email: admin@example.com, Pass: password123")

if __name__ == "__main__":
    create_admin()