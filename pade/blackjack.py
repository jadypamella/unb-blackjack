from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

from datetime import datetime
from sys import argv

import random

class CompRequestInterface(FipaRequestProtocol):
    """FIPA Request Behaviour of the Interface Agent"""
    def __init__(self, agent, message):
        super(CompRequestInterface, self).__init__(agent=agent,
                                           message=message,
                                           is_initiator=True)

    def handle_inform(self, message):
        display_message(self.agent.aid.localname, message.content)

class CompRequestAnalyticAgent(FipaRequestProtocol):
    """FIPA Request Behaviour of the Analytic Agent"""
    def __init__(self, agent):
        super(CompRequestAnalyticAgent, self).__init__(agent=agent,
                                          message=None,
                                          is_initiator=False)

    def handle_request(self, message):
        super(CompRequestAnalyticAgent, self).handle_request(message)
        display_message(self.agent.aid.localname, 'suggestion request message received from interface.')

        suggestion_list = ['Hit', 'Stand']
        suggestion = random.choice(suggestion_list)
 
        reply = message.create_reply()
        reply.set_performative(ACLMessage.INFORM)
        reply.set_content(suggestion)
        self.agent.send(reply)

class CompRequestResultAgent(FipaRequestProtocol):
    """FIPA Request Behaviour of the Result Agent"""
    def __init__(self, agent):
        super(CompRequestResultAgent, self).__init__(agent=agent,
                                          message=None,
                                          is_initiator=False)

    def handle_request(self, message):
        super(CompRequestResultAgent, self).handle_request(message)
        display_message(self.agent.aid.localname, 'results analysis request message received from interface.')
 
        result = "Análise de Resultados"
        reply = message.create_reply()
        reply.set_performative(ACLMessage.INFORM)
        reply.set_content(result)
        self.agent.send(reply)


class ComportTemporal(TimedBehaviour):
    """Timed Behaviour"""
    def __init__(self, agent, time, message):
        super(ComportTemporal, self).__init__(agent, time)
        self.message = message

    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.send(self.message)


class InterfaceAgent(Agent):
    """Class thet defines the Interface agent."""
    def __init__(self, aid, tradicional_agent_name, probabilistico_agent_name, historico_agent_name, resultado_agent):
        super(InterfaceAgent, self).__init__(aid=aid, debug=False)

        # message that requests suggestion to tradicional agent
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name=tradicional_agent_name))
        message.set_content('Sugestão')

        self.comport_request = CompRequestInterface(self, message)
        self.comport_temp = ComportTemporal(self, 10.0, message)
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)

        # message that requests suggestion to probabilistico agent
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name=probabilistico_agent_name))
        message.set_content('Sugestão')

        self.comport_request = CompRequestInterface(self, message)
        self.comport_temp = ComportTemporal(self, 11.0, message)
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)
        
        # message that requests suggestion to historico agent
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name=historico_agent_name))
        message.set_content('Sugestão')

        self.comport_request = CompRequestInterface(self, message)
        self.comport_temp = ComportTemporal(self, 12.0, message)
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)

        # message that requests suggestion to historico agent
        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name=resultado_agent_name))
        message.set_content('Resultado')

        self.comport_request = CompRequestInterface(self, message)
        self.comport_temp = ComportTemporal(self, 13.0, message)
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)


class TradicionalAgent(Agent):
    """Class that defines the Tradicional agent."""
    def __init__(self, aid):
        super(TradicionalAgent, self).__init__(aid=aid, debug=True)
        
        self.comport_request = CompRequestAnalyticAgent(self)
        self.behaviours.append(self.comport_request)


class ProbabilisticoAgent(Agent):
    """Class thet defines the Probabilistico agent."""
    def __init__(self, aid):
        super(ProbabilisticoAgent, self).__init__(aid=aid, debug=False)

        self.comport_request = CompRequestAnalyticAgent(self)
        self.behaviours.append(self.comport_request)


class HistoricoAgent(Agent):
    """Class thet defines the Historico agent."""
    def __init__(self, aid):
        super(HistoricoAgent, self).__init__(aid=aid, debug=False)

        self.comport_request = CompRequestAnalyticAgent(self)
        self.behaviours.append(self.comport_request)


class ResultadoAgent(Agent):
    """Class thet defines the Resultado agent."""
    def __init__(self, aid):
        super(ResultadoAgent, self).__init__(aid=aid, debug=False)

        self.comport_request = CompRequestResultAgent(self)
        self.behaviours.append(self.comport_request)


if __name__ == '__main__':

    agents_per_process = 1
    c = 0
    agents = list()
    for i in range(agents_per_process):
        port = int(argv[1]) + c
             
        tradicional_agent_name = 'agente_tradicional'
        tradicional_agent = TradicionalAgent(AID(name=tradicional_agent_name))
        agents.append(tradicional_agent)

        probabilistico_agent_name = 'agente_probabilistico'
        probabilistico_agent = ProbabilisticoAgent(AID(name=probabilistico_agent_name))
        agents.append(probabilistico_agent)

        historico_agent_name = 'agente_historico'
        historico_agent = HistoricoAgent(AID(name=historico_agent_name))
        agents.append(historico_agent)

        resultado_agent_name = 'agente_resultado'
        resultado_agent = ResultadoAgent(AID(name=resultado_agent_name))
        agents.append(resultado_agent)

        interface_agent_name = 'interface'
        interface_agent = InterfaceAgent(AID(name=interface_agent_name), tradicional_agent_name, probabilistico_agent_name, historico_agent_name, resultado_agent)
        agents.append(interface_agent)

        c += 1

    start_loop(agents)
