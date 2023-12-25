from .app import create_app

app, mongo = create_app()

from app import ocr_routes
