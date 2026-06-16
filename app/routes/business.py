from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from app.models import BusinessCreate, BusinessResponse
from app.services.business import BusinessService
from app.services.analytics import AnalyticsService
from supabase import Client

router = APIRouter()

@router.post("/", response_model=BusinessResponse)
async def create_business(business: BusinessCreate, db: Client = Depends(get_db)):
    """Create a new business"""
    try:
        result = await BusinessService.create_business(business, db)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{business_id}", response_model=BusinessResponse)
async def get_business(business_id: str, db: Client = Depends(get_db)):
    """Get business details"""
    try:
        result = await BusinessService.get_business(business_id, db)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

@router.put("/{business_id}", response_model=BusinessResponse)
async def update_business(business_id: str, business_data: dict, db: Client = Depends(get_db)):
    """Update business details"""
    try:
        result = await BusinessService.update_business(business_id, business_data, db)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/owner/{owner_id}")
async def get_owner_businesses(owner_id: str, db: Client = Depends(get_db)):
    """Get all businesses owned by a user"""
    try:
        result = await BusinessService.get_owner_businesses(owner_id, db)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{business_id}/stats")
async def get_business_stats(business_id: str, days: int = 30, db: Client = Depends(get_db)):
    """Get business statistics"""
    try:
        booking_stats = await AnalyticsService.get_booking_stats(business_id, db, days)
        revenue_stats = await AnalyticsService.get_revenue_stats(business_id, db, days)
        popular_services = await AnalyticsService.get_popular_services(business_id, db, days)
        
        return {
            "booking_stats": booking_stats,
            "revenue_stats": revenue_stats,
            "popular_services": popular_services
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
