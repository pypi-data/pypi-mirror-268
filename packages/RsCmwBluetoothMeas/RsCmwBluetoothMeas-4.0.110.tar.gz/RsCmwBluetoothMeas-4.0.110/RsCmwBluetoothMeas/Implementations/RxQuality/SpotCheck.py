from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ...Internal.Types import DataType
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpotCheckCls:
	"""SpotCheck commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spotCheck", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.Result:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck \n
		Snippet: value: enums.Result = driver.rxQuality.spotCheck.fetch() \n
		Queries the verdict of spot check. \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: spot_check_result: FAIL | PASS FAIL: no expected response from the EUT detected within advertising event PASS: SCAN_RSP detected"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:RXQuality:SPOTcheck?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Result)
