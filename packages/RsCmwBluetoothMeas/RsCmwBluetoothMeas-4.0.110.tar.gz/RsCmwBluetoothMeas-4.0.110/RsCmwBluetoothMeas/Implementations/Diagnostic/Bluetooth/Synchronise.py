from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SynchroniseCls:
	"""Synchronise commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("synchronise", core, parent)

	def set(self, min_no_valid_bursts: int, syn_check_filter: int, max_invalid_burst: int) -> None:
		"""SCPI: DIAGnostic:BLUetooth:SYNChronise \n
		Snippet: driver.diagnostic.bluetooth.synchronise.set(min_no_valid_bursts = 1, syn_check_filter = 1, max_invalid_burst = 1) \n
		No command help available \n
			:param min_no_valid_bursts: No help available
			:param syn_check_filter: No help available
			:param max_invalid_burst: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('min_no_valid_bursts', min_no_valid_bursts, DataType.Integer), ArgSingle('syn_check_filter', syn_check_filter, DataType.Integer), ArgSingle('max_invalid_burst', max_invalid_burst, DataType.Integer))
		self._core.io.write(f'DIAGnostic:BLUetooth:SYNChronise {param}'.rstrip())

	# noinspection PyTypeChecker
	class SynchroniseStruct(StructBase):
		"""Response structure. Fields: \n
			- Min_No_Valid_Bursts: int: No parameter help available
			- Syn_Check_Filter: int: No parameter help available
			- Max_Invalid_Burst: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Min_No_Valid_Bursts'),
			ArgStruct.scalar_int('Syn_Check_Filter'),
			ArgStruct.scalar_int('Max_Invalid_Burst')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_No_Valid_Bursts: int = None
			self.Syn_Check_Filter: int = None
			self.Max_Invalid_Burst: int = None

	def get(self) -> SynchroniseStruct:
		"""SCPI: DIAGnostic:BLUetooth:SYNChronise \n
		Snippet: value: SynchroniseStruct = driver.diagnostic.bluetooth.synchronise.get() \n
		No command help available \n
			:return: structure: for return value, see the help for SynchroniseStruct structure arguments."""
		return self._core.io.query_struct(f'DIAGnostic:BLUetooth:SYNChronise?', self.__class__.SynchroniseStruct())
