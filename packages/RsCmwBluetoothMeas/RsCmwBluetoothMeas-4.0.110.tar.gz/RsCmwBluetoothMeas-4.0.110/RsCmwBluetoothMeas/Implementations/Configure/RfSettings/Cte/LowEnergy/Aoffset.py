from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AoffsetCls:
	"""Aoffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aoffset", core, parent)

	def set(self, ant_ref_1: float, ant_ref_2: float, ant_ref_3: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset \n
		Snippet: driver.configure.rfSettings.cte.lowEnergy.aoffset.set(ant_ref_1 = 1.0, ant_ref_2 = 1.0, ant_ref_3 = 1.0) \n
		Specifies the offset of external attenuation per input antenna relative to the reference antenna. For the reference
		antenna, the offset is fixed and set to 0 dB. \n
			:param ant_ref_1: numeric Range: -3 dB to 3 dB
			:param ant_ref_2: numeric Range: -3 dB to 3 dB
			:param ant_ref_3: numeric Range: -3 dB to 3 dB
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ant_ref_1', ant_ref_1, DataType.Float), ArgSingle('ant_ref_2', ant_ref_2, DataType.Float), ArgSingle('ant_ref_3', ant_ref_3, DataType.Float))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset {param}'.rstrip())

	# noinspection PyTypeChecker
	class AoffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Ant_Ref_1: float: numeric Range: -3 dB to 3 dB
			- Ant_Ref_2: float: numeric Range: -3 dB to 3 dB
			- Ant_Ref_3: float: numeric Range: -3 dB to 3 dB"""
		__meta_args_list = [
			ArgStruct.scalar_float('Ant_Ref_1'),
			ArgStruct.scalar_float('Ant_Ref_2'),
			ArgStruct.scalar_float('Ant_Ref_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ant_Ref_1: float = None
			self.Ant_Ref_2: float = None
			self.Ant_Ref_3: float = None

	def get(self) -> AoffsetStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset \n
		Snippet: value: AoffsetStruct = driver.configure.rfSettings.cte.lowEnergy.aoffset.get() \n
		Specifies the offset of external attenuation per input antenna relative to the reference antenna. For the reference
		antenna, the offset is fixed and set to 0 dB. \n
			:return: structure: for return value, see the help for AoffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:CTE:LENergy:AOFFset?', self.__class__.AoffsetStruct())
