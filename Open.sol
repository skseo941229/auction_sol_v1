// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.10;

contract Open {
    struct Bidder {
      string name;
      uint value;
      uint hx;
      uint hy;
      uint b; 
    }

    struct Proof{
      string name;
      uint ap_x;
      uint ap_y; 
      uint sp_x;
      uint sp_y;
      uint t1p_x;
      uint t1p_y;
      uint t2p_x;
      uint t2p_y;
      uint tau;
      uint mu;
      uint t;
      string pff;
      uint rp_x;
      uint rp_y; 
    }
    
    Proof[] prof_list;
    Bidder[] bid_list; 
  
  // Add this function:
  function openBid(string memory _name, uint _value, uint _hx, uint _hy, uint _b) public returns (string memory res) {
     Bidder memory bid = Bidder(_name, _value, _hx, _hy, _b);
     bid_list.push(bid);
     res = "Stored" ;
  }
  
  function retrieveBid() public view returns (Bidder[] memory) {
    return bid_list; 
  }

  function receiveProof(Proof memory pf) public {
      prof_list.push(pf);
  }
  function compareStringsbyBytes(string memory s1, string memory s2) public pure returns(bool){
    return keccak256(abi.encodePacked(s1)) == keccak256(abi.encodePacked(s2));
}
  function retrieveProof(string memory myname) public view returns (Proof memory pf) {
      for (uint i=0; i<prof_list.length; i++) {
          if(compareStringsbyBytes(prof_list[i].name, myname) == true) {
            pf = prof_list[i]; 
            return pf ; 
          }
      }
   } 
 
}
