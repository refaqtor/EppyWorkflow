from pint import UnitRegistry
from eppy import modeleditor
from eppy.modeleditor import IDF

def VentilationFlow(idf_file,VentilationFlow):
	ureg = UnitRegistry()
	FanZoneExhaustObjects = idf_file.idfobjects["FAN:ZONEEXHAUST"]
	for i in range(0,len(FanZoneExhaustObjects)):
		VentilationFlow = float(VentilationFlow)
		VentilationFlowinIP = VentilationFlow*ureg.foot**3/ureg.minute
		VentilationFlowinSI = VentilationFlowinIP.to(ureg.meter**3/ureg.second)
		
		FanZoneExhaustObjects[i].Maximum_Flow_Rate = VentilationFlowinSI.magnitude

if __name__ == '__main':
	VentilationFlow(idf_file,VentilationFlow)