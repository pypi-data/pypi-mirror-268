from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


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
			- Nominal_Power: float or bool: float Average burst power during the carrier-on state Range: -99.99 dBm to 99.99 dBm
			- Sync_Bit_Errors: float or bool: decimal Sync bit errors Range: 0 to 10E+3
			- Trailer_Bit_Errs: float or bool: decimal Trailer bit errors Range: 0 to 10E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Sync_Bit_Errors'),
			ArgStruct.scalar_float_ext('Trailer_Bit_Errs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float or bool = None
			self.Sync_Bit_Errors: float or bool = None
			self.Trailer_Bit_Errs: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.pencoding.ssequence.edrate.current.calculate() \n
		Returns the 'Differential Phase Encoding' results for EDR packets in combined signal path. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent?', self.__class__.CalculateStruct())

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Nominal_Power: float: float Average burst power during the carrier-on state Range: -99.99 dBm to 99.99 dBm
			- Sync_Bit_Errors: int: decimal Sync bit errors Range: 0 to 10E+3
			- Trailer_Bit_Errs: int: decimal Trailer bit errors Range: 0 to 10E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_int('Sync_Bit_Errors'),
			ArgStruct.scalar_int('Trailer_Bit_Errs')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float = None
			self.Sync_Bit_Errors: int = None
			self.Trailer_Bit_Errs: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent \n
		Snippet: value: ResultData = driver.multiEval.pencoding.ssequence.edrate.current.read() \n
		Returns the 'Differential Phase Encoding' results for EDR packets in combined signal path. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent \n
		Snippet: value: ResultData = driver.multiEval.pencoding.ssequence.edrate.current.fetch() \n
		Returns the 'Differential Phase Encoding' results for EDR packets in combined signal path. The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:SSEQuence:EDRate:CURRent?', self.__class__.ResultData())
