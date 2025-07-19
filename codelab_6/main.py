from fastapi import FastAPI
from routers import users, items
from scalar_fastapi import get_scalar_api_reference
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="FastAPI Example",
    version="0.1.0",
    description="A beginner-friendly FastAPI project with routers, services, and docs."
)

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )

def custom_openapi():
    """
    Customize and cache the OpenAPI schema, injecting a logo and extra HTML metadata.
    """
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    schema["info"]["x-logo"] = {"url": "https://icons.veryicon.com/png/o/internet--web/internet-simple-icon/api-management.png"}
    # Add HTML links in description
    schema["info"]["description"] += "\n\n<a href='/docs'>Swagger UI</a> | <a href='/redoc'>ReDoc</a> | <a href='/scalar'>Scalar</a>"
    app.openapi_schema = schema
    return schema

app.openapi = custom_openapi