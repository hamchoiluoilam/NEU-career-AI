from fastapi import APIRouter
from app.schemas.curriculum import CurriculumListResponse
from app.services.curriculum_service import curriculum_service

router = APIRouter(prefix="/curriculum", tags=["Chương trình đào tạo NEU"])

@router.get("", response_model=CurriculumListResponse, summary="Lấy danh mục các môn học của NEU")
async def get_neu_curriculum():
    courses = curriculum_service.get_all_courses()
    return CurriculumListResponse(total=len(courses), courses=courses)
