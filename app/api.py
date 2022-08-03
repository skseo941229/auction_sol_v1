from csv import DictWriter
import json
from unittest import async_case
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import sys
from pybp.pederson import PedersonCommitment
from pybp.rangeproof import RangeProof
from fastapi.responses import  FileResponse
import pickle
import zipfile
import os
import time
import asyncio
from web3 import Web3 
import os


web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
 
abi = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "s1",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "s2",
				"type": "string"
			}
		],
		"name": "compareStringsbyBytes",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "pure",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_hx",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_hy",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_b",
				"type": "uint256"
			}
		],
		"name": "openBid",
		"outputs": [
			{
				"internalType": "string",
				"name": "res",
				"type": "string"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "ap_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ap_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "sp_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "sp_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t1p_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t1p_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t2p_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t2p_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "tau",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "mu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "pff",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "rp_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "rp_y",
						"type": "uint256"
					}
				],
				"internalType": "struct Open.Proof",
				"name": "pf",
				"type": "tuple"
			}
		],
		"name": "receiveProof",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "retrieveBid",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "value",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "hx",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "hy",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "b",
						"type": "uint256"
					}
				],
				"internalType": "struct Open.Bidder[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "myname",
				"type": "string"
			}
		],
		"name": "retrieveProof",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "name",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "ap_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "ap_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "sp_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "sp_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t1p_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t1p_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t2p_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t2p_y",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "tau",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "mu",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "t",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "pff",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "rp_x",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "rp_y",
						"type": "uint256"
					}
				],
				"internalType": "struct Open.Proof",
				"name": "pf",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]  
contract = web3.eth.contract(address='0x5965Fe7B2EAc19d041555c839399F3fB29574A10', abi=abi) 
address = '0x5Ce53C8e59E40a4b3C5CF6DA7b6cc7F9C3aDE483'
priv_key = 'baf1ca4073aa8c9abc95315d53cc58d611ad43becb451615d291f80f1b08660b'

app = FastAPI()  

origins = [
    "http://localhost:3000",  
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
bids = []
price = {}
close = "0"

@app.post("/bid", tags=["bids"])  
async def add_bids(bid: dict) -> str:
    '''
    add bid. format receive id, bid_x, bid_y (pedersen commitment is applied)
    
    '''
    if close == "0":
        bids.append(bid)  
        return "0"
    else:
        return str(close)


@app.get("/close", tags=["closing"])    
async def close_bids() -> str:
    global close
    close = "1"
    return "Not accept anymore"  

checking = 0

stored = {}

@app.get("/bfcheck")
async def bf_check()->str:
    global close
    if close =="0":
        return "Not closed anymore"
    if len(bids) ==0:
        return "Nothing in bids"
    else:
        return "Please enter your value"  
 
verf = 0   
def verf_stored():
    global verf
    global stored
    if verf == 1:
        return
    else:
        verf = 1
        arr = contract.functions.retrieveBid().call()
        for item in arr:
            stored[item[0]] = PedersonCommitment(item[1], b=item[4], h=(item[2],item[3])).get_commitment()
            price[item[0]] = item[1]

@app.post("/check")
async def check_bids(pcval:dict) -> str: 
    '''
    receive r, h, value and check that bidders don't lie 
    '''
    verf_stored()
    computedPC = 0
    for bid in bids:
        if bid['id'] == pcval['id']:
            
            
            computedPC =stored[bid['id']]
            if int(bid['bid_x']) == computedPC[0] and int(bid['bid_y']) == computedPC[1]:
                return "Confirmed"
            else:
                bids.remove(bid)    
                return "You are not allowed to participate"  

verf_check = 0 
@app.post("/get_win") 
async def get_winner(id:dict):
    '''
    if winning bid, notify you are the winner. if losing bid, send proof to verify that you are not winner 
    '''
    win_bid = max(price.values())  
    for idx in price:
        if price[idx] == win_bid:
            win_idx = idx
            break  
    
    if win_idx == id['id']:
        return "You are the winner"
    
    if  id['id'] =="owner":
        return str(win_idx+" is the winner")
    
    global verf_check  
    if verf_check == 0:
        
        for item in price:
            bid_price = price[item]
            diff_price = win_bid - bid_price
            proofval = int(diff_price)
            rp = RangeProof(32)  
            rp.generate_proof(proofval)
            proof = rp.get_proof_dict()  
            #tmp = {"name": item,  "ap_x": proof['Ap'][0], "ap_y": proof['Ap'][1],"sp_x": proof['Sp'][0], "sp_y": proof['Sp'][1],"t1p_x": proof['T1p'][0], "t1p_y": proof['T1p'][1], "t2p_x": proof['T2p'][0],"t2p_y" : proof['T2p'][1],"tau": proof['tau_x'],"mu": proof['mu'], "t": proof['t'], "pff": proof['proof'],"rp_x": rp.V[0], "rp_y":rp.V[1]}
            tmp = [item, proof['Ap'][0], proof['Ap'][1], proof['Sp'][0],  proof['Sp'][1],proof['T1p'][0],  proof['T1p'][1], proof['T2p'][0],proof['T2p'][1],proof['tau_x'],proof['mu'], proof['t'], str(proof['proof']), rp.V[0], rp.V[1]]
            res = contract.functions.receiveProof(tmp).buildTransaction({"chainId": 1337, "gasPrice": web3.eth.gas_price, "from": address, "nonce": web3.eth.getTransactionCount(address)})
		
            signed_tx = web3.eth.account.signTransaction(res, private_key=priv_key)
            web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        verf_check = 1
    return "You are the loser, we sent proof to smart contract! Check it!"
       

@app.get("/list")
async def list_bidders() -> dict:
    return bids

@app.get("/open_list")
async def open_list() -> dict:  
    return price 

@app.get('/stored_list') 
async def stored_list() ->dict:
    return stored  
