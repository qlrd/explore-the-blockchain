use bitcoincore_rpc::{Auth, Client};
use std::collections::HashMap;

pub fn connect(config: &HashMap<String, String>) -> Result<Client, bitcoincore_rpc::Error> {
    // Set up the Bitcoin Core RPC client
    let rpc_ip = config.get("rpcconnect").expect("Invalid url");
    let rpc_url = format!("{}:8332", rpc_ip);

    let rpc_user = config.get("rpcuser").expect("Invalid user");
    let rpc_pass = config.get("rpcpassword").expect("Invalid password");

    let rpc_auth = Auth::UserPass(rpc_user.clone(), rpc_pass.clone());

    // Create the RPC client
    Client::new(&rpc_url, rpc_auth)
}
