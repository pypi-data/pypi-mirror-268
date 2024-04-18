#!/usr/bin/python
# =============================================================================
#
# SuperArmor's Jupiter LFG Voter
# (c) SuperArmor
#
# ================================================================================
# 
from   solana.rpc.api                      import Client, Pubkey, Keypair
from   solders.instruction                 import Instruction, AccountMeta
from   typing                              import List, Any, TypedDict, Union, Optional
from  .anchorpy_governor.accounts.proposal import Proposal
from  .anchorpy_governor.accounts.governor import Governor
from   sapysol_jupiter_dao.governor        import CheckVoteExists, CheckEscrowExists, NewVoteIx, CheckVoteSide
from   sapysol_jupiter_dao.voter           import CastVoteIx
from   sapysol                             import *
from   sapysol.snippets.batcher            import SapysolBatcher
import logging
import json
import os

JUP_DELIMITER = 1_000_000

# ================================================================================
# 
class SapysolJupiterDaoBatcher:
    def __init__(self, 
                 connection:         Client,
                 proposalAddress:    SapysolPubkey,
                 votersList:         List[SapysolKeypair],
                 voteSide:           int,
                 connectionOverride: List[Union[str, Client]] = None,
                 txParams:           SapysolTxParams = SapysolTxParams(),
                 computePriceTx:     int = 1,
                 numThreads:         int = 20):

        self.CONNECTION:       Client                   = connection
        self.PROPOSAL_ADDRESS: Pubkey                   = MakePubkey(proposalAddress)
        self.VOTERS_LIST:      List[Keypair]            = [MakeKeypair(k) for k in votersList]
        self.VOTE_SIDE:        int                      = voteSide
        self.TX_PARAMS:        SapysolTxParams          = txParams
        self.COMPUTE_PRICE_TX: int                      = computePriceTx
        self.CONN_OVERRIDE:    List[Union[str, Client]] = connectionOverride
        self.DISTRIBUTOR_LIST: dict                     = {}
        self.BATCHER:          SapysolBatcher = SapysolBatcher(callback    = self.VoteSingle,
                                                               entityList  = self.VOTERS_LIST,
                                                               entityKwarg = "voter",
                                                               numThreads  = numThreads)
    
    def VoteSingle(self, voter: SapysolKeypair):
        while True:
            _voter:           Keypair = MakeKeypair(voter)
            _voterAddress:    Pubkey  = _voter.pubkey()
            voteExists: bool = CheckVoteExists(connection      = self.CONNECTION,
                                               proposalAddress = self.PROPOSAL_ADDRESS,
                                               voterAddress    = _voterAddress)
            if voteExists:
                voteSide, votePower = CheckVoteSide(connection      = self.CONNECTION,
                                                    proposalAddress = self.PROPOSAL_ADDRESS,
                                                    voterAddress    = _voterAddress)
                print(f"Voter: {_voter.pubkey()} already voted (side: {voteSide}, power: {votePower/JUP_DELIMITER}), skipping...")
                # TODO: check vote for who and tell
                return

            proposal: Proposal = Proposal.fetch(conn=self.CONNECTION, address=self.PROPOSAL_ADDRESS )
            governor: Governor = Governor.fetch(conn=self.CONNECTION, address=proposal.governor)

            escrowExists: bool = CheckEscrowExists(connection    = self.CONNECTION,
                                                   lockerAddress = governor.locker,
                                                   voterAddress  = _voterAddress)
            if not escrowExists:
                print(f"Voter: {_voter.pubkey()} no escrow, can't vote, skipping...")
                return

            print(f"Voter: {_voter.pubkey()} - voting...")

            newVote: Instruction = NewVoteIx(connection      = self.CONNECTION, 
                                             proposalAddress = self.PROPOSAL_ADDRESS, 
                                             voterAddress    = _voterAddress)

            castVote: Instruction = CastVoteIx(connection      = self.CONNECTION,
                                               proposalAddress = self.PROPOSAL_ADDRESS,
                                               voterAddress    = _voter,
                                               voteSide        = self.VOTE_SIDE)

            tx: SapysolTx = SapysolTx(connection=self.CONNECTION, payer=_voter)
            tx.FromInstructionsLegacy(instructions=[
                ComputeBudgetIx(),
                ComputePriceIx(self.COMPUTE_PRICE_TX),
                newVote,
                castVote,
            ])
            result: SapysolTxStatus = tx.Sign([_voter]).SendAndWait(connectionOverride=self.CONN_OVERRIDE)
            if result == SapysolTxStatus.SUCCESS:
                break

    # ========================================
    #
    def Start(self, **kwargs) -> None:
        self.RESULTS = {}
        self.BATCHER.Start(**kwargs)

# ================================================================================
# 
