from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	def set(self, enable: bool, frequency_start: float, frequency_end: float, level: float, rbw: enums.RbwA, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:CAGGregation \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.seMask.area.caggregation.set(enable = False, frequency_start = 1.0, frequency_end = 1.0, level = 1.0, rbw = enums.RbwA.K120, area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <area>. The activation state, the area borders, an upper
		limit and the resolution bandwidth must be specified. The emission mask applies to carrier aggregation (aggregated
		bandwidth) . \n
			:param enable: OFF: disables the check of these requirements ON: enables the check of these requirements
			:param frequency_start: Start frequency of the area = FrequencyStart * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth.
			:param frequency_end: Stop frequency of the area = FrequencyEnd * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth.
			:param level: Upper limit for the area.
			:param rbw: Resolution bandwidth to be used for the area, 120 kHz or 1 MHz.
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('frequency_start', frequency_start, DataType.Float), ArgSingle('frequency_end', frequency_end, DataType.Float), ArgSingle('level', level, DataType.Float), ArgSingle('rbw', rbw, DataType.Enum, enums.RbwA))
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:CAGGregation {param}'.rstrip())

	# noinspection PyTypeChecker
	class CaggregationStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area = FrequencyStart * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth.
			- Frequency_End: float: Stop frequency of the area = FrequencyEnd * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth.
			- Level: float: Upper limit for the area.
			- Rbw: enums.RbwA: Resolution bandwidth to be used for the area, 120 kHz or 1 MHz."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.RbwA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.RbwA = None

	def get(self, area=repcap.Area.Default) -> CaggregationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:CAGGregation \n
		Snippet: value: CaggregationStruct = driver.configure.nrMmwMeas.multiEval.limit.seMask.area.caggregation.get(area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <area>. The activation state, the area borders, an upper
		limit and the resolution bandwidth must be specified. The emission mask applies to carrier aggregation (aggregated
		bandwidth) . \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for CaggregationStruct structure arguments."""
		area_cmd_val = self._cmd_group.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:CAGGregation?', self.__class__.CaggregationStruct())
