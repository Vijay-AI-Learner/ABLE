from fastapi import APIRouter, Depends

from app.core.roles import require_role

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/")
def admin_dashboard(
    current_user=Depends(require_role("admin"))
):
    return {
        "message": "Welcome Admin"
    }