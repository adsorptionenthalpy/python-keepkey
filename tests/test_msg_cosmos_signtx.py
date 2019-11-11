import unittest
import common

from base64 import b64encode

import keepkeylib.messages_pb2 as proto
import keepkeylib.messages_stellar_pb2 as stellar_proto
from keepkeylib.tools import parse_path

DEFAULT_BIP32_PATH = "m/44h/148h/0h"

class TestMsgStellarSignTransaction(common.KeepKeyTest):

    ADDRESS_N = parse_path(DEFAULT_BIP32_PATH)
    NETWORK_PASSPHRASE = "Test SDF Network ; September 2015"

    def test_sign_tx_bump_sequence_op(self):
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarBumpSequenceOp()
        op.bump_to = 0x7FFFFFFFFFFFFFFF
        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )
        assert (
            b64encode(response.signature)
            == b"ZMIfHWhpyXdg40PzwOtkcXYnbZIO12Qy0WvkGqoYpb7jyWbG2HQCG7dgWhCoU5K81pvZTA2pMwiPjMwCXA//Bg=="
        )

    def test_sign_tx_account_merge_op(self):
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarAccountMergeOp()
        op.destination_account = (
            "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
        )

        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            response.public_key.encode("hex")
            == "15d648bfe4d36f196cfb5735ffd8ca54cd4b8233f743f22449de7cf301cdb469"
        )
        assert (
            b64encode(response.signature)
            == b"2R3Pj89U+dWrqy7otUrLLjtANjAg0lmBQL8E+89Po0Y94oqZkauP8j3WE7+/z7vF6XvAMLoOdqRYkUzr2oh7Dg=="
        )

    def test_sign_tx_create_account_op(self):
        """Create new account with initial balance of 100.0333"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarCreateAccountOp()
        op.new_account = "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
        op.starting_balance = 1000333000

        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"vrRYqkM4b54NrDR05UrW7ZHU7CNcidV0fn+bk9dqOW1bCbmX3YfeRbk2Tf1aea8nr9SD0sfBhtrDpdyxUenjBw=="
        )

    def test_sign_tx_payment_op_native(self):
        """Native payment of 50.0111 XLM to GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarPaymentOp()
        op.amount = 500111000
        op.destination_account = (
            "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"
        )

        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"pDc6ghKCLNoYbt3h4eBw+533237m0BB0Jp/d/TxJCA83mF3o5Fr4l5vwAWBR62hdTWAP9MhVluY0cd5i54UwDg=="
        )

    def test_sign_tx_payment_op_native_explicit_asset(self):
        """Native payment of 50.0111 XLM to GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarPaymentOp(
            amount = 500111000,
            destination_account = "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V",
            asset = stellar_proto.StellarAssetType(type = 0)
        )

        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"pDc6ghKCLNoYbt3h4eBw+533237m0BB0Jp/d/TxJCA83mF3o5Fr4l5vwAWBR62hdTWAP9MhVluY0cd5i54UwDg=="
        )

    def test_sign_tx_payment_op_custom_asset1(self):
        """Custom asset payment (code length 1) of 50.0111 X to GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarPaymentOp(
            amount = 500111000,
            destination_account = "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V",
            asset = stellar_proto.StellarAssetType(
                type = 1,
                code = "X",
                issuer = "GAUYJFQCYIHFQNS7CI6BFWD2DSSFKDIQZUQ3BLQODDKE4PSW7VVBKENC"
            )
        )
        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"ArZydOtXU2whoRuSjJLFIWPSIsq3AbsncJZ+THF24CRSriVWw5Fy/dHrDlUOu4fzU28I6osDMeI39aWezg5tDw=="
        )

    def test_sign_tx_payment_op_custom_asset12(self):
        """Custom asset payment (code length 12) of 50.0111 ABCDEFGHIJKL to GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarPaymentOp(
            amount = 500111000,
            destination_account = "GBOVKZBEM2YYLOCDCUXJ4IMRKHN4LCJAE7WEAEA2KF562XFAGDBOB64V",
            asset = stellar_proto.StellarAssetType(
                type = 2,
                code = "ABCDEFGHIJKL",
                issuer = "GAUYJFQCYIHFQNS7CI6BFWD2DSSFKDIQZUQ3BLQODDKE4PSW7VVBKENC",
            )
        )
        tx = self._create_msg()

        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"QZIP4XKPfe4OpZtuJiyrMZBX9YBzvGpHGcngdgFfHn2kcdONreF384/pCF80xfEnGm8grKaoOnUEKxqcMKvxAA=="
        )

    def test_sign_tx_set_options(self):
        """Set inflation destination"""
        self.setup_mnemonic_nopin_nopassphrase()

        op = stellar_proto.StellarSetOptionsOp()
        op.inflation_destination_account = (
            "GAFXTC5OV5XQD66T7WGOB2HUVUC3ZVJDJMBDPTVQYV3G3K7TUHC6CLBR"
        )

        tx = self._create_msg()
        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )

        assert (
            b64encode(response.signature)
            == b"dveWhKY8x7b0YqGHWH6Fo1SskxaHP11NXd2n6oHKGiv+T/LqB+CCzbmJA0tplZ+0HNPJbHD7L3Bsg/y462qLDA=="
        )

        op = stellar_proto.StellarSetOptionsOp()
        op.signer_type = 0
        op.signer_key = "72187adb879c414346d77c71af8cce7b6eaa57b528e999fd91feae6b6418628e".decode("hex")
        op.signer_weight = 2

        tx = self._create_msg()
        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )
        assert (
            b64encode(response.signature)
            == b"EAeihuFBhUnjH6Sgd/+uAHlvajfv944VEpNSCLsOULNxYWdo/S0lJdUZw/2kN6I+ztKL7ZPQ5gYPJRNUePTOCg=="
        )

        op = stellar_proto.StellarSetOptionsOp()
        op.medium_threshold = 0

        tx = self._create_msg()
        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )
        assert (
            b64encode(response.signature)
            == b"E2pz06PFB5CvIT3peUcY0wxo7u9da2h6/+/qim1eRWLHC73ZtFqDtLMBaKnr63ZfjB/kDzZmCzHxiv5m+m6+AQ=="
        )

        op = stellar_proto.StellarSetOptionsOp()
        op.low_threshold = 0
        op.high_threshold = 3
        op.clear_flags = 0

        tx = self._create_msg()
        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )
        assert (
            b64encode(response.signature)
            == b"ySQE4aS0TI+N1xjSwi/pABHpC+A6RrNPWDOuFYGJFQ5B4vIU2S+ql2gCGLE7bQiYZ5dK9021f+a30mZoYeFLDw=="
        )

        op = stellar_proto.StellarSetOptionsOp()
        op.set_flags = 3
        op.master_weight = 4
        op.home_domain = "hello"

        tx = self._create_msg()
        response = self.client.stellar_sign_tx(
            tx, [op], self.ADDRESS_N, self.NETWORK_PASSPHRASE
        )
        assert (
            b64encode(response.signature)
            == b"22rfcOrxBiE5akpNsnWX8yPgAOpclbajVqXUaXMNeL000p1OhFhi050t1+GNRpoSNyfVsJGNvtlICGpH4ksDAQ=="
        )

    def _create_msg(self):
        tx = stellar_proto.StellarSignTx()
        tx.source_account = "GAK5MSF74TJW6GLM7NLTL76YZJKM2S4CGP3UH4REJHPHZ4YBZW2GSBPW"
        tx.fee = 100
        tx.sequence_number = 0x100000000
        tx.memo_type = 0
        return tx

if __name__ == '__main__':
    unittest.main()