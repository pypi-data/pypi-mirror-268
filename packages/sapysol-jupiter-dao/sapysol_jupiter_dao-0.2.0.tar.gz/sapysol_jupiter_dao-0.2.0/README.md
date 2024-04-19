# sapysol_jupiter_dao

`sapysol` Jupiter LFG DAO Vote implementation. Based on JavaScript from [Jupiter DAO Website](https://vote.jup.ag) _(from Chrome developer tools)_, written from scratch with the help of [AnchorPy](https://github.com/kevinheavey/anchorpy).

WARNING! `sapysol_jupiter_dao` is currently in `alpha` version, so, bugs, lack of tests and descriptions are expected. Some things may not work, future versions may bring breaking changes.

WARNING! only casting initial vote is implemented! Changing vote, depositing JUP, withdrawing JUP is yet to be implemented!

# Installation

```sh
pip install sapysol-jupiter-dao
```

Note: Requires Python >= 3.10.

# Usage

```py
# DAO Voting (Round #1 of LFG Voting example)
# Automatically claims tokens for a list of wallets/keypairs.
# Can use multiple parallel threads.
#
from solana.rpc.api              import Client
from sapysol                     import *
from sapysol.token_cache         import *
from typing                      import List
from sapysol_jupiter_dao.batcher import SapysolJupiterDaoBatcher

SetupLogging()

connection: Client = Client("https://api.mainnet-beta.solana.com")

# Prepare a list of keypairs to claim tokens
keypairsList: List[Keypair] = [
    MakeKeypair("/path/to/keypair1.json"),
    MakeKeypair("/path/to/keypair2.json"),
    MakeKeypair("/path/to/keypair3.json"),
    MakeKeypair("/path/to/keypair4.json"),
]

# Set as you please
voteSide: int = 2

# Prepare batcher that automatically performs votes for all keypairs using 
# `numThreads` number of threads.
batcher = SapysolJupiterDaoBatcher(connection      = connection,
                                   proposalAddress = "6txWyf3guJrhnNJXcAHxnV2oVxBcvebuSbfYsgB3yUKc",
                                   votersList      = keypairsList,
                                   voteSide        = voteSide,
                                   numThreads      = 10)

# Start voting
batcher.Start()
```

TODO

# Changelog

v.0.2.0 - Add `voteOverride` param to `SapysolJupiterDaoBatcher` which allows to change existing votes.

# Contributing

TODO

# Tests

TODO

# Contact

[Telegram](https://t.me/sapysol)

Donations: `SAxxD7JGPQWqDihYDfD6mFp7JWz5xGrf9RXmE4BJWTS`

# Disclaimer

### Intended Purpose and Use
The Content is provided solely for educational, informational, and general purposes. It is not intended for use in making any business, investment, or legal decisions. Although every effort has been made to keep the information up-to-date and accurate, no representations or warranties, express or implied, are made regarding the completeness, accuracy, reliability, suitability, or availability of the Content.

### Opinions and Views
The views and opinions expressed herein are those of Anton Platonov and do not necessarily reflect the official policy, position, or views of any other agency, organization, employer, or company. These views are subject to change, revision, and rethinking at any time.

### Third-Party Content and Intellectual Property
Some Content may include or link to third-party materials. The User agrees to respect all applicable intellectual property laws, including copyrights and trademarks, when engaging with this Content.

### Amendments
Anton Platonov reserves the right to update or change this disclaimer at any time without notice. Continued use of the Content following modifications to this disclaimer will constitute acceptance of the revised terms.