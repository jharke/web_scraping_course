
import world_bank_data as wb

# Get estimates for the world population:
wb.get_series('SP.POP.TOTL', date='2017')

# Get timeseries of "Agricultural machinery, tractors" in Albania
wb.get_series('AG.AGR.TRAC.NO', country='ALB')
