from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffsetCls:
	"""IqOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqOffset", core, parent)

	def set(self, enable: bool, offset_0: float, offset_1: float, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IQOFfset \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.qam.iqOffset.set(enable = False, offset_0 = 1.0, offset_1 = 1.0, qam = repcap.Qam.Default) \n
		Defines upper limits for the I/Q origin offset (QAM modulations) . Two different I/Q origin offset limits can be set for
		two TX power ranges. \n
			:param enable: OFF: disables the limit check ON: enables the limit check
			:param offset_0: I/Q origin offset limit for high TX power range
			:param offset_1: I/Q origin offset limit for low TX power range
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('offset_0', offset_0, DataType.Float), ArgSingle('offset_1', offset_1, DataType.Float))
		qam_cmd_val = self._cmd_group.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IQOFfset {param}'.rstrip())

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Offset_0: float: I/Q origin offset limit for high TX power range
			- Offset_1: float: I/Q origin offset limit for low TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Offset_0: float = None
			self.Offset_1: float = None

	def get(self, qam=repcap.Qam.Default) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrMmwMeas.multiEval.limit.qam.iqOffset.get(qam = repcap.Qam.Default) \n
		Defines upper limits for the I/Q origin offset (QAM modulations) . Two different I/Q origin offset limits can be set for
		two TX power ranges. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		qam_cmd_val = self._cmd_group.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IQOFfset?', self.__class__.IqOffsetStruct())
