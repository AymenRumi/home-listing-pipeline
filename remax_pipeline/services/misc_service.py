import uuid


def generate_uuid_from_string(input_string: str):
    namespace_uuid = uuid.NAMESPACE_DNS  # Use the DNS namespace UUID
    generated_uuid = uuid.uuid5(namespace_uuid, input_string)
    return generated_uuid
