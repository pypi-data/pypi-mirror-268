from viggocore.common.subsystem import router


class Router(router.Router):

    def __init__(self, collection, routes=[]):
        super().__init__(collection, routes)
        self.collection_url = '/pay_facs'
        self.resource_url = '/pay_facs/<id>'

    @property
    def routes(self):
        return [
            {
                'action': 'Pega os dados do domain_account cadastrados ' +
                'na Matera',
                'method': 'POST',
                'url': self.collection_url + '/get_conta',
                'callback': 'get_conta'
            },
            {
                'action': 'Adiciona uma chave pix aleatória',
                'method': 'POST',
                'url': self.collection_url + '/add_chave_pix',
                'callback': 'add_chave_pix'
            },
            {
                'action': 'Lista as chaves pix ligadas a uma conta',
                'method': 'POST',
                'url': self.collection_url + '/list_chaves_pix',
                'callback': 'list_chaves_pix'
            },
            {
                'action': 'Lista transacoes de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_transacoes',
                'callback': 'get_transacoes'
            },
            {
                'action': 'Pega a ultima transacao de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_ultima_transacao',
                'callback': 'get_ultima_transacao'
            },
            {
                'action': 'Lista o extrato de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_extrato',
                'callback': 'get_extrato'
            },
            {
                'action': 'Pega o saldo de uma conta',
                'method': 'POST',
                'url': self.collection_url + '/get_saldo',
                'callback': 'get_saldo'
            },
            {
                'action': 'Realiza a retirada do dinheiro via pix',
                'method': 'POST',
                'url': self.collection_url + '/cashout_via_pix',
                'callback': 'cashout_via_pix'
            },
            {
                'action': 'Gera o QRCode a partir do pix',
                'method': 'POST',
                'url': self.collection_url + '/gerar_qrcode',
                'callback': 'gerar_qrcode'
            },
            {
                'action': 'Conculta os dados da chave pix do destinatario',
                'method': 'POST',
                'url': self.collection_url + '/consultar_alias_destinatario',
                'callback': 'consultar_alias_destinatario'
            },
            {
                'action': 'Gera o QRCode de Cobrança a partir do pix',
                'method': 'POST',
                'url': self.collection_url + '/gerar_qrcode_cobranca',
                'callback': 'gerar_qrcode_cobranca'
            }
        ]
