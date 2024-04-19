from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MslotCls:
	"""Mslot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mslot", core, parent)

	def set(self, measure_slot: enums.MeasureSlot, meas_slot_no: int = None) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MSLot \n
		Snippet: driver.configure.nrMmwMeas.multiEval.mslot.set(measure_slot = enums.MeasureSlot.ALL, meas_slot_no = 1) \n
		Selects which slots of the captured subframes of the first radio frame are evaluated. \n
			:param measure_slot: UDEF: single slot selected via MeasSlotNo ALL: all scheduled UL slots
			:param meas_slot_no: Slot number for MeasureSlot=UDEF The slot must be in the first radio frame. The number of slots per subframe depends on the SCS. And the slot must be within the captured number of subframes, see method RsCMPX_NrFr2Meas.Configure.NrMmwMeas.MultiEval.nsubFrames.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('measure_slot', measure_slot, DataType.Enum, enums.MeasureSlot), ArgSingle('meas_slot_no', meas_slot_no, DataType.Integer, None, is_optional=True))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MSLot {param}'.rstrip())

	# noinspection PyTypeChecker
	class MslotStruct(StructBase):
		"""Response structure. Fields: \n
			- Measure_Slot: enums.MeasureSlot: UDEF: single slot selected via MeasSlotNo ALL: all scheduled UL slots
			- Meas_Slot_No: int: Slot number for MeasureSlot=UDEF The slot must be in the first radio frame. The number of slots per subframe depends on the SCS. And the slot must be within the captured number of subframes, see [CMDLINKRESOLVED Configure.NrMmwMeas.MultiEval#NsubFrames CMDLINKRESOLVED]."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Measure_Slot', enums.MeasureSlot),
			ArgStruct.scalar_int('Meas_Slot_No')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Measure_Slot: enums.MeasureSlot = None
			self.Meas_Slot_No: int = None

	def get(self) -> MslotStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MSLot \n
		Snippet: value: MslotStruct = driver.configure.nrMmwMeas.multiEval.mslot.get() \n
		Selects which slots of the captured subframes of the first radio frame are evaluated. \n
			:return: structure: for return value, see the help for MslotStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MSLot?', self.__class__.MslotStruct())
