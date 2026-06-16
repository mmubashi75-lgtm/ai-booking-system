from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timedelta
from app.database import get_db
from app.utils.notifications import send_booking_reminder

scheduler = AsyncIOScheduler()

async def check_upcoming_bookings():
    """Check for upcoming bookings and send reminders"""
    try:
        db = await get_db()
        
        # Get bookings in the next 24 hours
        tomorrow = (datetime.utcnow() + timedelta(hours=24)).isoformat()
        today = datetime.utcnow().isoformat()
        
        bookings = db.table("bookings").select("*").gte("start_time", today).lte("start_time", tomorrow).execute()
        
        for booking in bookings.data:
            if booking.get('status') == 'confirmed':
                await send_booking_reminder(booking, hours_before=24)
    except Exception as e:
        print(f"Error checking bookings: {str(e)}")

def start_scheduler():
    """Start the background scheduler"""
    # Check for upcoming bookings every hour
    scheduler.add_job(
        check_upcoming_bookings,
        CronTrigger(minute=0),
        id='check_bookings',
        name='Check upcoming bookings',
        replace_existing=True
    )
    
    scheduler.start()
