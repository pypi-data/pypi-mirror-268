from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatnessCls:
	"""EsFlatness commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("esFlatness", core, parent)

	def set(self, enable: bool, range_1: float, range_2: float, max_1_min_2: float, max_2_min_1: float, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:ESFLatness \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.qam.esFlatness.set(enable = False, range_1 = 1.0, range_2 = 1.0, max_1_min_2 = 1.0, max_2_min_1 = 1.0, qam = repcap.Qam.Default) \n
		Defines limits for the equalizer spectrum flatness (QAM modulations) . \n
			:param enable: OFF: disables the limit check ON: enables the limit check
			:param range_1: Upper limit for max(range 1) - min(range 1)
			:param range_2: Upper limit for max(range 2) - min(range 2)
			:param max_1_min_2: Upper limit for max(range 1) - min(range 2)
			:param max_2_min_1: Upper limit for max(range 2) - min(range 1)
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('range_1', range_1, DataType.Float), ArgSingle('range_2', range_2, DataType.Float), ArgSingle('max_1_min_2', max_1_min_2, DataType.Float), ArgSingle('max_2_min_1', max_2_min_1, DataType.Float))
		qam_cmd_val = self._cmd_group.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:ESFLatness {param}'.rstrip())

	# noinspection PyTypeChecker
	class EsFlatnessStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Range_1: float: Upper limit for max(range 1) - min(range 1)
			- Range_2: float: Upper limit for max(range 2) - min(range 2)
			- Max_1_Min_2: float: Upper limit for max(range 1) - min(range 2)
			- Max_2_Min_1: float: Upper limit for max(range 2) - min(range 1)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Range_1'),
			ArgStruct.scalar_float('Range_2'),
			ArgStruct.scalar_float('Max_1_Min_2'),
			ArgStruct.scalar_float('Max_2_Min_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Range_1: float = None
			self.Range_2: float = None
			self.Max_1_Min_2: float = None
			self.Max_2_Min_1: float = None

	def get(self, qam=repcap.Qam.Default) -> EsFlatnessStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:ESFLatness \n
		Snippet: value: EsFlatnessStruct = driver.configure.nrMmwMeas.multiEval.limit.qam.esFlatness.get(qam = repcap.Qam.Default) \n
		Defines limits for the equalizer spectrum flatness (QAM modulations) . \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for EsFlatnessStruct structure arguments."""
		qam_cmd_val = self._cmd_group.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:ESFLatness?', self.__class__.EsFlatnessStruct())
