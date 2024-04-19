from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SusageCls:
	"""Susage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("susage", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Dl_Slots: int: No parameter help available
			- Ul_Slots: int: No parameter help available
			- Period: int: No parameter help available
			- Used_Slots: List[enums.UsedSlots]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Dl_Slots'),
			ArgStruct.scalar_int('Ul_Slots'),
			ArgStruct.scalar_int('Period'),
			ArgStruct('Used_Slots', DataType.EnumList, enums.UsedSlots, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dl_Slots: int = None
			self.Ul_Slots: int = None
			self.Period: int = None
			self.Used_Slots: List[enums.UsedSlots] = None

	def get(self, sc_spacing: enums.ScSpacing) -> GetStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:SUSage \n
		Snippet: value: GetStruct = driver.configure.nrMmwMeas.susage.get(sc_spacing = enums.ScSpacing.S120k) \n
		No command help available \n
			:param sc_spacing: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.enum_scalar_to_str(sc_spacing, enums.ScSpacing)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:SUSage? {param}', self.__class__.GetStruct())
