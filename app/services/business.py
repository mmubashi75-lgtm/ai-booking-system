from app.database import get_db
from app.models import BusinessCreate, BusinessResponse
from supabase import Client
from datetime import datetime

class BusinessService:
    """Service for business operations"""
    
    @staticmethod
    async def create_business(business: BusinessCreate, db: Client) -> dict:
        """Create a new business"""
        try:
            response = db.table("businesses").insert({
                "owner_id": business.owner_id,
                "name": business.name,
                "description": business.description,
                "phone": business.phone,
                "email": business.email,
                "address": business.address,
                "city": business.city,
                "timezone": business.timezone,
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat()
            }).execute()
            
            return response.data[0]
        except Exception as e:
            raise Exception(f"Error creating business: {str(e)}")
    
    @staticmethod
    async def get_business(business_id: str, db: Client) -> dict:
        """Get business details"""
        try:
            response = db.table("businesses").select("*").eq("id", business_id).execute()
            
            if not response.data:
                raise Exception("Business not found")
            
            return response.data[0]
        except Exception as e:
            raise Exception(f"Error fetching business: {str(e)}")
    
    @staticmethod
    async def update_business(business_id: str, business_data: dict, db: Client) -> dict:
        """Update business details"""
        try:
            business_data["updated_at"] = datetime.utcnow().isoformat()
            response = db.table("businesses").update(business_data).eq("id", business_id).execute()
            
            if not response.data:
                raise Exception("Business not found")
            
            return response.data[0]
        except Exception as e:
            raise Exception(f"Error updating business: {str(e)}")
    
    @staticmethod
    async def get_owner_businesses(owner_id: str, db: Client) -> list:
        """Get all businesses owned by a user"""
        try:
            response = db.table("businesses").select("*").eq("owner_id", owner_id).execute()
            return response.data
        except Exception as e:
            raise Exception(f"Error fetching businesses: {str(e)}")
