import datetime
import flet as ft


def main(page: ft.Page):
    def change_date(e):
        print(f"Date picker changed, value is {date_picker.value}")

    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")

    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

    # Create a Container to arrange the button and DatePicker
    container = ft.Container(
        padding=20,
        alignment=ft.Alignment.center,
        children=[
            date_picker,
            ft.ElevatedButton(
                text="Pick Date",
                icon=ft.icons.CALENDAR_MONTH,
                on_click=lambda _: date_picker.pick_date(),
            ),
        ],
    )

    page.add(container)

ft.app(target=main)
