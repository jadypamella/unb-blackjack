# Análise de Blackjack com Sistemas Multiagentes 
<br>

<p align="center">
    <img src="https://github.com/jadypamella/unb-blackjack/blob/master/docs/images/blackjack_logo.png" alt="blackjack" width="200">
</p>

O objetivo do Sistema de Análise de Blackjack com Multiagentes é determinar qual a melhor estratégia para vencer no jogo Blackjack (21) ou seja, o melhor momento para a ação Hit (pedir mais uma carta) ou para a ação Stand (permanecer com a pontuação atual).

O protótipo foi implementado utilizando PADE (Python Agent DEvelopment framework) e a comunicação entre os agentes atende aos padrões do protocolo FIPA (Foundation for Intelligent Physical Agents) Request.


## Execução do PADE
Para executar este protótipo de SMA siga o passo a passo:

1 - Instale o framework PADE (Python Agent DEvelopment) conforme a documentação: https://pade.readthedocs.io/en/latest/user/instalacao.html#installation-page

2 - Clonar o projeto de Análise de Blackjack com Sistemas Multiagentes na sua máquina

3 - Acesse o diretório blackjack/pade/ pelo terminal ou prompt de comando

4 - Execute o comando:
```bash
$ pade start-runtime --config_file pade_config.json
````

Se tudo correr bem, a saída do terminal deve ser semelhante a essa:
![Execução do PADE](https://github.com/jadypamella/unb-blackjack/blob/master/docs/images/pade_console.png?raw=true)
Figura 1 - Console PADE

5 - Acesse o endereço local da sua instalação do PADE (http://localhost:5000/diagrams) para visualizar o diagrama de comunicação entre os agentes, conforme exemplo abaixo:
![Execução do PADE](https://github.com/jadypamella/unb-blackjack/blob/master/docs/images/pade_message_diagram.png?raw=true)
Figura 2 - Diagrama de Comunicação entre os Agentes