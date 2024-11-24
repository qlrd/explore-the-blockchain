#[cfg(test)]
mod test_conn {
    use std::str::FromStr;

    use bitcoin::blockdata::block::BlockHash;
    use bitcoincore_rpc::RpcApi;
    use rust::bitcoinconf::{get_config, get_path};
    use rust::conn::connect;

    #[test]
    fn test_get_blockhash() {
        let buf = get_path().expect("Invalid path");
        let p = buf.to_str().expect("Invalid PathBuf");
        let conf = get_config(p).expect("Invalid config");
        let client = connect(&conf).expect("Failed to create RPC client");

        let block_height = 654321;
        let block_hash_str = "000000000000000000058452bbe379ad4364fe8fda68c45e299979b492858095";
        let expected = BlockHash::from_str(block_hash_str).expect("Invalid blockhash");

        match client.get_block_hash(block_height) {
            Ok(block_hash) => assert_eq!(block_hash, expected),
            Err(e) => panic!("{}", e),
        }
    }
}
