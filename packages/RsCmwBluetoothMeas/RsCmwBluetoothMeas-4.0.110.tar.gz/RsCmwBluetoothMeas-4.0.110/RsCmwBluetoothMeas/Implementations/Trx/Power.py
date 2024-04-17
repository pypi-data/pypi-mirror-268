from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Out_Of_Tol: float: float Out of tolerance result, i.e. percentage of measurement intervals of the statistic count ([CMDLINKRESOLVED Configure.MultiEval.Scount#PowerVsTime CMDLINKRESOLVED]) exceeding the specified limits, see [CMDLINKRESOLVED Configure.MultiEval.Limit.LowEnergy.Le1M.PowerVsTime#set CMDLINKRESOLVED]. Range: 0 % to 100 %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -128.0 dBm to 130.0 dBm , Unit: dBm
			- Peak_Power: float: float Peak power during the carrier-on state Range: -128.0 dBm to 130.0 dBm , Unit: dBm
			- Leakage_Power: float: float Average power during the carrier-off state Range: -128.0 dBm to 130.0 dBm , Unit: dBm
			- Peak_Min_Avg_Pow: float: float Peak power minus average power Range: 0 dB to 158 dB , Unit: dB"""
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
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:TRX:POWer \n
		Snippet: value: FetchStruct = driver.trx.power.fetch() \n
		Returns the power results for TX-RX measurements on advertiser packets LE 1M PHY (uncoded) .
		See also 'View TX Measurement - power vs time statistics'. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:TRX:POWer?', self.__class__.FetchStruct())
