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
from   typing                                  import List, Tuple, TypedDict, Union, Optional
from  .derive                                  import DeriveVote, DeriveEscrow
from  .anchorpy_governor.instructions.new_vote import NewVoteArgs, NewVoteAccounts, new_vote
from  .anchorpy_governor.instructions.set_vote import SetVoteArgs, SetVoteAccounts, set_vote
from  .anchorpy_governor.accounts.proposal     import Proposal
from  .anchorpy_governor.accounts.governor     import Governor
from  .anchorpy_governor.accounts.vote         import Vote
from  .anchorpy_voter.instructions.cast_vote   import CastVoteArgs, CastVoteAccounts, cast_vote
from  .anchorpy_governor.program_id            import PROGRAM_ID as GOVERNOR_PROGRAM_ID
from  .anchorpy_voter.program_id               import PROGRAM_ID as VOTER_PROGRAM_ID
from   sapysol import MakePubkey, MakeKeypair, SapysolPubkey, SapysolKeypair
import logging
import json
import os

# ================================================================================
#
def CheckVoteExists(connection: Client, proposalAddress: Pubkey, voterAddress: Pubkey) -> bool:
    voteAddress: Pubkey  = DeriveVote(proposal=proposalAddress, owner=voterAddress)
    voteAccount: Account = connection.get_account_info(pubkey=voteAddress).value
    return voteAccount is not None

# ================================================================================
#
def CheckVoteSide(connection: Client, proposalAddress: Pubkey, voterAddress: Pubkey) -> Optional[Tuple[int, int]]:
    voteAddress: Pubkey  = DeriveVote(proposal=proposalAddress, owner=voterAddress)
    vote: Vote = Vote.fetch(conn=connection, address=voteAddress)
    return (vote.side, vote.voting_power) if vote else None

# ================================================================================
#
def CheckEscrowExists(connection: Client, lockerAddress: Pubkey, voterAddress: Pubkey) -> bool:
    escrowAddress: Pubkey  = DeriveEscrow(locker=lockerAddress, escrowOwner=voterAddress)
    escrowAccount: Account = connection.get_account_info(pubkey=escrowAddress).value
    return escrowAccount is not None

# ================================================================================
#
def NewVoteIx(connection:      Client, 
              proposalAddress: SapysolPubkey, 
              voterAddress:    SapysolPubkey) -> Instruction:

    #voteExists: bool = CheckVoteExists(connection      = connection,
    #                                   proposalAddress = proposalAddress,
    #                                   voterAddress    = MakePubkey(voterAddress))
    #if voteExists:
    #    return None

    voteAddress: Pubkey          = DeriveVote(proposal=proposalAddress, owner=MakePubkey(voterAddress))
    args:        NewVoteArgs     = NewVoteArgs(voter=MakePubkey(voterAddress))
    accounts:    NewVoteAccounts = NewVoteAccounts(proposal = MakePubkey(proposalAddress),
                                                   vote     = voteAddress,
                                                   payer    = MakePubkey(voterAddress))

    return new_vote(args=args, accounts=accounts)

# ================================================================================
#
def SetVoteIx(connection:      Client, 
              proposalAddress: SapysolPubkey, 
              voter:           SapysolKeypair, 
              voteSide:        int,
              voteWeight:      int) -> Instruction:

    _voter:           Keypair = MakeKeypair(voter) # preserve original `voter`
    _proposalAddress: Pubkey  = MakePubkey(proposalAddress)
    voteExists:       bool    = CheckVoteExists(connection      = connection,
                                                proposalAddress = proposalAddress,
                                                voterAddress    = _voter.pubkey())
    if not voteExists:
        raise(Exception("SetVote error! Can't set vote because Vote was not created!"))

    voteAddress: Pubkey   = DeriveVote(proposal=proposalAddress, owner=voter.pubkey())
    proposal:    Proposal = Proposal.fetch(conn=connection, address=_proposalAddress )
    governor:    Governor = Governor.fetch(conn=connection, address=proposal.governor)

    args:     SetVoteArgs     = SetVoteArgs(side=voteSide, weight=voteWeight)
    accounts: SetVoteAccounts = SetVoteAccounts(governor = proposal.governor,
                                                proposal = _proposalAddress,
                                                vote     = voteAddress,
                                                locker   = governor.locker)

    vote: Instruction = set_vote(args     = args,
                                 accounts = accounts)


    # TODO

# ================================================================================
#
