from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPyCls:
	"""ListPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("listPy", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ListMode:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:LIST:MODE \n
		Snippet: value: enums.ListMode = driver.trigger.nrMmwMeas.listPy.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:LIST:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ListMode)

	def set_mode(self, mode: enums.ListMode) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:LIST:MODE \n
		Snippet: driver.trigger.nrMmwMeas.listPy.set_mode(mode = enums.ListMode.ONCE) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ListMode)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:LIST:MODE {param}')
