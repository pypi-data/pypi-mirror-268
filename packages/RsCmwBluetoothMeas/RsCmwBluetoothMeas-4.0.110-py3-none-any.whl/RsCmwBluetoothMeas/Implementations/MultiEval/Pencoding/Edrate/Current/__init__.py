from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 4 total commands, 1 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def c(self):
		"""c commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_c'):
			from .C import CCls
			self._c = CCls(self._core, self._cmd_group)
		return self._c

	# noinspection PyTypeChecker
	class ReadStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: float 'Reliability indicator'
			- Nominal_Power: float: float Average power during the carrier-on state Range: -128 dBm to 30 dBm , Unit: dBm
			- Bit_Error_Rate: float: float Number of bit errors in the received burst, as a percentage of the total number of bits received Range: 0 % to 100 %, Unit: %
			- Packets_0_Errors: float: float Number of bit error free packets received, as a percentage of all the bursts received Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Bit_Error_Rate'),
			ArgStruct.scalar_float('Packets_0_Errors')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float = None
			self.Bit_Error_Rate: float = None
			self.Packets_0_Errors: float = None

	def read(self) -> ReadStruct:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent \n
		Snippet: value: ReadStruct = driver.multiEval.pencoding.edrate.current.read() \n
		Returns the 'Differential Phase Encoding' results for EDR packets (single values) . The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for ReadStruct structure arguments."""
		return self._core.io.query_struct(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent?', self.__class__.ReadStruct())

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Bit_Error_Rate: float: No parameter help available
			- Packets_0_Errors: float: No parameter help available
			- Nominal_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Bit_Error_Rate'),
			ArgStruct.scalar_float('Packets_0_Errors'),
			ArgStruct.scalar_float('Nominal_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Bit_Error_Rate: float = None
			self.Packets_0_Errors: float = None
			self.Nominal_Power: float = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent \n
		Snippet: value: FetchStruct = driver.multiEval.pencoding.edrate.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: float 'Reliability indicator'
			- Nominal_Power: float or bool: float Average power during the carrier-on state Range: -128 dBm to 30 dBm , Unit: dBm
			- Bit_Error_Rate: float or bool: float Number of bit errors in the received burst, as a percentage of the total number of bits received Range: 0 % to 100 %, Unit: %
			- Packets_0_Errors: float or bool: float Number of bit error free packets received, as a percentage of all the bursts received Range: 0 % to 100 %, Unit: %"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float_ext('Nominal_Power'),
			ArgStruct.scalar_float_ext('Bit_Error_Rate'),
			ArgStruct.scalar_float_ext('Packets_0_Errors')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nominal_Power: float or bool = None
			self.Bit_Error_Rate: float or bool = None
			self.Packets_0_Errors: float or bool = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent \n
		Snippet: value: CalculateStruct = driver.multiEval.pencoding.edrate.current.calculate() \n
		Returns the 'Differential Phase Encoding' results for EDR packets (single values) . The values described below are
		returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each result
		listed below. \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:BLUetooth:MEASurement<Instance>:MEValuation:PENCoding:EDRate:CURRent?', self.__class__.CalculateStruct())

	def clone(self) -> 'CurrentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CurrentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
