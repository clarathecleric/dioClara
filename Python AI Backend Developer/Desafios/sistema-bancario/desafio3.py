from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def saque(self, valor):
        saldo = self.saldo
        saque_excedido = valor > saldo

        if saque_excedido:
            print('A operação falhou. Saldo insuficiente.')
        
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso.')
            return True
        
        else:
            print('A operação falhou. Valor informado inválido.')

        return False
    
    def deposito(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso.')
            return True
        else:
            print('A operação falhou. Valor informado inválido.')
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, lim_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.lim_saque = lim_saque

    def saque(self, valor):
        num_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == 'Saque']
        )

        limite_excedido = valor > self.limite
        saque_excedido = num_saques >= self.lim_saque

        if limite_excedido:
            print('A operação falhou. Valor de saque excedido.')

        elif saque_excedido:
            print('A operação falhou. Quantidade de saques excedida.')

        else:
            return super().saque(valor)
        
        return False
        
    def __str__(self):
        return f"""\
        Agência: {self.agencia}
        C/C: {self.numero}
        Titular: {self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
        
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.saque(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.deposito(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)