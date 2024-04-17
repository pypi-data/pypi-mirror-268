from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, spot_check: bool, power: bool, modulation: bool, spectrum_acp: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult[:ALL] \n
		Snippet: driver.configure.trx.result.all.set(spot_check = False, power = False, modulation = False, spectrum_acp = False) \n
		Enables or disables the evaluation of results. \n
			:param spot_check: OFF | ON Spot check ON: Evaluate results OFF: Do not evaluate results
			:param power: OFF | ON Statistical power results
			:param modulation: OFF | ON Statistical modulation results
			:param spectrum_acp: OFF | ON Spectrum ACP results Only ACP+/-5 channel mode supported (21 half-channels)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('spot_check', spot_check, DataType.Boolean), ArgSingle('power', power, DataType.Boolean), ArgSingle('modulation', modulation, DataType.Boolean), ArgSingle('spectrum_acp', spectrum_acp, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Spot_Check: bool: OFF | ON Spot check ON: Evaluate results OFF: Do not evaluate results
			- Power: bool: OFF | ON Statistical power results
			- Modulation: bool: OFF | ON Statistical modulation results
			- Spectrum_Acp: bool: OFF | ON Spectrum ACP results Only ACP+/-5 channel mode supported (21 half-channels)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Spot_Check'),
			ArgStruct.scalar_bool('Power'),
			ArgStruct.scalar_bool('Modulation'),
			ArgStruct.scalar_bool('Spectrum_Acp')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Spot_Check: bool = None
			self.Power: bool = None
			self.Modulation: bool = None
			self.Spectrum_Acp: bool = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.trx.result.all.get() \n
		Enables or disables the evaluation of results. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:TRX:RESult:ALL?', self.__class__.AllStruct())
