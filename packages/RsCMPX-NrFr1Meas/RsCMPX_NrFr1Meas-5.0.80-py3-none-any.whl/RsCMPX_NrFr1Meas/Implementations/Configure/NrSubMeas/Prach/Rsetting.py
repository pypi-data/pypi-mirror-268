from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsettingCls:
	"""Rsetting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsetting", core, parent)

	# noinspection PyTypeChecker
	def get(self, restricted_set: enums.RestrictedSet) -> enums.RestrictedSet:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:RSETting \n
		Snippet: value: enums.RestrictedSet = driver.configure.nrSubMeas.prach.rsetting.get(restricted_set = enums.RestrictedSet.URES) \n
		No command help available \n
			:param restricted_set: No help available
			:return: restricted_set: No help available"""
		param = Conversions.enum_scalar_to_str(restricted_set, enums.RestrictedSet)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:RSETting? {param}')
		return Conversions.str_to_scalar_enum(response, enums.RestrictedSet)
