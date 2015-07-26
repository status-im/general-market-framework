# -*- coding: utf-8 -*-

from ethereum import slogging, utils
from collections import namedtuple

Ticket = namedtuple("Ticket", "id owner epoch preferences")


class Trader:

    name = ''
    ticket = -1

    current_block = -1

    def reveal(self, data):
        owner = data[0]
        ticket_id = data[1]
        offer = data[2]
        if ticket_id == self.ticket.id:
            print(self.name, 'reveal announce', ticket_id, offer)

            # TODO: Look at offer, accept or decline

    def new_ticket(self, price):
        ticket_id = self.market.add()
        # self.market.add_preference(ticket, 'head', 10)
        # self.market.add_preference(ticket, 'tail', 20)
        self.market.add_preference(ticket_id, 'price', price)
        self.market.activate(ticket_id)

        info = self.market.get_info(ticket_id)
        # Rebuild Preferences
        preferences = self.market.get_preferences(ticket_id)
        keys = [utils.encode_int(x) for x in preferences[::2]]
        preferences = dict(zip(keys, preferences[1::2]))
        del preferences['']

        self.ticket = Ticket(ticket_id, info[0], info[1], preferences)
        print(self.name, 'created new ticket', ticket_id, price)

    def process(self):
        print(self.name, 'processing on block', self.current_block)

    def listener(self, msg):
        '''
        Dynamically call Methods based on first param
        Currently only announce exists

        Also calls process on new block number, based on delta event
        '''
        event = msg['event']
        # if event != 'LOG' and event != 'vm':
        #     print(event)

        if event == 'LOG' and msg['to'] == self.market.address:
            msg_type = utils.encode_int(msg['topics'][0]).rstrip('\x00')
            msg_data = msg['topics'][1:]
            if hasattr(self, msg_type):
                getattr(self, msg_type)(msg_data)
        elif event == 'delta':
            if self.current_block < self.state.block.number:
                self.current_block = self.state.block.number
                self.process()

    def __init__(self, state, market, name=''):
        self.state = state
        self.market = market
        self.name = name
        slogging.log_listeners.listeners.append(self.listener)
