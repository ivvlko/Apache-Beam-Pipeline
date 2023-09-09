"""
We might have different csv files in future so here we store all the mappings required
"""


CSV_MAPPING_COLUMNS = {
    "partners_data": {
        "column_names": [
            "date", "partner", "partner_type", "unique_clicks", "new_registrations",
            "first_time_depositing", "cpa_triggered", "cpa_earnings_eur",
            "rev_share_earnings_eur", "amount_deposited_eur", "net_revenue_eur",
            "country"
        ],

        "numeric_columns": [
            "unique_clicks", "new_registrations", "first_time_depositing",
            "cpa_triggered", "cpa_earnings_eur", "rev_share_earnings_eur",
            "amount_deposited_eur", "net_revenue_eur"
        ]

    }
}
