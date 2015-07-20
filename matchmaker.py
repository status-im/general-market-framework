# -*- coding: utf-8 -*-

from ethereum import slogging, utils
from collections import namedtuple

Ticket = namedtuple("Ticket", "id owner epoch preferences")
Offer = namedtuple("Offer", "id epoch buyer seller hash preferences")


class Matchmaker:

    buyers = []
    sellers = []

    sealed_offers = []

    current_block = -1

    def reveal_offers(self):
        for offer in self.sealed_offers:
            # TODO: submit if in REVEAL_WINDOW
            # self.market.reveal_offer()
            pass

    def make_match(self, buyer, seller):
        print('making match', buyer, seller)
        # TODO: check hash for adding sealed offer, ie hash preferences?
        shasum = utils.sha3([buyer.epoch, buyer.owner, seller.owner])
        # TODO check epoch against SEALED_WINDOW
        offer_id = self.market.add_sealed_offer(buyer.id, shasum)
        print('shasum', shasum)
        print('reveal', offer_id)

        # TODO, combine preferences
        offer = Offer(offer_id, buyer.epoch, buyer.owner, seller.owner, shasum, buyer.preferences)
        self.sealed_offers.append(offer)


    def process(self):
        # naively make matches
        for s in self.sellers:
            for b in self.buyers:
                for k, v in s.preferences.viewitems() & b.preferences.viewitems():
                    print('match found on', k, v)
                    self.sellers.remove(s)
                    self.buyers.remove(b)
                    self.make_match(b, s)
        self.reveal_offers()
        # TODO:
        # reveal offers
        # do cleanup
        print('processing on block', self.current_block)

    def announce(self, data):
        ''' A new ticket has arrived '''
        ticket_id = data[0]
        info = self.market.get_info(ticket_id)

        # Rebuild Preferences
        preferences = self.market.get_preferences(ticket_id)
        keys = [utils.encode_int(x) for x in preferences[::2]]
        preferences = dict(zip(keys, preferences[1::2]))
        del preferences['']

        ticket = Ticket(ticket_id, info[0], info[1], preferences)

        # Our match maker assumes there is a price
        if ticket.preferences['price'] < 0:
            ticket.preferences['price'] = abs(ticket.preferences['price'])
            self.sellers.append(ticket)
        else:
            self.buyers.append(ticket)

        self.process()

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
            # try:
            getattr(self, msg_type)(msg_data)
            # except:
            #     raise NotImplementedError(msg_type, msg_data)
        elif event == 'delta':
            if self.current_block < self.state.block.number:
                self.current_block = self.state.block.number
                self.process()

    def __init__(self, state, market):
        self.state = state
        self.market = market
        slogging.log_listeners.listeners.append(self.listener)