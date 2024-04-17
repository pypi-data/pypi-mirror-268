from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: float: No parameter help available
			- Nominal_Power: float: No parameter help available
			- Wi: float: No parameter help available
			- W_0_Wi: float: No parameter help available
			- W_0_Max: float: No parameter help available
			- Rms_Evm: float: No parameter help available
			- Peak_Evm: float: No parameter help available
			- Symbol_Rate_Error: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bursts_Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Wi'),
			ArgStruct.scalar_float('W_0_Wi'),
			ArgStruct.scalar_float('W_0_Max'),
			ArgStruct.scalar_float('Rms_Evm'),
			ArgStruct.scalar_float('Peak_Evm'),
			ArgStruct.scalar_int('Symbol_Rate_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Wi: float = None
			self.W_0_Wi: float = None
			self.W_0_Max: float = None
			self.Rms_Evm: float = None
			self.Peak_Evm: float = None
			self.Symbol_Rate_Error: int = None

	def read(self) -> ResultData:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum \n
		Snippet: value: ResultData = driver.hdrp.modulation.maximum.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum \n
		Snippet: value: ResultData = driver.hdrp.modulation.maximum.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bursts_Out_Of_Tol: enums.ResultStatus2: No parameter help available
			- Nominal_Power: enums.ResultStatus2: No parameter help available
			- Wi: enums.ResultStatus2: No parameter help available
			- W_0_Wi: enums.ResultStatus2: No parameter help available
			- W_0_Max: enums.ResultStatus2: No parameter help available
			- Rms_Evm: enums.ResultStatus2: No parameter help available
			- Peak_Evm: enums.ResultStatus2: No parameter help available
			- Symbol_Rate_Error: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_enum('Bursts_Out_Of_Tol', enums.ResultStatus2),
			ArgStruct.scalar_enum('Nominal_Power', enums.ResultStatus2),
			ArgStruct.scalar_enum('Wi', enums.ResultStatus2),
			ArgStruct.scalar_enum('W_0_Wi', enums.ResultStatus2),
			ArgStruct.scalar_enum('W_0_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Rms_Evm', enums.ResultStatus2),
			ArgStruct.scalar_enum('Peak_Evm', enums.ResultStatus2),
			ArgStruct.scalar_int('Symbol_Rate_Error')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bursts_Out_Of_Tol: enums.ResultStatus2 = None
			self.Nominal_Power: enums.ResultStatus2 = None
			self.Wi: enums.ResultStatus2 = None
			self.W_0_Wi: enums.ResultStatus2 = None
			self.W_0_Max: enums.ResultStatus2 = None
			self.Rms_Evm: enums.ResultStatus2 = None
			self.Peak_Evm: enums.ResultStatus2 = None
			self.Symbol_Rate_Error: int = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum \n
		Snippet: value: CalculateStruct = driver.hdrp.modulation.maximum.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:HDRP:MODulation:MAXimum?', self.__class__.CalculateStruct())
