from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float or bool: float | ON | OFF Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#Frange CMDLINKRESOLVED]) exceeding the specified limit. (see [CMDLINKRESOLVED Configure.MultiEval.Limit.Frange#set CMDLINKRESOLVED]) Additional ON/OFF enables/disables the out of tolerance evaluation. Range: 0 % to 100 %
			- Nominal_Power: float or bool: float Average power during the carrier-on state Range: -128 dBm to 30 dBm
			- Fl: float or bool: float Lowest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz
			- Fh: float or bool: float Highest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Fl'),
			ArgStruct.scalar_float_ext('Fh')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float or bool = None
			self.Fl: float or bool = None
			self.Fh: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.frange.brate.current.calculate() \n
		Returns the 'Frequency Range' results for BR. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float or bool: float | ON | OFF Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#Frange CMDLINKRESOLVED]) exceeding the specified limit. (see [CMDLINKRESOLVED Configure.MultiEval.Limit.Frange#set CMDLINKRESOLVED]) Additional ON/OFF enables/disables the out of tolerance evaluation. Range: 0 % to 100 %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -128 dBm to 30 dBm
			- Fl: float: float Lowest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz
			- Fh: float: float Highest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Fl'),
			ArgStruct.scalar_float('Fh')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float or bool = None
			self.Nominal_Power: float = None
			self.Fl: float = None
			self.Fh: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent \n
		Snippet: value: ReadStruct = driver.multiEval.frange.brate.current.read() \n
		Returns the 'Frequency Range' results for BR. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float: float | ON | OFF Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#Frange CMDLINKRESOLVED]) exceeding the specified limit. (see [CMDLINKRESOLVED Configure.MultiEval.Limit.Frange#set CMDLINKRESOLVED]) Additional ON/OFF enables/disables the out of tolerance evaluation. Range: 0 % to 100 %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -128 dBm to 30 dBm
			- Fl: float: float Lowest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz
			- Fh: float: float Highest frequency at which spectral power density drops below specified threshold Range: -1 MHz to +1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Fl'),
			ArgStruct.scalar_float('Fh')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Fl: float = None
			self.Fh: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.frange.brate.current.fetch() \n
		Returns the 'Frequency Range' results for BR. The values described below are returned by FETCh and READ commands.
		CALCulate commands return limit check results instead, one value for each result listed below. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:FRANge:BRATe:CURRent?', self.__class__.FetchStruct())
