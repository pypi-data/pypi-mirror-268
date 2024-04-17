from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SensitivityCls:
	"""Sensitivity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sensitivity", core, parent)

	def fetch(self) -> float:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity \n
		Snippet: value: float = driver.rxQuality.sensitivity.fetch() \n
		Queries the results of sensitivity search measurements for a target PER. \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: sensitivity_search: float Determined Tx level of R&S CMW for the specified PER value. Range: -120 dBm to 0 dBm"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity?', suppressed)
		return Conversions.str_to_float(response)
