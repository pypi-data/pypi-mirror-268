from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetupCls:
	"""Setup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	def set(self, segment_length: int, level: float, band: enums.Band, retrigger_flag: enums.RetriggerFlag, evaluat_offset: int, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.setup.set(segment_length = 1, level = 1.0, band = enums.Band.B257, retrigger_flag = enums.RetriggerFlag.IFPower, evaluat_offset = 1, sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		Send this command and the other segment configuration commands for all segments to be measured (method RsCMPX_NrFr2Meas.
		Configure.NrMmwMeas.ListPy.Lrange.set) . \n
			:param segment_length: Number of subframes in the segment
			:param level: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			:param band: Frequency band used in the segment
			:param retrigger_flag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. OFF: measure the segment without retrigger ON: wait for a trigger event from the trigger source configured via TRIGger:NRMMw:MEASi:MEValuation:SOURce IFPower: wait for a trigger event from the trigger source IF Power
			:param evaluat_offset: Number of subframes at the beginning of the segment that are not evaluated.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('segment_length', segment_length, DataType.Integer), ArgSingle('level', level, DataType.Float), ArgSingle('band', band, DataType.Enum, enums.Band), ArgSingle('retrigger_flag', retrigger_flag, DataType.Enum, enums.RetriggerFlag), ArgSingle('evaluat_offset', evaluat_offset, DataType.Integer))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup {param}'.rstrip())

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Response structure. Fields: \n
			- Segment_Length: int: Number of subframes in the segment
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the specifications document.
			- Band: enums.Band: Frequency band used in the segment
			- Retrigger_Flag: enums.RetriggerFlag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. OFF: measure the segment without retrigger ON: wait for a trigger event from the trigger source configured via TRIGger:NRMMw:MEASi:MEValuation:SOURce IFPower: wait for a trigger event from the trigger source IF Power
			- Evaluat_Offset: int: Number of subframes at the beginning of the segment that are not evaluated."""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Band: enums.Band = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None

	def get(self, sEGMent=repcap.SEGMent.Default) -> SetupStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet: value: SetupStruct = driver.configure.nrMmwMeas.listPy.segment.setup.get(sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		Send this command and the other segment configuration commands for all segments to be measured (method RsCMPX_NrFr2Meas.
		Configure.NrMmwMeas.ListPy.Lrange.set) . \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup?', self.__class__.SetupStruct())
