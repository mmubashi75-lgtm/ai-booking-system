import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import settings
from datetime import datetime

class EmailNotificationService:
    """Service for sending email notifications"""
    
    def __init__(self):
        self.smtp_server = settings.smtp_server
        self.smtp_port = settings.smtp_port
        self.sender_email = settings.smtp_user
        self.password = settings.smtp_password
    
    def send_email(
        self,
        recipient_email: str,
        subject: str,
        html_body: str,
        text_body: str = None
    ) -> bool:
        """Send email notification"""
        try:
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = recipient_email
            
            if text_body:
                message.attach(MIMEText(text_body, "plain"))
            message.attach(MIMEText(html_body, "html"))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.sendmail(
                    self.sender_email,
                    recipient_email,
                    message.as_string()
                )
            
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False

email_service = EmailNotificationService()

async def send_booking_confirmation(booking: dict):
    """Send booking confirmation email"""
    subject = "Booking Confirmed"
    html_body = f"""
    <h2>Your booking has been confirmed!</h2>
    <p>Booking Details:</p>
    <ul>
        <li>Booking ID: {booking.get('id')}</li>
        <li>Start Time: {booking.get('start_time')}</li>
        <li>Status: {booking.get('status')}</li>
    </ul>
    """
    
    # Get customer email (you'd need to fetch from DB)
    # For now, this is a template
    email_service.send_email(
        recipient_email="customer@example.com",
        subject=subject,
        html_body=html_body
    )

async def send_booking_status_notification(booking: dict):
    """Send booking status change notification"""
    subject = f"Booking {booking.get('status').title()}"
    html_body = f"""
    <h2>Your booking status has changed</h2>
    <p>New Status: {booking.get('status').upper()}</p>
    <p>Booking ID: {booking.get('id')}</p>
    """
    
    email_service.send_email(
        recipient_email="customer@example.com",
        subject=subject,
        html_body=html_body
    )

async def send_booking_reminder(booking: dict, hours_before: int = 24):
    """Send booking reminder email"""
    subject = f"Reminder: Your appointment is in {hours_before} hours"
    html_body = f"""
    <h2>Booking Reminder</h2>
    <p>Your appointment is coming up!</p>
    <p>Start Time: {booking.get('start_time')}</p>
    <p>Booking ID: {booking.get('id')}</p>
    """
    
    email_service.send_email(
        recipient_email="customer@example.com",
        subject=subject,
        html_body=html_body
    )
