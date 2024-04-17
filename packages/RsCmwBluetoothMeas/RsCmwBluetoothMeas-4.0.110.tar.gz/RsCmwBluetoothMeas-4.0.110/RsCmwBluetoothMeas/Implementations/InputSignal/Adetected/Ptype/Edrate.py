from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EdrateCls:
	"""Edrate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edrate", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.EdrPacketType:
		"""SCPI: FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:EDRate \n
		Snippet: value: enums.EdrPacketType = driver.inputSignal.adetected.ptype.edrate.fetch() \n
		Returns the detected EDR packet type. A result is available after the R&S CMW has auto-detected a packet (method
		RsCmwBluetoothMeas.Configure.InputSignal.dmode AUTO) . \n
		Use RsCmwBluetoothMeas.reliability.last_value to read the updated reliability indicator. \n
			:return: packet_type: E21P | E23P | E25P | E31P | E33P | E35P 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, or 3-DH5 packets"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:BLUetooth:MEASurement<Instance>:ISIGnal:ADETected:PTYPe:EDRate?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.EdrPacketType)
