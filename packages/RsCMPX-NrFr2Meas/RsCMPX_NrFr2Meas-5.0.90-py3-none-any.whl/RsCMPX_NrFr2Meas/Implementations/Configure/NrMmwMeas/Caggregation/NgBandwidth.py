from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NgBandwidthCls:
	"""NgBandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ngBandwidth", core, parent)

	def get_aggregated(self) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:NGBandwidth:AGGRegated \n
		Snippet: value: float = driver.configure.nrMmwMeas.caggregation.ngBandwidth.get_aggregated() \n
		No command help available \n
			:return: agg_bandwidth: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:NGBandwidth:AGGRegated?')
		return Conversions.str_to_float(response)
