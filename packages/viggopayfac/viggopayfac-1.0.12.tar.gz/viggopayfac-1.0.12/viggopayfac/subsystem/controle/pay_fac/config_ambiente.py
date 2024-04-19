from viggopayfac.subsystem.controle.configuracao_pay_fac.resource \
    import ConfiguracaoPayFacTipo as cpf_tipo


def get_api_payfac():
    # TODO(JorgeSilva): trocar por ambiente de PRODUCAO antes de subir
    return cpf_tipo.HOMOLOGACAO
