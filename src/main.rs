use std::env::var;
use std::time;
use mongodb::{
    bson::doc,
    sync::Client,
};


fn get_timestamp_ms() -> u64 {
    let now = time::SystemTime::now();
    now.duration_since(time::SystemTime::UNIX_EPOCH)
        .unwrap()
        .as_millis() as u64
}


fn main() {
    let mongo_uri = var("MONGODB_URI")
        .expect("Environment variable MONGODB_URI not set!");
    let mongo_db = var("MONGODB_DB")
        .expect("Environment variable MONGODB_DB not set!");

    let client = Client::with_uri_str(&mongo_uri)
        .expect("Could not connect to MongoDB!");
    
    let collection = client
        .database(&mongo_db)
        .collection("sample_data");

    let filter = doc! {
        "type": "A",
        "timestamp": {
            "$gte": 0,
        }
    };

    let start = get_timestamp_ms();

    let cursor = collection.find(filter, None)
        .expect("Running find failed!");


    let mut result = Vec::new();
    for document in cursor {
        result.push(document.unwrap());
    }

    let duration_s = (get_timestamp_ms() - start) as f32 / 1000.;

    println!("Done, fetched {} document in {} seconds", result.len(), duration_s);

}
