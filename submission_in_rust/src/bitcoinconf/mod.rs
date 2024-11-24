use config::{Config, ConfigError, File, FileFormat};
use dirs::home_dir;
use std::collections::HashMap;
use std::path::PathBuf;

pub fn get_path() -> Option<PathBuf> {
    home_dir().map(|home| home.join(".bitcoin").join("bitcoin.conf"))
}

pub fn get_config(file_path: &str) -> Result<HashMap<String, String>, ConfigError> {
    let config = Config::builder()
        .add_source(File::new(file_path, FileFormat::Ini))
        .build()?;

    config.try_deserialize::<HashMap<String, String>>()
}
