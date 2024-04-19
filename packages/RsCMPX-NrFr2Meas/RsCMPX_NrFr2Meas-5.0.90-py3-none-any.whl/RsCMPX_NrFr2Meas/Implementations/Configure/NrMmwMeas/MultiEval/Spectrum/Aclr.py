from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AclrCls:
	"""Aclr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aclr", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.spectrum.aclr.get_enable() \n
		No command help available \n
			:return: nr: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, nr: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: driver.configure.nrMmwMeas.multiEval.spectrum.aclr.set_enable(nr = False) \n
		No command help available \n
			:param nr: No help available
		"""
		param = Conversions.bool_to_str(nr)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle {param}')
