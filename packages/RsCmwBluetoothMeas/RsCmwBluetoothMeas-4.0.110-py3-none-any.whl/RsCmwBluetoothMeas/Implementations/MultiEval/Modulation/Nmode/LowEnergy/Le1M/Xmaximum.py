from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XmaximumCls:
	"""Xmaximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xmaximum", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float or bool: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits, see 'Modulation limits (LE) '. Range: 0 % to 100 %
			- Freq_Accuracy: float or bool: float Unit: Hz
			- Freq_Offset: float or bool: float Unit: Hz
			- Freq_Drift: float or bool: float Unit: Hz
			- Init_Freq_Drift: float or bool: float Unit: Hz
			- Max_Drift_Rate: float or bool: float Unit: Hz/50 μs
			- Freq_Dev_Avg_F_1: float or bool: No parameter help available
			- Freq_Dev_Min_F_1: float or bool: No parameter help available
			- Freq_Dev_Max_F_1: float or bool: No parameter help available
			- Freq_Dev_Avg_F_2: float or bool: No parameter help available
			- Freq_Dev_Min_F_2: float or bool: No parameter help available
			- Freq_Dev_Max_F_2: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Freq_Accuracy'),
			ArgStruct.scalar_float_ext('Freq_Offset'),
			ArgStruct.scalar_float_ext('Freq_Drift'),
			ArgStruct.scalar_float_ext('Init_Freq_Drift'),
			ArgStruct.scalar_float_ext('Max_Drift_Rate'),
			ArgStruct.scalar_float_ext('Freq_Dev_Avg_F_1'),
			ArgStruct.scalar_float_ext('Freq_Dev_Min_F_1'),
			ArgStruct.scalar_float_ext('Freq_Dev_Max_F_1'),
			ArgStruct.scalar_float_ext('Freq_Dev_Avg_F_2'),
			ArgStruct.scalar_float_ext('Freq_Dev_Min_F_2'),
			ArgStruct.scalar_float_ext('Freq_Dev_Max_F_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Freq_Accuracy: float or bool = None
			self.Freq_Offset: float or bool = None
			self.Freq_Drift: float or bool = None
			self.Init_Freq_Drift: float or bool = None
			self.Max_Drift_Rate: float or bool = None
			self.Freq_Dev_Avg_F_1: float or bool = None
			self.Freq_Dev_Min_F_1: float or bool = None
			self.Freq_Dev_Max_F_1: float or bool = None
			self.Freq_Dev_Avg_F_2: float or bool = None
			self.Freq_Dev_Min_F_2: float or bool = None
			self.Freq_Dev_Max_F_2: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy[:LE1M]:XMAXimum \n
		Snippet: value: CalculateStruct = driver.multiEval.modulation.nmode.lowEnergy.le1M.xmaximum.calculate() \n
		Returns the current, average, xmin, xmax, and maximum modulation results for LE 1M PHY in normal mode, see 'Normal mode
		classic: statistical modulation results'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy:LE1M:XMAXimum?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#Modulation CMDLINKRESOLVED]) exceeding the specified limits, see 'Modulation limits (LE) '. Range: 0 % to 100 %
			- Freq_Accuracy: float: float Unit: Hz
			- Freq_Offset: float: float Unit: Hz
			- Freq_Drift: float: float Unit: Hz
			- Init_Freq_Drift: float: float Unit: Hz
			- Max_Drift: float: float Unit: Hz/50 μs
			- Freq_Dev_Avg_F_1: float: No parameter help available
			- Freq_Dev_Min_F_1: float: No parameter help available
			- Freq_Dev_Max_F_1: float: No parameter help available
			- Freq_Dev_Avg_F_2: float: No parameter help available
			- Freq_Dev_Min_F_2: float: No parameter help available
			- Freq_Dev_Max_F_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Freq_Accuracy'),
			ArgStruct.scalar_float('Freq_Offset'),
			ArgStruct.scalar_float('Freq_Drift'),
			ArgStruct.scalar_float('Init_Freq_Drift'),
			ArgStruct.scalar_float('Max_Drift'),
			ArgStruct.scalar_float('Freq_Dev_Avg_F_1'),
			ArgStruct.scalar_float('Freq_Dev_Min_F_1'),
			ArgStruct.scalar_float('Freq_Dev_Max_F_1'),
			ArgStruct.scalar_float('Freq_Dev_Avg_F_2'),
			ArgStruct.scalar_float('Freq_Dev_Min_F_2'),
			ArgStruct.scalar_float('Freq_Dev_Max_F_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Freq_Accuracy: float = None
			self.Freq_Offset: float = None
			self.Freq_Drift: float = None
			self.Init_Freq_Drift: float = None
			self.Max_Drift: float = None
			self.Freq_Dev_Avg_F_1: float = None
			self.Freq_Dev_Min_F_1: float = None
			self.Freq_Dev_Max_F_1: float = None
			self.Freq_Dev_Avg_F_2: float = None
			self.Freq_Dev_Min_F_2: float = None
			self.Freq_Dev_Max_F_2: float = None

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy[:LE1M]:XMAXimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.nmode.lowEnergy.le1M.xmaximum.fetch() \n
		Returns the current, average, xmin, xmax, and maximum modulation results for LE 1M PHY in normal mode, see 'Normal mode
		classic: statistical modulation results'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy:LE1M:XMAXimum?', self.__class__.ResultData())

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy[:LE1M]:XMAXimum \n
		Snippet: value: ResultData = driver.multiEval.modulation.nmode.lowEnergy.le1M.xmaximum.read() \n
		Returns the current, average, xmin, xmax, and maximum modulation results for LE 1M PHY in normal mode, see 'Normal mode
		classic: statistical modulation results'. The values described below are returned by FETCh and READ commands. CALCulate
		commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:NMODe:LENergy:LE1M:XMAXimum?', self.__class__.ResultData())
