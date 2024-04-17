from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float or bool: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits, see [CMDLINKRESOLVED Configure.MultiEval.Limit.LowEnergy.Le1M.PowerVsTime#set CMDLINKRESOLVED]. Range: 0 % to 100 %, Unit: %
			- Nominal_Power: float or bool: float Average power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Power: float or bool: float Peak power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Leakage_Power: float or bool: float Average power during the carrier-off state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Min_Avg_Pow: float or bool: float Peak power minus average power Range: -99.99 dBm to 99.99 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Peak_Power'),
			ArgStruct.scalar_float_ext('Leakage_Power'),
			ArgStruct.scalar_float_ext('Peak_Min_Avg_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Peak_Power: float or bool = None
			self.Leakage_Power: float or bool = None
			self.Peak_Min_Avg_Pow: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy[:LE1M]:MAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.powerVsTime.lowEnergy.le1M.maximum.calculate() \n
		Returns the power results for LE 1M PHY (uncoded) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy:LE1M:MAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float or bool: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits, see [CMDLINKRESOLVED Configure.MultiEval.Limit.LowEnergy.Le1M.PowerVsTime#set CMDLINKRESOLVED]. Range: 0 % to 100 %, Unit: %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Power: float: float Peak power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Leakage_Power: float: float Average power during the carrier-off state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Min_Avg_Pow: float: float Peak power minus average power Range: -99.99 dBm to 99.99 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Leakage_Power'),
			ArgStruct.scalar_float('Peak_Min_Avg_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float = None
			self.Peak_Power: float = None
			self.Leakage_Power: float = None
			self.Peak_Min_Avg_Pow: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy[:LE1M]:MAXimum \n
		Snippet: value: ReadStruct = driver.multiEval.powerVsTime.lowEnergy.le1M.maximum.read() \n
		Returns the power results for LE 1M PHY (uncoded) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy:LE1M:MAXimum?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits, see [CMDLINKRESOLVED Configure.MultiEval.Limit.LowEnergy.Le1M.PowerVsTime#set CMDLINKRESOLVED]. Range: 0 % to 100 %, Unit: %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Power: float: float Peak power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Leakage_Power: float: float Average power during the carrier-off state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Peak_Min_Avg_Pow: float: float Peak power minus average power Range: -99.99 dBm to 99.99 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Leakage_Power'),
			ArgStruct.scalar_float('Peak_Min_Avg_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Peak_Power: float = None
			self.Leakage_Power: float = None
			self.Peak_Min_Avg_Pow: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy[:LE1M]:MAXimum \n
		Snippet: value: FetchStruct = driver.multiEval.powerVsTime.lowEnergy.le1M.maximum.fetch() \n
		Returns the power results for LE 1M PHY (uncoded) . The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PVTime:LENergy:LE1M:MAXimum?', self.__class__.FetchStruct())
