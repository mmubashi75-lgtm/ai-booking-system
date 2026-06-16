from datetime import datetime, timedelta
from app.database import get_db
from supabase import Client

class AnalyticsService:
    """Service for business analytics"""
    
    @staticmethod
    async def get_booking_stats(business_id: str, db: Client, days: int = 30) -> dict:
        """Get booking statistics for a business"""
        try:
            date_from = (datetime.utcnow() - timedelta(days=days)).isoformat()
            
            bookings = db.table("bookings").select("*").eq("business_id", business_id).gte("created_at", date_from).execute()
            
            total_bookings = len(bookings.data)
            confirmed = sum(1 for b in bookings.data if b.get('status') == 'confirmed')
            completed = sum(1 for b in bookings.data if b.get('status') == 'completed')
            cancelled = sum(1 for b in bookings.data if b.get('status') == 'cancelled')
            pending = sum(1 for b in bookings.data if b.get('status') == 'pending')
            
            return {
                "total_bookings": total_bookings,
                "confirmed": confirmed,
                "completed": completed,
                "cancelled": cancelled,
                "pending": pending,
                "period_days": days
            }
        except Exception as e:
            raise Exception(f"Error getting booking stats: {str(e)}")
    
    @staticmethod
    async def get_revenue_stats(business_id: str, db: Client, days: int = 30) -> dict:
        """Get revenue statistics for a business"""
        try:
            date_from = (datetime.utcnow() - timedelta(days=days)).isoformat()
            
            # Get all bookings for the business
            bookings = db.table("bookings").select("id").eq("business_id", business_id).gte("created_at", date_from).execute()
            booking_ids = [b["id"] for b in bookings.data]
            
            total_revenue = 0
            completed_revenue = 0
            
            for booking_id in booking_ids:
                payments = db.table("payments").select("*").eq("booking_id", booking_id).execute()
                
                for payment in payments.data:
                    total_revenue += payment.get("amount", 0)
                    if payment.get("status") == "completed":
                        completed_revenue += payment.get("amount", 0)
            
            return {
                "total_revenue": total_revenue,
                "completed_revenue": completed_revenue,
                "average_booking_value": total_revenue / len(booking_ids) if booking_ids else 0,
                "period_days": days
            }
        except Exception as e:
            raise Exception(f"Error getting revenue stats: {str(e)}")
    
    @staticmethod
    async def get_popular_services(business_id: str, db: Client, days: int = 30) -> list:
        """Get most popular services for a business"""
        try:
            date_from = (datetime.utcnow() - timedelta(days=days)).isoformat()
            
            bookings = db.table("bookings").select("service_id").eq("business_id", business_id).gte("created_at", date_from).execute()
            
            service_counts = {}
            for booking in bookings.data:
                service_id = booking.get("service_id")
                service_counts[service_id] = service_counts.get(service_id, 0) + 1
            
            # Sort by count
            sorted_services = sorted(service_counts.items(), key=lambda x: x[1], reverse=True)
            
            result = []
            for service_id, count in sorted_services:
                service = db.table("services").select("*").eq("id", service_id).execute()
                if service.data:
                    service_data = service.data[0]
                    service_data["booking_count"] = count
                    result.append(service_data)
            
            return result
        except Exception as e:
            raise Exception(f"Error getting popular services: {str(e)}")
