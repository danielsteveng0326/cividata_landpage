import reflex as rx
from cividata_company_landing_page.states.landing_state import (
    LandingState,
    PricingTier,
)


def pricing_card(tier: PricingTier) -> rx.Component:
    return rx.el.div(
        rx.cond(
            tier["is_popular"],
            rx.el.div(
                "Most Popular",
                class_name="absolute top-0 left-1/2 transform -translate-x-1/2 -translate-y-1/2 px-3 py-1 bg-teal-600 text-white text-xs font-semibold rounded-full",
            ),
            None,
        ),
        rx.el.h3(
            tier["name"],
            class_name="text-2xl font-bold text-gray-900 mb-3",
        ),
        rx.el.div(
            rx.el.span(
                tier["price"],
                class_name="text-4xl font-extrabold text-gray-900",
            ),
            rx.cond(
                tier["price"] != "Custom",
                rx.el.span(
                    "/month",
                    class_name="text-lg text-gray-500 ml-1",
                ),
                None,
            ),
            class_name="mb-6",
        ),
        rx.el.p(
            tier["description"],
            class_name="text-gray-600 mb-6 min-h-[48px]",
        ),
        rx.el.ul(
            rx.foreach(
                tier["features"],
                lambda feature: rx.el.li(
                    rx.icon(
                        tag="square_check",
                        class_name="h-5 w-5 text-green-500 mr-2 shrink-0",
                    ),
                    feature,
                    class_name="flex items-center text-gray-700 mb-3",
                ),
            ),
            class_name="space-y-3 mb-8",
        ),
        rx.el.button(
            tier["cta_text"],
            on_click=lambda: LandingState.handle_pricing_cta_click(
                tier["name"]
            ),
            class_name=rx.cond(
                tier["is_popular"],
                "w-full py-3 px-6 bg-teal-600 text-white font-semibold rounded-lg shadow-md hover:bg-teal-700 transition-colors transform hover:scale-105",
                "w-full py-3 px-6 bg-white text-teal-600 border-2 border-teal-600 font-semibold rounded-lg hover:bg-teal-50 transition-colors",
            ),
        ),
        class_name=rx.cond(
            tier["is_popular"],
            "relative bg-white p-8 rounded-xl shadow-2xl border-2 border-teal-600 flex flex-col",
            "relative bg-white p-8 rounded-xl shadow-lg border border-gray-200 flex flex-col",
        ),
    )


def pricing_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Transparent ",
                rx.el.span(
                    "Pricing for CiviData",
                    class_name="text-teal-600",
                ),
                class_name="text-3xl sm:text-4xl font-bold text-gray-900 text-center mb-4",
            ),
            rx.el.p(
                "Choose a plan that aligns with your government's needs and budget. Scale effortlessly.",
                class_name="text-lg text-gray-600 text-center mb-12 max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(
                    LandingState.pricing_tiers_data,
                    pricing_card,
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 items-stretch",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
        ),
        id="pricing",
        class_name="bg-gradient-to-br from-sky-50 via-green-50 to-teal-50",
    )