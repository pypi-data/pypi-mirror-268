from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FDEViation:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.fdeviation.current.fetch() \n
		Returns the values of the frequency deviation traces. The results of the current, average minimum and maximum traces can
		be retrieved. The frequency deviation traces are available for BR and LE bursts. See also 'PvT and frequency deviation
		trace points (classic) ' and 'PvT and modulation trace points (LE) ' \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: freq_deviation: float m frequency deviation results, depending on the packet type and payload length Range: –2 MHz to 2 MHz , Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FDEViation:CURRent?', suppressed)
		return response

	def read(self) -> List[float]:
		"""SCPI: READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FDEViation:CURRent \n
		Snippet: value: List[float] = driver.multiEval.trace.fdeviation.current.read() \n
		Returns the values of the frequency deviation traces. The results of the current, average minimum and maximum traces can
		be retrieved. The frequency deviation traces are available for BR and LE bursts. See also 'PvT and frequency deviation
		trace points (classic) ' and 'PvT and modulation trace points (LE) ' \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: freq_deviation: float m frequency deviation results, depending on the packet type and payload length Range: –2 MHz to 2 MHz , Unit: Hz"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:BLUetooth:MEASurement<Instance>:MEValuation:TRACe:FDEViation:CURRent?', suppressed)
		return response
