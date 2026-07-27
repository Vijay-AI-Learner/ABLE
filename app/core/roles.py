from fastapi import Depends, HTTPException

from app.core.auth import get_current_user


def require_role(required_role: str):

    def role_checker(current_user=Depends(get_current_user)):
        print("Current User:", current_user.username)
        print("Current Role:", current_user.role)
        print("Required Role:", required_role)

        if current_user.role != required_role:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return current_user

    return role_checker