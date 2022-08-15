# Sealed bid auction using smart contracts
This is the second step of a progressive sealed-bid auction. For the first step, please refer to https://github.com/skseo941229/pure_auction_v1.   

## Description

In this phase, smart contracts were used to transferring data.   Instead of sending and receiving commitment value and proof between them, the smart contract receives the commitment from bidders and transfers it to the auctioneer. In the verification part, the auctioneer sends proof of each bidder to the smart contract for bidders to receive. Since they communicate via smart contracts, it is so unlikely to manipulate the commitment value or proof. 

- Auction starts a auction server and responds to the requests from auction_info and bidders. It generates proofs  for bidders who lost and sends to smart contracts. 
- Auction_info gives information about the auction such as list of bidders, and has a permission to close bid.
- Bidders can submit the value and check their results. Bidders who lost receive their proofs using smart contracts and verify using bulletproof. 

## Getting Started

### Dependencies

* Ganache

### Installing

* pybp package (https://github.com/kendricktan/pybp)
* web3 package
```
pip install web3
```

### Executing program
* Executing the auction: 
```
python auction.py
```

* To query auction status, execute the auction_info:
```
python auction_info.py
```

* To be a bidder of a program, execute the bidder:
```
python bidder.py <bidder_name>
```
