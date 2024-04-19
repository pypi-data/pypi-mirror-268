from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McarrierCls:
	"""Mcarrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcarrier", core, parent)

	def set(self, meas_carrier: enums.MeasCarrier, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CAGGregation:MCARrier \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.caggregation.mcarrier.set(meas_carrier = enums.MeasCarrier.CC1, sEGMent = repcap.SEGMent.Default) \n
		Selects a component carrier for synchronization. \n
			:param meas_carrier: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
		"""
		param = Conversions.enum_scalar_to_str(meas_carrier, enums.MeasCarrier)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CAGGregation:MCARrier {param}')

	# noinspection PyTypeChecker
	def get(self, sEGMent=repcap.SEGMent.Default) -> enums.MeasCarrier:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CAGGregation:MCARrier \n
		Snippet: value: enums.MeasCarrier = driver.configure.nrMmwMeas.listPy.segment.caggregation.mcarrier.get(sEGMent = repcap.SEGMent.Default) \n
		Selects a component carrier for synchronization. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: meas_carrier: No help available"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CAGGregation:MCARrier?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCarrier)
