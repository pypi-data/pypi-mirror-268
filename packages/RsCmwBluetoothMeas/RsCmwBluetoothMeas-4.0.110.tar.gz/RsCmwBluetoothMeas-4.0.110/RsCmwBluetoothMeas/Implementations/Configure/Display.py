from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Types import DataType
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DisplayCls:
	"""Display commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def set(self, measurement: enums.DisplayMeasurement, view: enums.DisplayView = None) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DISPlay \n
		Snippet: driver.configure.display.set(measurement = enums.DisplayMeasurement.MEV, view = enums.DisplayView.DEVM) \n
		Selects the view to be displayed. \n
			:param measurement: MEV Multi-evaluation measurement
			:param view: PVTime | FDEViation | SACP | MODulation | POWer | OVERview | DEVM | PDIFference | IQABs | IQDiff | IQERr | SOBW | SGACp | FRANge | PENCoding OVERview: 'Overview' PVTime: 'Power vs Time' DEVM: 'DEVM' (EDR) PDIFference: 'Phase Difference' (EDR) IQABs: 'IQ Constellation Absolute' (EDR) IQDiff: 'IQ Constellation Differential' (EDR) IQERr: 'IQ Constellation Error' (EDR) SACP: 'Spectrum ACP' (BR, LE) MODulation: 'Modulation Scalars' POWer: 'Power Scalars' FDEViation: 'Frequency Deviation' (BR, LE) SOBW: 'Spectrum 20 dB Bandwidth' (BR) SGACp: 'Spectrum Gated ACP' (EDR) FRANge: 'Frequency Range' (BR) PENCoding: 'Differential Phase Encoding' (EDR)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('measurement', measurement, DataType.Enum, enums.DisplayMeasurement), ArgSingle('view', view, DataType.Enum, enums.DisplayView, is_optional=True))
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:DISPlay {param}'.rstrip())

	# noinspection PyTypeChecker
	class DisplayStruct(StructBase):
		"""Response structure. Fields: \n
			- Measurement: enums.DisplayMeasurement: MEV Multi-evaluation measurement
			- View: enums.DisplayView: PVTime | FDEViation | SACP | MODulation | POWer | OVERview | DEVM | PDIFference | IQABs | IQDiff | IQERr | SOBW | SGACp | FRANge | PENCoding OVERview: 'Overview' PVTime: 'Power vs Time' DEVM: 'DEVM' (EDR) PDIFference: 'Phase Difference' (EDR) IQABs: 'IQ Constellation Absolute' (EDR) IQDiff: 'IQ Constellation Differential' (EDR) IQERr: 'IQ Constellation Error' (EDR) SACP: 'Spectrum ACP' (BR, LE) MODulation: 'Modulation Scalars' POWer: 'Power Scalars' FDEViation: 'Frequency Deviation' (BR, LE) SOBW: 'Spectrum 20 dB Bandwidth' (BR) SGACp: 'Spectrum Gated ACP' (EDR) FRANge: 'Frequency Range' (BR) PENCoding: 'Differential Phase Encoding' (EDR)"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Measurement', enums.DisplayMeasurement),
			ArgStruct.scalar_enum('View', enums.DisplayView)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Measurement: enums.DisplayMeasurement = None
			self.View: enums.DisplayView = None

	def get(self) -> DisplayStruct:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:DISPlay \n
		Snippet: value: DisplayStruct = driver.configure.display.get() \n
		Selects the view to be displayed. \n
			:return: structure: for return value, see the help for DisplayStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:BLUetooth:MEASurement<Instance>:DISPlay?', self.__class__.DisplayStruct())
