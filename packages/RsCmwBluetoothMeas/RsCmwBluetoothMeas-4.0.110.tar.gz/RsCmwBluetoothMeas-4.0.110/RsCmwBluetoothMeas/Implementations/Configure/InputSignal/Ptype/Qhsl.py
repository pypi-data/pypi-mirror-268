from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QhslCls:
	"""Qhsl commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qhsl", core, parent)

	# noinspection PyTypeChecker
	def get_p_2_q(self) -> enums.PacketTypeQhsl:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P2Q \n
		Snippet: value: enums.PacketTypeQhsl = driver.configure.inputSignal.ptype.qhsl.get_p_2_q() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P2Q?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeQhsl)

	def set_p_2_q(self, packet_type: enums.PacketTypeQhsl) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P2Q \n
		Snippet: driver.configure.inputSignal.ptype.qhsl.set_p_2_q(packet_type = enums.PacketTypeQhsl.DATA) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeQhsl)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P2Q {param}')

	# noinspection PyTypeChecker
	def get_p_3_q(self) -> enums.PacketTypeQhsl:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P3Q \n
		Snippet: value: enums.PacketTypeQhsl = driver.configure.inputSignal.ptype.qhsl.get_p_3_q() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P3Q?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeQhsl)

	def set_p_3_q(self, packet_type: enums.PacketTypeQhsl) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P3Q \n
		Snippet: driver.configure.inputSignal.ptype.qhsl.set_p_3_q(packet_type = enums.PacketTypeQhsl.DATA) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeQhsl)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P3Q {param}')

	# noinspection PyTypeChecker
	def get_p_4_q(self) -> enums.PacketTypeQhsl:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P4Q \n
		Snippet: value: enums.PacketTypeQhsl = driver.configure.inputSignal.ptype.qhsl.get_p_4_q() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P4Q?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeQhsl)

	def set_p_4_q(self, packet_type: enums.PacketTypeQhsl) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P4Q \n
		Snippet: driver.configure.inputSignal.ptype.qhsl.set_p_4_q(packet_type = enums.PacketTypeQhsl.DATA) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeQhsl)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P4Q {param}')

	# noinspection PyTypeChecker
	def get_p_5_q(self) -> enums.PacketTypeQhsl:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P5Q \n
		Snippet: value: enums.PacketTypeQhsl = driver.configure.inputSignal.ptype.qhsl.get_p_5_q() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P5Q?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeQhsl)

	def set_p_5_q(self, packet_type: enums.PacketTypeQhsl) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P5Q \n
		Snippet: driver.configure.inputSignal.ptype.qhsl.set_p_5_q(packet_type = enums.PacketTypeQhsl.DATA) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeQhsl)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P5Q {param}')

	# noinspection PyTypeChecker
	def get_p_6_q(self) -> enums.PacketTypeQhsl:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P6Q \n
		Snippet: value: enums.PacketTypeQhsl = driver.configure.inputSignal.ptype.qhsl.get_p_6_q() \n
		No command help available \n
			:return: packet_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P6Q?')
		return Conversions.str_to_scalar_enum(response, enums.PacketTypeQhsl)

	def set_p_6_q(self, packet_type: enums.PacketTypeQhsl) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P6Q \n
		Snippet: driver.configure.inputSignal.ptype.qhsl.set_p_6_q(packet_type = enums.PacketTypeQhsl.DATA) \n
		No command help available \n
			:param packet_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(packet_type, enums.PacketTypeQhsl)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PTYPe:QHSL:P6Q {param}')
