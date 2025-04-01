import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # page.add(
    #     ft.Row()
    #     ft.Row(
    #         [
    #             ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             ft.IconButton(ft.Icons.ADD, on_click=plus_click),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #     )
    # )
    headerRow = ft.Row(
        [
            ft.Text(value="Inventory Manager!")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    buttonsRow = ft.Row(
        [
            ft.ElevatedButton(text="Check Inventory"),
            ft.ElevatedButton(text="Check Product"),
            ft.ElevatedButton(text="Add Product")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.controls.append(headerRow)
    page.controls.append(buttonsRow)
    page.update()

ft.app(main)