import asyncio
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from database import SessionLocal, Borrowing, User, Equipment

async def read_borrowings():
    async with SessionLocal() as db:
        borrowing_query = (
            select(Borrowing, Equipment, User)
            .join(Equipment, Borrowing.borrowed_item == Equipment.id)
            .join(User, Borrowing.borrowers_id == User.id)
            .where(Borrowing.request_status == "Pending")
            .order_by(Borrowing.created_at.desc())
        )
        res = await db.execute(borrowing_query)
        print("Borrowings count:", len(res.all()))

async def main():
    await read_borrowings()

if __name__ == "__main__":
    asyncio.run(main())
