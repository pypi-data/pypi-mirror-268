#!/usr/bin/python
# =============================================================================
#
# SuperArmor's Jupiter LFG Voter
# (c) SuperArmor
#
# =============================================================================
# 
from   solana.rpc.api                          import Client, Pubkey, Keypair
from   solders.account                         import Account
from   solders.instruction                     import Instruction, AccountMeta
from   typing                                  import List, Any, TypedDict, Union, Optional
from  .derive                                  import DeriveVote, DeriveEscrow
from  .anchorpy_governor.instructions.new_vote import NewVoteArgs, NewVoteAccounts, new_vote
from  .anchorpy_governor.instructions.set_vote import SetVoteArgs, SetVoteAccounts, set_vote
from  .anchorpy_governor.accounts.proposal     import Proposal
from  .anchorpy_governor.accounts.governor     import Governor
from  .anchorpy_voter.instructions.cast_vote   import CastVoteArgs, CastVoteAccounts, cast_vote
from  .anchorpy_governor.program_id            import PROGRAM_ID as GOVERNOR_PROGRAM_ID
from  .anchorpy_voter.program_id               import PROGRAM_ID as VOTER_PROGRAM_ID
from   sapysol import MakePubkey, MakeKeypair, SapysolPubkey, SapysolKeypair
import logging
import json
import os

# ================================================================================
#
def CastVoteIx(connection:      Client, 
               proposalAddress: SapysolPubkey, 
               voterAddress:    SapysolPubkey, 
               voteSide:        int) -> List[Instruction]:

    proposal:    Proposal = Proposal.fetch(conn=connection, address=MakePubkey(proposalAddress))
    governor:    Governor = Governor.fetch(conn=connection, address=proposal.governor)
    voteAddress: Pubkey   = DeriveVote(proposal=proposalAddress, owner=MakePubkey(voterAddress))

    args:        CastVoteArgs     = CastVoteArgs(side=voteSide)
    accounts:    CastVoteAccounts = CastVoteAccounts(locker         = governor.locker,
                                                     escrow         = DeriveEscrow(locker=governor.locker, escrowOwner=MakePubkey(voterAddress)),
                                                     vote_delegate  = MakePubkey(voterAddress),
                                                     proposal       = MakePubkey(proposalAddress),
                                                     vote           = voteAddress,
                                                     governor       = proposal.governor,
                                                     govern_program = GOVERNOR_PROGRAM_ID)

    return cast_vote(args=args, accounts=accounts)

# ================================================================================
#
