import reflex as rx
from cividata_company_landing_page.states.landing_state import LandingState


def app_toast() -> rx.Component:
    return rx.cond(
        LandingState.show_toast,
        rx.el.div(
            rx.el.div(
                rx.icon(
                    tag=rx.cond(
                        LandingState.toast_status
                        == "success",
                        "check-circle-2",
                        "alert-circle",
                    ),
                    class_name=rx.cond(
                        LandingState.toast_status
                        == "success",
                        "text-white mr-3 size-6",
                        "text-white mr-3 size-6",
                    ),
                ),
                rx.el.p(
                    LandingState.toast_message,
                    class_name="text-sm font-medium text-white",
                ),
                rx.el.button(
                    rx.icon(
                        tag="x",
                        class_name="size-5 text-white hover:text-gray-200",
                    ),
                    on_click=LandingState.hide_toast,
                    class_name="ml-auto p-1 rounded-md hover:bg-white/20 transition-colors",
                ),
                class_name=rx.cond(
                    LandingState.toast_status == "success",
                    "flex items-center w-full max-w-xs sm:max-w-md p-4 rounded-lg shadow-md bg-green-500",
                    "flex items-center w-full max-w-xs sm:max-w-md p-4 rounded-lg shadow-md bg-red-500",
                ),
            ),
            class_name="fixed top-5 right-5 z-50 transition-all duration-300 ease-out transform translate-x-0 opacity-100",
        ),
        rx.el.div(
            class_name="fixed top-5 right-5 z-50 transition-all duration-300 ease-in transform translate-x-full opacity-0"
        ),
    )