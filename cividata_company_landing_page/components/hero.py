import reflex as rx
from cividata_company_landing_page.states.landing_state import LandingState


def hero_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Empowering Local Governments with ",
                    rx.el.span(
                        "Data-Driven Decisions",
                        class_name="text-teal-600",
                    ),
                    class_name="text-4xl sm:text-5xl md:text-6xl font-extrabold text-gray-900 tracking-tight leading-tight",
                ),
                rx.el.p(
                    "CiviData provides an AI-powered platform for contract monitoring, development plan analysis, and interactive geoportals to build smarter, more responsive communities.",
                    class_name="mt-6 max-w-2xl text-lg sm:text-xl text-gray-600",
                ),
                rx.el.div(
                    rx.el.button(
                        "Request a Demo",
                        on_click=lambda: rx.call_script(
                            "document.getElementById('cta').scrollIntoView({ behavior: 'smooth' });"
                        ),
                        class_name="px-8 py-3 bg-teal-600 text-white text-lg font-semibold rounded-lg shadow-md hover:bg-teal-700 transition-colors transform hover:scale-105",
                    ),
                    rx.el.button(
                        "Explore Modules",
                        on_click=lambda: rx.call_script(
                            "document.getElementById('modules').scrollIntoView({ behavior: 'smooth' });"
                        ),
                        class_name="ml-4 px-8 py-3 bg-transparent text-teal-600 text-lg font-semibold rounded-lg border-2 border-teal-600 hover:bg-teal-50 transition-colors",
                    ),
                    class_name="mt-10 flex flex-col sm:flex-row items-center justify-center sm:justify-start gap-4",
                ),
                class_name="max-w-3xl text-center sm:text-left",
            ),
            rx.el.div(
                rx.image(
                    src="/placeholder.png",
                    alt="CiviData Platform Illustration",
                    class_name="w-full max-w-md lg:max-w-lg rounded-lg shadow-xl",
                ),
                class_name="mt-12 sm:mt-0 flex justify-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center",
        ),
        class_name="bg-gradient-to-br from-teal-50 via-sky-50 to-green-50",
    )