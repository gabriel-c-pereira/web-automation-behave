#language: pt
#encoding:UTF8


Funcionalidade: Transferencias Pix.

    Cenario: Transferência Pix por chave CPF
        Dado que o usuário está logado no IB
        E que acessa o menu de pagamentos e transferências pix
        Quando é feita uma transferência para chave 00821159909 do tipo CPF
        Então deve aparecer o comprovante da transação
