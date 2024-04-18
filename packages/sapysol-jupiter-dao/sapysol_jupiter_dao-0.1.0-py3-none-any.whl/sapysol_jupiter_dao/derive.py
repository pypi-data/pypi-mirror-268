# ================================================================================
# 
from  solana.rpc.api               import Pubkey
from .anchorpy_governor.program_id import PROGRAM_ID as GOVERNOR_PROGRAM_ID
from .anchorpy_voter.program_id    import PROGRAM_ID as VOTER_PROGRAM_ID

# =============================================================================
# 
def DeriveVote(proposal: Pubkey, owner: Pubkey) -> Pubkey:
    assert(isinstance(proposal, Pubkey))
    assert(isinstance(owner,    Pubkey))
    return Pubkey.find_program_address(seeds      = [bytes(b"Vote"),
                                                     bytes(proposal),
                                                     bytes(owner)],
                                       program_id = GOVERNOR_PROGRAM_ID)[0]

# ================================================================================
# TODO - FIX
#function deriveSmartWallet(e) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("SmartWallet"), e.toBytes()], v)
#}

# ================================================================================
#
def DeriveGovern(proposal: Pubkey) -> Pubkey:
    assert(isinstance(proposal, Pubkey))
    return Pubkey.find_program_address(seeds      = [bytes(b"Governor"),
                                                     bytes(proposal)],
                                       program_id = GOVERNOR_PROGRAM_ID)[0]

# ================================================================================
# TODO - FIX
def DeriveLocker(proposal: Pubkey) -> Pubkey:
    assert(isinstance(proposal, Pubkey))
    return Pubkey.find_program_address(seeds      = [bytes(b"Locker"),
                                                     bytes(proposal)],
                                       program_id = VOTER_PROGRAM_ID)[0]

#function deriveLocker(e, t) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("Locker"), e.toBytes()], t)
#}

# ================================================================================
#
def DeriveEscrow(locker: Pubkey, escrowOwner: Pubkey) -> Pubkey:
    assert(isinstance(locker,      Pubkey))
    assert(isinstance(escrowOwner, Pubkey))
    return Pubkey.find_program_address(seeds      = [bytes(b"Escrow"),
                                                     bytes(locker),
                                                     bytes(escrowOwner)],
                                       program_id = VOTER_PROGRAM_ID)[0]

# ================================================================================
# TODO - FIX
#function deriveTransaction(e, t) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("Transaction"), e.toBytes(), t.toArrayLike(S, "le", 8)], v)
#}

# ================================================================================
# TODO - FIX
#function deriveProposal(e, t) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("Proposal"), e.toBytes(), t.toArrayLike(S, "le", 8)], h)
#}

# ================================================================================
# TODO - FIX
#function deriveProposalMeta(e) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("ProposalMeta"), e.toBytes()], h)
#}

# ================================================================================
# TODO - FIX
#function deriveOptionProposalMeta(e) {
#    return d.rV.PublicKey.findProgramAddressSync([S.from("OptionProposalMeta"), e.toBytes()], h)
#}

# ================================================================================
#