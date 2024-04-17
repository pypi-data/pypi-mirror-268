from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PerCls:
	"""Per commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("per", core, parent)

	@property
	def rxPackets(self):
		"""rxPackets commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rxPackets'):
			from .RxPackets import RxPacketsCls
			self._rxPackets = RxPacketsCls(self._core, self._cmd_group)
		return self._rxPackets

	def fetch(self) -> float:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:RXQuality:PER \n
		Snippet: value: float = driver.rxQuality.per.fetch() \n
		Queries the PER results for the specified Tx level of R&S CMW. \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: result: float Packet error rate"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:RXQuality:PER?', suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'PerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
