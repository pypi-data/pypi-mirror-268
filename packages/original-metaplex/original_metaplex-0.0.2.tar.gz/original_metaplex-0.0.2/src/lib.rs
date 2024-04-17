use base64::engine::Engine as _;
use base64::engine::general_purpose::STANDARD as BASE64;
use bincode;
use bs58;
use mpl_core::{
    instructions::{CreateCollectionV1Builder, CreateV1Builder},
    types::{Plugin, PluginAuthority, PluginAuthorityPair, UpdateDelegate},
    Collection
};
use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use serde_json::{json};
use solana_program::pubkey::Pubkey;
use solana_program::system_program;
use solana_sdk::{
    signature::{Keypair, Signer},
    transaction::Transaction,
};

fn keypair_from_bs58(bs58_string: &str) -> PyResult<Keypair> {
    let bytes = bs58::decode(bs58_string)
        .into_vec()
        .map_err(|e| PyValueError::new_err(format!("Failed to decode BS58: {}", e)))?;

    Keypair::from_bytes(&bytes)
        .map_err(|e| PyValueError::new_err(format!("Failed to create keypair from bytes: {:?}", e)))
}

fn pubkey_from_bs58(bs58_string: &str) -> PyResult<Pubkey> {
    bs58_string.parse::<Pubkey>()
        .map_err(|e| PyValueError::new_err(format!("Failed to decode BS58 pubkey: {}", e)))
}

fn encoded_latest_blockhash(latest_blockhash: &str) -> PyResult<solana_sdk::hash::Hash> {
	latest_blockhash.parse::<solana_sdk::hash::Hash>()
		.map_err(|e| PyValueError::new_err(format!("Failed to parse latest_blockhash: {}", e)))
}

fn encoded_transaction(transaction: &Transaction) -> PyResult<String> {
	let serialized_tx = bincode::serialize(transaction)
		.map_err(|e| PyValueError::new_err(format!("Failed to serialize transaction: {}", e)))?;
	Ok(BASE64.encode(serialized_tx))
}

#[pyfunction]
fn create_collection_v1(
    _py: Python,
    payer: String,
    name: String,
    uri: String,
    latest_blockhash: String,
    update_delegate: Option<String>
) -> PyResult<(String, String)> {
	let payer = keypair_from_bs58(&payer)?;

	let collection_keypair = Keypair::new();
    let collection_pubkey = collection_keypair.pubkey();
    let update_authority_pubkey = payer.pubkey();

    let mut plugins: Vec<PluginAuthorityPair> = vec![];

    // If update_delegate is provided, add it to the plugins vector
    if let Some(update_delegate_key) = update_delegate {
        let update_delegate_pubkey = pubkey_from_bs58(&update_delegate_key)
            .map_err(|e| PyValueError::new_err(format!("Invalid BS58 for update_delegate: {}", e)))?;
        plugins.push(
			PluginAuthorityPair {
	            plugin: Plugin::UpdateDelegate(UpdateDelegate { additional_delegates: vec![] }),
	            authority: Some(PluginAuthority::Address {
					address: update_delegate_pubkey
				}),
            }
		);
    }

    let create_ix = CreateCollectionV1Builder::new()
        .collection(collection_pubkey)
        .update_authority(Some(update_authority_pubkey))
        .payer(payer.pubkey())
        .system_program(system_program::ID)
        .name(name)
        .uri(uri)
        .plugins(plugins) // TODO handle plugin for royalties
        .instruction();

    let mut transaction = Transaction::new_with_payer(&[create_ix], Some(&payer.pubkey()));

    let recent_blockhash = encoded_latest_blockhash(&latest_blockhash)?;
    transaction.try_sign(&[&payer, &collection_keypair], recent_blockhash).unwrap();

    let signed_tx = encoded_transaction(&transaction)?;
	let collection_hex = collection_pubkey.to_string();

    Ok((signed_tx, collection_hex))
}


#[pyfunction]
fn fetch_collection_v1(
    _py: Python,
    collection_account: &[u8]
) -> PyResult<String> {
    let collection = Collection::from_bytes(&collection_account)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
            format!("Failed to parse collection: {}", e)))?;

    let base = &collection.base;
    let json_value = json!({
        "update_authority": base.update_authority.to_string(),
        "name": base.name,
        "uri": base.uri,
        "num_minted": base.num_minted,
        "current_size": base.current_size,
        // TODO: Handle plugins if needed
    });

    serde_json::to_string(&json_value)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(
            format!("Error serializing to JSON: {}", e)))
}


#[pyfunction]
fn create_v1(
    _py: Python,
    payer: String,
    name: String,
    uri: String,
    owner: String,
    collection: String,
    latest_blockhash: String,
) -> PyResult<(String, String)> {
	let payer = keypair_from_bs58(&payer)?;
	let owner = pubkey_from_bs58(&owner)?;
	let collection = pubkey_from_bs58(&collection)?;

	let asset = Keypair::new();

    let create_asset_ix = CreateV1Builder::new()
        .asset(asset.pubkey())
        .collection(Some(collection))
        .payer(payer.pubkey())
        .owner(Some(owner))
        .system_program(system_program::ID)
        .name(name)
        .uri(uri)
        .instruction();

	let mut transaction = Transaction::new_with_payer(
        &[create_asset_ix],
        Some(&payer.pubkey()),
    );

    let recent_blockhash = encoded_latest_blockhash(&latest_blockhash)?;
    transaction.try_sign(&[&payer, &asset], recent_blockhash).unwrap();

	let signed_tx = encoded_transaction(&transaction)?;
	let asset_hex = asset.pubkey().to_string();

    Ok((signed_tx, asset_hex))
}


#[pyfunction]
fn call_metaplex_function() -> PyResult<String> {
    // Example Metaplex call
    // let result = mpl_core::some_function();
    Ok("Result from Metaplex".to_string())
}

#[pymodule]
#[pyo3(name="original_metaplex")]
fn metaplex(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Here you add all the functions you want to expose to Python.
    m.add_function(wrap_pyfunction!(call_metaplex_function, m)?)?;
    m.add_function(wrap_pyfunction!(create_collection_v1, m)?)?;
	m.add_function(wrap_pyfunction!(create_v1, m)?)?;
	m.add_function(wrap_pyfunction!(fetch_collection_v1, m)?)?;
    Ok(())
}

