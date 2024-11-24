#[cfg(test)]
mod test_bitcoinconf {

    use rust::bitcoinconf;

    #[test]
    fn test_get_path() {
        let p = bitcoinconf::get_path().expect("Invalid path");
        assert!(p.exists());
    }

    #[test]
    fn test_get_conf() {
        let buf = bitcoinconf::get_path().unwrap();
        let p = buf.to_str().unwrap();
        let conf = bitcoinconf::get_config(p).expect("Invalid config");
        assert!(conf.get("rpcuser").is_some())
    }
}
