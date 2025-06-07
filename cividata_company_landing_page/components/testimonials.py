import reflex as rx
from cividata_company_landing_page.states.landing_state import (
    LandingState,
    TestimonialEntry,
)


def testimonial_card(
    testimonial: TestimonialEntry,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                tag="message-square-quote",
                class_name="h-8 w-8 text-teal-400 mb-4",
            ),
            rx.el.p(
                testimonial["quote"],
                class_name="text-gray-700 italic text-lg leading-relaxed mb-6",
            ),
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={testimonial['name']}&backgroundColor=teal&textColor=white&radius=50",
                    alt=f"Avatar of {testimonial['name']}",
                    class_name="h-12 w-12 rounded-full mr-4 border-2 border-teal-200",
                ),
                rx.el.div(
                    rx.el.p(
                        testimonial["name"],
                        class_name="font-semibold text-gray-900",
                    ),
                    rx.el.p(
                        testimonial["role"],
                        class_name="text-sm text-gray-600",
                    ),
                    rx.el.p(
                        testimonial["organization"],
                        class_name="text-xs text-gray-500",
                    ),
                ),
                class_name="flex items-center mt-auto pt-4 border-t border-gray-200",
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="bg-white p-6 rounded-xl shadow-lg border border-gray-200 hover:shadow-xl transition-shadow duration-300 flex flex-col",
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Trusted by ",
                rx.el.span(
                    "Public Sector Leaders",
                    class_name="text-teal-600",
                ),
                class_name="text-3xl sm:text-4xl font-bold text-gray-900 text-center mb-4",
            ),
            rx.el.p(
                "See how CiviData is making a difference in local governments and public agencies.",
                class_name="text-lg text-gray-600 text-center mb-12 max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(
                    LandingState.testimonials_data,
                    testimonial_card,
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24",
        ),
        id="testimonials",
        class_name="bg-gray-50",
    )