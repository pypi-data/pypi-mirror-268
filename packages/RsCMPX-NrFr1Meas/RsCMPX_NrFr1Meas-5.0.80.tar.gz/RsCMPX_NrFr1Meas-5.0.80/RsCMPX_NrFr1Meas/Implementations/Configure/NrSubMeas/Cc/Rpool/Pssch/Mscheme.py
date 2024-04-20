from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MschemeCls:
	"""Mscheme commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mscheme", core, parent)

	def set(self, mod_scheme: enums.ModulationSchemeB, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:MSCHeme \n
		Snippet: driver.configure.nrSubMeas.cc.rpool.pssch.mscheme.set(mod_scheme = enums.ModulationSchemeB.Q16, carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param mod_scheme: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(mod_scheme, enums.ModulationSchemeB)
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:MSCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> enums.ModulationSchemeB:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol:PSSCh:MSCHeme \n
		Snippet: value: enums.ModulationSchemeB = driver.configure.nrSubMeas.cc.rpool.pssch.mscheme.get(carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
			:return: mod_scheme: No help available"""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol:PSSCh:MSCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.ModulationSchemeB)
