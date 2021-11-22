import pandas as pd
import xlsxwriter
from Supportive import *

ResSheet=r"C:\Users\tkowalc\OneDrive - National Instruments\Remote HW reserv\Draft Reservation Sheet.xlsx"

WorkingWeeks = GetWrokingWeeks()
#CreateExcel(ResSheet,WorkingWeeks)
UpdateIPs(ResSheet,WorkingWeeks)

