import reflex as rx
from typing import TypedDict, List
import re
import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno
load_dotenv()

class ModuleHighlight(TypedDict):
    icon: str
    title: str
    description: str


class TestimonialEntry(TypedDict):
    name: str
    role: str
    organization: str
    quote: str
    avatar_seed: str


class PricingTier(TypedDict):
    name: str
    price: str
    description: str
    features: List[str]
    is_popular: bool
    cta_text: str


def is_valid_email(email: str) -> bool:
    pattern = (
        "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    )
    return bool(re.match(pattern, email))


class LandingState(rx.State):
    # Estados para el formulario
    email: str = ""
    is_loading: bool = False
    message: str = ""
    message_type: str = "info"  # success, error, info
    
    # Estados originales del toast
    email_input: str = ""
    show_toast: bool = False
    toast_message: str = ""
    toast_status: str = "success"
    selected_module_for_toast: str = ""
    
    # Datos estáticos
    module_highlights_data: list[ModuleHighlight] = [
        {
            "icon": "file-signature",
            "title": "Monitoreo de Contratación",
            "description": "Vigilancia estratégica de la contratación pública, promoviendo el cumplimiento y la rendición de cuentas.",
        },
        {
            "icon": "clipboard-check",
            "title": "Seguimiento al Plan de Desarrollo",
            "description": "Seguimiento y Evaluación del Plan de Desarrollo.",
        },
        {
            "icon": "map",
            "title": "Observatorios Inteligentes",
            "description": "Visualiza datos clave en tiempo real para fortalecer la planeación y gestión institucional.",
        },
        {
            "icon": "bar-chart-big",
            "title": "Enfoque en inteligencia institucional",
            "description": "Moderniza la toma de decisiones con herramientas basadas en datos y análisis automatizado.",
        },
    ]
    testimonials_data: list[TestimonialEntry] = [
        {
            "name": "Mayor Jane Smith",
            "role": "City of Progressville",
            "organization": "Progressville City Hall",
            "quote": "CiviData transformed how we approach urban development, making our processes more efficient and transparent.",
            "avatar_seed": "jane_smith",
        },
        {
            "name": "Dr. Alistair Finch",
            "role": "Head of Urban Planning, New Harmony County",
            "organization": "New Harmony County",
            "quote": "The geoportals are an invaluable tool for community engagement and data visualization.",
            "avatar_seed": "alistair_finch",
        },
        {
            "name": "Maria Gonzalez",
            "role": "Chief Procurement Officer, Civic Solutions Hub",
            "organization": "Civic Solutions Hub",
            "quote": "Contract monitoring with CiviData has significantly improved our compliance and saved public funds.",
            "avatar_seed": "maria_gonzalez",
        },
    ]
    pricing_tiers_data: list[PricingTier] = [
        {
            "name": "Community",
            "price": "$99",
            "description": "For small municipalities and local agencies.",
            "features": [
                "1 Core Module Access",
                "Basic Data Analytics",
                "Community Support",
                "50GB Data Storage",
            ],
            "is_popular": False,
            "cta_text": "Get Started",
        },
        {
            "name": "District",
            "price": "$499",
            "description": "For growing cities and regional authorities.",
            "features": [
                "3 Core Modules Access",
                "Advanced Data Analytics",
                "Priority Email Support",
                "250GB Data Storage",
                "User Roles & Permissions",
            ],
            "is_popular": True,
            "cta_text": "Choose Plan",
        },
        {
            "name": "Metropolis",
            "price": "Custom",
            "description": "Tailored solutions for large urban centers and governments.",
            "features": [
                "All Modules & Custom Solutions",
                "Predictive Analytics Suite",
                "Dedicated Account Manager",
                "Unlimited Data Storage",
                "Custom Integrations & APIs",
            ],
            "is_popular": False,
            "cta_text": "Contact Sales",
        },
    ]

    @rx.event
    def set_email(self, email: str):
        """Actualizar el valor del email"""
        self.email = email
        self.message = ""  # Limpiar mensaje previo

    def _get_supabase_client(self) -> Client:
        """Crear cliente de Supabase"""
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError("Faltan las credenciales de Supabase en el archivo .env")
        
        return create_client(supabase_url, supabase_key)

    @rx.event
    async def handle_demo_request(self, form_data: dict):
        """Manejar la solicitud de demo y guardar en Supabase"""
        email = form_data.get("email", "") or self.email
        
        # Validar email
        if not email or not is_valid_email(email):
            self.message = "Por favor ingresa un correo electrónico válido."
            self.message_type = "error"
            return
        
        # Mostrar estado de carga
        self.is_loading = True
        self.message = ""
        
        try:
            # Conectar con Supabase
            supabase = self._get_supabase_client()
            
            # Insertar email en la base de datos
            result = supabase.table("email_subscribers").insert({
                "email": email,
                "source": "landing_page_demo",
                "subscribed_at": datetime.datetime.now().isoformat()
            }).execute()
            
            # Éxito
            self.message = "¡Gracias por tu interés! Te contactaremos pronto para agendar tu demostración de CiviData."
            self.message_type = "success"
            self.email = ""  # Limpiar campo
            
            print(f"✅ Email guardado exitosamente: {email}")
            
        except Exception as e:
            # Manejar errores específicos
            error_message = str(e).lower()
            
            if "duplicate key" in error_message or "unique constraint" in error_message:
                self.message = "Este correo ya está registrado. Te contactaremos pronto."
                self.message_type = "error"
            elif "network" in error_message or "connection" in error_message:
                self.message = "Error de conexión. Por favor intenta de nuevo."
                self.message_type = "error"
            else:
                self.message = "Hubo un problema al procesar tu solicitud. Intenta de nuevo."
                self.message_type = "error"
            
            print(f"❌ Error al guardar email: {e}")
        
        finally:
            self.is_loading = False

    @rx.event
    def handle_pricing_cta_click(self, tier_name: str):
        self.toast_message = f"Interested in the {tier_name} plan for CiviData? Please request a demo or contact sales to proceed."
        self.toast_status = "success"
        self.show_toast = True
        yield rx.call_script(
            "document.getElementById('cta').scrollIntoView({ behavior: 'smooth' });"
        )

    @rx.event
    def hide_toast(self):
        self.show_toast = False

    @rx.event
    def set_email_input(self, value: str):
        self.email_input = value

    @rx.var
    def current_year(self) -> int:
        return datetime.date.today().year