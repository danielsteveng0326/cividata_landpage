import reflex as rx
from cividata_company_landing_page.states.landing_state import (
    LandingState,
    ModuleHighlight,
)


def module_card(module: ModuleHighlight) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                tag=module["icon"],
                class_name="h-10 w-10 text-teal-600 mb-4",
            )
        ),
        rx.el.h3(
            module["title"],
            class_name="text-xl font-semibold text-gray-900 mb-2",
        ),
        rx.el.p(
            module["description"],
            class_name="text-gray-600 text-sm leading-relaxed",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-lg transition-shadow duration-300 flex flex-col items-start",
    )


def features_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Core ",
                rx.el.span(
                    "CiviData Modules",
                    class_name="text-teal-600",
                ),
                class_name="text-3xl sm:text-4xl font-bold text-gray-900 text-center mb-4",
            ),
            rx.el.p(
                "Explore the key modules CiviData offers to enhance civic operations and decision-making.",
                class_name="text-lg text-gray-600 text-center mb-12 max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(
                    LandingState.module_highlights_data,
                    module_card,
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
        ),
        id="modules",
        class_name="bg-gray-50",
    )