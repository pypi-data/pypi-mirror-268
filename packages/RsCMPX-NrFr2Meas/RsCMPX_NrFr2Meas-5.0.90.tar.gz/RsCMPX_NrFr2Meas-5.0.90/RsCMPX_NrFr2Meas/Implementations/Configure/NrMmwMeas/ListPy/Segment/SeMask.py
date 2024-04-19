from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMaskCls:
	"""SeMask commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seMask", core, parent)

	def set(self, sem_statistics: int, sem_enable: bool, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SEMask \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.seMask.set(sem_statistics = 1, sem_enable = False, sEGMent = repcap.SEGMent.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param sem_statistics: Statistical length in slots
			:param sem_enable: Enable or disable the measurement of spectrum emission results.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sem_statistics', sem_statistics, DataType.Integer), ArgSingle('sem_enable', sem_enable, DataType.Boolean))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SEMask {param}'.rstrip())

	# noinspection PyTypeChecker
	class SeMaskStruct(StructBase):
		"""Response structure. Fields: \n
			- Sem_Statistics: int: Statistical length in slots
			- Sem_Enable: bool: Enable or disable the measurement of spectrum emission results."""
		__meta_args_list = [
			ArgStruct.scalar_int('Sem_Statistics'),
			ArgStruct.scalar_bool('Sem_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sem_Statistics: int = None
			self.Sem_Enable: bool = None

	def get(self, sEGMent=repcap.SEGMent.Default) -> SeMaskStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SEMask \n
		Snippet: value: SeMaskStruct = driver.configure.nrMmwMeas.listPy.segment.seMask.get(sEGMent = repcap.SEGMent.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SeMaskStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SEMask?', self.__class__.SeMaskStruct())
