from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SacpCls:
	"""Sacp commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sacp", core, parent)

	def set(self, ptx_limit: float, exc_ptx_limit: float, no_of_ex_limit: int, ptx_enable: bool, no_of_exc_enable: bool) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:SACP \n
		Snippet: driver.configure.multiEval.limit.lowEnergy.le2M.sacp.set(ptx_limit = 1.0, exc_ptx_limit = 1.0, no_of_ex_limit = 1, ptx_enable = False, no_of_exc_enable = False) \n
		These commands define and enable the 'Spectrum ACP' limits for BR (...:LIMit:SACP) , LE 1M PHY ( ...:LE1M...) , LE 2M PHY
		(...:LE2M...) , and LE coded PHY (...:LRANge...) , respectively. \n
			:param ptx_limit: numeric Power limit for 1 MHz channels fTX± 2 MHz Range: -80 dBm to -10 dBm
			:param exc_ptx_limit: numeric Power limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... Range: -80 dBm to -10 dBm
			:param no_of_ex_limit: numeric Maximum number of tolerable exceptions, i.e. 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... whose power is above ExcPTxLimit, but below PTxLimit Range: 0 to 16
			:param ptx_enable: OFF | ON Disables | enables the PTxLimit limit for 1 MHz channels fTX± 2 MHz
			:param no_of_exc_enable: OFF | ON Disables | enables the ExcPTxLimit limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... with NoOfExLimit tolerable exceptions (per statistic cycle) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ptx_limit', ptx_limit, DataType.Float), ArgSingle('exc_ptx_limit', exc_ptx_limit, DataType.Float), ArgSingle('no_of_ex_limit', no_of_ex_limit, DataType.Integer), ArgSingle('ptx_enable', ptx_enable, DataType.Boolean), ArgSingle('no_of_exc_enable', no_of_exc_enable, DataType.Boolean))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:SACP {param}'.rstrip())

	# noinspection PyTypeChecker
	class SacpStruct(StructBase):
		"""Response structure. Fields: \n
			- Ptx_Limit: float: numeric Power limit for 1 MHz channels fTX± 2 MHz Range: -80 dBm to -10 dBm
			- Exc_Ptx_Limit: float: numeric Power limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... Range: -80 dBm to -10 dBm
			- No_Of_Ex_Limit: int: numeric Maximum number of tolerable exceptions, i.e. 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... whose power is above ExcPTxLimit, but below PTxLimit Range: 0 to 16
			- Ptx_Enable: bool: OFF | ON Disables | enables the PTxLimit limit for 1 MHz channels fTX± 2 MHz
			- No_Of_Exc_Enable: bool: OFF | ON Disables | enables the ExcPTxLimit limit for 1 MHz channels fTX±3 MHz, fTX±4 MHz, ... with NoOfExLimit tolerable exceptions (per statistic cycle) ."""
		__meta_args_list = [
			ArgStruct.scalar_float('Ptx_Limit'),
			ArgStruct.scalar_float('Exc_Ptx_Limit'),
			ArgStruct.scalar_int('No_Of_Ex_Limit'),
			ArgStruct.scalar_bool('Ptx_Enable'),
			ArgStruct.scalar_bool('No_Of_Exc_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Ptx_Limit: float = None
			self.Exc_Ptx_Limit: float = None
			self.No_Of_Ex_Limit: int = None
			self.Ptx_Enable: bool = None
			self.No_Of_Exc_Enable: bool = None

	def get(self) -> SacpStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:SACP \n
		Snippet: value: SacpStruct = driver.configure.multiEval.limit.lowEnergy.le2M.sacp.get() \n
		These commands define and enable the 'Spectrum ACP' limits for BR (...:LIMit:SACP) , LE 1M PHY ( ...:LE1M...) , LE 2M PHY
		(...:LE2M...) , and LE coded PHY (...:LRANge...) , respectively. \n
			:return: structure: for return value, see the help for SacpStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:MEValuation:LIMit:LENergy:LE2M:SACP?', self.__class__.SacpStruct())
