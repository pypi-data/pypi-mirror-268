from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YieldPyCls:
	"""YieldPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("yieldPy", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:YIELd \n
		Snippet: value: List[float] = driver.multiEval.modulation.lowEnergy.le2M.yieldPy.fetch() \n
		Returns the percentages of auto-detected LE packets with a particular pattern type. Commands for uncoded LE 1M PHY (..
		:LE1M..) and LE 2M PHY (..:LE2M..) are available. A result is available after the R&S CMW has auto-detected a packet
		(method RsCmwBluetoothMeas.Configure.InputSignal.dmodeAUTO) . \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: pattern_yield: float Pattern yield for 11110000 patterns, 10101010 patterns, and any other patterns (3 values) Range: 0 to 100, Unit: %"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:MEValuation:MODulation:LENergy:LE2M:YIELd?', suppressed)
		return response
