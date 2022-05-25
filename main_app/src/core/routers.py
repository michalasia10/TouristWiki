from main_app.src.features.accounts.admin.api import route as admin_router
from main_app.src.features.accounts.user.api import route as user_router
from main_app.src.features.data.api import route as data_router

ROUTERS = [user_router, admin_router, data_router]
