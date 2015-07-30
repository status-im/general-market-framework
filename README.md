General Market Framework
=================================

_Last Updated: 30 July 2015_  
_Author: Jarrad Hope_

Our goal for GMF is to create generalised market designed to be the backbone to "sharing economy" services, our examples will include a Car Ride service & a Fiat/Cryptocurrency exchange service.

Traders add tickets to the pool with their preferences(price, dispute contract address, trade contract address, etc), covering their ticket price with insurance references(from [TrustDavis](https://github.com/syng-io/trustdavis)), 

Match Makers are used to pair the Traders, adding sealed offers that match, when revealed (or after sealed bid TBD) the Traders have the option accept or decline the match, only when both accepted will a trade contract be created.

### Development Status

In Development (pre-alpha)

- `<incomplete>`
- Build a Frontend around GMF ([MOVΞ](https://github.com/syng-io/move))
- Figure out Economics, ie fee's for matches
- How to handle declines/timeouts, clean up
- Create Trade on accepts
- <del>Reveal & Announce</del>
- <del>Add Sealed Bid</del>
- <del>Naive Match Maker</del>
- <del>Preferences Added</del>
- <del>XOR Linked List</del>

### Communication

Live Chat: [gitter.im/syng-io/general](http://gitter.im/syng-io/general)

### Technical Skills Required to Contribute

Any of the following; Python, Serpent 2
