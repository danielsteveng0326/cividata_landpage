import reflex as rx
from cividata_company_landing_page.components.navbar import navbar
from cividata_company_landing_page.components.hero import hero_section
from cividata_company_landing_page.components.features import features_section
from cividata_company_landing_page.components.pricing import pricing_section
from cividata_company_landing_page.components.testimonials import testimonials_section
from cividata_company_landing_page.components.cta_section import cta_section
from cividata_company_landing_page.components.footer import footer
from cividata_company_landing_page.components.toast import app_toast


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero_section(),
        features_section(),
        pricing_section(),
        testimonials_section(),
        cta_section(),
        footer(),
        app_toast(),
        class_name="font-['Inter'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="anonymous",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index, title="CiviData - Empowering Local Governments"
)