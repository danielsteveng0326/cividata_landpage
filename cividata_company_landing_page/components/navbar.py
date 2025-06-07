import reflex as rx


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon(
                        tag="landmark",
                        class_name="h-8 w-8 text-teal-600 mr-2",
                    ),
                    rx.el.span(
                        "CiviData",
                        class_name="text-2xl font-bold text-gray-800",
                    ),
                    class_name="flex items-center",
                ),
                href="/",
            ),
            rx.el.nav(
                rx.el.a(
                    "Modules",
                    href="#modules",
                    class_name="text-gray-600 hover:text-teal-600 px-3 py-2 rounded-md text-sm font-medium transition-colors",
                ),
                rx.el.a(
                    "Pricing",
                    href="#pricing",
                    class_name="text-gray-600 hover:text-teal-600 px-3 py-2 rounded-md text-sm font-medium transition-colors",
                ),
                rx.el.a(
                    "Testimonials",
                    href="#testimonials",
                    class_name="text-gray-600 hover:text-teal-600 px-3 py-2 rounded-md text-sm font-medium transition-colors",
                ),
                rx.el.a(
                    "Request Demo",
                    href="#cta",
                    class_name="text-gray-600 hover:text-teal-600 px-3 py-2 rounded-md text-sm font-medium transition-colors",
                ),
                class_name="hidden md:flex space-x-4",
            ),
            rx.el.button(
                "Request Demo",
                on_click=lambda: rx.call_script(
                    "document.getElementById('cta').scrollIntoView({ behavior: 'smooth' });"
                ),
                class_name="hidden md:inline-flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-lg text-white bg-teal-600 hover:bg-teal-700 transition-colors shadow-sm",
            ),
            rx.el.div(class_name="md:hidden"),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16",
        ),
        class_name="sticky top-0 z-40 w-full bg-white/80 backdrop-blur-md border-b border-gray-200",
    )