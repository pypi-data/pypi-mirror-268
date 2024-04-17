from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: decimal 'Reliability indicator'
			- Seg_Reliability: int: decimal Reliability indicator for the segment. The meaning of the returned values is the same as for the common reliability indicator, see previous parameter.
			- Out_Of_Tol: float: float Percentage of measured bursts with failed limit check Range: 0 % to 100 % , Unit: %
			- Nominal_Power: float: float Average power during the carrier-on state Range: -99.99 dBm to 99.99 dBm, Unit: dBm
			- Delta_F_1_Avg: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz
			- Delta_F_1_Min: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz
			- Delta_F_1_Max: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz
			- Delta_F_2_Avg: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz
			- Delta_F_2_Min: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz
			- Delta_F_2_Max: float: float Frequency deviation results (BR, LE) Range: 0 Hz to 250 kHz , Unit: Hz"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_float('Out_Of_Tol'),
			ArgStruct.scalar_float('Nominal_Power'),
			ArgStruct.scalar_float('Delta_F_1_Avg'),
			ArgStruct.scalar_float('Delta_F_1_Min'),
			ArgStruct.scalar_float('Delta_F_1_Max'),
			ArgStruct.scalar_float('Delta_F_2_Avg'),
			ArgStruct.scalar_float('Delta_F_2_Min'),
			ArgStruct.scalar_float('Delta_F_2_Max')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Out_Of_Tol: float = None
			self.Nominal_Power: float = None
			self.Delta_F_1_Avg: float = None
			self.Delta_F_1_Min: float = None
			self.Delta_F_1_Max: float = None
			self.Delta_F_2_Avg: float = None
			self.Delta_F_2_Min: float = None
			self.Delta_F_2_Max: float = None

	def fetch(self, segment=repcap.Segment.Default) -> FetchStruct:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>:MODulation:MINimum \n
		Snippet: value: FetchStruct = driver.multiEval.listPy.segment.modulation.minimum.fetch(segment = repcap.Segment.Default) \n
		Returns modulation single value results for segment<no> in list mode. The command returns all parameters listed below,
		independent of the selected list mode setup. However, only for some of the parameters measured values are available. For
		the other parameters, only an indicator is returned (e.g. NAV) . \n
			:param segment: optional repeated capability selector. Default value: S1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		return self._core.io.query_struct(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:LIST:SEGMent{segment_cmd_val}:MODulation:MINimum?', self.__class__.FetchStruct())
