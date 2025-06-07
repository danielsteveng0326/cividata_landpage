import reflex as rx
from cividata_company_landing_page.states.landing_state import LandingState


def cta_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "¿Listos para modernizar su entidad con CiviData?",
                    class_name="text-3xl sm:text-4xl font-bold text-white text-center",
                ),
                rx.el.p(
                    "Solicita una demostración personalizada y descubre cómo CiviData puede potenciar tu entidad con inteligencia basada en datos.",
                    class_name="mt-4 text-lg text-teal-100 text-center max-w-2xl mx-auto",
                ),
                # Mensaje de feedback
                rx.cond(
                    LandingState.message != "",
                    rx.el.div(
                        rx.el.p(
                            LandingState.message,
                            class_name="text-center font-medium",
                        ),
                        class_name=rx.cond(
                            LandingState.message_type == "success",
                            "mt-4 p-3 bg-green-100 border border-green-400 text-green-700 rounded-lg max-w-xl mx-auto",
                            rx.cond(
                                LandingState.message_type == "error",
                                "mt-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded-lg max-w-xl mx-auto",
                                "mt-4 p-3 bg-blue-100 border border-blue-400 text-blue-700 rounded-lg max-w-xl mx-auto"
                            )
                        )
                    )
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            placeholder="Ingresa tu correo institucional o corporativo",
                            type="email",
                            name="email",
                            value=LandingState.email,
                            on_change=LandingState.set_email,
                            disabled=LandingState.is_loading,
                            class_name="w-full px-5 py-3 rounded-lg border-2 border-transparent focus:border-teal-300 focus:ring-2 focus:ring-teal-300 outline-none transition-colors text-gray-800 placeholder-gray-500 disabled:opacity-50 disabled:bg-gray-100",
                            required=True,
                        ),
                        rx.el.button(
                            rx.cond(
                                LandingState.is_loading,
                                rx.el.span(
                                    "Enviando...",
                                    class_name="flex items-center justify-center"
                                ),
                                "Prueba CiviData"
                            ),
                            type="submit",
                            disabled=LandingState.is_loading,
                            class_name="w-full sm:w-auto px-8 py-3 bg-white text-teal-700 font-semibold rounded-lg shadow-md hover:bg-teal-50 transition-colors transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100",
                        ),
                        class_name="mt-8 max-w-xl mx-auto flex flex-col sm:flex-row gap-4 items-center",
                    ),
                    on_submit=LandingState.handle_demo_request,
                    prevent_default=True,
                ),
                class_name="py-16 sm:py-24",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="cta",
        class_name="bg-gradient-to-r from-teal-600 to-sky-700",
    )