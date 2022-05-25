from fastapi import APIRouter, Depends
from fastapi import status

from main_app.src.core.settings import ADMIN_TOKEN
from main_app.src.features.accounts.common.auth import JWTBearer
from main_app.src.features.data.schema import OSMQuery
from main_app.src.features.data.utils import data_to_db

route = APIRouter(tags=['data'], prefix='/data')


@route.post('/add-data', dependencies=[Depends(JWTBearer(credentials_type=ADMIN_TOKEN))])
def add_data(osm_query: OSMQuery):
    data_to_db(**dict(osm_query))
    return {"status": status.HTTP_200_OK, "message": f"Data for query {dict(osm_query)} added"}
