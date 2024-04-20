from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrbCls:
	"""Nrb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nrb", core, parent)

	def set(self, no_rbs: enums.SubChanSize, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSCCh:NRB \n
		Snippet: driver.configure.nrSubMeas.cc.rpool.pscch.nrb.set(no_rbs = enums.SubChanSize.RB10, carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param no_rbs: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(no_rbs, enums.SubChanSize)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSCCh:NRB {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> enums.SubChanSize:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSCCh:NRB \n
		Snippet: value: enums.SubChanSize = driver.configure.nrSubMeas.cc.rpool.pscch.nrb.get(carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
			:return: no_rbs: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSCCh:NRB?')
		return Conversions.str_to_scalar_enum(response, enums.SubChanSize)
