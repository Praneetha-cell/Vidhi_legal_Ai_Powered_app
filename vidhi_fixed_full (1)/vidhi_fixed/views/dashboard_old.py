import flet as ft
from i18n import t

from components.navbar import navbar
from components.cards import stat_card

def dashboard_view():


 return ft.Container(
    expand=True,
    padding=20,

    content=ft.Column(
        scroll=ft.ScrollMode.AUTO,

        controls=[

            navbar(),

            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                controls=[

                    stat_card("Active Cases", 148),

                    stat_card("Hearings This Week", 23),

                    stat_card("Cases Won", 87),

                    stat_card("Cases Lost", 14),

                    stat_card("Annual Revenue", "₹45.2L")
                ]
            ),

            ft.Container(
                bgcolor="white",
                padding=20,
                border_radius=10,

                content=ft.Column(
                    controls=[

                        ft.Text(
                            t("Case Analytics"),
                            size=20,
                            color="black",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Divider(),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,

                            controls=[

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(t("148"), size=32, color="green"),
                                        ft.Text(t("Active Cases"), color="black")
                                    ]
                                ),

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(t("23"), size=32, color="blue"),
                                        ft.Text(t("Hearings This Week"), color="black")
                                    ]
                                ),

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(t("87"), size=32, color="green"),
                                        ft.Text(t("Cases Won"), color="black")
                                    ]
                                ),

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(t("14"), size=32, color="red"),
                                        ft.Text(t("Cases Lost"), color="black")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),

            ft.Container(
                bgcolor="white",
                padding=20,
                border_radius=10,

                content=ft.Column(
                    controls=[

                        ft.Text(
                            t("Case Performance"),
                            size=20,
                            color="black",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Dropdown(
                            width=250,
                            label=t("Report Type"),
                            value="Monthly",
                            options=[
                                ft.dropdown.Option(key="Weekly", text=t("Weekly")),
                                ft.dropdown.Option(key="Monthly", text=t("Monthly")),
                                ft.dropdown.Option(key="Yearly", text=t("Yearly"))
                            ]
                        ),

                        ft.Divider(),

                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,

                            controls=[

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            t("87"),
                                            size=32,
                                            color="green"
                                        ),
                                        ft.Text(
                                            t("Cases Won"),
                                            color="black"
                                        )
                                    ]
                                ),

                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            t("14"),
                                            size=32,
                                            color="red"
                                        ),
                                        ft.Text(
                                            t("Cases Lost"),
                                            color="black"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),

            ft.Container(
                bgcolor="white",
                padding=20,
                border_radius=10,

                content=ft.Column(
                    controls=[

                        ft.Text(
                            t("Recent Cases"),
                            size=20,
                            color="black",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.DataTable(

                            columns=[

                                ft.DataColumn(
                                    ft.Text(t("Case ID"), color="black")
                                ),

                                ft.DataColumn(
                                    ft.Text(t("Case Name"), color="black")
                                ),

                                ft.DataColumn(
                                    ft.Text(t("Status"), color="black")
                                ),

                                ft.DataColumn(
                                    ft.Text(t("Court"), color="black")
                                ),

                                ft.DataColumn(
                                    ft.Text(t("Win %"), color="black")
                                )
                            ],

                            rows=[

                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(t("VD001"), color="black")),
                                        ft.DataCell(ft.Text(t("State vs Kumar"), color="black")),
                                        ft.DataCell(ft.Text(t("Active"), color="green")),
                                        ft.DataCell(ft.Text(t("High Court"), color="black")),
                                        ft.DataCell(ft.Text(t("82%"), color="green"))
                                    ]
                                ),

                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(t("VD002"), color="black")),
                                        ft.DataCell(ft.Text(t("Property Dispute"), color="black")),
                                        ft.DataCell(ft.Text(t("Active"), color="green")),
                                        ft.DataCell(ft.Text(t("District Court"), color="black")),
                                        ft.DataCell(ft.Text(t("67%"), color="orange"))
                                    ]
                                ),

                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(t("VD003"), color="black")),
                                        ft.DataCell(ft.Text(t("Contract Breach"), color="black")),
                                        ft.DataCell(ft.Text(t("Active"), color="green")),
                                        ft.DataCell(ft.Text(t("Civil Court"), color="black")),
                                        ft.DataCell(ft.Text(t("74%"), color="green"))
                                    ]
                                ),

                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text(t("VD004"), color="black")),
                                        ft.DataCell(ft.Text(t("Property Registration"), color="black")),
                                        ft.DataCell(ft.Text(t("Active"), color="green")),
                                        ft.DataCell(ft.Text(t("District Court"), color="black")),
                                        ft.DataCell(ft.Text(t("91%"), color="green"))
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),

            ft.Container(
                padding=20,

                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Divider(),

                        ft.Text(
                            t("VIDHI Legal AI © 2026"),
                            size=14
                        ),

                        ft.Text(
                            t("AI-Powered Legal Intelligence Platform"),
                            size=12
                        )
                    ]
                )
            )
        ]
    )
)
