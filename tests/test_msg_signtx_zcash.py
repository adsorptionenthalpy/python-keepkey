# This file is part of the TREZOR project.
#
# Copyright (C) 2012-2016 Marek Palatinus <slush@satoshilabs.com>
# Copyright (C) 2012-2016 Pavol Rusnak <stick@satoshilabs.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import common
import binascii

import keepkeylib.messages_pb2 as proto
import keepkeylib.types_pb2 as proto_types
from keepkeylib.client import CallException
from keepkeylib.tx_api import TxApiZcashTestnet

class TestMsgSigntx(common.KeepKeyTest):

    def test_transparent_one_one(self):
        self.setup_mnemonic_allallall()

        # tx: 08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357
        # input 0: 9.99884999 TAZ
        inp1 = proto_types.TxInputType(address_n=[2147483692, 2147483649, 2147483648, 0, 0],  # t1YxYiYy8Hjq5HBN7sioDtTs98SX2SzW5q8
                              amount=999884999,
                             prev_hash=binascii.unhexlify(b'08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='tmJ1xYxP8XNTtCoDgvdmQPSrxh5qZJgy65Z',
                              amount=999884999 - 1940,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        with self.client:
            self.client.set_tx_api(TxApiZcashTestnet)
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify(b"08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify(b"08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify(b"08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify(b"08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=2, tx_hash=binascii.unhexlify(b"08a18fc5a768f8b08c4f5b53a502e2b182107b90b5b4e5f23294074670e57357"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),

                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),

            ])

            (signatures, serialized_tx) = self.client.sign_tx('Zcash Testnet', [inp1, ], [out1, ])

        self.assertEqual(binascii.hexlify(serialized_tx), b'01000000015773e57046079432f2e5b4b5907b1082b1e202a5535b4f8cb0f868a7c58fa108000000006a47304402203c3777f62eb368ab5a94b4e3e7b9f157a66c7e2c3faf3eac2111b464e0e809a002205a668aa1ce9ac4edb5610703926a8cd0d6c658f898d4f6809728a591aa9076610121030e669acac1f280d1ddf441cd2ba5e97417bf2689e4bbec86df4f831bf9f7ffd0ffffffff013301993b000000001976a914255b157a678a10021243307e4bb58f36375aa80e88ac00000000')

    def test_transparent_one_one_feeOver(self):
        self.setup_mnemonic_allallall()

        # tx:  c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56
        # input 0: 10.0 TAZ

        inp1 = proto_types.TxInputType(address_n=[2147483692, 2147483649, 2147483648, 0, 0],  # t1YxYiYy8Hjq5HBN7sioDtTs98SX2SzW5q8
                             # amount=1000000000,
                             prev_hash=binascii.unhexlify(b'c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='tmJ1xYxP8XNTtCoDgvdmQPSrxh5qZJgy65Z',
                              amount=100000000- 1940,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        with self.client:
            self.client.set_tx_api(TxApiZcashTestnet)
            self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify(b"c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56"))),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify(b"c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify(b"c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=1, tx_hash=binascii.unhexlify(b"c8ff96d72e80c01792146d8f0970cbc970882fb315ab1ae043342b4d455e6b56"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_FeeOverThreshold),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),

                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),

            ])

            (signatures, serialized_tx) = self.client.sign_tx('Zcash Testnet', [inp1, ], [out1, ])

        self.assertEqual(binascii.hexlify(serialized_tx), b'0100000001566b5e454d2b3443e01aab15b32f8870c9cb70098f6d149217c0802ed796ffc8000000006b483045022100c291cff800cd8f3e85890b7ebbce792d4485ddabb442fca3ee35e041a50c7814022049fcd09fe22f75e9cd9b7d2ab9f592cbbc4d4511d72fff14be3f38599b2855540121030e669acac1f280d1ddf441cd2ba5e97417bf2689e4bbec86df4f831bf9f7ffd0ffffffff016cd9f505000000001976a914255b157a678a10021243307e4bb58f36375aa80e88ac00000000')

    def test_shielded_one_one_fee(self):
        self.setup_mnemonic_allallall()

        # tx: c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1
        # input 0: 19.9973 ZEC

        inp1 = proto_types.TxInputType(address_n=[2147483692, 2147483649, 2147483648, 0, 0],  # t1YxYiYy8Hjq5HBN7sioDtTs98SX2SzW5q8
                             #amount=1990000000
                             prev_hash=binascii.unhexlify(b'c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1'),
                             prev_index=0,
                             )

        out1 = proto_types.TxOutputType(address='tmJ1xYxP8XNTtCoDgvdmQPSrxh5qZJgy65Z',
                              amount=1990000000 - 1940,
                              script_type=proto_types.PAYTOADDRESS,
                              )

        with self.client:
            self.client.set_tx_api(TxApiZcashTestnet)
	    self.client.set_expected_responses([
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXMETA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify(b"c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1"))),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0, tx_hash=binascii.unhexlify(b"c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1"))),
                proto.TxRequest(request_type=proto_types.TXEXTRADATA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify(b"c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1"),extra_data_offset=0, extra_data_len=1024)),
                proto.TxRequest(request_type=proto_types.TXEXTRADATA, details=proto_types.TxRequestDetailsType(tx_hash=binascii.unhexlify(b"c6eddfbedd5821baea352b79fbd0d793a55257111c46a79002844b86a1c872e1"),extra_data_offset=1024, extra_data_len=875)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.ButtonRequest(code=proto_types.ButtonRequest_ConfirmOutput),
                proto.ButtonRequest(code=proto_types.ButtonRequest_SignTx),
                proto.TxRequest(request_type=proto_types.TXINPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXOUTPUT, details=proto_types.TxRequestDetailsType(request_index=0)),
                proto.TxRequest(request_type=proto_types.TXFINISHED),
            ])
            (signatures, serialized_tx) = self.client.sign_tx('Zcash Testnet', [inp1, ], [out1, ])

        self.assertEqual(binascii.hexlify(serialized_tx), b'0100000001e172c8a1864b840290a7461c115752a593d7d0fb792b35eaba2158ddbedfedc6000000006b483045022100d803daf203681f4149546b5601b3efe955b7bb3135b3e95d65752588a9323a8c02206044654ff06e1571e8a02e6e80bcb886c1d679bc5bd6aef95a74dfec6ecbe89f0121030e669acac1f280d1ddf441cd2ba5e97417bf2689e4bbec86df4f831bf9f7ffd0ffffffff01ecf59c76000000001976a914255b157a678a10021243307e4bb58f36375aa80e88ac00000000')

if __name__ == '__main__':
    unittest.main()

