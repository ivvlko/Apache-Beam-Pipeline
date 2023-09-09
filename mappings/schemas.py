"""
This module defines different schemas based on the csv file type;
"""

PG_SCHEMAS = {
    "partners_data": "date:DATE, partner:STRING, partner_type:STRING, unique_clicks:FLOAT, new_registrations:FLOAT, first_time_depositing:FLOAT, cpa_triggered:FLOAT, cpa_earnings_eur:FLOAT, rev_share_earnings_eur:FLOAT, amount_deposited_eur:FLOAT, net_revenue_eur:FLOAT, country:STRING"
}
