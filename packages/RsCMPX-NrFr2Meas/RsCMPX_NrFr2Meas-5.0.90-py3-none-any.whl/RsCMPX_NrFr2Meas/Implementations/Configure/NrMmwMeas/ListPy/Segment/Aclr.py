from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	def set(self, aclr_statistics: int, aclr_enable: bool, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:ACLR \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.aclr.set(aclr_statistics = 1, aclr_enable = False, sEGMent = repcap.SEGMent.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param aclr_statistics: Statistical length in slots
			:param aclr_enable: Enable or disable the measurement of ACLR results.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('aclr_statistics', aclr_statistics, DataType.Integer), ArgSingle('aclr_enable', aclr_enable, DataType.Boolean))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:ACLR {param}'.rstrip())

	# noinspection PyTypeChecker
	class AclrStruct(StructBase):
		"""Response structure. Fields: \n
			- Aclr_Statistics: int: Statistical length in slots
			- Aclr_Enable: bool: Enable or disable the measurement of ACLR results."""
		__meta_args_list = [
			ArgStruct.scalar_int('Aclr_Statistics'),
			ArgStruct.scalar_bool('Aclr_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aclr_Statistics: int = None
			self.Aclr_Enable: bool = None

	def get(self, sEGMent=repcap.SEGMent.Default) -> AclrStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:ACLR \n
		Snippet: value: AclrStruct = driver.configure.nrMmwMeas.listPy.segment.aclr.get(sEGMent = repcap.SEGMent.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for AclrStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:ACLR?', self.__class__.AclrStruct())
