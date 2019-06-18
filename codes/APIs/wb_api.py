
import world_bank_data as wb

# GET indicators
wb.get_indicators(topic=3, source=2)

# Get estimates for the world population:
wb.get_series('SP.POP.TOTL', date='2010:2018')
