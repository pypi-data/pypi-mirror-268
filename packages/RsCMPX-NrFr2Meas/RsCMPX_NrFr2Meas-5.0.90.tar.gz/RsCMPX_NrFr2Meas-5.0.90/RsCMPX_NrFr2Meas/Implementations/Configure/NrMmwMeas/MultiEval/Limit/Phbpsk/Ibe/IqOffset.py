from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffsetCls:
	"""IqOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqOffset", core, parent)

	def set(self, offset_0: float, offset_1: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:IBE:IQOFfset \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.phbpsk.ibe.iqOffset.set(offset_0 = 1.0, offset_1 = 1.0) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the in-band emission, for π/2-BPSK modulation.
		Two different values can be set for two TX power ranges. \n
			:param offset_0: I/Q origin offset limit for high TX power range
			:param offset_1: I/Q origin offset limit for low TX power range
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('offset_0', offset_0, DataType.Float), ArgSingle('offset_1', offset_1, DataType.Float))
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:IBE:IQOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Offset_0: float: I/Q origin offset limit for high TX power range
			- Offset_1: float: I/Q origin offset limit for low TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_0: float = None
			self.Offset_1: float = None

	def get(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:IBE:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrMmwMeas.multiEval.limit.phbpsk.ibe.iqOffset.get() \n
		Defines I/Q origin offset values used for calculation of an upper limit for the in-band emission, for π/2-BPSK modulation.
		Two different values can be set for two TX power ranges. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:PHBPsk:IBE:IQOFfset?', self.__class__.IqOffsetStruct())
