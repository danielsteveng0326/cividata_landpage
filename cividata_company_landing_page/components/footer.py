import reflex as rx
from cividata_company_landing_page.states.landing_state import LandingState


def footer_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-500 hover:text-teal-600 transition-colors text-sm",
    )


def social_icon_link(
    icon_tag: str, href: str, aria_label: str
) -> rx.Component:
    return rx.el.a(
        rx.icon(tag=icon_tag, class_name="h-5 w-5"),
        href=href,
        aria_label=aria_label,
        target="_blank",
        rel="noopener noreferrer",
        class_name="text-gray-400 hover:text-teal-500 transition-colors",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.div(
                            rx.icon(
                                tag="landmark",
                                class_name="h-7 w-7 text-teal-600 mr-2",
                            ),
                            rx.el.span(
                                "CiviData",
                                class_name="text-xl font-semibold text-gray-800",
                            ),
                            class_name="flex items-center",
                        ),
                        href="/",
                    ),
                    rx.el.p(
                        "Empowering local governments with data-driven decisions.",
                        class_name="mt-2 text-sm text-gray-600 max-w-xs",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Platform",
                            class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
                        ),
                        rx.el.ul(
                            rx.el.li(
                                footer_link(
                                    "Contract Monitoring",
                                    "#modules",
                                )
                            ),
                            rx.el.li(
                                footer_link(
                                    "Development Plans",
                                    "#modules",
                                )
                            ),
                            rx.el.li(
                                footer_link(
                                    "Geoportals", "#modules"
                                )
                            ),
                            rx.el.li(
                                footer_link(
                                    "Pricing", "#pricing"
                                )
                            ),
                            class_name="mt-4 space-y-2",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Company",
                            class_name="text-sm font-semibold text-gray-900 tracking-wider uppercase",
                        ),
                        rx.el.ul(
                            rx.el.li(
                                footer_link("About Us", "#")
                            ),
                            rx.el.li(
                                footer_link("Careers", "#")
                            ),
                            rx.el.li(
                                footer_link(
                                    "Contact Sales", "#cta"
                                )
                            ),
                            rx.el.li(
                                footer_link(
                                    "Privacy Policy", "#"
                                )
                            ),
                            class_name="mt-4 space-y-2",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-8",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 xl:gap-16",
            ),
            rx.el.div(
                rx.el.p(
                    f"© {LandingState.current_year} CiviData, Inc. All rights reserved.",
                    class_name="text-sm text-gray-500",
                ),
                rx.el.div(
                    social_icon_link(
                        "twitter",
                        "#",
                        "CiviData on Twitter",
                    ),
                    social_icon_link(
                        "linkedin",
                        "#",
                        "CiviData on LinkedIn",
                    ),
                    social_icon_link(
                        "mail",
                        "mailto:info@cividata.com",
                        "Email CiviData",
                    ),
                    class_name="flex space-x-5",
                ),
                class_name="mt-12 pt-8 border-t border-gray-200 flex flex-col sm:flex-row justify-between items-center",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50 border-t border-gray-200",
    )