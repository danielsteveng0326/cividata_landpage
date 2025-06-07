import reflex as rx
import os

config = rx.Config(
    app_name="cividata_company_landing_page",
    frontend_port=int(os.environ.get("PORT", 3000)),
    backend_port=int(os.environ.get("PORT", 3000)),
    api_url=f"https://{os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost:3000')}",
    deploy_url=f"https://{os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'localhost:3000')}",
)