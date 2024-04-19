from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, mod_statistics: int, modenable: bool, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:MODulation \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.modulation.set(mod_statistics = 1, modenable = False, sEGMent = repcap.SEGMent.Default) \n
		Defines settings for modulation measurements in list mode for segment <no>. \n
			:param mod_statistics: Statistical length in slots
			:param modenable: Enable or disable the measurement of modulation results.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('mod_statistics', mod_statistics, DataType.Integer), ArgSingle('modenable', modenable, DataType.Boolean))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:MODulation {param}'.rstrip())

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Response structure. Fields: \n
			- Mod_Statistics: int: Statistical length in slots
			- Modenable: bool: Enable or disable the measurement of modulation results."""
		__meta_args_list = [
			ArgStruct.scalar_int('Mod_Statistics'),
			ArgStruct.scalar_bool('Modenable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mod_Statistics: int = None
			self.Modenable: bool = None

	def get(self, sEGMent=repcap.SEGMent.Default) -> ModulationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:MODulation \n
		Snippet: value: ModulationStruct = driver.configure.nrMmwMeas.listPy.segment.modulation.get(sEGMent = repcap.SEGMent.Default) \n
		Defines settings for modulation measurements in list mode for segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:MODulation?', self.__class__.ModulationStruct())
