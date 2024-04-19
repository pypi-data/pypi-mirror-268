from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def get_ew_length(self) -> List[int]:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWLength \n
		Snippet: value: List[int] = driver.configure.nrMmwMeas.prach.modulation.get_ew_length() \n
		Specifies the EVM window length in samples for all preamble formats. \n
			:return: evm_window_length: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWLength?')
		return response

	def set_ew_length(self, evm_window_length: List[int]) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWLength \n
		Snippet: driver.configure.nrMmwMeas.prach.modulation.set_ew_length(evm_window_length = [1, 2, 3]) \n
		Specifies the EVM window length in samples for all preamble formats. \n
			:param evm_window_length: No help available
		"""
		param = Conversions.list_to_csv_str(evm_window_length)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWLength {param}')

	# noinspection PyTypeChecker
	def get_ew_position(self) -> enums.LowHigh:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWPosition \n
		Snippet: value: enums.LowHigh = driver.configure.nrMmwMeas.prach.modulation.get_ew_position() \n
		Specifies the position of the EVM window used for calculation of the trace results. \n
			:return: evm_window_pos: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWPosition?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ew_position(self, evm_window_pos: enums.LowHigh) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWPosition \n
		Snippet: driver.configure.nrMmwMeas.prach.modulation.set_ew_position(evm_window_pos = enums.LowHigh.HIGH) \n
		Specifies the position of the EVM window used for calculation of the trace results. \n
			:param evm_window_pos: No help available
		"""
		param = Conversions.enum_scalar_to_str(evm_window_pos, enums.LowHigh)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:MODulation:EWPosition {param}')
