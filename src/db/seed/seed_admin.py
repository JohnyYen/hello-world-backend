from src.models.user import User
from src.db.session import AsyncSession
from sqlalchemy import select

async def seed_admin(db : AsyncSession):
    query = select(User).where(User.username == 'superadmin')
    admin = (await db.execute(query)).scalars().first()
    if not admin:
        print("Seeding admin user...")
        admin = User(
            username = 'superadmin',
            name = 'Admin',
            email = 'admin@example.com',
            is_active = True,
            password = 'adminpass',  # In a real scenario, ensure to hash the password
            role_id = 1  # Assuming 1 is the role ID for admin
        )
        db.add(admin)
        print("Seeded admin user: superadmin")