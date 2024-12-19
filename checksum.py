import hashlib

# Function to calculate checksum for List<Map<String, String>>
def calculate_checksum(data):
    # Sorting is import because we might get different checksums even if we have same data
    sorted_data = sorted(
        data,
        key=lambda map_: str(sorted(map_.items()))
    )
    
    concatenated = ''.join(
        ','.join(f"{key}={value}" for key, value in sorted(map_.items()))
        for map_ in sorted_data
    )
    
    # Generate checksum using MD5
    checksum = hashlib.md5(concatenated.encode('utf-8')).hexdigest()
    return checksum

# Local dummy data
local_data = [
    {"id": "1"},
    {"id": "2"},
    {"id": "3"},
    {"id": "4"},
    {"id": "5"}
]

# migrated data which we got from gcp or aws
migrated_data = [
    {"id": "1"},
    {"id": "4"},
    {"id": "2"},
    {"id": "3"},
    {"id": "5"}
]

# Calculate checksums for both
local_checksum = calculate_checksum(local_data)
migrated_checksum = calculate_checksum(migrated_data)

print(local_checksum, migrated_checksum)
